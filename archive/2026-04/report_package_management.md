# Package Management

## Summary

The package management category contains 59 bugs spanning from issue #878 to #14096, representing problems accumulated over much of Dune's history. The oldest issues (e.g., #878 on `dune subst` adding duplicate version fields, #2100 on dynamic linking failures, #2773 on broken odoc cross-references in sandboxes) date back to early Dune development, while a cluster of newer issues (#13545, #13841, #13878, #14096) point to ongoing regressions and unresolved design problems in the newer `dune pkg` subsystem. A dominant theme is **sandbox path handling**: package variables like `%{pkg:foo:lib}` expand to sandbox paths instead of relative paths (#14096), the generated `topfind` file retains absolute sandbox paths (#10291), environment variables like PATH and OCAMLPATH are not relocated into the sandbox (#10294), and `$DUNE_WORKSPACE` leaks into nested sandbox builds (#12924). These sandbox issues collectively make `dune pkg` unreliable for real-world package builds.

A second major theme is **lock file and solver correctness**. Lock files embed absolute paths for local pins (#13878), making them non-portable. The `lock_dir` workspace stanza is ignored by `dune pkg lock` (#13841). The solver ignores version constraints on optional dependencies (#13223), and locking fails entirely for `ocaml-system` since Dune 3.21.0 (#13545). Offline locking is impossible even when the opam repo is cached (#10508). Variable expansion is also fragile: `%{version:...}` fails when a declared dependency is not yet installed (#13894), and `%{version:pkg}` resolves incorrectly under `-p` (#9882). Type information is lost when variables are serialized in the lock directory, causing string "false" to become boolean false (#9464).

A third cluster involves **opam file generation and interaction with opam**. Dune generates opam files with redundant version constraints (#11106, #3916), silently accepts typos like `:with_test` instead of `:with-test` (#11002), produces incorrect dune version bounds for nested projects (#4051), and does not respect `(lang dune)` settings when generating depends clauses (#3700). The `dune install` command modifies the opam switch without updating opam's state (#8844), and the dune cache cannot populate inside opam's sandbox due to hardlink restrictions (#6162). Several issues also affect tooling integration: `dune utop` fails with unmet dependencies (#12143) or loads conflicting package versions (#10653), `dune fmt` and `dune show targets` unnecessarily build all package dependencies when a lockdir is present (#11037, #11521), and `dune show depexts` triggers a full compiler build (#13677). The breadth and persistence of these bugs suggest that package management remains one of Dune's most problematic areas, with sandbox isolation, lock file correctness, and opam interoperability each requiring focused attention.


### Severity Breakdown

| Severity | Count |
|----------|-------|
| **S1** — Silent Correctness Failures | 6 |
| **S2** — Crashes & Data Loss | 2 |
| **S3** — Broken Documented Behavior | 24 |
| **S5** — Regressions | 4 |
| **S6** — Misleading Errors & Poor UX | 1 |
| **S7** — Workaroundable Bugs | 22 |

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| **D1** — Straightforward Fix | 4 |
| **D2** — Moderate Investigation | 41 |
| **D3** — Subsystem Rework | 9 |
| **D4** — Cross-Cutting Architectural | 2 |
| **D5** — Design Problem | 3 |

## Issues (59 bugs)

- **#14096** `S1` `D2` - Dependency package variables incorrectly expand to sandbox in (run) — Package variables like `%{pkg:foo:lib}` incorrectly expand to sandbox paths inside `(run)` in lock files instead of relative paths
- **#13894** `S3` `D2` - Interactions between `%{version:...}` and OPAM dependencies — `%{version:ppxlib}` fails with error when package is not yet installed, even though it's declared as a dependency; breaks opam CI builds
- **#13878** `S7` `D2` - Lock for local dependency uses absolute path — `dune pkg lock` with local pin uses absolute path instead of relative, making lock files non-portable
- **#13841** `S7` `D2` - `dune pkg lock` doesn't respect `dune-workspace`'s `lock_dir` stanza — Running `dune pkg lock` without arguments ignores the configured `lock_dir` path from workspace and always creates at `dune.lock`
- **#13732** `S3` `D1` - `dune-action-trace` packaging is misconfigured — `opam install dune-action-trace --with-test` fails with missing dependencies due to misconfigured package
- **#13677** `S7` `D2` - dune show depexts triggers building the compiler — `dune show depexts` unnecessarily builds the OCaml compiler when it should not need to
- **#13603** `S3` `D2` - Building opam package Nx fails with linker error, likely due to bad include directory formatting — Package build fails with linker error, suspected dune bug in include directory formatting
- **#13545** `S5` `D2` - Dune 3.21.0 unable to lock project depending on ocaml-system — Regression from 3.20.2: `dune pkg lock` fails when project depends on `ocaml-system` package
- **#13471** `S3` `D2` - pkg: dune utop and #require — `dune utop` with package management produces findlib warnings about non-existent directories when using `#require`
- **#13467** `S1` `D2` - ocamlbuild failing to build dependents if sandbox is not properly cleared up — ocamlbuild hardcodes sandbox paths, causing build failures when sandbox is partially cleared
- **#13223** `S7` `D2` - Constraints are not accounted for `depopts` — Solver ignores version constraints for optional dependencies specified in lock_dir constraints
- **#12976** `S2` `D5` - behavior of `dune clean` is surprising/wrong when used with dune package management — `dune clean` deletes package management data in `_build`, surprising users who lose installed packages/tools
- **#12924** `S7` `D2` - `$DUNE_WORKSPACE` should be cleared in `dune pkg` sandboxes — Environment variable leaks into nested dune calls in sandboxes, causing incorrect behavior
- **#12855** `S1` `D2` - Depext not building at all (and no hint) when no `libraries` field — System dependencies silently not built and no error/hint given, leading to confusing runtime failures
- **#12475** `S3` `D2` - [pkg] build a simple unikernel — Dune pkg fails to build packages due to incorrect handling of directory targets in fetched archives
- **#12390** `S5` `D3` - `dune pkg` no longer picks up the compiler from its cache — Regression in 3.20: compiler is rebuilt from scratch every time instead of being picked up from cache
- **#12143** `S7` `D2` - `dune utop` in a `dune pkg` managed workspace can fail with unmet library dependencies — `dune utop` fails because test-only dependencies (via `:with-test`) are picked up by utop but not actually installed
- **#11999** `S3` `D3` - Dune pkg don't find dune-site plugins for dependencies — Executables using dune-site plugins cannot find plugins from package-managed dependencies
- **#11615** `S3` `D2` - Dune can only understand opam repos matching the layout of opam-repository — Dune fails to find packages in opam repos that use a different (but valid) directory layout
- **#11536** `S3` `D2` - pkgconf: unknown option -- personality — Bug: dune uses `--personality` flag not supported by older pkgconf versions, causing build failures.
- **#11521** `S3` `D2` - `dune show targets` builds package dependencies before printing targets if a lockdir is present — Bug: `dune show targets` should not build dependencies, but does so when a lockdir is present.
- **#11290** `S5` `D3` - `dune subst` issues with OCaml-CI — Bug/regression: `dune subst` fails since 3.17 in directories containing only an `.opam` file, which used to work in 3.16.1.
- **#11276** `S3` `D2` - Package management should Ignore unused opam files when pinning — Bug: unused opam files with missing version info cause build failures when pinning.
- **#11114** `S3` `D2` - Package management fails to read files when lock directory is ignored — Bug: `dune build` fails when the lock directory is listed in `.gitignore` or similar ignore files.
- **#11106** `S7` `D1` - Redundant dune version constraint — Bug: dune generates opam files with duplicate/redundant version constraints (e.g., `"dune" {>= "3.16" & >= "3.16.0"}`).
- **#11062** `S3` `D2` - dune should give priority to libraries in OPAM_SWITCH_PREFIX instead of ocamlc -where — Bug/misfeature: opam-installed packages are ignored in favor of system-wide packages, causing failures.
- **#11037** `S3` `D2` - `dune fmt` and `dune build @fmt` build all the project's dependencies when a lockdir is present — Bug: formatting commands unnecessarily build all project dependencies when a lockdir exists.
- **#11002** `S1` `D3` - opam file generation could be made less error-prone — Bug/misfeature: dune silently generates incorrect opam files from typos like `:with_test` (should be `:with-test`), causing confusing downstream failures.
- **#10970** `S3` `D2` - pkg: dune package management cannot build z3 — Bug: dune package management fails to build the z3 package.
- **#10806** `S2` `D2` - Formatting of multi-line / end of line / block strings — Bug/misfeature: `dune fmt` destroys multi-line string syntax by converting them to normal strings.
- **#10653** `S7` `D2` - dune top --only-package pkg when pkg is also installed globally make the toplevel load both versions — Bug: `dune top` loads both local and globally-installed versions of the same package, causing conflicts.
- **#10509** `S7` `D2` - pkg: adding a lockdir should invalidate built artifacts and force a rebuild — Stale artifacts from a previous build (without lockdir) are not invalidated, leading to potentially incorrect builds
- **#10508** `S3` `D4` - pkg: cannot run `dune pkg lock` while offline — Dune requires internet access even when the opam repo is already cached locally, which is incorrect behavior
- **#10294** `S7` `D4` - Environment Variables aren't relocated to the Sandbox — Environment variables like PATH, OCAMLPATH etc. are not properly relocated when running actions inside the package management sandbox, causing incorrect behavior
- **#10291** `S1` `D3` - pkg: generated topfind file contains sandbox paths — The generated topfind file contains absolute paths to the build sandbox which no longer exist after install, breaking ocamlfind
- **#9882** `S7` `D2` - Incorrect handling of `%{version:pkg}` — `%{version:foo}` always resolves to the project version even when `-p` is used to filter packages, which is incorrect
- **#9727** `S7` `D2` - Interaction between opam and dune broken w/ (opam_file_location inside_opam_directory) — Using opam_file_location causes opam to copy the wrong source folder, resulting in missing compiled artifacts after install
- **#9716** `S1` `D2` - Empty Directories Not Copied — Empty directories are silently dropped when using local directory sources in package management
- **#9464** `S7` `D5` - Introduce a literal syntax for booleans — Variables serialized as strings in lockdir lose type information (string "false" becomes boolean false), a correctness issue
- **#8844** `S7` `D5` - `dune install` shouldn't install to opam prefix — `dune install` modifies opam switch state without updating it, which is a misfeature/incorrect default behavior.
- **#7586** `S3` `D2` - "dune top -p <pkg>" tries to pull the dependencies of unrelated vendored executables — `dune top -p` incorrectly pulls dependencies from unrelated vendored executables
- **#7534** `S3` `D2` - `-p` does not detect packages in `opam/` subfolder even when `(opam_file_location inside_opam_directory)` — `-p` flag fails to find packages located in the `opam/` directory
- **#6162** `S3` `D2` - Cache doesn't work on `opam install` — Dune cache files cannot be hardlinked inside OPAM sandbox, silently failing to populate the cache
- **#5814** `S3` `D3` - Binaries installed using `dune` and `dune-site` via `opam` cannot find sites — Bug: installed binaries get an empty list for site locations, preventing dune-site from working after opam install
- **#5301** `S7` `D2` - Vendored libraries are not linked statically to public libraries that use them — Bug: vendored git submodule libraries are not properly linked statically when installing via opam
- **#5267** `S3` `D2` - [3.0 opam failures] Could not find the .cmi file — Bug: dune 3.0 fails to find .cmi files for packages that built fine with dune 2.x
- **#4962** `S3` `D2` - Vendored dependencies interacting poorly with esy and opam — Vendored deps cause incorrect behavior with esy/opam package managers
- **#4068** `S7` `D2` - Allow to create sublibraries named "opam" — Creating a sublibrary named "opam" causes symlink errors during build
- **#4051** `S7` `D3` - opam file generation: dune bound only considers toplevel project — Generated opam files have incorrect dune version bounds when nested projects use a higher dune language version
- **#3916** `S7` `D1` - Duplicate bounds on autogenerated opam files — Generated opam files contain duplicate dune version bounds (e.g. `{>= "2.7" & >= "2.7"}`)
- **#3868** `S7` `D2` - Incorrect passing of linker options from pkg-config to ocamlmklib — ocamlmklib emits warnings about link options returned by pkg-config (e.g. `-Wl,--export-dynamic`), meaning options are incorrectly passed/omitted
- **#3784** `S6` `D2` - "Too many opam files for package" error is incorrect — Error message references opam files even for packages defined in dune-project, producing a misleading/wrong error
- **#3700** `S7` `D3` - OPAM file generation doesn't respect (lang dune) — When `(lang dune 2.5)` is set but `(dune (>= 1.11))` is specified in depends, dune silently generates an invalid opam file instead of warning
- **#3378** `S3` `D2` - Library variable expansion needs a library installed to work — `%{lib:<pkg>:<file>}` fails when the package only has `install` stanzas and no actual library/executable definition
- **#3192** `S3` `D2` - (package ...) doesn't work when package is installed and not in the workspace — `(deps (package bar))` fails with "No rule found for alias .bar-files" when the package is installed via opam rather than in the workspace
- **#3008** `S5` `D2` - Failed to pass tests: "The selected switch default is not installed" — Test suite fails because it assumes a global opam switch named "default" exists
- **#2773** `S7` `D3` - [sandbox] odoc rules are broken — Odoc rules produce broken cross-references (xref-unresolved) inside the sandbox
- **#2100** `S3` `D2` - [dynlink] Error on dynamic link — Bug: dynamic linking fails with "undefined symbol: caml_mutex_lock" when using Fl_dynload with dune-built libraries
- **#878** `S7` `D1` - `dune subst` can add a duplicate version field in opam — Bug: `dune subst` does not check for an existing version field in opam files before adding a new one, resulting in duplicate version fields
