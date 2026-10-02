# ocaml-dune-triage

Keeps a triaged record of every open [ocaml/dune](https://github.com/ocaml/dune)
issue and writes [`TOP.md`](TOP.md): the issues worth working on next,
ordered by how soon the work can deliver value.

## Running it

Requires Python 3.11+, `gh` logged in to GitHub, and `claude` logged in.

```sh
./triage.py run              # sync, assess, rank, write TOP.md
./triage.py run --commit     # ... and commit state/ and TOP.md
./triage.py run --dry-run    # show what would be assessed; change nothing
```

`./triage.py run --help` lists flags that override `config.toml` for one
run. The first runs face a backlog, so `--assess-cap 200` clears it faster.

## How it works

1. **Sync.** List the open issues on GitHub. Issues that have closed are marked
   closed. Issues that are new, or have had activity since they were last
   assessed, are queued.
2. **Assess.** Claude reads each queued issue's thread and records its
   classification (`rubric/classification.md`) and how close it is to a merged
   fix (`rubric/assess.md`). At most `assess_cap` are assessed per run, new
   issues first.
3. **Shortlist.** A simple pre-score (`config.toml`) picks the candidates. Any
   whose assessment is missing, stale or out of date is re-assessed first.
4. **Rank.** Claude orders the shortlist using `rubric/ranking.md`, with the
   previous ranking as a reference so items only move for a reason. The result
   is written to `TOP.md`.

Claude is run without any tools: issue text goes in on stdin and JSON comes
back, which the script validates before saving. Issue threads are untrusted
input, so Claude cannot touch files, run commands or reach the network. Each
call's input and output is kept in `work/` (not committed).

The first test runs cost about $0.07 per issue assessed at API prices. With a
Claude subscription, that comes out of the plan's usage instead.

## Files

| Path | What it is |
|------|------------|
| `TOP.md` | The deliverable |
| `rubric/ranking.md` | What "value soonest" means. Edit this to change the order |
| `rubric/assess.md`, `rubric/classification.md` | How issues are assessed |
| `overrides.toml` | Your calls on specific issues: skip, in progress, boost, notes |
| `config.toml` | Batch sizes, caps and pre-score weights |
| `state/issues.jsonl` | One record per issue. Git history is the audit trail |
| `state/last_ranking.json` | The previous ranking, used for stability |
| `archive/2026-04/` | The April 2026 triage this state was seeded from (`./triage.py seed`) |
