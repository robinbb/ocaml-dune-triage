# What to work on in ocaml/dune

_Updated 2026-10-02. 913 open issues, 867 classified (338 bugs). 734 are new or have changed since they were last assessed; up to 30 are assessed per run._

Ordered by how soon the work can deliver value, not by severity alone. See [rubric/ranking.md](rubric/ranking.md).

## In progress

- [#10335](https://github.com/ocaml/dune/issues/10335) Cannot build executable in a target directory: Reproducer test pushed to robinbb/dune, branch robinbb-fix-exe-in-dir-target-10335.

## Next up

### 1. [#11017](https://github.com/ocaml/dune/issues/11017) Coqdoc flags --with-header and --with-footer should imply a dependency on the argument files

S1 silent wrong result · D2 moderate · Rocq · size: hours · new

- **Do:** Close as fixed by #11131
- **Why now:** Already fixed: merged PR #11131 added coqdoc_header/coqdoc_footer fields that track their dependencies. Closing takes minutes and makes the tracker more accurate.
- **First step:** Check that coqdoc_header/coqdoc_footer are in the current docs and on main, then close the issue with a comment pointing to #11131 and the new fields.

### 2. [#14267](https://github.com/ocaml/dune/issues/14267) Dune Internal Error with `rocq.theory` and `include_subdirs`

S2 crash or data loss · D1 straightforward · Rocq · size: hours · new

- **Do:** Close as duplicate of #14260 after confirming 3.23+ reports a user error
- **Why now:** A collaborator says main already turns the crash into a proper error. Confirming that and closing takes very little work.
- **First step:** Run the reporter's reproducer on current main and check that it prints a user error, not 'Map.add_exn: key already exists'. Then close as a duplicate of #14260.
- **Risks:** If it still crashes, it becomes a small fix in the rocq rules. The reporter may also push back, since older versions accepted this setup.

### 3. [#15609](https://github.com/ocaml/dune/issues/15609) `dune build` over RPC reports diagnostics twice

S5 regression · D2 moderate · watch mode and RPC · size: hours · new

- **Do:** Land PR #16491 fixing duplicated diagnostics for `dune build` over RPC
- **Why now:** Regression since 3.24.1 that is on the 3.25.0 milestone and release tracker #15593. The fix PR is open, a reproduction test is already merged, and the PR only needs a review.
- **First step:** Review PR #16491 against the merged reproduction test from #15610 and check that the expected output now shows each diagnostic once.
- **Risks:** The fix changes how the watch server reports diagnostics, which affects RPC clients (editors). Check for knock-on changes in other RPC tests.

### 4. [#16226](https://github.com/ocaml/dune/issues/16226) Regression: some setting of `OCAMLFIND_CONF` now raises an error

S2 crash or data loss · D2 moderate · vendoring, ppx, cross-compilation · size: hours · new

- **Do:** Help land PR #16239 fixing the OCAMLFIND_CONF crash for 3.24.3
- **Why now:** Regression in 3.24.2 that blocks MirageOS/solo5 builds in Nixpkgs, and it is planned for the 3.24.3 patch release. The reproduction test is merged and a fix exists, but the PR has been a draft for a month.
- **First step:** Ask Alizter on #16239 what is left before it leaves draft. Then review the change against the merged test from #16236.
- **Risks:** The draft may be waiting on something not mentioned in the thread. The patch release timing depends on the maintainers.

### 5. [#16516](https://github.com/ocaml/dune/issues/16516) Strange dependency cycle error on build with no cycles

S2 crash or data loss · D2 moderate · crash · size: days · new

- **Do:** Help land PR #16518 fixing the spurious dependency cycle from compile_commands.json rules
- **Why now:** High reach: any project that bumps to lang 3.23 and uses copy_files from a parent directory can hit it. The reproduction test is merged and the root cause is known. A good candidate for the 3.25.0 tracker.
- **First step:** Review draft PR #16518. Check that Dir_contents is only evaluated for stanzas with foreign stubs, and add a test case where foreign stubs are present.
- **Risks:** Alizter is actively working on it, so help with review rather than starting a competing fix. There is still an open question about whether the cycle can come back when foreign stubs are used.

### 6. [#11941](https://github.com/ocaml/dune/issues/11941) Dune overwrites the user provided debug flag in foreign stubs

S1 silent wrong result · D1 straightforward · build correctness · size: hours · new

- **Do:** Fix foreign stubs overriding the user's -g0 by moving -g into :standard
- **Why now:** S1 build-correctness bug with a known root cause, an approach a collaborator agreed to, and a previous PR (#11942) that the reporter confirmed worked. Reviving it is a small local diff.
- **First step:** Find out why #11942 was closed unmerged (check its thread). Then re-apply the change in src/dune_rules/foreign_rules.ml with a cram test.
- **Risks:** May need a dune lang version guard to keep current behaviour for older projects. #11942 may have been closed for a reason that still applies.

### 7. [#8352](https://github.com/ocaml/dune/issues/8352) (allow_empty) rules and messages are confusing

S6 misleading error · D1 straightforward · error messages · size: hours · new

- **Do:** Land PR #15071 clarifying the empty-package error
- **Why now:** High-reach UX problem with an approach a collaborator agreed to. The PR has been open since 2026-06 with no activity and needs only a review or rebase.
- **First step:** Rebase PR #15071 on main, check that its message matches the proposed 'has nothing to install' wording, and request review.
- **Risks:** There may be pressure to also mention public_name, or to make (modes js) imply allow_empty. Keep those out of scope.

### 8. [#5313](https://github.com/ocaml/dune/issues/5313) `(dirs ..` with paths of depth ≥ 2 are just ignored

S6 misleading error · D1 straightforward · error messages · size: hours · new

- **Do:** Land PR #14981 rejecting nested paths in (dirs ...)
- **Why now:** Small, already-written PR that turns a silent misconfiguration into an error. Only needs review and landing.
- **First step:** Rebase PR #14981, run the cram tests, and request a maintainer review.
- **Risks:** Rejecting nested paths could break projects that relied on them being silently ignored. Check whether the error needs a lang version guard.

### 9. [#15093](https://github.com/ocaml/dune/issues/15093) `dune describe pp` crashes when given an absolute path

S2 crash or data loss · D1 straightforward · crash · size: hours · new

- **Do:** Fix the `dune describe pp` internal error when given an absolute path
- **Why now:** Internal-error crash with a known fix pattern (from #15104) and an agreed approach. A small local diff that also moves umbrella #12230 forward.
- **First step:** Write a cram test that runs `dune describe pp $PWD/foo.ml`. Then localize the path in describe_pp.ml with Path.Expert.try_localize_external or Arg.Workspace_path.

### 10. [#16375](https://github.com/ocaml/dune/issues/16375) `generate_opam_files` broken in 3.24

S1 silent wrong result · D2 moderate · package management · size: days · new

- **Do:** Fix `dune build <pkg>.opam` silently doing nothing since 3.24
- **Why now:** Regression in the latest release with high reach: many projects regenerate opam files this way. A fix could ship in a 3.24.x point release.
- **First step:** Write a cram test showing `dune build foo.opam` exits 0 without updating the file. Then propose in the issue that it prints a hint pointing to `dune build @opam` (or promotes the file), and get a maintainer to agree.
- **Risks:** No agreed approach yet: maintainers need to decide between a promotion and a warning or error. Interacts with the intentional behaviour change in #14108.

### 11. [#15060](https://github.com/ocaml/dune/issues/15060) dune cache clear/trim doesn't delete cache files from old layout

S5 regression · D2 moderate · package management · size: days · new

- **Do:** Make `dune cache clear` and `dune cache trim` remove entries in the pre-3.22 cache layout
- **Why now:** High reach: after an upgrade, the cache grows without bound and the existing commands can't reclaim the space. The first step is agreed and has a reproducer.
- **First step:** Check with dibrinsofor on the issue whether they are still working on it. If not, write a cram test that seeds an old-layout cache directory, then extend clear/trim to delete the legacy versioned directories.
- **Risks:** Someone offered to work on it, so coordinate before starting. There is an open question about how to handle future layouts. The size-accounting discrepancy sim642 reported may be a separate bug.

### 12. [#9979](https://github.com/ocaml/dune/issues/9979) Dune links against wrong cstubs in byte mode

S1 silent wrong result · D2 moderate · build correctness · size: days · new

- **Do:** Fix byte-mode linking so local stub libraries come before installed stublibs
- **Why now:** S1 that hits developers of libraries also installed in their switch (eio, mirage-crypto). A failing test is already merged and two maintainers support reordering the -I flags.
- **First step:** In the bytecode link rule, put the -I flags for local libraries before the installed stublibs directory, and update the expected output of the test from #10028.
- **Risks:** The approach has support but has not been formally agreed. Reordering -I flags may change behaviour in other link setups, such as #3910.

## This run

- Assessed 30 new or changed issues and refreshed 0 shortlisted ones.
- 0 tracked issues closed since the last run.
- 5 claude calls, about $1.07 at API prices.
