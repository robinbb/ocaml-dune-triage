# ocaml/dune — Open Issues Classified as Bugs

Generated: 2026-04-10 (updated: 2026-04-12)

Out of **1,003 open issues**, **404** were identified as actual bugs, misfeatures,
or problems (incorrect behavior, crashes, regressions, things not working as documented).
8 issues from the original 412 have since been closed or fixed.

Issues classified as feature requests, enhancements, RFCs, documentation-only,
chores, and performance optimizations were excluded.

Each bug is tagged with a severity (S1-S7) and difficulty (D1-D5).
See [methodology.md](methodology.md) for classification criteria.

## Severity Distribution

| Severity | Description | Count |
|----------|-------------|-------|
| **S1** | Silent Correctness Failures | 30 |
| **S2** | Crashes & Data Loss | 54 |
| **S3** | Broken Documented Behavior | 136 |
| **S4** | Platform/Environment Blockers | 34 |
| **S5** | Regressions | 34 |
| **S6** | Misleading Errors & Poor UX | 17 |
| **S7** | Workaroundable Bugs | 99 |
| | **Total** | **404** |

## Difficulty Distribution

| Difficulty | Description | Count |
|------------|-------------|-------|
| **D1** | Straightforward Fix | 18 |
| **D2** | Moderate Investigation | 229 |
| **D3** | Subsystem Rework | 110 |
| **D4** | Cross-Cutting Architectural | 31 |
| **D5** | Design Problem | 16 |
| | **Total** | **404** |

## Priority Matrix (Severity x Difficulty)

| | D1 | D2 | D3 | D4 | D5 |
|---|---|---|---|---|---|
| **S1** | 0 | **19** | **7** | **4** | 0 |
| **S2** | 0 | **8** | **37** | **6** | **3** |
| **S3** | **3** | **97** | **24** | **7** | **5** |
| **S4** | **4** | **6** | **23** | **1** | 0 |
| **S5** | **4** | **19** | **8** | **2** | **1** |
| **S6** | **2** | **13** | **1** | **1** | 0 |
| **S7** | **5** | **67** | **10** | **10** | **7** |

## Bugs (404 open, 8 closed/fixed)




- **#14096** `S1` `D2` - Dependency package variables incorrectly expand to sandbox in (run) — Package variables like `%{pkg:foo:lib}` incorrectly expand to sandbox paths inside `(run)` in lock files instead of relative paths
- **#14085** `S5` `D2` - 3.22.0 regression: error about non-existent excluded module from `(select)` in a different stanza — Regression in 3.22.0 where `dune build` errors claiming a module doesn't exist when using `(select)` in a separate stanza with module exclusion
- **#13993** `S4` `D3` - unicode in sandbox prevents sandbox cleanup on Windows — Sandbox cleanup fails on Windows when directories contain unicode characters
- **#13909** `S1` `D3` - sandbox cleanup fails on Windows when junctions are present — NTFS junctions cause sandbox cleanup failures with "Directory not empty" errors on Windows
- **#13903** `S2` `D3` - Internal error during `dune install` with pkg-enabled dune-workspace — `dune install` crashes with internal error "Unexpected build progress state" when using pkg-enabled dune-workspace
- **#13894** `S3` `D2` - Interactions between `%{version:...}` and OPAM dependencies — `%{version:ppxlib}` fails with error when package is not yet installed, even though it's declared as a dependency; breaks opam CI builds
- **#13891** `S5` `D2` ~~CLOSED~~ - Revert the behavior of --diff-command wrt to non-existent files — Closed upstream
- **#13878** `S7` `D2` - Lock for local dependency uses absolute path — `dune pkg lock` with local pin uses absolute path instead of relative, making lock files non-portable
- **#13841** `S7` `D2` - `dune pkg lock` doesn't respect `dune-workspace`'s `lock_dir` stanza — Running `dune pkg lock` without arguments ignores the configured `lock_dir` path from workspace and always creates at `dune.lock`
- **#13832** `S3` `D2` - Dependency cycle with dynamic `enabled_if` on `library` stanza and `package` directive — Build fails with dependency cycle error when using `%{read:...}` in `enabled_if` with a `package` directive present, but works without the directive
- **#13825** `S3` `D2` - archives are incorrectly detected by inspecting the extension — Archive type detection by file extension doesn't work because downloaded files have generic filenames like `download`
- **#13823** `S4` `D3` - pkg: OpenBSD tar still lacks -z in 3.22.0_alpha2 — tar extraction fails on OpenBSD because dune constructs incorrect tar flags, causing build failures
- **#13815** `S6` `D2` - patch action should fail without source stanza — Patch action on packages without a source stanza gives confusing "No such file or directory" error instead of an informative message
- **#13788** `S7` `D4` - with RPC/watch: short job waits for long job to return — When using `dune build --watch` with RPC, a short formatting command blocks until the watch process finishes its current work
- **#13782** `S3` `D2` - `dune show targets` does not work on build-only directories — `dune show targets _build/default/.simple.objs` fails when it should work
- **#13774** `S3` `D3` - Rocq rules do not support Rocq 9.0 — Dune always invokes `rocq --config` which only works in Rocq 9.1+, making it impossible to build Rocq 9.0 projects without warnings
- **#13768** `S7` `D4` - Usability issues with Dune contexts — `dune exec --context=tsan` picks up the wrong binary from the default context instead of the specified one
- **#13738** `S3` `D3` ~~CLOSED~~ - `(generate_project_file)` is not compatible with VSRocq — Closed upstream
- **#13732** `S3` `D1` - `dune-action-trace` packaging is misconfigured — `opam install dune-action-trace --with-test` fails with missing dependencies due to misconfigured package
- **#13677** `S7` `D2` - dune show depexts triggers building the compiler — `dune show depexts` unnecessarily builds the OCaml compiler when it should not need to
- **#13658** `S4` `D3` - Known behavioral differences in Windows: `--release` flag needed? — On Windows, `dune build @install` does not compile dune-site plugins unless `--release` flag is used, unlike Linux/macOS
- **#13650** `S4` `D3` - ctypes stubs fail to build on 32-bit platforms — ctypes builds fail on 32-bit platforms with incorrect `.cmxa` path (should use `.cma`)
- **#13638** `S3` `D2` - `diff` action directive isn't working as expected with a non-existent file — diff action with a non-existent file gives "Unable to resolve symlink" error instead of comparing with empty file as documented
- **#13603** `S3` `D2` - Building opam package Nx fails with linker error, likely due to bad include directory formatting — Package build fails with linker error, suspected dune bug in include directory formatting
- **#13566** `S3` `D3` - @ocaml-index fails when multiple executables in a directory don't specify (modules) — ocaml-index fails with "Unbound module" when multiple executables share a directory without explicit module specifications
- **#13551** `S7` `D2` - Dune should respect user-specified PPX order in `(preprocess (pps ...))` stanza — Dune alphabetically sorts PPX transformations, discarding user-specified order which is semantically significant
- **#13545** `S5` `D2` - Dune 3.21.0 unable to lock project depending on ocaml-system — Regression from 3.20.2: `dune pkg lock` fails when project depends on `ocaml-system` package
- **#13525** `S5` `D4` - Formatting dune files on save while the build is running — `dune format-dune-file` conflicts with build locks when a watch-mode build is running, breaking editor format-on-save workflows
- **#13500** `S2` `D3` - Dune 3.21.0 crashes and hangs with "Dependency cycle between ..." — Dune crashes with a spurious dependency cycle error in a multi-project workspace
- **#13492** `S1` `D4` - install stanza in dynamic_include is ignored — Install stanza inside a `dynamic_include` file is silently ignored, contrary to what documentation implies should work
- **#13471** `S3` `D2` - pkg: dune utop and #require — `dune utop` with package management produces findlib warnings about non-existent directories when using `#require`
- **#13467** `S1` `D2` - ocamlbuild failing to build dependents if sandbox is not properly cleared up — ocamlbuild hardcodes sandbox paths, causing build failures when sandbox is partially cleared
- **#13418** `S3` `D2` - `dune runtest --force` does not work for `(mdx)` stanza — `dune runtest --force` fails to re-trigger mdx tests
- **#13307** `S2` `D3` - Crash when multiple install stanzas are targeting share_root for their directory — Dune crashes with internal error "Map.add_exn: key already exists" when multiple install stanzas target share_root
- **#13230** `S2` `D3` - Invalid Variable_name.t error raised — Dune crashes with internal error "Invalid Variable_name.t" due to a typo in dune-project (space in `: with-dev-setup`)
- **#13225** `S3` `D2` - `:standard` in an `:include`d file is ignored — Using `:standard` inside an `:include`d file silently ignores environment flags instead of working or raising an error
- **#13223** `S7` `D2` - Constraints are not accounted for `depopts` — Solver ignores version constraints for optional dependencies specified in lock_dir constraints
- **#13108** `S2` `D3` - pkg lock fails on repos that need dune subst — `dune pkg lock` crashes with internal error when dune-project contains `%%VERSION_NUM%%` placeholder
- **#13080** `S3` `D4` - dune build --watch + dune exec + DUNE_BUILD_DIR does not work — `dune exec` fails with "Don't know how to build" when DUNE_BUILD_DIR is set and watch mode is active
- **#13011** `S3` `D5` - pkg: the current dependency update model is unpredictable and impractical — Dependencies update unexpectedly during normal `dune build`/`dune test`, causing builds to break when network is unavailable or upstream APIs change
- **#13001** `S7` `D2` - modules of library using ctypes without (modules) field are incorrectly validated — ctypes library without explicit (modules) field causes incorrect module validation, breaking builds
- **#12996** `S2` `D5` - `dune exec` doesn't perform install stanza — `dune exec` skips install stanza processing, causing binaries using dune-site to fail finding static files
- **#12976** `S2` `D5` - behavior of `dune clean` is surprising/wrong when used with dune package management — `dune clean` deletes package management data in `_build`, surprising users who lose installed packages/tools
- **#12975** `S3` `D2` - running `dune tools exec <p>` when `p` is not already installed as a dev tool should suggest users run `dune tools install <p>` — Unhelpful/confusing error messages when running `dune tools exec` for a tool that is not installed
- **#12964** `S4` `D3` - Possible race condition observed on FreeBSD CI — Intermittent linker failure (library not found) indicates a race condition in dune's build process
- **#12924** `S7` `D2` - `$DUNE_WORKSPACE` should be cleared in `dune pkg` sandboxes — Environment variable leaks into nested dune calls in sandboxes, causing incorrect behavior
- **#12900** `S2` `D4` - dune hangs in mdx tests waiting for _build/default/_build/.rpc/dune — Dune hangs indefinitely when background process is used in mdx tests; regression in behavior
- **#12897** `S5` `D2` - breakage with `dune format-dune-file` and `opam-dune-lint` — Breaking change requiring `(lang ...)` field breaks existing tools that relied on prior behavior
- **#12866** `S2` `D3` - Adding constraint to `ocamlformat` developer tool fails — Internal crash ("as_outside_build_dir_exn") when adding constraints to dev tool lock directories
- **#12855** `S1` `D2` - Depext not building at all (and no hint) when no `libraries` field — System dependencies silently not built and no error/hint given, leading to confusing runtime failures
- **#12854** `S3` `D3` - `--display=quiet` has no effect on `--root`-changing messages — The `--display=quiet` flag fails to suppress "Entering/Leaving directory" messages, contrary to expected behavior
- **#12818** `S5` `D3` - If dune tools install fails to install a tool it can break a user's environment — Failed tool installation (due to tar incompatibility on OpenBSD) leaves the environment in a broken state where `dune build` no longer works
- **#12752** `S7` `D4` - RPC builds don't transfer warnings to the client — Non-fatal warnings are silently swallowed; RPC client reports "Success" without showing build warnings
- **#12725** `S7` `D4` - [RPC] Eager watch mode doesn't register promotions at all — Promotions via `dune promote` are completely ignored during eager watch mode
- **#12715** `S1` `D4` - RPC system hanging non-deterministically on eager watch mode — Server stops answering requests and clients hang forever in eager watch mode
- **#12700** `S7` `D2` - under-specified dependencies for build env — Package build rules don't account for environment changes, causing incorrect builds
- **#12660** `S2` `D4` - dune forwarding rpc occasionally gets EINVAL backtrace — Uncaught exception (Unix.EINVAL from setsockopt) during RPC forwarding causes crash
- **#12611** `S7` `D2` - [Merlin] Curious Unbound module issue — Merlin/LSP reports false "Unbound module" errors depending on alphabetical ordering of executables in a dune file
- **#12609** `S2` `D3` - dune build hangs if curl not installed — Build hangs indefinitely after reporting curl is missing instead of exiting with an error
- **#12551** `S2` `D3` - pkg: `dune utop src/...` fails because of duplicate .cmas: tools and pkgs — `dune utop` crashes with "Duplicated implementations" errors due to conflicting .cma files between dev tools and packages
- **#12544** `S5` `D2` - The error message "optional with unavailable dependencies" is hard to digest — Error message is misleading and does not point to the actual missing transitive dependency
- **#12535** `S2` `D2` - Crash when compiling diffast-cli.0.3.5.1 on Windows — Dune crashes with internal error on Windows (MinGW/Cygwin) during compilation
- **#12475** `S3` `D2` - [pkg] build a simple unikernel — Dune pkg fails to build packages due to incorrect handling of directory targets in fetched archives
- **#12439** `S3` `D2` - Confusing message with erroneous rules — Error message "You cannot use %{target} with inferred rules" is confusing when the actual issue is a missing `(target ...)` field
- **#12431** `S4` `D3` - Can't build ocamlbuild on Windows: `Error: opendir(): No such file or directory` — Build failure on Windows due to symlinks in ocamlbuild source; also `dune clean` fails afterwards
- **#12429** `S4` `D3` - Error fetching compiler package on Windows relating to directory targets — Dune fails to recognize directory targets it created on Windows, claiming the action didn't produce them
- **#12390** `S5` `D3` - `dune pkg` no longer picks up the compiler from its cache — Regression in 3.20: compiler is rebuilt from scratch every time instead of being picked up from cache
- **#12322** `S3` `D2` - Don't include .output files with "default" targets — `dune build` unnecessarily executes test binaries (building `.output` files) causing confusing error reports for failing tests
- **#12317** `S6` `D2` - User-defined rules cannot be added to the 'empty' alias — Upgrading lang dune to 3.20 triggers an error with no location information, making it impossible to diagnose
- **#12309** `S7` `D2` - `--cache=disabled` is triggering some re-compilation — Building with `--cache=disabled` incorrectly triggers recompilation of already-built artifacts
- **#12143** `S7` `D2` - `dune utop` in a `dune pkg` managed workspace can fail with unmet library dependencies — `dune utop` fails because test-only dependencies (via `:with-test`) are picked up by utop but not actually installed
- **#12122** `S4` `D3` - Hardlinks on Haiku not allowed — Package management fails on Haiku because hardlinks for cookies fail and there is no way to change sandbox mode
- **#12109** `S3` `D2` - Empty Coq/Rocq theory leads to package error — `dune build` incorrectly claims a package has no stanzas when it has a `coq.theory` stanza
- **#12108** `S2` `D3` - Poor error reporting in cram tests, take 2 — `set -o pipefail` causes `***** UNREACHABLE *****` output instead of a meaningful error; stderr from shell is not reported
- **#12104** `S3` `D2` - Cram tests don't pick up env variables — Inline environment variable assignments (e.g., `VAR=val command`) are not picked up by commands in cram tests
- **#12103** `S7` `D2` - [pkg] Passing `-j` to `dune build` causes the compiler package to be rebuilt — Changing the `-j` parallelism flag causes all dependencies including the compiler to be unnecessarily rebuilt
- **#12075** `S2` `D3` - Building dune crashes with Unexpected_find_result for pp library — `make release` crashes with internal error "Unexpected find result" for the `pp` library
- **#12063** `S2` `D3` - Dune segfaults during bootstrap on ppc64 — Generated dune.exe is corrupt and segfaults on ppc64 Darwin during bootstrap
- **#12018** `S2` `D3` - crash when using ctypes stanza — Internal error "link_many: unable to find module" crash when using ctypes stanza with `--profile release`
- **#12007** `S7` `D2` ~~FIXED~~ - dune build @ocaml-index builds too many files — Fixed in PR #14137 (merged)
- **#11999** `S3` `D3` - Dune pkg don't find dune-site plugins for dependencies — Executables using dune-site plugins cannot find plugins from package-managed dependencies
- **#11941** `S1` `D2` - Dune overwrites the user provided debug flag in foreign stubs — Dune appends `-g` after user-specified C flags, making it impossible to disable debug info with `-g0`
- **#11932** `S3` `D2` - baffling error message when a "dune lang" version is too new — Error message when `(lang dune X)` version is unsupported is confusing and misleading
- **#11923** `S1` `D2` - Dune builds C stubs with `bytecode_cflags` and never `native_cflags` — Wrong compiler flags used for native C stubs; can cause crashes with ThreadSanitizer
- **#11848** `S7` `D2` - Test stanza allows expectation files to be generated — This breaks promotion in the test stanza
- **#11836** `S2` `D2` - Dune cannot build empty `coq.theory` — Fatal exception when building a coq.theory with `(modules )` that excludes all Coq files
- **#11774** `S1` `D2` - `dune install` with an out-of-workspace build directory produces absolute paths in dune-package files — Absolute build paths leak into installed dune-package files, making distributed packages unusable
- **#11633** `S7` `D2` - odoc required by cram depending on objs/byte — Cram tests with `(deps (glob_files .foo.objs/byte/*))` incorrectly require odoc to be installed
- **#11631** `S7` `D1` - dune watch rpc is sending off by minus one lines inconsistently — Diagnostic line numbers are off by one compared to compiler output, and the offset is inconsistent
- **#11618** `S2` `D3` - Internal error: [as_in_build_dir_exn] called on something not in build dir — Internal crash when building Rocq/Coq projects with opam-installed plugins; should be a user-facing error
- **#11615** `S3` `D2` - Dune can only understand opam repos matching the layout of opam-repository — Dune fails to find packages in opam repos that use a different (but valid) directory layout
- **#11593** `S7` `D2` - dune takes >2GB of RAM building some targets of frama-c.30.0 — Excessive memory usage (>2GB) when building certain targets, suggesting a resource leak or inefficiency
- **#11590** `S4` `D3` - Support MSVC command-line flags syntax with pkg-config in dune-configurator — pkg-config returns Unix-style flags to MSVC compiler, causing build failures on Windows
- **#11583** `S3` `D3` - packages depending on a toolchain-provided compiler can't cache the first time — Bug: shared cache misses occur on first build when using toolchains; second build does not benefit from the cache as expected.
- **#11574** `S4` `D4` - Cannot install dune using opam on Windows due to non-exist directory/file — Bug: dune compilation fails on Windows due to missing directory/file during bootstrap.
- **#11542** `S6` `D1` - `dune subst` inferred version is totally misleading and wrong — Bug/misfeature: `dune subst` uses `git describe` which produces misleading version strings that confuse users.
- **#11536** `S3` `D2` - pkgconf: unknown option -- personality — Bug: dune uses `--personality` flag not supported by older pkgconf versions, causing build failures.
- **#11523** `S7` `D2` - symlinks in directory targets don't go in shared cache — Bug: symlinks in directory targets prevent caching, which is incorrect behavior.
- **#11521** `S3` `D2` - `dune show targets` builds package dependencies before printing targets if a lockdir is present — Bug: `dune show targets` should not build dependencies, but does so when a lockdir is present.
- **#11518** `S3` `D2` - [BUG] dune build @check fails mysteriously with overlapping executables — Bug: `dune build @check` fails with confusing errors while `dune build @all` succeeds in the same project.
- **#11506** `S3` `D2` - error message on failing copy action is unclear — Bug: unclear/misleading error message when a copy action fails.
- **#11501** `S6` `D2` - dune doesn't reset DUNE_CACHE_ROOT inside cram tests — Bug: environment variable leakage causes spurious warnings inside cram tests.
- **#11500** `S3` `D2` - `@ocaml-index` is empty when not built from the root of a project — Bug: `@ocaml-index` alias produces no output when invoked from a subdirectory, unlike other aliases.
- **#11444** `S2` `D3` - ERROR while compiling dune.3.17.2 ($HOME/.cache/dune perms problem?) — Bug: dune compilation fails due to cache directory permissions issue.
- **#11440** `S3` `D3` - ctypes' `deps` field doesn't follow the dependency specification language — Bug: the `deps` field in ctypes doesn't work as documented; it doesn't follow the dependency specification language.
- **#11418** `S3` `D2` - dune-build-info is not working on flambda1 switch — Bug: `dune-build-info` fails with warning 58 error on Flambda1 switches; works on closure.
- **#11377** `S7` `D3` - dune build @doc doesn't update generated documentation properly — Bug: incremental documentation rebuild is broken; unchanged modules sometimes disappear from index.
- **#11303** `S4` `D3` - Too easy to reach MAX_PATH on windows — Bug: dune generates paths that are too long on Windows, hitting the MAX_PATH limit.
- **#11290** `S5` `D3` - `dune subst` issues with OCaml-CI — Bug/regression: `dune subst` fails since 3.17 in directories containing only an `.opam` file, which used to work in 3.16.1.
- **#11281** `S7` `D3` - Dune site (without plugins) forces `-linkall` — Bug/misfeature: `-linkall` is forced even when using dune sites without plugins, which is unnecessary and harmful.
- **#11276** `S3` `D2` - Package management should Ignore unused opam files when pinning — Bug: unused opam files with missing version info cause build failures when pinning.
- **#11229** `S2` `D3` - Dune developer preview: ocamllsp cannot read stdlib.cmi (corrupted compiled interface) — Bug: ocamllsp fails with corrupted compiled interface when using dune developer preview.
- **#11225** `S1` `D3` - dune-build-info: spurious `git describe` output instead of version string — Bug: `dune-build-info` returns git describe output instead of the version specified in `dune-project`.
- **#11190** `S2` `D3` - Internal error with `(env (_ (binaries (../tools/myrock.exe as coqc))))` — Bug: internal dependency cycle error when trying to override coqc binary via env stanza.
- **#11163** `S7` `D2` - dune cache — Bug concern: dune cache was enabled by default despite known issues; reporter asks whether prior cache bugs were actually fixed.
- **#11138** `S1` `D4` - Promotion and cross-compilation — Bug: file promotion with cross-compilation is non-deterministic; the wrong file may be promoted.
- **#11134** `S6` `D2` - Dune shows "Source files changed, restarting current build" for more than 30s — Bug: dune restarts build unnecessarily for 30+ seconds after file changes, causing confusing UX.
- **#11114** `S3` `D2` - Package management fails to read files when lock directory is ignored — Bug: `dune build` fails when the lock directory is listed in `.gitignore` or similar ignore files.
- **#11110** `S7` `D1` ~~WIP~~ - Custom `libexec` sites install does not set executable bit — Bug: binaries installed to custom `libexec` sites lack the executable permission bit. (PR #14171 open — test only)
- **#11106** `S7` `D1` - Redundant dune version constraint — Bug: dune generates opam files with duplicate/redundant version constraints (e.g., `"dune" {>= "3.16" & >= "3.16.0"}`).
- **#11062** `S3` `D2` - dune should give priority to libraries in OPAM_SWITCH_PREFIX instead of ocamlc -where — Bug/misfeature: opam-installed packages are ignored in favor of system-wide packages, causing failures.
- **#11042** `S3` `D2` - Using (enabled_if %{read:...}) — Bug: documented feature `(enabled_if %{read:...})` doesn't work; produces error "%{read:..} isn't allowed in this position."
- **#11038** `S7` `D2` - `dune fmt` requires `ocamlc` to be in path but does not guarantee that this is the case — Bug: `dune fmt` with dev tools fails when `ocamlc` is not in PATH, even though dune should provide it.
- **#11037** `S3` `D2` - `dune fmt` and `dune build @fmt` build all the project's dependencies when a lockdir is present — Bug: formatting commands unnecessarily build all project dependencies when a lockdir exists.
- **#11017** `S3` `D1` - Coqdoc flags --with-header and --with-footer should imply a dependency on the argument files — Bug: changes to coqdoc header/footer files don't trigger documentation rebuild due to missing dependency tracking.
- **#11016** `S3` `D2` - Coq documentation generation fails with Coq in the workspace — Bug: coqdoc rules don't receive correct environment variables to locate the standard library when Coq is in the workspace.
- **#11014** `S2` `D3` - `coq.extraction` + `coq.theory` raises internal errors — Bug: combining `coq.extraction` and `coq.theory` stanzas produces unhelpful internal errors instead of a clear diagnostic.
- **#11012** `S3` `D3` - Coq cannot find the cmxs file for transitive ocaml dependencies — Bug: dune fails to place `.cmxs` files for transitive OCaml dependencies where Coq expects them.
- **#11010** `S2` `D4` - Dune crashes when editing a file in exec watch mode — Bug: dune crashes when editing a file during `exec --watch` mode.
- **#11002** `S1` `D3` - opam file generation could be made less error-prone — Bug/misfeature: dune silently generates incorrect opam files from typos like `:with_test` (should be `:with-test`), causing confusing downstream failures.
- **#10974** `S3` `D3` - "Shared cache miss" error while building project on different filesystem to cache directory — Bug: shared cache fails with EXDEV error when project and cache are on different filesystems.
- **#10970** `S3` `D2` - pkg: dune package management cannot build z3 — Bug: dune package management fails to build the z3 package.
- **#10954** `S2` `D3` - 'opam install dune' segfaults — Bug: installing dune via opam causes a segfault.
- **#10940** `S4` `D3` - Compilation of Dune 3.16.0 Fails on macOS M2 (ARM64) During `opam install` — Bug: dune 3.16.0 fails to compile on macOS ARM64.
- **#10896** `S3` `D4` - Using `@ocaml-index` with vendored libraries: `Error: Conflict between the following libraries` — Bug: `dune build @ocaml-index` fails with conflict errors when vendored libraries are present.
- **#10874** `S5` `D3` - macos: ld: warning: ignoring duplicate libraries: '-lunixbyt' — Bug: regression since #10763; duplicate library warnings appear on macOS.
- **#10872** `S2` `D2` - CRAM tests on windows — Bug: CRAM tests crash with internal error on Windows when `sh` is not found, instead of giving a clear error message.
- **#10806** `S2` `D2` - Formatting of multi-line / end of line / block strings — Bug/misfeature: `dune fmt` destroys multi-line string syntax by converting them to normal strings.
- **#10805** `S4` `D3` - [dune-configurator] PKG_CONFIG_PATH is ignored on macos — Bug: `PKG_CONFIG_PATH` environment variable is ignored on macOS in favor of brew paths.
- **#10799** `S4` `D3` - Dune 3.16 doesn't compile in OCaml 4.08/4.09 on Windows — Bug: dune 3.16 uses `Unix.ftruncate` which is unavailable on Windows before OCaml 4.10.
- **#10792** `S3` `D2` - Doc for building byte code incorrect — Bug: documentation for building bytecode executables is incorrect; `dune build foo.bc` doesn't work as documented.
- **#10764** `S2` `D2` - Dune crash with melange-webapi on Windows — Bug: dune crashes with internal error `Path.drop_prefix_exn` on Windows with melange-webapi.
- **#10732** `S5` `D2` - menhir option `--only-tokens` does not work — Bug: `--only-tokens` flag works with menhir 2.0 but not with 3.0; produces error about missing `.conflicts` file.
- **#10731** `S3` `D3` - Many noisy shared cache miss messages when using multiple filesystems — Bug: dune spams many cache miss error messages instead of showing a single warning when cache is on a different filesystem.
- **#10707** `S3` `D1` ~~WIP~~ - Add correct lower bound to menhir — Bug/misfeature: dune assumes menhir supports `--infer-write-query` but doesn't enforce a minimum version, causing build failures with older menhir. (PR #14168 open — fix)
- **#10697** `S3` `D3` - Dynamic loading of packages: linking issues — Bug: dynamic loading of plugins with native dependencies (e.g., LLVM) fails with undefined symbol errors.
- **#10679** `S2` `D3` - `coq.extraction`: Adding a nested module to `extracted_modules` raises an internal error — Bug: internal error occurs when using nested modules in `extracted_modules` field.
- **#10678** `S7` `D2` - Dangling internal path when using virtual library — Bug: using a pinned virtual library (sexplib0) causes dangling internal path errors during compilation.
- **#10659** `S3` `D3` - Dynamic linking error via a Coq plugin or running an executable — Bug: dynamic linking errors occur when using Coq plugins, possibly due to dune's handling of linking.
- **#10653** `S7` `D2` - dune top --only-package pkg when pkg is also installed globally make the toplevel load both versions — Bug: `dune top` loads both local and globally-installed versions of the same package, causing conflicts.
- **#10588** `S3` `D2` - --ignore-promoted-rules has no effect on copy_files — The flag does not work as documented for copy_files rules, which is a behavior/documentation mismatch
- **#10578** `S3` `D2` - `dune build @fmt` exits with 1 if `ocamlformat` is not installed — Dune errors out instead of gracefully skipping ocamlformat rules when no .ocamlformat file is present and ocamlformat is not installed, breaking CI workflows
- **#10509** `S7` `D2` - pkg: adding a lockdir should invalidate built artifacts and force a rebuild — Stale artifacts from a previous build (without lockdir) are not invalidated, leading to potentially incorrect builds
- **#10508** `S3` `D4` - pkg: cannot run `dune pkg lock` while offline — Dune requires internet access even when the opam repo is already cached locally, which is incorrect behavior
- **#10466** `S3` `D3` - Packaging a library with `extra_objects` — Installed library with extra_objects fails to link when consumed by downstream projects; the .o file path is wrong at link time
- **#10423** `S3` `D2` - GCC and GLIBC supported minimums for Dune on Linux — Dune fails to build on platforms where OCaml itself builds fine, due to vendored C code using C99 features without requesting C99 mode
- **#10393** `S2` `D3` - Improve error message when git is not found — Build aborts with unhelpful "git: command not found" without explaining the cause or suggesting a fix
- **#10360** `S7` `D1` ~~CLOSED~~ - (executables_implicit_empty_intf ...) expects dune >= 2.9 but was only added in 3.0 — Non-issue; version check is intentional (closed by nojb)
- **#10335** `S3` `D4` - Cannot build executable in a target directory — Architectural: module discovery happens at rule-generation time but directory target contents are only known after execution; fix requires bridging this timing gap (see dir_contents.ml CR-someday comment)
- **#10294** `S7` `D4` - Environment Variables aren't relocated to the Sandbox — Environment variables like PATH, OCAMLPATH etc. are not properly relocated when running actions inside the package management sandbox, causing incorrect behavior
- **#10291** `S1` `D3` - pkg: generated topfind file contains sandbox paths — The generated topfind file contains absolute paths to the build sandbox which no longer exist after install, breaking ocamlfind
- **#10285** `S2` `D3` - Internal error: link_many: unable to find module — Dune crashes with an internal error when building a project with certain module configurations
- **#10268** `S7` `D4` - Module name conflict with vendored library — Vendored libraries with duplicate module names cause unexpected compilation errors; vendored libraries are not properly isolated
- **#10234** `S1` `D2` - Changes made to the build/install commands of a pinned non-dune package are not picked up until `dune pkg lock` is run — Changes to pinned package build commands are silently ignored until re-locking, leading to stale builds
- **#10177** `S4` `D2` - Tests fail on Windows: dune: PATH argument: no ... directory — Merlin-related tests fail on Windows due to Unix-style vs Windows-style path mismatch
- **#10176** `S2` `D3` - Tests fail on Windows with: Cannot decode build prefix map — Dune crashes on Windows with an internal error because colons in Windows paths are not escaped in the build prefix map
- **#10173** `S7` `D4` - Percent forms are allowed to escape from one context to another — Security/correctness issue where relative paths in percent forms can access files from other build contexts
- **#10158** `S3` `D2` - The `pin` stanza requires a `name` when it appears in `dune-workspace` but not in `dune-project` — Inconsistent behavior between the same stanza in different files, with a confusing error message
- **#10144** `S7` `D2` - All Recursive Aliases are broken in vendored directories — Recursive aliases (not just test-related ones) are disabled in vendored directories, which is too aggressive
- **#10141** `S5` `D1` - git describe is incorrect for Dune's main branch since 3.12 — `git describe --tags` reports incorrect version information on the main branch
- **#10111** `S7` `D2` - Using ambiguous hash references for git repos leads to unexpected results — A branch name formatted like a SHA1 hash silently resolves to the default branch instead of the correct branch, without any warning
- **#10042** `S4` `D3` - Add MSVC libNAME.lib and dllNAME.dll to stub libraries — On Windows with MSVC, incorrect `-lxdg_stubs` flag is used instead of the proper MSVC format, and -L path is missing, causing link failures
- **#10038** `S5` `D2` - Undocumented change related to install dir and workspaces — Regression: building packages with different workspaces now deletes previously built install artifacts, changed behavior from dune 3.10
- **#10029** `S6` `D2` - Building the cmo of a module of a disabled library gives a bad error — Error message is unhelpful; should indicate that the target is missing because the library is disabled
- **#9979** `S1` `D2` - Dune links against wrong cstubs in byte mode — Dune picks up an installed (stale) version of stub libraries instead of the locally built ones when building in byte mode
- **#9963** `S2` `D3` - Aborted `init` command leaves empty directory — `dune init proj` with an invalid name creates an empty directory that should be cleaned up on failure
- **#9943** `S3` `D2` - dune fmt should not fail to format when depopt isn't available / `and` isn't lazy — `dune fmt` fails when an optional dependency is not installed due to `enabled_if` evaluation, and `and` is not evaluated lazily as expected
- **#9882** `S7` `D2` - Incorrect handling of `%{version:pkg}` — `%{version:foo}` always resolves to the project version even when `-p` is used to filter packages, which is incorrect
- **#9873** `S5` `D2` - Error with directory symlink: Unexpected file kind "S_DIR" — Directory symlinks in directory targets cause build errors; regression from a specific commit
- **#9775** `S7` `D2` - glob_file_rec is not recursive on generated folder — `glob_files_rec` behaves as non-recursive glob inside generated directories, which is unexpected
- **#9773** `S5` `D3` - Ctypes and foreign bindings won't bundle library properly — Multiple rules generated for the same libdash.a; foreign archives with ctypes causes build failures
- **#9759** `S3` `D2` - data_only_dirs documentation seems to imply that ordered set language applies — Documentation is misleading about ordered set language support in data_only_dirs, causing confusion
- **#9757** `S1` `D2` - `dune runtest` compiles but does not execute `(inline_tests) (modes byte)` — Inline tests are compiled but silently not executed when library has `(modes byte)`, which is a serious bug
- **#9744** `S7` `D2` - @doc-new's index.html might be missing a link to `/local/index.html` — Navigation links are broken in generated documentation; clicking a subindex and going "up" does not return to the expected page
- **#9727** `S7` `D2` - Interaction between opam and dune broken w/ (opam_file_location inside_opam_directory) — Using opam_file_location causes opam to copy the wrong source folder, resulting in missing compiled artifacts after install
- **#9724** `S3` `D2` - `dune build @check` should pass if `dune build @all` does — @check fails in cases where @all succeeds, but @check should be a subset of @all
- **#9716** `S1` `D2` - Empty Directories Not Copied — Empty directories are silently dropped when using local directory sources in package management
- **#9690** `S3` `D5` - `default` alias usability issues for projects with nested folders — Custom `default` alias in a subdirectory is ignored when building from a parent directory; the `all` alias overrides it
- **#9687** `S7` `D2` - Inconsistent assumptions over interface when additional copy of library is present in vendored_dirs — Vendored directories within installed packages leak module definitions, causing inconsistent assumption errors
- **#9672** `S7` `D2` - Bug/Request `--context` should work the same with dune build and dune exec — `dune build --context=foo` does not restrict to the specified context (builds all contexts), unlike `dune exec --context=foo` which works correctly
- **#9662** `S3` `D2` - dune-site: use string list instead of Location.t — Generated sites module uses an abstract type that requires consumers to also depend on dune-site, causing build failures
- **#9650** `S1` `D2` - ppx is skipped when `(modes byte)` — PPX rewriter is silently not applied when the PPX library has `(modes byte)`, causing extension points to remain unexpanded
- **#9482** `S4` `D1` - opam files from template generated with carriage return on windows — Opam file generation adds carriage returns on Windows, causing unnecessary diffs and promotions
- **#9464** `S7` `D5` - Introduce a literal syntax for booleans — Variables serialized as strings in lockdir lose type information (string "false" becomes boolean false), a correctness issue
- **#9396** `S4` `D1` - dune-project parser does not work if dune-project has a UTF-8 byte-order mark — Parser fails with garbled output when a UTF-8 BOM is present, which is valid UTF-8; this is incorrect behavior on Windows where PowerShell writes BOM by default.
- **#9326** `S2` `D3` - freebsd: Error trying to read targets after a rule was run — Build error ("Bad file descriptor") when building on FreeBSD; a crash/failure in the build system.
- **#9128** `S4` `D2` - windows: run cannot find *.cmd — `(run)` fails to find programs with `.cmd` extension on Windows because it only tries `.exe`; programs that should be found are not.
- **#9071** `S5` `D3` - Error "rmdir(...): Directory not empty" on an NFS setup — Regression from dune 3.7.0 to 3.11.1; NFS cache setup that used to work now fails with errors.
- **#9024** `S2` `D2` - Dune crashes when menhir_flags is in dune-workspace — Unhandled exception/crash when a valid-looking configuration is used; dune should not crash.
- **#8989** `S7` `D2` - Menhir parsers as module group interfaces — When `(include_subdirs qualified)` is enabled, menhir parser files cannot serve as group interfaces, which is a limitation that prevents a valid use case from working.
- **#8970** `S7` `D1` - dune build accepts trailing slashes — Incorrect argument parsing; `dune build abc/` is silently accepted and misinterpreted even if `abc` is a file.
- **#8968** `S2` `D3` - Restarting OCaml LSP caused Internal error: attempting to write to a closed channel — Internal error/crash when restarting LSP, dune should handle channel closure gracefully.
- **#8844** `S7` `D5` - `dune install` shouldn't install to opam prefix — `dune install` modifies opam switch state without updating it, which is a misfeature/incorrect default behavior.
- **#8811** `S2` `D3` - dune crashes when passing `-w` after `dune clean` on aarch64-unknown-linux-gnu — Crash with internal error ("Fs_memo.Event.create called on a build path") on a specific platform.
- **#8770** `S7` `D2` - TUI captures clicks when using inside vscode — TUI captures mouse clicks in vscode integrated terminal, preventing clicking on underlined locations; this is broken interaction behavior.
- **#8727** `S5` `D2` - The issues of `--ignore-promote-rules` — The flag has known misfeatures: it doesn't work correctly with the fallback mechanism due to a race condition, and the overall design is acknowledged as problematic.
- **#8709** `S5` `D2` - Generate cmi files that match the input — Dune generates `.cmi` files with incorrect casing (lowercasing filenames with multiple capitals like `QCheck2`), which surfaced a compiler regression and is itself incorrect behavior.
- **#8651** `S2` `D3` - Internal error on tests on windows, hooks failed — Crash/internal error on Windows with "hooks failed" and ENOTEMPTY rmdir errors causing CI timeouts.
- **#8643** `S4` `D3` - Enabling (use_standard_c_and_cxx_flags) fails when paired with C++ stubs on Windows — Build failure on Windows because flexlink doesn't understand `-shared-libgcc` flag passed by dune.
- **#8626** `S3` `D2` - `#use_output "dune ocaml top"` fails in a project where `dune utop` works — Command fails with undefined global reference even though `dune utop` works fine in the same project; inconsistent behavior.
- **#8587** `S3` `D2` - Add support for `staged_pps` in `dune describe pp` — `dune describe pp` does not work for staged PPXs, producing an error instead of the expected output; acknowledged as an unfixed bug.
- **#8417** `S7` `D2` - Dune sometimes changes *.opam files in release mode — In release mode (`-p`), dune should not modify opam files but it does; this is incorrect behavior.
- **#8358** `S4` `D1` - Cram tests on Windows, line termination and Git warning — Cram tests produce incorrect diffs on Windows due to line terminator handling issues; test output contains the entire file as a diff.
- **#8352** `S3` `D2` - (allow_empty) rules and messages are confusing — Confusing/incorrect error message for a valid project setup (executable with `(modes js)`); the error message is misleading and the `(allow_empty)` workaround is itself confusing.
- **#8291** `S7` `D5` - Please honor CFLAGS — Dune ignores the standard CFLAGS/CXXFLAGS environment variables when compiling C code, which deviates from standard build system behavior and breaks expected workflows.
- **#8281** `S2` `D3` - Exception when secondary .opam with bad name exists while running build doc — Internal error/crash when building documentation with a secondary .opam file that has a bad name.
- **#8242** `S5` `D2` - Very slow emacs compilation buffer updates — Regression from dune 3.7 to 3.9; emacs compilation buffer updates became very slow due to excessive "Done: 100%" output even when nothing needs building.
- **#8231** `S4` `D3` - Displaying full filenames in dune-site before load — Debugging/diagnostic issue where dune-site fails to load on Cygwin with an opaque "Permission denied" error, providing insufficient information to diagnose the problem.
- **#8075** `S3` `D2` - Fail to promote over a non-existing file — Promotion fails with a symlink resolution error even though documentation/tests show it should work; broken functionality.
- **#8073** `S7` `D2` - Cannot promote empty files over a non-existing file — Empty files cannot be promoted when the target doesn't exist; dune logs that files differ but doesn't create the promoted file.
- **#8026** `S6` `D3` - Warning: ltac_plugin.cmxs already found — Spurious warning when building Coq plugins that use `coq-core.plugins.ltac`; the warning is confusing and indicates incorrect library path handling.
- **#8025** `S1` `D3` - dune-build-info reports wrong library version in vendored dir — Library version is incorrectly reported as the git hash of the CWD repository instead of the actual library version.
- **#7962** `S2` `D3` - Crash when depending on source_tree outside workspace — Crash with internal error instead of a proper error message when `source_tree` references a path outside the workspace.
- **#7917** `S4` `D3` - dune clean fails because of .filesystem-clock and .digest-db (NFS) — `dune clean` fails on NFS because dune creates files in `_build` and then complains the directory is not empty.
- **#7831** `S3` `D2` - Install fails for a directory with symlinks to a directory — `dune install` fails when the directory contains symlinks to directories; broken install functionality.
- **#7811** `S3` `D2` - Vendoring of foreign source trees with leading underscores — Dune silently ignores directories with leading underscores in vendored foreign source trees, causing missing file errors.
- **#7800** `S3` `D2` - `(byte shared_object)` linking mode does not allow linking C stubs — Documented linking mode doesn't work as expected; C stubs cannot be linked with byte shared_object mode.
- **#7761** `S3` `D3` - `dune build --passive-watch-mode` ignores its argument — Command silently ignores arguments instead of erroring; incorrect behavior.
- **#7720** `S3` `D3` - `dune build @doc` does not rebuild pages — After modifying `.mli` files, `dune build @doc` does not rebuild the documentation pages and produces dangling links; broken incremental rebuild.
- **#7664** `S5` `D2` - program output from `exec -w` and rule actions interspersed with repeated dune status output — Regression from dune 3.4.1 to 3.7.1; program output is interspersed with repeated status messages, making output unreadable.
- **#7624** `S6` `D4` - In `dune_rpc_lwt` closing the output channel should also close the input channel — Closing the output channel raises `Unix.Unix_error(Unix.EBADF)` instead of returning `None` on the input channel
- **#7586** `S3` `D2` - "dune top -p <pkg>" tries to pull the dependencies of unrelated vendored executables — `dune top -p` incorrectly pulls dependencies from unrelated vendored executables
- **#7583** `S3` `D5` - What should happen when exposing code from a private package? — Compilation fails with missing `.cmi` files when re-exposing private package code through a public module, with no warning at library compile time
- **#7573** `S3` `D2` - Build failing due to existence of broken symbolic link (unused in build) — Dune fails the build when a broken symlink exists in vendored sources even though it is not used by the build
- **#7571** `S3` `D2` - env not supported in enabled_if Boolean language in library stanza — `%{env:...}` variable not allowed in `enabled_if` despite documentation saying it should be supported; documentation and behavior mismatch
- **#7568** `S2` `D4` - Dune doesn't respond to RPC methods when run in watch mode in the dune repository — RPC ping command hangs forever when dune is running in watch mode within its own repository
- **#7534** `S3` `D2` - `-p` does not detect packages in `opam/` subfolder even when `(opam_file_location inside_opam_directory)` — `-p` flag fails to find packages located in the `opam/` directory
- **#7470** `S3` `D3` - `dune-site` cannot be used in top-level REPL — Loading `dune-site` in OCaml toplevel raises `Error: Reference to undefined global 'Dune_site__Dune_site_data'`
- **#7464** `S7` `D2` - `preprocess` `per_module` dependencies are not relative — Preprocessing with action `run` in `preprocess` stanza resolves paths relative to workspace root instead of the dune file directory
- **#7460** `S1` `D2` - Cache hits "hide" warnings — When dune cache is enabled, cache hits suppress compiler warnings that should still be displayed
- **#7454** `S7` `D2` - `dune fmt` unexpectedly triggers menhir rules — `dune fmt` / `dune build @fmt` builds menhir parsers when it should not build anything
- **#7448** `S5` `D3` - Potential bug: dune commands no longer work after updating macOS to Ventura — `dune build` produces `Error: write(): Operation timed out` after macOS Ventura update
- **#7413** `S7` `D3` - Debug mapping is sometimes inconsistent with installed locations — `BUILD_PATH_PREFIX_MAP` in compiled libraries is missing package name information, causing incorrect debug source mappings after installation
- **#7223** `S3` `D4` - "I/O error" with `.pp.ml` file when running `dune build . -w` — Watch mode intermittently fails with I/O error on `.pp.ml` files that resolves on restart
- **#7222** `S1` `D2` - compiler errors have wrong relative path — Compiler errors show paths relative to the parent project root instead of the current project when building from a submodule
- **#7170** `S7` `D2` - Folders excluded from `dirs` are visited when calling `dune build @my_alias` — Directories excluded via `dirs` stanza are still visited (stat'd) during alias builds
- **#7155** `S7` `D3` - Spurious warning when a private library is in the deps of a Coq plugin — False warning triggered when a Coq plugin has a private library in its transitive dependencies
- **#7146** `S3` `D3` - Linker is invoked from unexpected directory — Linker cannot find libraries referenced with relative paths in `c_library_flags` because the linker runs from an unexpected directory
- **#7135** `S3` `D2` - Hidden folders are ignored in source_tree dep — Files in hidden directories (e.g. `.cargo/`) are silently excluded from `source_tree` dependencies with no way to include them
- **#7091** `S3` `D2` - Dune cannot handle `From ... Extra Dependency` — Dune fails to build Coq files using `From ... Extra Dependency` because non-`.v` files are not copied to the target directory
- **#7073** `S3` `D2` - ld: Error: unable to disambiguate: -shared-libgcc — Linker error when building with `(modes object)` due to conflicting `-shared-libgcc` flags
- **#7053** `S2` `D2` - Dune does not validate non-existent Coq modules being excluded — Excluding non-existent Coq modules silently accepted, and using `(modules \ I.dont.exist)` causes a `List.hd` exception
- **#7043** `S7` `D2` - Dune tests are being executed in unexpected dir while vendoring — Tests in vendored projects execute from `%{workspace_root}` instead of the vendored `%{project_root}`
- **#7034** `S5` `D4` - Dune treats warnings as errors according to the workspace `lang dune` version when building vendored packages with a more permissive `lang dune` version — Warning-as-error settings from top-level `dune-project` version are applied to vendored packages instead of respecting their own `lang dune` version
- **#6844** `S3` `D3` - Bug when linking ocaml with a dune package including a static library — Dynlink error when linking a Coq plugin that includes a Rust-built static library via foreign_archives
- **#6830** `S3` `D2` - Rule collision when multiple vendored projects contain executables with matching names — Dune errors with "Multiple rules generated" when two vendored packages both contain executables with the same public name
- **#6817** `S7` `D4` - `dune utop --watch` Appears to be broken — `dune utop --watch` does not rebuild/reload when source files change
- **#6730** `S4` `D3` - Terminal UI is broken on Windows — `--display tui` mode is completely broken on Windows
- **#6680** `S3` `D2` - OCaml toplevel sometimes fails to load default implementation for a virtual library — `#require` in toplevel fails to load default implementation for virtual libraries, causing undefined global errors
- **#6615** `S7` `D3` - `coq.theory` stanza should work on the transitive closure of the `plugins` field — Coq plugin dependencies are not transitively resolved, causing Coq to fail to find required libraries
- **#6607** `S7` `D2` - Test suite is broken when CLICOLOR_FORCE=1 — Dune's own test suite fails when `CLICOLOR_FORCE=1` is set because expect tests include color codes
- **#6598** `S6` `D2` - Confusing 'Module ... is used in several stanzas' error — Error message mentions a module name that is not in the listed stanza, making the error confusing and misleading
- **#6568** `S3` `D2` - Preprocessing with actions and future syntax cannot be used in conjunction with (instrumentation ...) — Cannot combine `preprocess` action with `instrumentation` stanza despite no inherent conflict
- **#6481** `S1` `D2` - ctypes: flags are added twice — ctypes build adds flags twice, causing linker errors (regression from dune 3.5.0 to 3.6.0)
- **#6393** `S3` `D3` - coq: native compilation failing on macos — Coq native compilation fails on macOS with linker warning about missing directory
- **#6263** `S3` `D2` - C archive for byte target not built to include dynamic dependencies — Bytecode library C stubs do not include dynamic dependencies, so `ldd` on the resulting `.so` does not show them
- **#6162** `S3` `D2` - Cache doesn't work on `opam install` — Dune cache files cannot be hardlinked inside OPAM sandbox, silently failing to populate the cache
- **#6149** `S1` `D3` - Dune does not rerun coqdep if filesystem layout changes — Dune does not reinvoke `coqdep` when files are added/removed, causing stale dependency information
- **#6148** `S3` `D1` ~~FIXED~~ - `root_module` generates duplicate module definition when `logs.lwt` is a dependency — Fixed in PR #14135 (merged)
- **#6145** `S2` `D3` - dune caches "failing" coqdep invocations even when adding missing files — Bug: coqdep returning wrong output gets cached, corrupting the build; adding the missing library does not fix the build without cleaning
- **#6133** `S3` `D2` - The new dir install feature does not work on existing directories — Bug: the `(dirs ...)` install stanza fails with "No rule found for existing-dir" when using existing directories
- **#6128** `S1` `D2` - Warnings leak through `vendored_dirs` subpath — Bug: nested vendored directories still emit warnings that should be suppressed
- **#6106** `S5` `D2` - dune 3.0 cannot find file through relative path during ppx preprocessing — Bug: regression in dune 3.0+ where ppx_blob can no longer find files via relative paths that worked in earlier versions
- **#6099** `S5` `D2` - No error is raised when building an empty package not defined in the dune-project file — Bug: regression where dune stopped raising an error for empty packages, a feature that was lost when tests were removed
- **#6086** `S3` `D3` - The `embed_in_plugin_libraries` stanza fails with libraries requiring link-time code — Bug: "Multiple rules generated" error when using embed_in_plugin_libraries with link-time generated code
- **#6074** `S3` `D2` - "Error: Pure bytecode executables cannot contain foreign stubs." is misleading — Bug: misleading/incorrect error message implies something is impossible when it can be done by wrapping stubs in a library
- **#6073** `S3` `D2` - test stanza does not work with bytecode compiled with foreign_stubs — Bug: test stanza fails to set up LD_LIBRARY_PATH correctly for bytecode executables with foreign_stubs
- **#6012** `S1` `D2` - Cram tests can access OCaml libraries not in deps, if they are compiled — Bug: cram tests can use libraries not listed in their dependencies if those libraries happen to be already compiled
- **#6005** `S7` `D5` - Compositional Coq builds depend on the current root — Bug: paths in compositional Coq builds are relative to the outer root rather than the inner project, defeating build caching
- **#5992** `S1` `D2` - Usability/Documentation issues with copy_files/glob — Bug (partially): copy_files silently does nothing when glob matches a directory or non-existing file instead of reporting an error
- **#5946** `S3` `D2` - `dune fmt` ignores `--disable-promotion` flag — Bug: the `--disable-promotion` flag is not honored by `dune fmt`, causing unexpected file promotion
- **#5899** `S7` `D2` - Incorrect implementation of Workspace_root — Bug: the `to_cwd` value is incorrect in the workspace root implementation
- **#5864** `S3` `D2` - [coq] [coqdoc] Coqdoc doesn't work when a boot library is present — Bug: coqdoc is not passed `-coqlib` for the `-boot` library, causing it to fail
- **#5833** `S3` `D2` - [dune engine] [bug] Error file unavailable when an absolute path points to a symlink — Bug: dune errors on `dune build $file` when `$file` is an absolute path pointing to a symlink
- **#5814** `S3` `D3` - Binaries installed using `dune` and `dune-site` via `opam` cannot find sites — Bug: installed binaries get an empty list for site locations, preventing dune-site from working after opam install
- **#5809** `S3` `D3` - ctypes stanza does not compile cstubs .o files with -fPIC — Bug: ctypes stub generation produces non-position-independent object files, causing linking failures for shared libraries
- **#5789** `S3` `D2` - Got this error message while trying to build Hello_world project — Bug: confusing/undocumented error message about `(allow_empty)` when building a new hello world project; the error message references a stanza not documented
- **#5749** `S1` `D3` - Incorrect value when installing a relocatable binary with dune-site — Bug: relocatable install produces incorrect doubled path prefix (e.g., `/tmp/bla//tmp/bla/share/...`)
- **#5735** `S7` `D2` - cmxs should not be installed in libexec — Bug: .cmxs files are incorrectly installed in libexec instead of lib due to a wrong fix for the exec bit
- **#5733** `S5` `D1` - dune 3.2.0 changes mandir from /usr/share/man to /usr/man — Bug: regression where the default mandir changed from `/usr/share/man` to `/usr/man`
- **#5697** `S3` `D5` - env stanza should support variables `%{...}` — Bug: variables like `%{project_root}` unexpectedly fail in the env stanza with "Atom or quoted string expected"
- **#5659** `S4` `D2` - dune-configurator: `C_define.import` fails on windows when includes are present — Bug: C_define.import fails on Windows when custom header includes are used
- **#5647** `S3` `D2` - Moving a file as a previously existing directory — Bug: renaming a cram test from a directory to a file causes shared cache errors due to stale directory entries
- **#5638** `S2` `D3` - Unix.EOPNOTSUPP when trying `dune build --watch` on windows using WSL2 — Bug: uncaught exception (EOPNOTSUPP) when using watch mode on WSL2
- **#5621** `S3` `D5` - (optional) in executables doesn't work — Bug: the `(optional)` field in executables stanza does not work, preventing conditional building of executables
- **#5566** `S7` `D2` - Error: Reference to undefined global `Build_info__Build_info_data' — Bug: dune-build-info cannot be loaded in an OCaml toplevel due to missing generated module
- **#5549** `S7` `D4` - dune build -w restricting job number for no reason — Bug: watch mode rebuilds are observably slower than fresh builds due to unnecessary job number restriction during rule finding
- **#5486** `S6` `D2` - no-cmx-file warning emitted for external dependency after adding internal library — Bug: spurious Warning 58 emitted for external dependencies when an internal library is added
- **#5485** `S4` `D2` - Dune 3 cannot delete files named `NUL` on Windows — Bug: dune creates `NUL` files on Windows that it then cannot delete, blocking builds
- **#5468** `S2` `D2` - Internal error: EACCES exception uncaught, opinions on how to catch it? — Bug: uncaught EACCES exception when XDG_RUNTIME_DIR points to a non-existent/inaccessible directory
- **#5467** `S5` `D1` - Dune 3 all generated or promoted files on Windows are set executable — Bug: regression from dune 2.9 where all promoted/generated files on Windows/Cygwin get their executable bit set
- **#5460** `S3` `D2` - Project initialized with `init exec` does not build (cannot find root) — Bug: `dune init exec` creates a project that immediately fails to build because dune cannot find the workspace root
- **#5447** `S2` `D4` - dependency cycle that does not involve any files — Bug: internal error / crash with "dependency cycle that does not involve any files" message
- **#5417** `S7` `D2` - `grep -z` causes files to diff as binary — Bug: using `grep -z` (which produces NUL-separated output) causes dune to treat diff output as binary, preventing test correction
- **#5378** `S4` `D2` - wrong call to --ppx flags (slash issue) — Bug: ppx flags have incorrect path separators on Windows, preventing compilation
- **#5322** `S3` `D3` - Relocatable site does not work when the install directory is outside the build directory — Bug: site location placeholder is replaced by absolute path regardless of --relocatable flag
- **#5313** `S1` `D2` - `(dirs ..` with paths of depth >= 2 are just ignored — Bug: paths with depth >= 2 in the `(dirs ...)` stanza are silently ignored without any error message
- **#5312** `S2` `D3` - dune utop blows up with an exception when cohttp-lwt-unix is present in ~/.ocamlinit — Bug: dune utop crashes with an exception when certain packages are required in ~/.ocamlinit
- **#5301** `S7` `D2` - Vendored libraries are not linked statically to public libraries that use them — Bug: vendored git submodule libraries are not properly linked statically when installing via opam
- **#5267** `S3` `D2` - [3.0 opam failures] Could not find the .cmi file — Bug: dune 3.0 fails to find .cmi files for packages that built fine with dune 2.x
- **#5238** `S1` `D2` - Bad ppx annotations are not reported — Bug: invalid/unused ppx annotations are silently ignored instead of producing errors
- **#5229** `S3` `D2` - @doc "Couldn't find the following modules: Stdlib" — Bug: `dune build @doc` fails with missing module errors for Stdlib and other installed libraries
- **#5122** `S5` `D5` - Package dependency check doesn't take into account recursive dependencies — Bug: dune fails to resolve transitive/recursive package dependencies across nested dune-project files
- **#5104** `S5` `D2` - Possible regression in the `select` stanza — Bug: regression where select stanza no longer allows files in subdirectories in dune lang 2.9+
- **#5081** `S3` `D2` - Use of (modes c) does not work — Bug: `(modes c)` to produce `.bc.c` files is documented but does not work, giving "Unknown value c"
- **#5044** `S6` `D2` - Warning 58 with virtual_modules — Bug: spurious Warning 58 (no-cmx-file) when using virtual_modules with --profile=release
- **#4971** `S3` `D2` - MDX stanza not causing dependencies to be built — Bug: mdx stanza silently ignores missing files instead of raising an error or building them
- **#4962** `S3` `D2` - Vendored dependencies interacting poorly with esy and opam — Vendored deps cause incorrect behavior with esy/opam package managers
- **#4957** `S7` `D2` - Using `findlib.dynload` shouldn't imply `-linkall` for executables — Adding findlib.dynload incorrectly forces -linkall, creating excessively large executables
- **#4949** `S6` `D2` - Remove runtime dependency on OCaml when building a pure Coq project — Dune incorrectly requires ocamlc even when building a project that needs no OCaml, producing a misleading error
- **#4895** `S7` `D2` - The documentation/value of %{system} is not consistent — The %{system} variable value does not match what the documentation claims it should be
- **#4892** `S3` `D2` - Private modules cause missing build path (in the ocaml-merlin dump) — Merlin config is missing the byte directory for libraries with private modules, causing locate failures
- **#4866** `S7` `D2` - dune doesn't cleanup all .merlin files and doesn't inform user of using them — Dune leaves behind stale generated .merlin files and doesn't inform users about the transition
- **#4816** `S5` `D2` - Optional argument for --promote-install-files breaks CLI compatibility — Dune 2.9.0 breaks backward compatibility of the --promote-install-files CLI flag
- **#4547** `S4` `D3` - Too much string escaping in overlapped dependencies error path on Windows — Error messages on Windows show excessively escaped backslashes, making paths unreadable
- **#4531** `S3` `D2` - Issues with --action-stdxxx-on-success — The option operates at the wrong level (single run vs whole action), producing unintuitive behavior
- **#4525** `S7` `D2` - Making (setenv) easy to test — When an action with setenv fails, the reproduced command omits environment variables, making it impossible to reproduce
- **#4482** `S4` `D3` - Random "Permission denied" errors on macOS ARM64 — Random compilation failures specific to macOS ARM64, working fine on other platforms
- **#4479** `S5` `D2` - interop between dune and merlin since 2.8 does not work with ppx_expect — Regression: merlin queries fail with ppx_expect after upgrading from dune 2.7.1 to later versions
- **#4468** `S7` `D2` - Error: Invalid dune file on Unicode in dune file — Dune incorrectly rejects Unicode characters in paths within dune files
- **#4457** `S7` `D2` - Documentation for determining package version is incorrect — Actual behavior of package version detection does not match what the documentation states
- **#4445** `S6` `D2` - action plugin: trying to read empty / non-existing directory raises — read_directory_with_glob raises an unhelpful error on empty or non-existing directories instead of returning empty
- **#4347** `S7` `D2` - Byte target can't be debugged with ocamldebug — Dune-built .bc files are missing debug symbols that ocamlc -g produces correctly
- **#4194** `S2` `D3` - Crash in Stdune__io.Make.eagerly_input_string — Dune crashes with Invalid_argument("Bytes.create") exception on arm32 when running tests
- **#4156** `S3` `D4` - ppxs are built in the target context in cross-compilation settings — PPX libraries are incorrectly built in the target context instead of the host context during cross-compilation, causing build failures
- **#4130** `S4` `D3` - pkg-config not resolved on windows with dune configurator — C.Pkg_config.get always returns None on Windows even when pkg-config works correctly
- **#4123** `S3` `D2` - -opaque option breaks equivalence between release and dev compilation in presence of [@inline always] — dune build fails while dune build --release succeeds due to -opaque flag interaction with @inlined always
- **#4111** `S7` `D2` - Dune doesn't generate correct .merlin file when directory path contains space — Generated .merlin file has incorrect path escaping when project path contains spaces
- **#4070** `S1` `D4` - Undesired conflict between vendored library and public library by the same name — Dune incorrectly reports a conflict when a vendored library has the same name as an external one used by a different dependency
- **#4068** `S7` `D2` - Allow to create sublibraries named "opam" — Creating a sublibrary named "opam" causes symlink errors during build
- **#4051** `S7` `D3` - opam file generation: dune bound only considers toplevel project — Generated opam files have incorrect dune version bounds when nested projects use a higher dune language version
- **#4039** `S3` `D2` - flambda with -nostdlib and transitive stdlib not finding cmx — Dune fails to add stdlib during linking when it is a transitive dependency with -nostdlib, causing flambda optimization failures
- **#4021** `S7` `D2` - auto-formatting of dune files does not preserve end-of-line strings — Auto-formatter incorrectly converts end-of-line strings to regular escaped strings
- **#4018** `S5` `D3` - Cannot add absolute paths to CRAM sanitizer on Windows — Path sanitization is broken on Windows because colons in absolute paths conflict with the separator format
- **#4017** `S4` `D3` - Sanitized paths for CRAM tests in Windows mix `/` and `\` — Path sanitization fails on Windows due to inconsistent forward/back slash mixing
- **#3917** `S3` `D4` - Explicit executable dependencies and cross-compilation — Explicit .exe dependencies in rules resolve to cross-compiled workspace instead of host context, breaking cross-compilation
- **#3916** `S7` `D1` - Duplicate bounds on autogenerated opam files — Generated opam files contain duplicate dune version bounds (e.g. `{>= "2.7" & >= "2.7"}`)
- **#3913** `S7` `D4` - Dune finds non existing library conflict without (implicit_transitive_deps false) — Dune incorrectly detects a library conflict that doesn't actually exist in certain vendoring scenarios
- **#3910** `S5` `D2` - Mode `(byte shared_object)` cannot find stubs in Dune >= 2.1 — Regression from dune 2.0: byte shared object mode fails to find stubs that were found before
- **#3908** `S3` `D2` - does dune enforce complete cmxs files? — Generated .cmxs files may be missing necessary C stubs, causing dynamic linking failures
- **#3868** `S7` `D2` - Incorrect passing of linker options from pkg-config to ocamlmklib — ocamlmklib emits warnings about link options returned by pkg-config (e.g. `-Wl,--export-dynamic`), meaning options are incorrectly passed/omitted
- **#3805** `S3` `D2` - No such file or directory when DUNE_BUILD_DIR is set during test — `dune runtest` fails when `DUNE_BUILD_DIR` environment variable is set
- **#3784** `S6` `D2` - "Too many opam files for package" error is incorrect — Error message references opam files even for packages defined in dune-project, producing a misleading/wrong error
- **#3779** `S3` `D2` - %{lib-private} and multiple packages — `%{lib-private}` does not work when used across packages defined in the same project
- **#3755** `S3` `D2` - %{env:FOO=<val>} does not accept spaces in <val> — Spaces in default values for env variable expansion cause a parse error, which is a limitation/misfeature
- **#3700** `S7` `D3` - OPAM file generation doesn't respect (lang dune) — When `(lang dune 2.5)` is set but `(dune (>= 1.11))` is specified in depends, dune silently generates an invalid opam file instead of warning
- **#3645** `S3` `D2` - "The module X is an alias for module Y.X, which is missing" when X comes from a virtual library — Aliased modules from virtual libraries produce incorrect errors when installed/pinned (works when vendored)
- **#3642** `S7` `D2` - Adding new formatters can break older projects — Dune tries to invoke ocamlformat even without a `.ocamlformat` file, producing warnings/errors for projects that don't use it
- **#3638** `S7` `D2` - env-vars ignored under exec — `env-vars` set in the `(env)` stanza are not applied when running executables with `dune exec`
- **#3634** `S7` `D5` - foreign archive handling — Inconsistent behavior regarding whether dune links against .a or .so archives; different behavior from identical configuration
- **#3618** `S5` `D2` - Test "github660" does not pass with flambda — A dune test fails when built with flambda, indicating a regression or incorrect behavior
- **#3591** `S2` `D4` - Internal error: dependency cycle with virtual_modules — Building a project with virtual_modules causes an internal error (dependency cycle crash) instead of proper behavior
- **#3569** `S3` `D4` - Expect tests with (implicit_transitive_deps false) — Setting `(implicit_transitive_deps false)` causes `Unbound module Expect_test_common` when using expect tests, even though the dependency should be resolved
- **#3549** `S7` `D2` - dune not checking modules in modules_before_stdlib — Dune doesn't validate/complain about invalid module names in `modules_before_stdlib`
- **#3516** `S7` `D2` - dune format-dune-file doesn't respect the formatting stanza — `dune format-dune-file` ignores the `(formatting (enabled_for ocaml reason))` stanza and formats dune files anyway
- **#3487** `S6` `D2` - Hinted `external-lib-deps` for `dune utop` does not include Odoc — The suggested `dune external-lib-deps --missing` command does not detect the missing `utop` library, giving misleading guidance
- **#3484** `S2` `D3` - stacktrace when trying to promote into a binary in use (linux) — Dune crashes with a stacktrace when trying to promote a binary that is currently running, instead of handling the "Text file busy" error gracefully
- **#3474** `S7` `D2` - bootstrap does not properly search PATH — Dune bootstrap incorrectly assumes all `ocaml*` programs live next to the first one found, instead of properly searching PATH for each
- **#3467** `S3` `D2` - modes not respected in combination with library with public_name — `(modes native)` still causes `ocamlc` to run on implementation files when a library has a `public_name`
- **#3463** `S2` `D3` - Dune is mangling qtest/ounit output — Dune's output buffering corrupts escape codes related to cursor movement, producing garbled test output
- **#3382** `S3` `D2` - "Unknown constructor vendored_dirs" when using OCaml syntax — `vendored_dirs` works in static dune files but fails with "Unknown constructor" when using OCaml (tuareg) syntax
- **#3378** `S3` `D2` - Library variable expansion needs a library installed to work — `%{lib:<pkg>:<file>}` fails when the package only has `install` stanzas and no actual library/executable definition
- **#3362** `S3` `D2` ~~FIXED~~ - Cannot use `%{lib:...}` in the `flags` stanza — Test added in PR #14146 (merged); already works on current main
- **#3349** `S3` `D1` ~~CLOSED~~ - `(disable_dynamically_linked_foreign_archives true)` should not try to build js targets — No longer reproducible; jsoo pipeline reworked since 2020
- **#3322** `S4` `D1` - dune exec needs to add .exe on Windows — `dune exec -- foo` on Windows doesn't consider `foo.exe`, leading to stale execution or errors
- **#3286** `S3` `D2` - Failing package builds with Load commands in Coq files — `dune build -p` doesn't copy non-module files needed by Coq's `Load` command into the build tree, causing build failures
- **#3230** `S7` `D2` - Long form target inference is not properly versioned — Target inference for long-form actions lacks a `since` version check, allowing it in `(lang dune 1.2)` when it should only work in >= 2.0
- **#3223** `S7` `D2` - dune-project not formatted with @fmt — `dune build @fmt` does not format the `dune-project` file, inconsistent with formatting of other dune files
- **#3214** `S3` `D2` - Fl_dynload.load_packages in a PPX — `findlib_initl.ml-gen` is not generated for PPX preprocessors, so `Fl_dynload.load_packages` fails in PPX rewriters
- **#3192** `S3` `D2` - (package ...) doesn't work when package is installed and not in the workspace — `(deps (package bar))` fails with "No rule found for alias .bar-files" when the package is installed via opam rather than in the workspace
- **#3182** `S7` `D2` - The @all alias does not produce .cmt files which are produced by @check — `dune build` produces only `.cmti` but not `.cmt`, while `dune build @check` produces both, which is inconsistent
- **#3173** `S3` `D2` - can't promote into a directory start with underscore — Promoting output into a directory starting with underscore fails with "directory does not exist" even though the directory exists
- **#3160** `S2` `D3` - Dune runtest incorrectly changes escape codes related to cursor movement — Dune's output processing corrupts ANSI escape codes that involve cursor movement, breaking formatted test output (e.g., Rely)
- **#3151** `S7` `D5` - Recursive alias in vendored directories are not well defined — `@all` and `@@all` behave inconsistently in vendored directories
- **#3040** `S4` `D3` - Dune does not correctly handle c_compiler using a shim — Dune incorrectly splits a C compiler shim command (e.g., `xcrun -sdk macosx10.14 clang`) and passes parts as separate `-ccopt` arguments
- **#3025** `S3` `D2` - dune install: ocamlfind point to the wrong directory in a local switch — In a local switch without ocamlfind, dune uses the global switch's ocamlfind and tries to install to the wrong location
- **#3008** `S5` `D2` - Failed to pass tests: "The selected switch default is not installed" — Test suite fails because it assumes a global opam switch named "default" exists
- **#2991** `S4` `D2` - Error "The command line is too long" for very short command line (<250 characters) on Cygwin/Windows — Build fails with "command line too long" error even for very short command lines on Windows/Cygwin
- **#2938** `S3` `D2` - (dirs ...) not recognised in dune2 — `(dirs *)` works in a static dune file but is rejected with "Unknown constructor" when used via OCaml-syntax dune file generation
- **#2913** `S7` `D2` - Dune should not look up other sub-directories when given `-p` — `dune build -p project-a` incorrectly scans for packages used by `project-b` in sibling directories, causing race conditions
- **#2909** `S3` `D3` - Virtual Libraries: Dune files don't include required source entries when relying on virtual modules — Generated `.merlin` files for modules depending on virtual libraries lack `S` source entries, breaking goto-location in merlin
- **#2818** `S6` `D2` - Cycles reported by dune are cryptic — Module cycle errors reported by dune don't correspond to actual user code, likely due to over-approximation of the dependency graph
- **#2773** `S7` `D3` - [sandbox] odoc rules are broken — Odoc rules produce broken cross-references (xref-unresolved) inside the sandbox
- **#2757** `S7` `D2` - dune install ignores --for-release-of-packages — The `install` command ignores the `--for-release-of-packages` flag that works for `build`, `runtest`, and `external-lib-deps`, requiring a different invocation
- **#2565** `S3` `D3` - Minor improvements for Build_info and install — Multiple bugs: documentation example code doesn't compile (wrong API usage), `--display=quiet` is not respected by install messages, `dune install --help` claims `--watch` support but ignores it, and setting `--prefix=_build/install/...` silently produces empty executables
- **#2445** `S7` `D2` - dune forwards signal to process but sends SIGKILL right away — Bug: dune sends SIGKILL immediately after SIGINT instead of giving processes time to clean up, making graceful shutdown impossible
- **#2420** `S7` `D3` - Configurator does not have access to C flags set in (env) — Bug: configurator ignores C flags set in workspace env stanza, producing incorrect build configuration results in multi-context workspaces
- **#2370** `S5` `D1` ~~WIP~~ - Hygiene issue in _build with .h files — Bug/regression: since Dune 1.9.0, .h files are copied eagerly into _build even when no C compilation is needed, creating misleading build artifacts (PR #14172 open — test only)
- **#2353** `S6` `D1` - Dune installs empty META file for package with no library — Bug: dune generates and installs a blank META file for executable-only packages, causing confusing output from ocamlfind (version: n/a)
- **#2144** `S3` `D2` - Error in documentation for dirs stanza — Bug: the documentation claims files in ignored sub-directories can be depended on, but this does not work; also `(data_only_dirs)` requires listing dirs in both `(dirs)` and `(data_only_dirs)` which is undocumented and confusing
- **#2100** `S3` `D2` - [dynlink] Error on dynamic link — Bug: dynamic linking fails with "undefined symbol: caml_mutex_lock" when using Fl_dynload with dune-built libraries
- **#2003** `S3` `D2` - Ability to use sub-extensions for virtual modules — Bug/misfeature: module name normalization (stripping sub-extensions like `.test.re`) does not work for virtual library implementations, unlike everywhere else in dune
- **#1974** `S7` `D2` - `@all` target doesn't interact well with `(include_subdirs ...)` — Bug: targets generated by subdirs are not included in the `@all` alias, which should contain all buildable targets
- **#1920** `S7` `D5` - Detect case-insensitive filesystems and prevent double-linking — Bug: on case-insensitive filesystems, dune links `Base` and `base` as separate libraries causing "both define a module" errors at link time
- **#1819** `S2` `D5` - Dune always sets -no-alias-deps for all files — Bug/misfeature: dune unconditionally sets `-no-alias-deps` which was never intended to be the default, causing runtime crashes for libraries like lablgtk3 that depend on module initialization side effects
- **#1645** `S3` `D2` - Odoc: valid module name clashes cause issues — Bug: dune/odoc produces "multiple rules generated" errors when two valid sub-libraries in the same package have unwrapped modules with the same name, even though they cannot be linked together
- **#1593** `S7` `D3` - Watermarking works only in the GIT root, not dune root — Bug: `dune subst` looks for `.git` directory rather than `dune-project` to determine the project root, preventing watermarking from working when OCaml code is in a subdirectory of a git repository
- **#1415** `S3` `D2` - Implementations of virtual libraries aren't installed correctly — Bug: cmt, cmti, and source files belonging to virtual libraries are not installed with their implementations, breaking tooling features like "go to definition"
- **#1371** `S7` `D2` - -nostdlib in flags field, but forgotten when building stubs files — Bug: when `-nostdlib` is specified in flags, dune does not pass it when building C stubs, causing unwanted include paths to be passed to gcc
- **#1187** `S3` `D2` - $ dune utop doesn't work for dune itself — Bug: `dune utop` fails with "Required module `Which_program' is unavailable" error when used on the dune project itself
- **#878** `S7` `D1` ~~FIXED~~ - `dune subst` can add a duplicate version field in opam — Fixed in PR #14136 (merged)
- **#108** `S3` `D2` - bytecode + c stubs not working as expected — Bug: bytecode executables with C stubs fail at runtime with "cannot load shared library" error
