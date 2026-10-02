# Bug Classification Methodology

This document describes the methodology used to classify 412 open bugs in the
[ocaml/dune](https://github.com/ocaml/dune) repository, as of 2026-04-10.

## Scope

Starting from 1,003 open GitHub issues, each issue was read and evaluated to
determine whether it describes an actual bug, misfeature, or problem. Issues
that are purely feature requests, enhancement proposals, RFCs/design
discussions, documentation-only issues, chores/maintenance tasks, or
performance optimization requests (unless something is broken) were excluded.
412 issues (41%) were identified as bugs.

Each bug was then assigned a **severity** (S1-S7) and **difficulty** (D1-D5).

## Category Assignment

Bugs were sorted into 10 categories by keyword matching on the issue title,
description, and body text. Categories were chosen to produce roughly even
groups covering the major subsystems and failure modes:

| Category | Report File | Description |
|----------|-------------|-------------|
| Build Correctness & Linking | `report_build_correctness.md` | Wrong flags, incorrect linking, missing deps, stale builds |
| Package Management | `report_package_management.md` | Lock files, sandbox, solver, caching, opam interop |
| Windows & Platform-Specific | `report_windows_platform.md` | Windows, macOS, BSD, ARM, NFS, WSL failures |
| Error Messages & UX | `report_error_messages_ux.md` | Misleading/missing errors, confusing behavior |
| Paths, Files & Symlinks | `report_paths_files_symlinks.md` | Path resolution, symlinks, directory targets |
| Crashes & Internal Errors | `report_crashes_internal.md` | Segfaults, uncaught exceptions, hangs |
| Tooling Integration | `report_tooling_integration.md` | Merlin, odoc, utop, LSP, formatting, mdx |
| Vendoring & Cross-Compilation | `report_vendoring_cross.md` | Vendored lib conflicts, PPX, context resolution |
| Coq & Rocq Integration | `report_coq_rocq.md` | coqdep, native compilation, plugins, theory builds |
| Watch Mode & RPC | `report_watch_rpc.md` | Watch mode hangs, RPC issues, incremental rebuilds |

When an issue matches multiple categories, the most specific category wins
(e.g., a Windows crash goes to "Windows & Platform-Specific" rather than
"Crashes & Internal Errors").

## Severity Levels (S1-S7)

Severity measures **how bad the impact is** for a user who hits the bug.
When a bug qualifies for multiple levels, the most severe one is assigned.

### S1 -- Silent Correctness Failures

The build succeeds but produces wrong results. The user does not know anything
is wrong. This is the most dangerous category because it erodes trust without
warning.

**Signals:** PPX silently not applied, tests compiled but never executed, wrong
library version linked, stale cache used without notification, wrong flags
passed to the compiler, build paths leaked into installed artifacts, file
promotion picks the wrong file.

**Key distinction from S3:** If the build *fails* with a compilation error,
that is S3 (Broken Documented Behavior), not S1 — even if the underlying
cause is incorrect code generation (e.g., duplicate module definitions). S1
is strictly for cases where the build succeeds and the user has no indication
that anything is wrong.

**Examples:** #9650 (PPX skipped with `(modes byte)`), #9757 (inline tests
compiled but silently not run), #9979 (wrong cstubs linked in byte mode),
#11225 (git describe output instead of version string).

### S2 -- Crashes & Data Loss

Dune crashes, segfaults, hangs indefinitely, or destroys user state. Internal
errors that abort the build. The user is completely blocked.

**Signals:** "Internal error" in output, segfault, process hangs forever,
uncaught exceptions in stack traces, user data deleted unexpectedly.

**Examples:** #10954 (segfault during `opam install dune`), #12063 (segfault
on ppc64), #12609 (hang when curl not installed), #13500 (crash with spurious
dependency cycle).

### S3 -- Broken Documented Behavior

A feature exists and is documented but does not work. The user reads the
documentation, tries to use the feature, and hits a wall.

**Signals:** Documented flag/stanza/syntax rejected or ignored, "Unknown
value" errors for valid inputs, behavior contradicts documentation, feature
works in some configurations but not others.

**Examples:** #5081 (`(modes c)` gives "Unknown value"), #5621 (`(optional)`
in executables does nothing), #10588 (`--ignore-promoted-rules` has no
effect), #11042 (`(enabled_if %{read:...})` rejected).

### S4 -- Platform/Environment Blockers

The feature works on some platforms but is completely broken on others. Blocks
adoption of dune on the affected platform or environment.

**Signals:** Issue title/body mentions a specific OS (Windows, macOS, FreeBSD,
OpenBSD, Haiku), architecture (ARM64, ppc64, arm32), or environment (NFS,
WSL, Cygwin) where the behavior differs from the expected.

**Examples:** #13993 (Windows sandbox cleanup with unicode), #13823 (OpenBSD
tar flags), #12122 (Haiku hardlinks), #4482 (random "Permission denied" on
macOS ARM64).

### S5 -- Regressions

Something that used to work in a prior version of dune but broke. These are
high priority because they break existing users on upgrade.

**Signals:** Issue mentions a specific prior version where things worked,
phrases like "regression", "used to work", "broke in", "no longer works
since".

**Examples:** #14085 (3.22.0 regression in `(select)`), #12390 (compiler
cache no longer works in 3.20), #11290 (`dune subst` broken since 3.17),
#13545 (3.21.0 can't lock ocaml-system).

### S6 -- Misleading Errors & Poor UX

The build fails, but the error message points the user in the wrong direction
or is incomprehensible. The user wastes time debugging the wrong thing.

**Signals:** Error message references wrong file/stanza, error message
is garbled or cryptic, no location information provided, error suggests
an impossible fix.

**Examples:** #2818 (cryptic cycle errors), #12439 (confusing `%{target}`
message), #6598 (error mentions wrong module), #5789 (confusing
`allow_empty` error on new project).

### S7 -- Workaroundable Bugs

Real bugs, but users can work around them with reasonable effort. Annoying
but not blocking.

**Signals:** Issue author or commenters describe a workaround, the bug
affects a narrow use case, the behavior is suboptimal but not wrong in a
way that causes failures.

**Examples:** #3916 (duplicate opam bounds -- cosmetic), #13878 (absolute
path in lock file -- edit manually), #3223 (dune-project not formatted by
`@fmt` -- run formatter separately).

## Difficulty Levels (D1-D5)

Difficulty measures **how hard the bug is to fix** from an implementation
perspective. The key factors are:

1. **Locality** -- How many subsystems does the fix touch?
2. **Ambiguity** -- Is the correct behavior obvious, or does it require a
   design decision?
3. **Regression risk** -- Could the fix break something else?
4. **Testability** -- Can you write a deterministic test?

### D1 -- Straightforward Fix

The root cause is obvious from the issue description. The fix is localized
to one or two files. No design decisions are needed. A contributor familiar
with the codebase could fix this in under a day.

**Signals:** Wrong constant or version number, missing single flag, duplicate
string generation, simple off-by-one, trivial error message text change,
missing file extension check.

**Examples:** #10360 (version check says 2.9 but should be 3.0), #3916
(duplicate opam bounds), #5733 (mandir default changed), #10707 (missing
menhir version lower bound).

### D2 -- Moderate Investigation

The fix probably touches 2-5 files and requires understanding a subsystem,
but the scope is bounded. May need a few test cases. A few days of work.

**Signals:** Environment variable handling, missing dependency edges, flag
ordering issues, single-subsystem behavior fixes, error message improvements
where the right information needs to be threaded through.

**Examples:** #13551 (PPX order alphabetically sorted), #12924 (env var
leaks into sandbox), #11017 (coqdoc header/footer deps missing), #13225
(`:standard` in `:include` ignored).

### D3 -- Subsystem Rework

The bug exposes a design limitation in a specific subsystem. The fix requires
changing data structures or control flow in a non-trivial way, and likely
affects multiple callers. Risk of regressions in adjacent behavior. A week
or more.

**Signals:** Path relocation/sandboxing architecture, shared cache
cross-filesystem handling, tool integration (merlin, ctypes), platform
subsystem fixes requiring understanding of OS-specific behavior, dynamic
linking model.

**Examples:** #10974 (shared cache cross-filesystem), #10291 (sandbox path
in topfind), #9773 (ctypes + foreign stubs linking), #2909 (merlin +
virtual libraries).

### D4 -- Cross-Cutting Architectural

The bug sits at the intersection of multiple subsystems (e.g., build engine +
package management + caching, or watch mode + RPC + file system). Fixing it
may require rethinking invariants or interfaces. High regression risk.

**Signals:** Involves concurrency between file watcher, build engine, and RPC;
crosses context boundaries (host vs target, vendored vs non-vendored); requires
coordinating state across package management and the build graph.

**Examples:** #12715 (RPC hangs non-deterministically in eager watch mode),
#4156 (PPX built in target context during cross-compilation), #10268
(vendored module name isolation), #12976 (`dune clean` + package management
state ownership).

### D5 -- Design Problem

There is no clear "right fix." The issue reflects a fundamental design
tension that requires RFC-level discussion or a phased migration. Multiple
stakeholders may disagree on the correct behavior. Changing behavior may
break existing users who depend on the current (wrong) behavior.

**Signals:** Long comment threads with disagreement, behavior that different
users rely on in contradictory ways, fix requires deprecation cycle, issue
has been open for years with no resolution.

**Examples:** #1819 (`-no-alias-deps` always set -- changing it breaks
existing users), #8844 (`dune install` to opam prefix -- build system vs
package manager boundary), #13011 (when should pkg deps refresh?), #1920
(case-insensitive filesystem handling).

## Using the Priority Matrix

The most actionable bugs are **high severity + low difficulty**:

| Priority | Combination | Action |
|----------|-------------|--------|
| Immediate | S1/S2 + D1/D2 | Fix now -- dangerous bugs with known fixes |
| High | S1/S2 + D3, or S3-S5 + D1/D2 | Schedule in next milestone |
| Medium | S3-S5 + D3, or any + D4 | Plan with subsystem owner |
| Low | S6/S7 + D2/D3 | Good first issues or backlog |
| Strategic | Any + D5 | Needs RFC / design discussion |

## Limitations

- **Severity is assessed from the issue text only.** Some issues may be
  more or less severe than classified based on how many users are affected,
  which is not always evident from the report.
- **Difficulty is estimated heuristically** based on the description of the
  bug and the subsystems involved. Actual difficulty may vary based on
  codebase familiarity and whether the root cause matches the reported
  symptoms.
- **Classification was performed by automated analysis** of issue titles,
  descriptions, and body text. Edge cases exist where a bug could
  reasonably be assigned to a different severity or difficulty level.
- **Issues were not cross-referenced with PRs or branches.** Some bugs
  may already have partial fixes in progress.
