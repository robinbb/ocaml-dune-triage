# Vendoring & Cross-Compilation

## Summary

This category contains 28 bugs spanning issue numbers #2420 through #13768, representing some of the oldest unresolved problems in Dune. The issues cluster around three interrelated areas: vendored directory isolation failures, cross-compilation context confusion, and PPX preprocessing defects. The common thread is that Dune's abstractions for build contexts, library namespacing, and vendored project boundaries leak in practice, producing incorrect builds, silent miscompilation, or confusing errors.

Vendoring is the most heavily affected area, with at least 12 issues stemming from insufficient isolation of vendored code. Module name conflicts between vendored and non-vendored libraries (#10268, #4070, #3913) show that vendored libraries are not properly sandboxed — duplicate module names or matching public names cause spurious conflict errors rather than being resolved by the vendoring boundary. Vendored directories also break in subtler ways: warnings leak through nested vendored paths (#6128), recursive aliases like `@all` are overly suppressed (#10144, #3151), `dune-build-info` reports the wrong version (#8025), tests run from the wrong directory (#7043), and directories with leading underscores are silently ignored (#7811). Even broken symlinks that play no role in the build cause failures (#7573). These collectively suggest that `vendored_dirs` was implemented as a shallow overlay rather than a robust isolation mechanism, and edge cases have accumulated over years without a unified fix.

Cross-compilation and build context bugs are fewer but high-impact. The most critical is #4156, where PPX rewriters are built in the target context instead of the host context, directly breaking cross-compilation workflows. Similarly, explicit `.exe` dependencies resolve to the wrong context (#3917), file promotion is non-deterministic across contexts (#11138), and percent-form paths can escape from one context to another (#10173), which is both a correctness and a potential security concern. The `--context` flag itself behaves inconsistently between `dune build` and `dune exec` (#9672, #13768). On the PPX side, several bugs are independent of cross-compilation: PPX order is silently reshuffled (#13551), PPX is silently skipped when the library is byte-only (#9650), bad PPX annotations are not reported (#5238), `staged_pps` is unsupported in `dune describe pp` (#8587), and `Fl_dynload` does not work in PPX rewriters (#3214). The PPX issues are particularly insidious because several of them fail silently — the user gets a successful build but incorrect output.


### Severity Breakdown

| Severity | Count |
|----------|-------|
| **S1** — Silent Correctness Failures | 6 |
| **S3** — Broken Documented Behavior | 10 |
| **S5** — Regressions | 1 |
| **S7** — Workaroundable Bugs | 11 |

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| **D2** — Moderate Investigation | 17 |
| **D3** — Subsystem Rework | 2 |
| **D4** — Cross-Cutting Architectural | 8 |
| **D5** — Design Problem | 1 |

## Issues (28 bugs)

- **#13768** `S7` `D4` - Usability issues with Dune contexts — `dune exec --context=tsan` picks up the wrong binary from the default context instead of the specified one
- **#13551** `S7` `D2` - Dune should respect user-specified PPX order in `(preprocess (pps ...))` stanza — Dune alphabetically sorts PPX transformations, discarding user-specified order which is semantically significant
- **#11138** `S1` `D4` - Promotion and cross-compilation — Bug: file promotion with cross-compilation is non-deterministic; the wrong file may be promoted.
- **#10423** `S3` `D2` - GCC and GLIBC supported minimums for Dune on Linux — Dune fails to build on platforms where OCaml itself builds fine, due to vendored C code using C99 features without requesting C99 mode
- **#10268** `S7` `D4` - Module name conflict with vendored library — Vendored libraries with duplicate module names cause unexpected compilation errors; vendored libraries are not properly isolated
- **#10173** `S7` `D4` - Percent forms are allowed to escape from one context to another — Security/correctness issue where relative paths in percent forms can access files from other build contexts
- **#10144** `S7` `D2` - All Recursive Aliases are broken in vendored directories — Recursive aliases (not only test-related ones) are disabled in vendored directories, which is too aggressive
- **#9687** `S7` `D2` - Inconsistent assumptions over interface when additional copy of library is present in vendored_dirs — Vendored directories within installed packages leak module definitions, causing inconsistent assumption errors
- **#9672** `S7` `D2` - Bug/Request `--context` should work the same with dune build and dune exec — `dune build --context=foo` does not restrict to the specified context (builds all contexts), unlike `dune exec --context=foo` which works correctly
- **#9650** `S1` `D2` - ppx is skipped when `(modes byte)` — PPX rewriter is silently not applied when the PPX library has `(modes byte)`, causing extension points to remain unexpanded
- **#8587** `S3` `D2` - Add support for `staged_pps` in `dune describe pp` — `dune describe pp` does not work for staged PPXs, producing an error instead of the expected output; acknowledged as an unfixed bug.
- **#8025** `S1` `D3` - dune-build-info reports wrong library version in vendored dir — Library version is incorrectly reported as the git hash of the CWD repository instead of the actual library version.
- **#7811** `S3` `D2` - Vendoring of foreign source trees with leading underscores — Dune silently ignores directories with leading underscores in vendored foreign source trees, causing missing file errors.
- **#7573** `S3` `D2` - Build failing due to existence of broken symbolic link (unused in build) — Dune fails the build when a broken symlink exists in vendored sources even though it is not used by the build
- **#7043** `S7` `D2` - Dune tests are being executed in unexpected dir while vendoring — Tests in vendored projects execute from `%{workspace_root}` instead of the vendored `%{project_root}`
- **#6830** `S3` `D2` - Rule collision when multiple vendored projects contain executables with matching names — Dune errors with "Multiple rules generated" when two vendored packages both contain executables with the same public name
- **#6128** `S1` `D2` - Warnings leak through `vendored_dirs` subpath — Bug: nested vendored directories still emit warnings that should be suppressed
- **#6106** `S5` `D2` - dune 3.0 cannot find file through relative path during ppx preprocessing — Bug: regression in dune 3.0+ where ppx_blob can no longer find files via relative paths that worked in earlier versions
- **#5238** `S1` `D2` - Bad ppx annotations are not reported — Bug: invalid/unused ppx annotations are silently ignored instead of producing errors
- **#4156** `S3` `D4` - ppxs are built in the target context in cross-compilation settings — PPX libraries are incorrectly built in the target context instead of the host context during cross-compilation, causing build failures
- **#4070** `S1` `D4` - Undesired conflict between vendored library and public library by the same name — Dune incorrectly reports a conflict when a vendored library has the same name as an external one used by a different dependency
- **#3917** `S3` `D4` - Explicit executable dependencies and cross-compilation — Explicit .exe dependencies in rules resolve to cross-compiled workspace instead of host context, breaking cross-compilation
- **#3913** `S7` `D4` - Dune finds non existing library conflict without (implicit_transitive_deps false) — Dune incorrectly detects a library conflict that doesn't actually exist in certain vendoring scenarios
- **#3645** `S3` `D2` - "The module X is an alias for module Y.X, which is missing" when X comes from a virtual library — Aliased modules from virtual libraries produce incorrect errors when installed/pinned (works when vendored)
- **#3382** `S3` `D2` - "Unknown constructor vendored_dirs" when using OCaml syntax — `vendored_dirs` works in static dune files but fails with "Unknown constructor" when using OCaml (tuareg) syntax
- **#3214** `S3` `D2` - Fl_dynload.load_packages in a PPX — `findlib_initl.ml-gen` is not generated for PPX preprocessors, so `Fl_dynload.load_packages` fails in PPX rewriters
- **#3151** `S7` `D5` - Recursive alias in vendored directories are not well defined — `@all` and `@@all` behave inconsistently in vendored directories
- **#2420** `S7` `D3` - Configurator does not have access to C flags set in (env) — Bug: configurator ignores C flags set in workspace env stanza, producing incorrect build configuration results in multi-context workspaces
