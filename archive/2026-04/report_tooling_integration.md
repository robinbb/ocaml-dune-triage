# Tooling Integration

## Summary

The 34 open bugs in this category span from issue #1187 to #13566, indicating that some tooling integration problems have persisted for years without resolution. The issues cluster around several distinct subsystems: the `@ocaml-index` alias (issues with vendored libraries, cross-compilation over-building, empty output from subdirectories, and failures with multiple executables), Merlin/LSP integration (false "Unbound module" errors tied to executable ordering, missing source entries for virtual libraries, broken locate for private modules, ppx_expect regressions, and incorrect `.merlin` files when paths contain spaces), formatting via `dune fmt` (ignoring `--disable-promotion`, requiring `ocamlc` unnecessarily, triggering menhir builds, failing on missing optional dependencies, and not formatting `dune-project` files), and toplevel/REPL support (`dune utop` and `#use_output "dune ocaml top"` failing with undefined globals for `dune-build-info`, `dune-site`, and virtual libraries).

A recurring pattern is that dune's build graph bleeds into tooling commands that should be lightweight. For instance, `dune fmt` unexpectedly triggers menhir parser generation (#7454), cram tests pull in odoc as a dependency (#11633), and `@ocaml-index` builds cross-compilation targets it should ignore (#12007). Another pattern involves vendored or multi-project setups causing conflicts: `@ocaml-index` fails with vendored library conflicts (#10896), and dune applies the top-level project's warning-as-error policy to vendored packages (#7034). The Merlin-related bugs are particularly impactful for day-to-day developer experience, as issues like #12611 (false errors depending on alphabetical ordering of executables) and #4892 (missing build paths for private modules) directly break editor navigation and error reporting.

The documentation tooling (`@doc`, `@doc-new`, odoc) also has long-standing issues: `dune build @doc` fails to rebuild after `.mli` changes (#7720), fails entirely with missing Stdlib (#5229), and produces errors on valid module name collisions in unwrapped sub-libraries (#1645). The MDX test integration has its own problems, with `dune runtest --force` not re-triggering mdx tests (#13418) and the mdx stanza silently ignoring missing dependencies (#4971). Together, these bugs paint a picture of tooling integrations that work in simple project layouts but break under real-world conditions involving vendoring, workspaces, virtual libraries, and cross-compilation.


### Severity Breakdown

| Severity | Count |
|----------|-------|
| **S2** — Crashes & Data Loss | 1 |
| **S3** — Broken Documented Behavior | 18 |
| **S5** — Regressions | 2 |
| **S6** — Misleading Errors & Poor UX | 1 |
| **S7** — Workaroundable Bugs | 12 |

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| **D2** — Moderate Investigation | 26 |
| **D3** — Subsystem Rework | 6 |
| **D4** — Cross-Cutting Architectural | 2 |

## Issues (34 bugs)

- **#13566** `S3` `D3` - @ocaml-index fails when multiple executables in a directory don't specify (modules) — ocaml-index fails with "Unbound module" when multiple executables share a directory without explicit module specifications
- **#13418** `S3` `D2` - `dune runtest --force` does not work for `(mdx)` stanza — `dune runtest --force` fails to re-trigger mdx tests
- **#12611** `S7` `D2` - [Merlin] Curious Unbound module issue — Merlin/LSP reports false "Unbound module" errors depending on alphabetical ordering of executables in a dune file
- **#12007** `S7` `D2` - dune build @ocaml-index builds too many files — The `@ocaml-index` alias incorrectly builds cross-compilation targets and unreferenced files
- **#11633** `S7` `D2` - odoc required by cram depending on objs/byte — Cram tests with `(deps (glob_files .foo.objs/byte/*))` incorrectly require odoc to be installed
- **#11500** `S3` `D2` - `@ocaml-index` is empty when not built from the root of a project — Bug: `@ocaml-index` alias produces no output when invoked from a subdirectory, unlike other aliases.
- **#11229** `S2` `D3` - Dune developer preview: ocamllsp cannot read stdlib.cmi (corrupted compiled interface) — Bug: ocamllsp fails with corrupted compiled interface when using dune developer preview.
- **#11038** `S7` `D2` - `dune fmt` requires `ocamlc` to be in path but does not guarantee that this is the case — Bug: `dune fmt` with dev tools fails when `ocamlc` is not in PATH, even though dune should provide it.
- **#10896** `S3` `D4` - Using `@ocaml-index` with vendored libraries: `Error: Conflict between the following libraries` — Bug: `dune build @ocaml-index` fails with conflict errors when vendored libraries are present.
- **#10578** `S3` `D2` - `dune build @fmt` exits with 1 if `ocamlformat` is not installed — Dune errors out instead of gracefully skipping ocamlformat rules when no .ocamlformat file is present and ocamlformat is not installed, breaking CI workflows
- **#9943** `S3` `D2` - dune fmt should not fail to format when depopt isn't available / `and` isn't lazy — `dune fmt` fails when an optional dependency is not installed due to `enabled_if` evaluation, and `and` is not evaluated lazily as expected
- **#9744** `S7` `D2` - @doc-new's index.html might be missing a link to `/local/index.html` — Navigation links are broken in generated documentation; clicking a subindex and going "up" does not return to the expected page
- **#8626** `S3` `D2` - `#use_output "dune ocaml top"` fails in a project where `dune utop` works — Command fails with undefined global reference even though `dune utop` works fine in the same project; inconsistent behavior.
- **#7720** `S3` `D3` - `dune build @doc` does not rebuild pages — After modifying `.mli` files, `dune build @doc` does not rebuild the documentation pages and produces dangling links; broken incremental rebuild.
- **#7470** `S3` `D3` - `dune-site` cannot be used in top-level REPL — Loading `dune-site` in OCaml toplevel raises `Error: Reference to undefined global 'Dune_site__Dune_site_data'`
- **#7454** `S7` `D2` - `dune fmt` unexpectedly triggers menhir rules — `dune fmt` / `dune build @fmt` builds menhir parsers when it should not build anything
- **#7034** `S5` `D4` - Dune treats warnings as errors according to the workspace `lang dune` version when building vendored packages with a more permissive `lang dune` version — Warning-as-error settings from top-level `dune-project` version are applied to vendored packages instead of respecting their own `lang dune` version
- **#6680** `S3` `D2` - OCaml toplevel sometimes fails to load default implementation for a virtual library — `#require` in toplevel fails to load default implementation for virtual libraries, causing undefined global errors
- **#5946** `S3` `D2` - `dune fmt` ignores `--disable-promotion` flag — Bug: the `--disable-promotion` flag is not honored by `dune fmt`, causing unexpected file promotion
- **#5566** `S7` `D2` - Error: Reference to undefined global `Build_info__Build_info_data' — Bug: dune-build-info cannot be loaded in an OCaml toplevel due to missing generated module
- **#5322** `S3` `D3` - Relocatable site does not work when the install directory is outside the build directory — Bug: site location placeholder is replaced by absolute path regardless of --relocatable flag
- **#5229** `S3` `D2` - @doc "Couldn't find the following modules: Stdlib" — Bug: `dune build @doc` fails with missing module errors for Stdlib and other installed libraries
- **#4971** `S3` `D2` - MDX stanza not causing dependencies to be built — Bug: mdx stanza silently ignores missing files instead of raising an error or building them
- **#4892** `S3` `D2` - Private modules cause missing build path (in the ocaml-merlin dump) — Merlin config is missing the byte directory for libraries with private modules, causing locate failures
- **#4866** `S7` `D2` - dune doesn't cleanup all .merlin files and doesn't inform user of using them — Dune leaves behind stale generated .merlin files and doesn't inform users about the transition
- **#4479** `S5` `D2` - interop between dune and merlin since 2.8 does not work with ppx_expect — Regression: merlin queries fail with ppx_expect after upgrading from dune 2.7.1 to later versions
- **#4111** `S7` `D2` - Dune doesn't generate correct .merlin file when directory path contains space — Generated .merlin file has incorrect path escaping when project path contains spaces
- **#3642** `S7` `D2` - Adding new formatters can break older projects — Dune tries to invoke ocamlformat even without a `.ocamlformat` file, producing warnings/errors for projects that don't use it
- **#3516** `S7` `D2` - dune format-dune-file doesn't respect the formatting stanza — `dune format-dune-file` ignores the `(formatting (enabled_for ocaml reason))` stanza and formats dune files anyway
- **#3487** `S6` `D2` - Hinted `external-lib-deps` for `dune utop` does not include Odoc — The suggested `dune external-lib-deps --missing` command does not detect the missing `utop` library, giving misleading guidance
- **#3223** `S7` `D2` - dune-project not formatted with @fmt — `dune build @fmt` does not format the `dune-project` file, inconsistent with formatting of other dune files
- **#2909** `S3` `D3` - Virtual Libraries: Dune files don't include required source entries when relying on virtual modules — Generated `.merlin` files for modules depending on virtual libraries lack `S` source entries, breaking goto-location in merlin
- **#1645** `S3` `D2` - Odoc: valid module name clashes cause issues — Bug: dune/odoc produces "multiple rules generated" errors when two valid sub-libraries in the same package have unwrapped modules with the same name, even though they cannot be linked together
- **#1187** `S3` `D2` - $ dune utop doesn't work for dune itself — Bug: `dune utop` fails with "Required module `Which_program' is unavailable" error when used on the dune project itself
