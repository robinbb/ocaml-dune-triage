#!/usr/bin/env python3
"""Triage ocaml/dune issues and write TOP.md, an ordered list of what to work on.

  ./triage.py seed        build state/issues.jsonl from archive/2026-04 (once)
  ./triage.py run         sync with GitHub, assess new and changed issues,
                          rank the shortlist, write TOP.md

Requires Python 3.11+, an authenticated `gh`, and a logged-in `claude`.
"""

import argparse
import datetime as dt
import json
import math
import re
import subprocess
import sys
import tomllib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATE = ROOT / "state" / "issues.jsonl"
LAST_RANKING = ROOT / "state" / "last_ranking.json"
TOP = ROOT / "TOP.md"
WORK = ROOT / "work"
APRIL = ROOT / "archive" / "2026-04"
APRIL_FETCHED = "2026-04-09T21:26:00Z"
REPO = ("ocaml", "dune")

CATEGORY_NAMES = {
    "build_correctness": "build correctness",
    "package_management": "package management",
    "windows_platform": "platform-specific",
    "error_messages_ux": "error messages",
    "paths_files_symlinks": "paths and symlinks",
    "crashes_internal": "crash",
    "tooling_integration": "tooling",
    "vendoring_cross": "vendoring, ppx, cross-compilation",
    "coq_rocq": "Rocq",
    "watch_rpc": "watch mode and RPC",
}
SEVERITY_NAMES = {
    "S1": "silent wrong result", "S2": "crash or data loss",
    "S3": "broken documented behavior", "S4": "platform blocker",
    "S5": "regression", "S6": "misleading error", "S7": "workaroundable",
}
DIFFICULTY_NAMES = {
    "D1": "straightforward", "D2": "moderate", "D3": "subsystem rework",
    "D4": "cross-cutting", "D5": "design problem",
}
SIZES = ["hours", "days", "weeks", "unknown"]
REACH = ["low", "medium", "high"]
PARKED = ("skip", "in-progress")

# Fields Claude fills in, in the order they are stored.
ASSESSED = [
    "is_bug", "not_bug_reason", "category", "severity", "difficulty", "desc",
    "reproducer", "root_cause_known", "approach_agreed", "approach_note",
    "open_questions", "active_prs", "reach", "next_step", "size", "notes",
]
FIELDS = ["number", "title", "state", *ASSESSED, "readiness_assessed",
          "source", "assessed_at", "issue_updated_at", "closed_seen_at"]


def log(msg):
    print(msg, file=sys.stderr, flush=True)


# --- state ---------------------------------------------------------------

def load_records():
    if not STATE.exists():
        return {}
    records = {}
    for line in STATE.read_text().splitlines():
        if line.strip():
            rec = json.loads(line)
            records[rec["number"]] = rec
    return records


def save_records(records):
    tmp = STATE.with_suffix(".tmp")
    with tmp.open("w") as f:
        for n in sorted(records):
            rec = records[n]
            f.write(json.dumps({k: rec.get(k) for k in FIELDS},
                               ensure_ascii=False) + "\n")
    tmp.replace(STATE)


def load_overrides():
    path = ROOT / "overrides.toml"
    if not path.exists():
        return {}
    issues = tomllib.loads(path.read_text()).get("issues", {})
    return {int(n): v for n, v in issues.items()}


# --- seed ----------------------------------------------------------------

NOT_BUG_LINE = re.compile(r"^- \*\*#(\d+)\*\* - (.*) — (.*)$")


def cmd_seed(args):
    if STATE.exists() and not args.force:
        sys.exit(f"{STATE.relative_to(ROOT)} already exists (use --force to overwrite)")
    base = dict(state="open", readiness_assessed=False, source="april-2026",
                assessed_at="2026-04-10", issue_updated_at=APRIL_FETCHED)
    records = {}
    for bug in json.loads((APRIL / "difficulty_all.json").read_text()):
        n = bug["number"]
        records[n] = base | dict(
            number=n, title=bug["title"], is_bug=True,
            category=bug["category"], severity=bug["severity"],
            difficulty=bug["difficulty"], desc=bug["desc"])
    for md in sorted(APRIL.glob("bugs_batch_*.md")):
        in_not_bugs = False
        for line in md.read_text().splitlines():
            if line.startswith("## "):
                in_not_bugs = line.startswith("## Not Bugs")
                continue
            m = in_not_bugs and NOT_BUG_LINE.match(line)
            if m:
                n = int(m[1])
                records[n] = base | dict(number=n, title=m[2], is_bug=False,
                                         not_bug_reason=m[3])
    STATE.parent.mkdir(exist_ok=True)
    save_records(records)
    bugs = sum(r["is_bug"] for r in records.values())
    log(f"Seeded {len(records)} records ({bugs} bugs) from {APRIL.relative_to(ROOT)}")


# --- GitHub --------------------------------------------------------------

def gh_graphql(query, **variables):
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    for k, v in variables.items():
        if v is not None:
            cmd += ["-f", f"{k}={v}"]
    for attempt in (1, 2):
        r = subprocess.run(cmd, capture_output=True, text=True)
        try:
            data = json.loads(r.stdout).get("data")
        except json.JSONDecodeError:
            data = None
        if data is not None:
            if r.returncode != 0:
                log(f"GitHub returned partial data: {r.stderr.strip()[:300]}")
            return data
        log(f"gh api graphql failed (attempt {attempt}): {r.stderr.strip()[:500]}")
    sys.exit("Giving up on the GitHub API")


LIST_QUERY = """
query($owner: String!, $name: String!, $cursor: String) {
  repository(owner: $owner, name: $name) {
    issues(states: OPEN, first: 100, after: $cursor,
           orderBy: {field: CREATED_AT, direction: ASC}) {
      pageInfo { hasNextPage endCursor }
      nodes {
        number title url createdAt updatedAt
        labels(first: 20) { nodes { name } }
        reactions { totalCount }
        comments { totalCount }
      }
    }
  }
}"""


def list_open_issues():
    live, cursor = {}, None
    while True:
        data = gh_graphql(LIST_QUERY, owner=REPO[0], name=REPO[1], cursor=cursor)
        page = data["repository"]["issues"]
        for i in page["nodes"]:
            live[i["number"]] = dict(
                title=i["title"], url=i["url"], created_at=i["createdAt"],
                updated_at=i["updatedAt"],
                labels=[label["name"] for label in i["labels"]["nodes"]],
                reactions=i["reactions"]["totalCount"],
                comments=i["comments"]["totalCount"])
        if not page["pageInfo"]["hasNextPage"]:
            return live
        cursor = page["pageInfo"]["endCursor"]


THREAD_FIELDS = """
  number title url state createdAt updatedAt
  author { login } authorAssociation body
  labels(first: 20) { nodes { name } }
  milestone { title }
  reactions { totalCount }
  comments(last: 20) {
    totalCount
    nodes { author { login } authorAssociation createdAt body }
  }
  timelineItems(last: 50, itemTypes: [CROSS_REFERENCED_EVENT, CONNECTED_EVENT]) {
    nodes {
      ... on CrossReferencedEvent { createdAt source { ...Ref } }
      ... on ConnectedEvent { createdAt subject { ...Ref } }
    }
  }"""

REF_FRAGMENT = """
fragment Ref on ReferencedSubject {
  ... on PullRequest {
    __typename number title state isDraft updatedAt url
    author { login } repository { nameWithOwner }
  }
  ... on Issue {
    __typename number title state url repository { nameWithOwner }
  }
}"""


def login(actor):
    return (actor or {}).get("login", "ghost")


def clip(text, limit):
    text = text or ""
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n[... {len(text) - limit} more characters]"


def compact_thread(i):
    refs = {}
    for event in i["timelineItems"]["nodes"]:
        src = event.get("source") or event.get("subject") or {}
        if "number" not in src:
            continue
        state = src["state"]
        if src.get("isDraft") and state == "OPEN":
            state = "DRAFT"
        ref = dict(kind=src["__typename"], repo=src["repository"]["nameWithOwner"],
                   number=src["number"], title=src["title"], state=state,
                   referenced_at=event["createdAt"])
        if src["__typename"] == "PullRequest":
            ref |= dict(author=login(src["author"]), updated_at=src["updatedAt"])
        refs[(ref["repo"], ref["number"])] = ref
    return dict(
        number=i["number"], title=i["title"], url=i["url"], state=i["state"],
        created_at=i["createdAt"], updated_at=i["updatedAt"],
        author=login(i["author"]), author_association=i["authorAssociation"],
        labels=[label["name"] for label in i["labels"]["nodes"]],
        milestone=(i["milestone"] or {}).get("title"),
        reactions=i["reactions"]["totalCount"],
        comment_count=i["comments"]["totalCount"],
        body=clip(i["body"], 8000),
        comments=[dict(author=login(c["author"]),
                       association=c["authorAssociation"],
                       at=c["createdAt"], body=clip(c["body"], 2000))
                  for c in i["comments"]["nodes"]],
        references=list(refs.values()))


def fetch_threads(numbers):
    threads = {}
    for chunk in chunked(numbers, 10):
        aliases = "\n".join(f"i{n}: issue(number: {n}) {{{THREAD_FIELDS}\n}}"
                            for n in chunk)
        query = (f'query {{ repository(owner: "{REPO[0]}", name: "{REPO[1]}") '
                 f"{{\n{aliases}\n}} }}\n{REF_FRAGMENT}")
        repo = gh_graphql(query)["repository"] or {}
        for n in chunk:
            if repo.get(f"i{n}"):
                threads[n] = compact_thread(repo[f"i{n}"])
            else:
                log(f"#{n}: not found on GitHub (transferred or deleted?)")
    return threads


def chunked(items, size):
    return [items[k:k + size] for k in range(0, len(items), size)]


# --- claude --------------------------------------------------------------

def nullable(schema):
    if "enum" in schema:
        return {"enum": [*schema["enum"], None]}
    return {"type": [schema["type"], "null"]}


def obj(**properties):
    return {"type": "object", "properties": properties,
            "required": list(properties), "additionalProperties": False}


STRING = {"type": "string"}
BOOL = {"type": "boolean"}
INT = {"type": "integer"}

ASSESSMENT_SCHEMA = obj(
    number=INT, is_bug=BOOL, not_bug_reason=nullable(STRING),
    category=nullable({"enum": list(CATEGORY_NAMES)}),
    severity=nullable({"enum": list(SEVERITY_NAMES)}),
    difficulty=nullable({"enum": list(DIFFICULTY_NAMES)}),
    desc=STRING, reproducer=BOOL, root_cause_known=BOOL, approach_agreed=BOOL,
    approach_note=nullable(STRING), open_questions=nullable(STRING),
    active_prs={"type": "array", "items": obj(
        repo=STRING, number=INT, author=STRING, state=STRING, note=STRING)},
    reach={"enum": REACH}, next_step=nullable(STRING), size={"enum": SIZES},
    notes=nullable(STRING))
BATCH_SCHEMA = obj(assessments={"type": "array", "items": ASSESSMENT_SCHEMA})

RANKING_SCHEMA = obj(
    items={"type": "array", "items": obj(
        number=INT, action=STRING, why_now=STRING, first_step=STRING,
        size={"enum": SIZES}, risks=nullable(STRING),
        movement=nullable(STRING))},
    dropped={"type": "array", "items": obj(number=INT, reason=STRING)})


def rubric(*names):
    return "\n\n---\n\n".join((ROOT / "rubric" / n).read_text() for n in names)


class Run:
    def __init__(self, cfg):
        self.cfg = cfg
        self.today = dt.date.today().isoformat()
        self.records = load_records()
        self.overrides = load_overrides()
        self.previous = (json.loads(LAST_RANKING.read_text())
                         if LAST_RANKING.exists() else {})
        self.live = {}
        self.cost = 0.0
        self.calls = 0
        self.tasks = 0
        self.assessed = Counter()
        self.log_dir = WORK / dt.datetime.now().strftime("%Y-%m-%dT%H%M%S")

    def status(self, n):
        return self.overrides.get(n, {}).get("status")

    def claude(self, task, instructions, payload, schema):
        """Run claude with no tools at all: the payload goes in on stdin and
        a JSON object matching the schema comes back."""
        cmd = ["claude", "-p", instructions,
               "--output-format", "json", "--json-schema", json.dumps(schema),
               "--tools", "", "--restricted", "--strict-mcp-config",
               "--permission-mode", "dontAsk", "--no-session-persistence",
               "--disable-slash-commands"]
        for flag in ("model", "effort"):
            if self.cfg["run"][flag]:
                cmd += [f"--{flag}", self.cfg["run"][flag]]
        stdin = json.dumps(payload, ensure_ascii=False, indent=1)
        self.tasks += 1
        task = f"{self.tasks:02d}-{task}"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        (self.log_dir / f"{task}.in.json").write_text(stdin)
        for attempt in (1, 2):
            self.calls += 1
            try:
                r = subprocess.run(cmd, input=stdin, capture_output=True,
                                   text=True, cwd=ROOT, timeout=1800)
            except subprocess.TimeoutExpired:
                log(f"{task}: claude timed out (attempt {attempt})")
                continue
            (self.log_dir / f"{task}.out.json").write_text(r.stdout)
            try:
                out = json.loads(r.stdout)
            except json.JSONDecodeError:
                out = {}
            self.cost += out.get("total_cost_usd") or 0.0
            result = out.get("structured_output")
            if r.returncode == 0 and not out.get("is_error") and isinstance(result, dict):
                return result
            detail = (r.stderr or str(out.get("result", "")))[-500:]
            log(f"{task}: claude failed (attempt {attempt}, exit {r.returncode}): {detail}")
        return None


# --- assessing -----------------------------------------------------------

def assessment_problem(a):
    if a["is_bug"]:
        if None in (a["category"], a["severity"], a["difficulty"]):
            return "bug without category, severity or difficulty"
    elif not a["not_bug_reason"]:
        return "non-bug without a reason"
    return None


def batches(numbers, threads, max_items, max_chars=150_000):
    """Group issues for claude calls, keeping each call's input bounded."""
    out, current, size = [], [], 0
    for n in numbers:
        length = len(json.dumps(threads[n]))
        if current and (len(current) >= max_items or size + length > max_chars):
            out.append(current)
            current, size = [], 0
        current.append(n)
        size += length
    return out + [current] if current else out


def assess(run, numbers, label):
    if not numbers:
        return
    log(f"Assessing {len(numbers)} issues ({label})")
    threads = fetch_threads(numbers)
    instructions = rubric("assess.md", "classification.md")
    todo = [n for n in numbers if n in threads]
    for k, batch in enumerate(batches(todo, threads, run.cfg["run"]["batch_size"]), 1):
        payload = {"today": run.today, "issues": [threads[n] for n in batch]}
        result = run.claude(f"assess-{label}-{k}", instructions, payload, BATCH_SCHEMA)
        if result is None:
            continue
        got = {}
        for a in result["assessments"]:
            n = a["number"]
            problem = ("not in this batch" if n not in batch
                       else "assessed twice" if n in got
                       else assessment_problem(a))
            if problem:
                log(f"#{n}: ignoring assessment ({problem})")
                continue
            got[n] = a
        for n, a in got.items():
            run.records[n] = run.records.get(n, {}) | {k: a[k] for k in ASSESSED} | dict(
                number=n, title=threads[n]["title"], state="open",
                readiness_assessed=True, source="claude", assessed_at=run.today,
                issue_updated_at=threads[n]["updated_at"], closed_seen_at=None)
        missing = [n for n in batch if n not in got]
        if missing:
            log(f"No usable assessment for {missing}; they stay queued")
        run.assessed[label] += len(got)
        save_records(run.records)


def is_changed(run, n):
    rec = run.records.get(n)
    return rec is None or run.live[n]["updated_at"] > (rec.get("issue_updated_at") or "")


def build_queue(run):
    new, changed = [], []
    for n in run.live:
        if run.status(n) in PARKED or not is_changed(run, n):
            continue
        (changed if n in run.records else new).append(n)
    new.sort(key=lambda n: -(run.live[n]["reactions"] + run.live[n]["comments"]))
    changed.sort(key=lambda n: -prescore(run, n))
    return new, changed


# --- shortlist and ranking -----------------------------------------------

def prescore(run, n):
    rec, meta = run.records.get(n), run.live.get(n)
    if not rec or not rec.get("is_bug") or not meta:
        return 0.0
    s = run.cfg["score"]
    score = (s["severity"].get(rec["severity"], 0)
             * s["difficulty"].get(rec["difficulty"], 0)
             * (1 + s["activity"] * math.log2(1 + meta["reactions"] + meta["comments"])))
    if rec.get("readiness_assessed"):
        r = s["readiness"]
        for key in ("reproducer", "root_cause_known", "approach_agreed"):
            if rec.get(key):
                score *= r[key]
        if rec.get("open_questions"):
            score *= r["open_questions"]
        score *= s["reach"].get(rec.get("reach"), 1.0)
    return score * run.overrides.get(n, {}).get("boost", 1.0)


def shortlist(run, extra=0):
    """The ranking candidates, plus `extra` runners-up when asked."""
    def eligible(n):
        rec = run.records.get(n)
        return (n in run.live and rec is not None and rec.get("is_bug")
                and run.status(n) not in PARKED)

    picked = sorted(filter(eligible, run.live), key=lambda n: -prescore(run, n))
    picked = picked[:run.cfg["run"]["shortlist"] + extra]
    # Keep the previous items in view so the ranking can stay stable.
    for item in run.previous.get("items", []):
        if eligible(item["number"]) and item["number"] not in picked:
            picked.append(item["number"])
    return picked


def needs_refresh(run, n):
    rec = run.records[n]
    if not rec.get("readiness_assessed") or is_changed(run, n):
        return True
    age = dt.date.fromisoformat(run.today) - dt.date.fromisoformat(rec["assessed_at"])
    return age.days > run.cfg["run"]["stale_days"]


def rank(run, picked):
    top = run.cfg["run"]["top"]
    candidates = []
    for n in picked:
        rec, meta = run.records[n], run.live[n]
        c = dict(number=n, title=meta["title"], labels=meta["labels"],
                 reactions=meta["reactions"], comments=meta["comments"],
                 opened=meta["created_at"][:10], last_activity=meta["updated_at"][:10],
                 assessed_at=rec["assessed_at"],
                 readiness_assessed=rec["readiness_assessed"])
        c |= {k: rec.get(k) for k in ASSESSED if k not in ("is_bug", "not_bug_reason")}
        if note := run.overrides.get(n, {}).get("note"):
            c["note"] = note
        candidates.append(c)
    previous = [dict(position=k, number=item["number"], action=item["action"],
                     why_now=item["why_now"])
                for k, item in enumerate(run.previous.get("items", []), 1)]
    payload = dict(today=run.today, top=top,
                   previous_ranking_date=run.previous.get("date"),
                   previous_ranking=previous, candidates=candidates)
    log(f"Ranking {len(candidates)} candidates")
    result = run.claude("rank", rubric("ranking.md"), payload, RANKING_SCHEMA)
    if result is None:
        return None
    items, seen = [], set()
    for item in result["items"]:
        n = item["number"]
        if n in picked and n not in seen:
            items.append(item)
            seen.add(n)
        else:
            log(f"#{n}: ignoring ranked item (not a candidate, or repeated)")
    if not items:
        return None
    dropped = [d for d in result["dropped"] if d["number"] not in seen]
    return dict(date=run.today, items=items[:top], dropped=dropped)


# --- TOP.md --------------------------------------------------------------

def issue_link(run, n):
    meta = run.live.get(n)
    title = meta["title"] if meta else run.records.get(n, {}).get("title", "")
    url = meta["url"] if meta else f"https://github.com/{REPO[0]}/{REPO[1]}/issues/{n}"
    return f"[#{n}]({url}) {title}"


def render(run, ranking, closed_now):
    open_issues = len(run.live)
    classified = [n for n in run.live if n in run.records]
    bugs = sum(1 for n in classified if run.records[n].get("is_bug"))
    awaiting = sum(1 for n in run.live
                   if run.status(n) not in PARKED and is_changed(run, n))
    lines = [
        "# What to work on in ocaml/dune", "",
        f"_Updated {run.today}. {open_issues} open issues, {len(classified)} "
        f"classified ({bugs} bugs). {awaiting} are new or have changed since "
        f"they were last assessed; up to {run.cfg['run']['assess_cap']} are "
        f"assessed per run._", "",
        "Ordered by how soon the work can deliver value, not by severity "
        "alone. See [rubric/ranking.md](rubric/ranking.md).", ""]

    in_progress = [n for n in sorted(run.overrides) if run.status(n) == "in-progress"]
    if in_progress:
        lines += ["## In progress", ""]
        for n in in_progress:
            note = run.overrides[n].get("note")
            closed = "" if n in run.live else " (closed on GitHub)"
            lines.append(f"- {issue_link(run, n)}{closed}" + (f": {note}" if note else ""))
        lines.append("")

    previous = {item["number"]: k for k, item in enumerate(run.previous.get("items", []), 1)}
    lines += ["## Next up", ""]
    for pos, item in enumerate(ranking["items"], 1):
        n = item["number"]
        rec = run.records[n]
        old = previous.get(n)
        move = ("new" if old is None else "same place" if old == pos
                else f"up {old - pos}" if old > pos else f"down {pos - old}")
        tags = [f"{rec['severity']} {SEVERITY_NAMES[rec['severity']]}",
                f"{rec['difficulty']} {DIFFICULTY_NAMES[rec['difficulty']]}",
                CATEGORY_NAMES[rec["category"]], f"size: {item['size']}", move]
        lines += [f"### {pos}. {issue_link(run, n)}", "", " · ".join(tags), "",
                  f"- **Do:** {item['action']}",
                  f"- **Why now:** {item['why_now']}",
                  f"- **First step:** {item['first_step']}"]
        if item["risks"]:
            lines.append(f"- **Risks:** {item['risks']}")
        if item["movement"] and old is not None and old != pos:
            lines.append(f"- **Moved:** {item['movement']}")
        if note := run.overrides.get(n, {}).get("note"):
            lines.append(f"- **Note:** {note}")
        lines.append("")

    ranked = {item["number"] for item in ranking["items"]}
    reasons = {d["number"]: d["reason"] for d in ranking["dropped"]}
    gone = []
    for n in previous:
        if n in ranked:
            continue
        if n not in run.live:
            reason = "closed on GitHub"
        elif run.status(n) in PARKED:
            reason = f"marked {run.status(n)} in overrides.toml"
        else:
            reason = reasons.get(n, "no reason given")
        gone.append(f"- {issue_link(run, n)}: {reason}")
    if gone:
        lines += ["## Dropped since the last run", "", *gone, ""]

    lines += ["## This run", "",
              f"- Assessed {run.assessed['queue']} new or changed issues and "
              f"refreshed {run.assessed['shortlist']} shortlisted ones.",
              f"- {len(closed_now)} tracked issues closed since the last run.",
              f"- {run.calls} claude calls, about ${run.cost:.2f} at API prices.", ""]
    return "\n".join(lines)


# --- run -----------------------------------------------------------------

def cmd_run(args):
    cfg = tomllib.loads((ROOT / "config.toml").read_text())
    for key in ("assess_cap", "refresh_cap", "shortlist", "top", "model", "effort"):
        if getattr(args, key) is not None:
            cfg["run"][key] = getattr(args, key)
    run = Run(cfg)
    if not run.records:
        sys.exit("No state yet: run ./triage.py seed first")

    log("Listing open issues on GitHub")
    run.live = list_open_issues()
    closed_now = []
    for n, rec in run.records.items():
        if rec["state"] == "open" and n not in run.live:
            rec |= dict(state="closed", closed_seen_at=run.today)
            closed_now.append(n)
        elif rec["state"] == "closed" and n in run.live:
            rec |= dict(state="open", closed_seen_at=None)
    new, changed = build_queue(run)
    queue = (new + changed)[:cfg["run"]["assess_cap"]]
    log(f"{len(run.live)} open issues; {len(closed_now)} closed since the last run; "
        f"{len(new)} new and {len(changed)} changed since assessed; "
        f"assessing {len(queue)} of them now")

    if args.dry_run:
        print("Would assess:", " ".join(f"#{n}" for n in queue))
        print("Shortlist before refresh (pre-score, needs refresh):")
        for n in shortlist(run):
            flag = " refresh" if needs_refresh(run, n) else ""
            print(f"  {prescore(run, n):6.2f}{flag}  {issue_link(run, n)}")
        return

    save_records(run.records)
    assess(run, queue, "queue")
    # A fresh assessment often demotes an issue, which pulls a new one into
    # the shortlist; keep refreshing until it is stable or the budget runs out.
    budget = cfg["run"]["refresh_cap"]
    # Runners-up are refreshed in the same batch, as they are the likeliest
    # replacements.
    while budget > 0 and any(needs_refresh(run, n) for n in shortlist(run)):
        todo = [n for n in shortlist(run, extra=cfg["run"]["batch_size"])
                if needs_refresh(run, n)][:budget]
        assess(run, todo, "shortlist")
        budget -= len(todo)

    picked = shortlist(run)
    ranking = rank(run, picked) if picked else None
    if ranking is None:
        log("Ranking failed; TOP.md left unchanged")
    else:
        TOP.write_text(render(run, ranking, closed_now))
        LAST_RANKING.write_text(json.dumps(ranking, indent=1, ensure_ascii=False) + "\n")
        log(f"Wrote {TOP.relative_to(ROOT)} with {len(ranking['items'])} items")
    log(f"{run.calls} claude calls, about ${run.cost:.2f} at API prices; "
        f"logs in {run.log_dir.relative_to(ROOT)}")

    if args.commit:
        paths = [p for p in ("state", "TOP.md") if (ROOT / p).exists()]
        subprocess.run(["git", "add", "--", *paths], cwd=ROOT, check=True)
        if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT).returncode:
            subprocess.run(["git", "commit", "-s", "-q", "-m", f"triage: {run.today}"],
                           cwd=ROOT, check=True)
            log("Committed")


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    seed = sub.add_parser("seed", help="build the initial state from archive/2026-04")
    seed.add_argument("--force", action="store_true", help="overwrite existing state")
    seed.set_defaults(func=cmd_seed)
    run = sub.add_parser("run", help="sync, assess, rank and write TOP.md")
    run.add_argument("--assess-cap", type=int, help="new or changed issues to assess")
    run.add_argument("--refresh-cap", type=int, help="shortlisted issues to re-assess")
    run.add_argument("--shortlist", type=int, help="candidates for the ranking step")
    run.add_argument("--top", type=int, help="items in TOP.md")
    run.add_argument("--model", help="claude model")
    run.add_argument("--effort", help="claude effort level")
    run.add_argument("--dry-run", action="store_true",
                     help="show what would be assessed and shortlisted; change nothing")
    run.add_argument("--commit", action="store_true",
                     help="commit state/ and TOP.md afterwards")
    run.set_defaults(func=cmd_run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
