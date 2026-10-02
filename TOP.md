# What to work on in ocaml/dune

_Updated 2026-10-01. 914 open issues, 837 classified (324 bugs). 765 are new or have changed since they were last assessed; up to 30 are assessed per run._

Ordered by how soon the work can deliver value, not by severity alone. See [rubric/ranking.md](rubric/ranking.md).

## In progress

- [#10335](https://github.com/ocaml/dune/issues/10335) Cannot build executable in a target directory: Reproducer test pushed to robinbb/dune, branch robinbb-fix-exe-in-dir-target-10335.

## Next up

### 1. [#11017](https://github.com/ocaml/dune/issues/11017) Coqdoc flags --with-header and --with-footer should imply a dependency on the argument files

S1 silent wrong result · D2 moderate · Rocq · size: hours · new

- **Do:** Close as fixed by #11131
- **Why now:** The fix was merged in #11131 (coqdoc_header/coqdoc_footer fields), but the issue is still open. Closing it takes minutes.
- **First step:** Check that #11131 is in a released dune and that the docs mention the new fields, then close with a comment linking #11131.

### 2. [#14267](https://github.com/ocaml/dune/issues/14267) Dune Internal Error with `rocq.theory` and `include_subdirs`

S2 crash or data loss · D1 straightforward · Rocq · size: hours · new

- **Do:** Close as a duplicate of #14260 once it is confirmed that 3.23 reports a user error
- **Why now:** A collaborator says main already gives a proper error instead of the internal error. Checking that and closing is quick.
- **First step:** Run the reporter's rocq.theory + rocq.extraction + include_subdirs reproducer on current main and check that the output is a user error, not Map.add_exn.
- **Risks:** If it still crashes, it becomes a real fix in Rocq rules, which is an unfamiliar area.

### 3. [#11941](https://github.com/ocaml/dune/issues/11941) Dune overwrites the user provided debug flag in foreign stubs

S1 silent wrong result · D1 straightforward · build correctness · size: hours · new

- **Do:** Fix foreign stubs overriding the user's -g0 by moving -g into :standard (revive #11942)
- **Why now:** S1 silent build-correctness bug. The approach is agreed, a prototype exists that the reporter confirmed works, and the diff is a small one in dune_rules (foreign_rules.ml).
- **First step:** Read why #11942 was closed unmerged. Then rebase or redo it on main with a cram test showing that `:standard \ -g` drops -g.
- **Risks:** May need a dune lang version guard to keep the current flag order for older projects. #11942 may have been closed for a reason that still applies.

### 4. [#16375](https://github.com/ocaml/dune/issues/16375) `generate_opam_files` broken in 3.24

S1 silent wrong result · D2 moderate · package management · size: days · new

- **Do:** Fix `dune build <pkg>.opam` silently doing nothing since 3.24
- **Why now:** S1 regression in the latest release with high reach. It is in opam-file generation, a familiar area, and a fix could ship in a 3.24 point release.
- **First step:** Write a cram test showing that `dune build foo.opam` exits 0 without updating the file. Then ask Alizter on the issue whether promoting or a hint pointing to `@opam` is preferred.
- **Risks:** No fix is agreed for the explicit-target case. The behaviour change from #14108 may have been intentional, which would limit the fix to a hint.

### 5. [#8352](https://github.com/ocaml/dune/issues/8352) (allow_empty) rules and messages are confusing

S6 misleading error · D1 straightforward · error messages · size: hours · new

- **Do:** Land PR #15071 (clearer empty-package / allow_empty error)
- **Why now:** High-reach UX confusion. A maintainer's PR already exists and only needs review, plus whatever follow-up the review asks for.
- **First step:** Review #15071, rebase it if needed, check the cram test output, and ping rgrinberg to merge.
- **Risks:** Side questions (mention public_name? should `(modes js)` imply allow_empty?) could widen the scope. Keep them out of the PR.

### 6. [#5313](https://github.com/ocaml/dune/issues/5313) `(dirs ..` with paths of depth ≥ 2 are just ignored

S6 misleading error · D1 straightforward · error messages · size: hours · new

- **Do:** Land PR #14981 (reject nested paths in `dirs`)
- **Why now:** The PR is open and only needs review or a rebase. Turning a silent no-op into an error is a small change.
- **First step:** Review #14981, rebase it on main, check the error test, and ask rgrinberg about merging.
- **Risks:** Projects that currently have harmless nested `dirs` entries will start to fail. Check whether a lang version guard is needed.

### 7. [#14085](https://github.com/ocaml/dune/issues/14085) 3.22.0 regression: error about non-existent excluded module from `(select)` in a different stanza

S5 regression · D2 moderate · build correctness · size: days · new

- **Do:** Fix the 3.22.0 regression where excluding a `(select)`-generated module from another stanza's modules errors
- **Why now:** A regression that blocks downstream: goblint added a conflict with dune 3.22. It is in library dependencies and module selection, a familiar area.
- **First step:** Turn the reporter's reproducer into a cram test, then bisect 3.21.1..3.22.0 (anmonteiro's changes are suspected).
- **Risks:** Root cause unknown, and the fix may need anmonteiro's input.

### 8. [#9979](https://github.com/ocaml/dune/issues/9979) Dune links against wrong cstubs in byte mode

S1 silent wrong result · D2 moderate · build correctness · size: days · new

- **Do:** Fix byte-mode linking picking installed stublibs before local ones
- **Why now:** S1 correctness bug for anyone developing a library that is also installed in the switch (eio, mirage-crypto). A failing test (#10028) is already merged, and the proposed fix is local.
- **First step:** Find where the bytecode link rule emits the -I stublibs flags, order local libraries before installed ones, and update the expected output of the #10028 test.
- **Risks:** No maintainer has formally signed off on the approach, only proposals and support. Reordering could change other users' link behaviour.

### 9. [#15060](https://github.com/ocaml/dune/issues/15060) dune cache clear/trim doesn't delete cache files from old layout

S5 regression · D2 moderate · package management · size: days · new

- **Do:** Make `dune cache clear`/`trim` remove pre-3.22 cache layout entries
- **Why now:** High reach: after an upgrade the cache grows without bound. The first step is agreed and the scope is clear.
- **First step:** Ask dibrinsofor on the issue whether they are still working on it. If not, write a cram test that seeds a legacy-layout cache dir and extend clear/trim to delete it.
- **Risks:** A contributor offered to do it (no PR yet). The open question about future layout versions, and the separate size-accounting problem sim642 reported, could widen the scope.

### 10. [#8025](https://github.com/ocaml/dune/issues/8025) dune-build-info reports wrong library version in vendored dir

S1 silent wrong result · D2 moderate · vendoring, ppx, cross-compilation · size: days · new

- **Do:** Make dune-build-info return None for versionless projects in vendored dirs
- **Why now:** The approach was agreed at a dev meeting. It affects opam-monorepo and mirage users and has waited since 2023.
- **First step:** Write a cram test with a vendored dune-project without (version) inside a git repo, showing the wrong version, then implement the None case.
- **Risks:** There is no reproducer yet, so building one is the first piece of work.

### 11. [#15755](https://github.com/ocaml/dune/issues/15755) It looks like --force doesn't rerun cram tests. Should it?

S3 broken documented behavior · D2 moderate · build correctness · size: days · new

- **Do:** Help land PR #16237 so `dune test --force` reruns cram tests
- **Why now:** Recent, has medium reach, and a fix PR apparently exists. Cram tests are a familiar area.
- **First step:** Find PR #16237, check its author and status, and review it against a cram test showing that `--force` reruns a .t file.
- **Risks:** Maintainers disagree on what --force should mean (shonfeder vs Alizter), so the PR may stall on design.

### 12. [#5104](https://github.com/ocaml/dune/issues/5104) Possible regression in the `select` stanza

S6 misleading error · D1 straightforward · error messages · size: hours · new

- **Do:** Add an upgrade hint to the `select` file-format error and document the naming restriction
- **Why now:** Small change in lib_dep.ml, a familiar area. It removes a confusing error that has no hint.
- **First step:** Write a cram test with a `select` branch pointing to foo/a.foo.ml, then add a hint suggesting a copy rule into a.{name}.ml.
- **Risks:** Low reach. A maintainer may prefer relaxing the check (as bobot suggested) over a hint.

## This run

- Assessed 30 new or changed issues and refreshed 58 shortlisted ones.
- 0 tracked issues closed since the last run.
- 14 claude calls, about $3.43 at API prices.
