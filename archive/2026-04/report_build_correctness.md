# Build Correctness & Linking

## Summary

This category contains 79 bugs spanning from issue #108 to #14085, representing some of the oldest and newest open issues in the Dune tracker. The dominant theme is incorrect linking behavior, particularly around C stubs and bytecode: bytecode executables fail to find shared libraries at runtime (#108), byte shared_object mode cannot link C stubs (#7800, #3910), C archives for byte targets omit dynamic dependencies (#6263), and ctypes stubs are compiled without `-fPIC` (#5809). A closely related cluster involves ctypes integration problems more broadly — flags added twice causing linker errors (#6481), the `deps` field not following the dependency specification language (#11440), and foreign archives conflicting with ctypes (#9773). Linking issues also arise with plugins and dynamic loading: `.cmxs` files may be missing C stubs (#3908), `embed_in_plugin_libraries` fails with link-time code (#6086), and native plugin loading produces undefined symbol errors (#10697).

A second major theme is incorrect flag handling and environment interaction. Dune overwrites user-provided C debug flags by appending `-g` after `-g0` (#11941), ignores the standard `CFLAGS`/`CXXFLAGS` environment variables entirely (#8291), and forces `-linkall` unnecessarily when using dune-site without plugins (#11281) or when adding `findlib.dynload` (#4957). The `-opaque` flag in dev mode breaks builds that succeed in release mode (#4123), and flambda with `-nostdlib` fails to find transitive stdlib `.cmx` files (#4039). Several menhir-related issues show version-sensitive flag breakage (#10732, #10707). There are also multiple cases where documented features simply do not work: `(modes c)` (#5081), `(optional)` in executables (#5621), `(enabled_if %{read:...})` (#11042), and `%{lib:...}` in flags (#3362).

The third recurring pattern is cache and staleness problems. The dune cache suppresses compiler warnings on cache hits (#7460), `--cache=disabled` paradoxically triggers recompilation (#12309), toolchain-provided compiler packages miss the shared cache on first build (#11583), and `DUNE_CACHE_ROOT` leaks into cram test environments (#11501). Stale artifact issues appear when dune picks up installed (stale) stub libraries instead of locally built ones in byte mode (#9979). Build correctness across targets is also problematic: `@check` can fail when `@all` succeeds (#9724), cram tests can access libraries not in their declared deps (#6012), and `-p` causes dune to scan sibling directories for unrelated packages (#2913). Filesystem-level issues include case-insensitive filesystem double-linking (#1920), incorrect `.cmi` filename casing (#8709), and virtual library implementations not being installed with their artifacts (#1415). Many of these bugs have been open for years — over 30 issues predate #8000 — indicating deep, long-standing correctness gaps in Dune's build and linking model.


### Severity Breakdown

| Severity | Count |
|----------|-------|
| **S1** — Silent Correctness Failures | 6 |
| **S2** — Crashes & Data Loss | 2 |
| **S3** — Broken Documented Behavior | 33 |
| **S5** — Regressions | 13 |
| **S6** — Misleading Errors & Poor UX | 3 |
| **S7** — Workaroundable Bugs | 22 |

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| **D1** — Straightforward Fix | 6 |
| **D2** — Moderate Investigation | 56 |
| **D3** — Subsystem Rework | 9 |
| **D5** — Design Problem | 8 |

## Issues (79 bugs)

- **#14085** `S5` `D2` - 3.22.0 regression: error about non-existent excluded module from `(select)` in a different stanza — Regression in 3.22.0 where `dune build` errors claiming a module doesn't exist when using `(select)` in a separate stanza with module exclusion
- **#13825** `S3` `D2` - archives are incorrectly detected by inspecting the extension — Archive type detection by file extension doesn't work because downloaded files have generic filenames like `download`
- **#13782** `S3` `D2` - `dune show targets` does not work on build-only directories — `dune show targets _build/default/.simple.objs` fails when it should work
- **#13001** `S7` `D2` - modules of library using ctypes without (modules) field are incorrectly validated — ctypes library without explicit (modules) field causes incorrect module validation, breaking builds
- **#12996** `S2` `D5` - `dune exec` doesn't perform install stanza — `dune exec` skips install stanza processing, causing binaries using dune-site to fail finding static files
- **#12309** `S7` `D2` - `--cache=disabled` is triggering some re-compilation — Building with `--cache=disabled` incorrectly triggers recompilation of already-built artifacts
- **#12108** `S2` `D3` - Poor error reporting in cram tests, take 2 — `set -o pipefail` causes `***** UNREACHABLE *****` output instead of a meaningful error; stderr from shell is not reported
- **#11941** `S1` `D2` - Dune overwrites the user provided debug flag in foreign stubs — Dune appends `-g` after user-specified C flags, making it impossible to disable debug info with `-g0`
- **#11583** `S3` `D3` - packages depending on a toolchain-provided compiler can't cache the first time — Bug: shared cache misses occur on first build when using toolchains; second build does not benefit from the cache as expected.
- **#11501** `S6` `D2` - dune doesn't reset DUNE_CACHE_ROOT inside cram tests — Bug: environment variable leakage causes spurious warnings inside cram tests.
- **#11440** `S3` `D3` - ctypes' `deps` field doesn't follow the dependency specification language — Bug: the `deps` field in ctypes doesn't work as documented; it doesn't follow the dependency specification language.
- **#11418** `S3` `D2` - dune-build-info is not working on flambda1 switch — Bug: `dune-build-info` fails with warning 58 error on Flambda1 switches; works on closure.
- **#11281** `S7` `D3` - Dune site (without plugins) forces `-linkall` — Bug/misfeature: `-linkall` is forced even when using dune sites without plugins, which is unnecessary and harmful.
- **#11225** `S1` `D3` - dune-build-info: spurious `git describe` output instead of version string — Bug: `dune-build-info` returns git describe output instead of the version specified in `dune-project`.
- **#11163** `S7` `D2` - dune cache — Bug concern: dune cache was enabled by default despite known issues; reporter asks whether prior cache bugs were actually fixed.
- **#11110** `S7` `D1` - Custom `libexec` sites install does not set executable bit — Bug: binaries installed to custom `libexec` sites lack the executable permission bit.
- **#11042** `S3` `D2` - Using (enabled_if %{read:...}) — Bug: documented feature `(enabled_if %{read:...})` doesn't work; produces error "%{read:..} isn't allowed in this position."
- **#10792** `S3` `D2` - Doc for building byte code incorrect — Bug: documentation for building bytecode executables is incorrect; `dune build foo.bc` doesn't work as documented.
- **#10732** `S5` `D2` - menhir option `--only-tokens` does not work — Bug: `--only-tokens` flag works with menhir 2.0 but not with 3.0; produces error about missing `.conflicts` file.
- **#10707** `S3` `D1` - Add correct lower bound to menhir — Bug/misfeature: dune assumes menhir supports `--infer-write-query` but doesn't enforce a minimum version, causing build failures with older menhir.
- **#10697** `S3` `D3` - Dynamic loading of packages: linking issues — Bug: dynamic loading of plugins with native dependencies (e.g., LLVM) fails with undefined symbol errors.
- **#10588** `S3` `D2` - --ignore-promoted-rules has no effect on copy_files — The flag does not work as documented for copy_files rules, which is a behavior/documentation mismatch
- **#10360** `S7` `D1` - (executables_implicit_empty_intf ...) expects dune >= 2.9 but was only added in 3.0 — Version check is wrong; the feature requires 3.0 but the code/docs say 2.9
- **#10141** `S5` `D1` - git describe is incorrect for Dune's main branch since 3.12 — `git describe --tags` reports incorrect version information on the main branch
- **#9979** `S1` `D2` - Dune links against wrong cstubs in byte mode — Dune picks up an installed (stale) version of stub libraries instead of the locally built ones when building in byte mode
- **#9773** `S5` `D3` - Ctypes and foreign bindings won't bundle library properly — Multiple rules generated for the same libdash.a; foreign archives with ctypes causes build failures
- **#9724** `S3` `D2` - `dune build @check` should pass if `dune build @all` does — @check fails in cases where @all succeeds, but @check should be a subset of @all
- **#9662** `S3` `D2` - dune-site: use string list instead of Location.t — Generated sites module uses an abstract type that requires consumers to also depend on dune-site, causing build failures
- **#8770** `S7` `D2` - TUI captures clicks when using inside vscode — TUI captures mouse clicks in vscode integrated terminal, preventing clicking on underlined locations; this is broken interaction behavior.
- **#8727** `S5` `D2` - The issues of `--ignore-promote-rules` — The flag has known misfeatures: it doesn't work correctly with the fallback mechanism due to a race condition, and the overall design is acknowledged as problematic.
- **#8709** `S5` `D2` - Generate cmi files that match the input — Dune generates `.cmi` files with incorrect casing (lowercasing filenames with multiple capitals like `QCheck2`), which surfaced a compiler regression and is itself incorrect behavior.
- **#8291** `S7` `D5` - Please honor CFLAGS — Dune ignores the standard CFLAGS/CXXFLAGS environment variables when compiling C code, which deviates from standard build system behavior and breaks expected workflows.
- **#8242** `S5` `D2` - Very slow emacs compilation buffer updates — Regression from dune 3.7 to 3.9; emacs compilation buffer updates became very slow due to excessive "Done: 100%" output even when nothing needs building.
- **#7800** `S3` `D2` - `(byte shared_object)` linking mode does not allow linking C stubs — Documented linking mode doesn't work as expected; C stubs cannot be linked with byte shared_object mode.
- **#7664** `S5` `D2` - program output from `exec -w` and rule actions interspersed with repeated dune status output — Regression from dune 3.4.1 to 3.7.1; program output is interspersed with repeated status messages, making output unreadable.
- **#7583** `S3` `D5` - What should happen when exposing code from a private package? — Compilation fails with missing `.cmi` files when re-exposing private package code through a public module, with no warning at library compile time
- **#7460** `S1` `D2` - Cache hits "hide" warnings — When dune cache is enabled, cache hits suppress compiler warnings that should still be displayed
- **#7073** `S3` `D2` - ld: Error: unable to disambiguate: -shared-libgcc — Linker error when building with `(modes object)` due to conflicting `-shared-libgcc` flags
- **#6607** `S7` `D2` - Test suite is broken when CLICOLOR_FORCE=1 — Dune's own test suite fails when `CLICOLOR_FORCE=1` is set because expect tests include color codes
- **#6481** `S1` `D2` - ctypes: flags are added twice — ctypes build adds flags twice, causing linker errors (regression from dune 3.5.0 to 3.6.0)
- **#6263** `S3` `D2` - C archive for byte target not built to include dynamic dependencies — Bytecode library C stubs do not include dynamic dependencies, so `ldd` on the resulting `.so` does not show them
- **#6148** `S3` `D1` - `root_module` generates duplicate module definition when `logs.lwt` is a dependency — Bug: dune generates a `root.ml-gen` file with duplicate module definitions causing a compilation error
- **#6086** `S3` `D3` - The `embed_in_plugin_libraries` stanza fails with libraries requiring link-time code — Bug: "Multiple rules generated" error when using embed_in_plugin_libraries with link-time generated code
- **#6012** `S1` `D2` - Cram tests can access OCaml libraries not in deps, if they are compiled — Bug: cram tests can use libraries not listed in their dependencies if those libraries happen to be already compiled
- **#5899** `S7` `D2` - Incorrect implementation of Workspace_root — Bug: the `to_cwd` value is incorrect in the workspace root implementation
- **#5809** `S3` `D3` - ctypes stanza does not compile cstubs .o files with -fPIC — Bug: ctypes stub generation produces non-position-independent object files, causing linking failures for shared libraries
- **#5735** `S7` `D2` - cmxs should not be installed in libexec — Bug: .cmxs files are incorrectly installed in libexec instead of lib due to a wrong fix for the exec bit
- **#5697** `S3` `D5` - env stanza should support variables `%{...}` — Bug: variables like `%{project_root}` unexpectedly fail in the env stanza with "Atom or quoted string expected"
- **#5621** `S3` `D5` - (optional) in executables doesn't work — Bug: the `(optional)` field in executables stanza does not work, preventing conditional building of executables
- **#5486** `S6` `D2` - no-cmx-file warning emitted for external dependency after adding internal library — Bug: spurious Warning 58 emitted for external dependencies when an internal library is added
- **#5460** `S3` `D2` - Project initialized with `init exec` does not build (cannot find root) — Bug: `dune init exec` creates a project that immediately fails to build because dune cannot find the workspace root
- **#5417** `S7` `D2` - `grep -z` causes files to diff as binary — Bug: using `grep -z` (which produces NUL-separated output) causes dune to treat diff output as binary, preventing test correction
- **#5122** `S5` `D5` - Package dependency check doesn't take into account recursive dependencies — Bug: dune fails to resolve transitive/recursive package dependencies across nested dune-project files
- **#5104** `S5` `D2` - Possible regression in the `select` stanza — Bug: regression where select stanza no longer allows files in subdirectories in dune lang 2.9+
- **#5081** `S3` `D2` - Use of (modes c) does not work — Bug: `(modes c)` to produce `.bc.c` files is documented but does not work, giving "Unknown value c"
- **#5044** `S6` `D2` - Warning 58 with virtual_modules — Bug: spurious Warning 58 (no-cmx-file) when using virtual_modules with --profile=release
- **#4957** `S7` `D2` - Using `findlib.dynload` shouldn't imply `-linkall` for executables — Adding findlib.dynload incorrectly forces -linkall, creating excessively large executables
- **#4816** `S5` `D2` - Optional argument for --promote-install-files breaks CLI compatibility — Dune 2.9.0 breaks backward compatibility of the --promote-install-files CLI flag
- **#4531** `S3` `D2` - Issues with --action-stdxxx-on-success — The option operates at the wrong level (single run vs whole action), producing unintuitive behavior
- **#4525** `S7` `D2` - Making (setenv) easy to test — When an action with setenv fails, the reproduced command omits environment variables, making it impossible to reproduce
- **#4457** `S7` `D2` - Documentation for determining package version is incorrect — Actual behavior of package version detection does not match what the documentation states
- **#4347** `S7` `D2` - Byte target can't be debugged with ocamldebug — Dune-built .bc files are missing debug symbols that ocamlc -g produces correctly
- **#4123** `S3` `D2` - -opaque option breaks equivalence between release and dev compilation in presence of [@inline always] — dune build fails while dune build --release succeeds due to -opaque flag interaction with @inlined always
- **#4039** `S3` `D2` - flambda with -nostdlib and transitive stdlib not finding cmx — Dune fails to add stdlib during linking when it is a transitive dependency with -nostdlib, causing flambda optimization failures
- **#4021** `S7` `D2` - auto-formatting of dune files does not preserve end-of-line strings — Auto-formatter incorrectly converts end-of-line strings to regular escaped strings
- **#3910** `S5` `D2` - Mode `(byte shared_object)` cannot find stubs in Dune >= 2.1 — Regression from dune 2.0: byte shared object mode fails to find stubs that were found before
- **#3908** `S3` `D2` - does dune enforce complete cmxs files? — Generated .cmxs files may be missing necessary C stubs, causing dynamic linking failures
- **#3634** `S7` `D5` - foreign archive handling — Inconsistent behavior regarding whether dune links against .a or .so archives; different behavior from identical configuration
- **#3618** `S5` `D2` - Test "github660" does not pass with flambda — A dune test fails when built with flambda, indicating a regression or incorrect behavior
- **#3467** `S3` `D2` - modes not respected in combination with library with public_name — `(modes native)` still causes `ocamlc` to run on implementation files when a library has a `public_name`
- **#3362** `S3` `D2` - Cannot use `%{lib:...}` in the `flags` stanza — Using `%{lib:...}` in flags gives an error even though a workaround with intermediate files works, indicating an artificial restriction
- **#3349** `S3` `D1` - `(disable_dynamically_linked_foreign_archives true)` should not try to build js targets — Default build target tries to build `.bc.js` targets even when dynamic foreign archives are disabled, causing build failure
- **#2913** `S7` `D2` - Dune should not look up other sub-directories when given `-p` — `dune build -p project-a` incorrectly scans for packages used by `project-b` in sibling directories, causing race conditions
- **#2757** `S7` `D2` - dune install ignores --for-release-of-packages — The `install` command ignores the `--for-release-of-packages` flag that works for `build`, `runtest`, and `external-lib-deps`, requiring a different invocation
- **#2445** `S7` `D2` - dune forwards signal to process but sends SIGKILL right away — Bug: dune sends SIGKILL immediately after SIGINT instead of giving processes time to clean up, making graceful shutdown impossible
- **#2003** `S3` `D2` - Ability to use sub-extensions for virtual modules — Bug/misfeature: module name normalization (stripping sub-extensions like `.test.re`) does not work for virtual library implementations, unlike everywhere else in dune
- **#1920** `S7` `D5` - Detect case-insensitive filesystems and prevent double-linking — Bug: on case-insensitive filesystems, dune links `Base` and `base` as separate libraries causing "both define a module" errors at link time
- **#1415** `S3` `D2` - Implementations of virtual libraries aren't installed correctly — Bug: cmt, cmti, and source files belonging to virtual libraries are not installed with their implementations, breaking tooling features like "go to definition"
- **#108** `S3` `D2` - bytecode + c stubs not working as expected — Bug: bytecode executables with C stubs fail at runtime with "cannot load shared library" error
