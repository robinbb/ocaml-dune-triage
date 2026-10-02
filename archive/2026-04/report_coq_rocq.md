# Coq & Rocq Integration

## Summary

The 25 open bugs in this category reveal a subsystem that has accumulated significant technical debt across several years, with issues spanning from #3286 to #13774. The oldest bugs date back to fundamental design gaps -- such as `Load` commands failing under `dune build -p` (#3286) and Coq's native compilation breaking on macOS (#6393) -- while the newest reflect the ongoing Coq-to-Rocq transition, where Dune hardcodes `rocq --config` in a way that locks out Rocq 9.0 (#13774) and generates `_RocqProject` files incompatible with VSRocq (#13738). The breadth of issue ages suggests that Coq/Rocq integration receives limited maintenance attention relative to the number of open defects.

A dominant theme is broken dependency tracking and caching around `coqdep`. Dune does not reinvoke `coqdep` when files are added or removed (#6149), and worse, it caches failing `coqdep` results so that adding the missing file does not fix the build without a clean (#6145). Compositional builds are also affected: paths are relativized to the outer workspace root rather than the inner project, defeating build caching across project boundaries (#6005). These caching and dependency-tracking bugs undermine a core promise of Dune -- correct incremental builds -- and likely force Coq users into frequent `dune clean` cycles.

The second major cluster involves plugin loading and dynamic linking. Transitive OCaml dependencies of Coq plugins are not resolved correctly: `.cmxs` files are not placed where Coq expects them (#11012), the `plugins` field is not transitively closed (#6615), and dynlink errors arise with foreign archives like Rust static libraries (#6844) or during plugin loading generally (#10659). Spurious warnings about already-found plugins (#8026, #7155) add noise. Beyond plugins, several bugs produce raw internal errors (uncaught exceptions, `List.hd`, `as_in_build_dir_exn`) instead of user-facing diagnostics (#11618, #11014, #10679, #7053), and basic scenarios like empty theories (#11836, #12109) or `coq.extraction` combined with `coq.theory` (#11014) crash rather than report the problem clearly. Documentation generation (`coqdoc`) also has multiple open issues (#11017, #11016, #5864), indicating that the coqdoc integration is incomplete.


### Severity Breakdown

| Severity | Count |
|----------|-------|
| **S1** — Silent Correctness Failures | 1 |
| **S2** — Crashes & Data Loss | 7 |
| **S3** — Broken Documented Behavior | 12 |
| **S6** — Misleading Errors & Poor UX | 2 |
| **S7** — Workaroundable Bugs | 3 |

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| **D1** — Straightforward Fix | 1 |
| **D2** — Moderate Investigation | 8 |
| **D3** — Subsystem Rework | 15 |
| **D5** — Design Problem | 1 |

## Issues (25 bugs)

- **#13774** `S3` `D3` - Rocq rules do not support Rocq 9.0 — Dune always invokes `rocq --config` which only works in Rocq 9.1+, making it impossible to build Rocq 9.0 projects without warnings
- **#13738** `S3` `D3` - `(generate_project_file)` is not compatible with VSRocq — Generated `_RocqProject` file doesn't work with VSRocq editor; `include_subdirs qualified` has no effect on generation
- **#12109** `S3` `D2` - Empty Coq/Rocq theory leads to package error — `dune build` incorrectly claims a package has no stanzas when it has a `coq.theory` stanza
- **#11836** `S2` `D2` - Dune cannot build empty `coq.theory` — Fatal exception when building a coq.theory with `(modules )` that excludes all Coq files
- **#11618** `S2` `D3` - Internal error: [as_in_build_dir_exn] called on something not in build dir — Internal crash when building Rocq/Coq projects with opam-installed plugins; should be a user-facing error
- **#11190** `S2` `D3` - Internal error with `(env (_ (binaries (../tools/myrock.exe as coqc))))` — Bug: internal dependency cycle error when trying to override coqc binary via env stanza.
- **#11017** `S3` `D1` - Coqdoc flags --with-header and --with-footer should imply a dependency on the argument files — Bug: changes to coqdoc header/footer files don't trigger documentation rebuild due to missing dependency tracking.
- **#11016** `S3` `D2` - Coq documentation generation fails with Coq in the workspace — Bug: coqdoc rules don't receive correct environment variables to locate the standard library when Coq is in the workspace.
- **#11014** `S2` `D3` - `coq.extraction` + `coq.theory` raises internal errors — Bug: combining `coq.extraction` and `coq.theory` stanzas produces unhelpful internal errors instead of a clear diagnostic.
- **#11012** `S3` `D3` - Coq cannot find the cmxs file for transitive ocaml dependencies — Bug: dune fails to place `.cmxs` files for transitive OCaml dependencies where Coq expects them.
- **#10679** `S2` `D3` - `coq.extraction`: Adding a nested module to `extracted_modules` raises an internal error — Bug: internal error occurs when using nested modules in `extracted_modules` field.
- **#10659** `S3` `D3` - Dynamic linking error via a Coq plugin or running an executable — Bug: dynamic linking errors occur when using Coq plugins, possibly due to dune's handling of linking.
- **#8026** `S6` `D3` - Warning: ltac_plugin.cmxs already found — Spurious warning when building Coq plugins that use `coq-core.plugins.ltac`; the warning is confusing and indicates incorrect library path handling.
- **#7155** `S7` `D3` - Spurious warning when a private library is in the deps of a Coq plugin — False warning triggered when a Coq plugin has a private library in its transitive dependencies
- **#7091** `S3` `D2` - Dune cannot handle `From ... Extra Dependency` — Dune fails to build Coq files using `From ... Extra Dependency` because non-`.v` files are not copied to the target directory
- **#7053** `S2` `D2` - Dune does not validate non-existent Coq modules being excluded — Excluding non-existent Coq modules silently accepted, and using `(modules \ I.dont.exist)` causes a `List.hd` exception
- **#6844** `S3` `D3` - Bug when linking ocaml with a dune package including a static library — Dynlink error when linking a Coq plugin that includes a Rust-built static library via foreign_archives
- **#6615** `S7` `D3` - `coq.theory` stanza should work on the transitive closure of the `plugins` field — Coq plugin dependencies are not transitively resolved, causing Coq to fail to find required libraries
- **#6393** `S3` `D3` - coq: native compilation failing on macos — Coq native compilation fails on macOS with linker warning about missing directory
- **#6149** `S1` `D3` - Dune does not rerun coqdep if filesystem layout changes — Dune does not reinvoke `coqdep` when files are added/removed, causing stale dependency information
- **#6145** `S2` `D3` - dune caches "failing" coqdep invocations even when adding missing files — Bug: coqdep returning wrong output gets cached, corrupting the build; adding the missing library does not fix the build without cleaning
- **#6005** `S7` `D5` - Compositional Coq builds depend on the current root — Bug: paths in compositional Coq builds are relative to the outer root rather than the inner project, defeating build caching
- **#5864** `S3` `D2` - [coq] [coqdoc] Coqdoc doesn't work when a boot library is present — Bug: coqdoc is not passed `-coqlib` for the `-boot` library, causing it to fail
- **#4949** `S6` `D2` - Remove runtime dependency on OCaml when building a pure Coq project — Dune incorrectly requires ocamlc even when building a project that needs no OCaml, producing a misleading error
- **#3286** `S3` `D2` - Failing package builds with Load commands in Coq files — `dune build -p` doesn't copy non-module files needed by Coq's `Load` command into the build tree, causing build failures
