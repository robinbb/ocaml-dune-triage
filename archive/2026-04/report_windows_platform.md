# Windows & Platform-Specific

## Summary

Windows is by far the most affected platform in this category, accounting for roughly 30 of the 51 open bugs. The issues span nearly every layer of dune's interaction with the Windows operating system: path handling is a persistent source of failures, with bugs ranging from MAX_PATH limits (#11303) to backslash/forward-slash inconsistencies in ppx flags (#5378), CRAM test path sanitization (#4017, #4018), and build prefix map encoding that breaks on colons in drive letters (#10176). Sandbox cleanup is fragile on Windows due to both NTFS junctions (#13909) and unicode directory names (#13993). Several bugs involve dune crashing outright on Windows with internal errors, including crashes with melange-webapi (#10764), CRAM tests (#10872), and compilation of certain packages (#12535). Fundamental Windows conventions are also neglected: `dune exec` does not append `.exe` (#3322), `(run)` does not search for `.cmd` files (#9128), generated files get incorrect permissions (#5467), and opam templates are written with carriage returns (#9482). The MSVC toolchain has its own cluster of problems, including Unix-style pkg-config flags being passed to the MSVC compiler (#11590), incorrect stub library naming (#10042), and flexlink incompatibility with C++ flags (#8643). The terminal UI is entirely broken on Windows (#6730).

macOS contributes a notable subset of issues. The macOS linker produces duplicate library warnings as a regression (#10874), `PKG_CONFIG_PATH` is silently overridden by brew paths in dune-configurator (#10805), and the `xcrun` compiler shim is incorrectly parsed into separate arguments (#3040). Platform-specific crashes have appeared on macOS ARM64, including random "Permission denied" errors (#4482) and a compilation failure specific to M2 hardware (#10940). A macOS Ventura update triggered `write(): Operation timed out` errors (#7448), and dune segfaults during bootstrap on ppc64 Darwin (#12063).

The remaining bugs affect BSD variants, NFS, and other architectures. OpenBSD has recurring problems with tar flag construction (#13823) that can leave tool installations in a broken state (#12818). FreeBSD exhibits both a race condition in CI (#12964) and a "Bad file descriptor" build error (#9326). NFS setups suffer from two distinct issues: `dune clean` fails because dune creates internal files and then cannot remove the `_build` directory (#7917), and a regression introduced between dune 3.7.0 and 3.11.1 causes `rmdir` failures (#9071). Less common platforms are also affected: Haiku cannot use package management due to hardlink restrictions (#12122), WSL2 watch mode crashes with EOPNOTSUPP (#5638), and dune crashes on arm32 with an integer overflow in `Bytes.create` (#4194). The issues range from #2991 (filed in the dune 1.x era) to #13993, indicating that Windows and platform-specific bugs have accumulated over many years and that the oldest remain unresolved.


### Severity Breakdown

| Severity | Count |
|----------|-------|
| **S1** — Silent Correctness Failures | 1 |
| **S2** — Crashes & Data Loss | 10 |
| **S4** — Platform/Environment Blockers | 34 |
| **S5** — Regressions | 6 |

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| **D1** — Straightforward Fix | 5 |
| **D2** — Moderate Investigation | 9 |
| **D3** — Subsystem Rework | 36 |
| **D4** — Cross-Cutting Architectural | 1 |

## Issues (51 bugs)

- **#13993** `S4` `D3` - unicode in sandbox prevents sandbox cleanup on Windows — Sandbox cleanup fails on Windows when directories contain unicode characters
- **#13909** `S1` `D3` - sandbox cleanup fails on Windows when junctions are present — NTFS junctions cause sandbox cleanup failures with "Directory not empty" errors on Windows
- **#13823** `S4` `D3` - pkg: OpenBSD tar still lacks -z in 3.22.0_alpha2 — tar extraction fails on OpenBSD because dune constructs incorrect tar flags, causing build failures
- **#13658** `S4` `D3` - Known behavioral differences in Windows: `--release` flag needed? — On Windows, `dune build @install` does not compile dune-site plugins unless `--release` flag is used, unlike Linux/macOS
- **#13650** `S4` `D3` - ctypes stubs fail to build on 32-bit platforms — ctypes builds fail on 32-bit platforms with incorrect `.cmxa` path (should use `.cma`)
- **#12964** `S4` `D3` - Possible race condition observed on FreeBSD CI — Intermittent linker failure (library not found) indicates a race condition in dune's build process
- **#12818** `S5` `D3` - If dune tools install fails to install a tool it can break a user's environment — Failed tool installation (due to tar incompatibility on OpenBSD) leaves the environment in a broken state where `dune build` no longer works
- **#12535** `S2` `D2` - Crash when compiling diffast-cli.0.3.5.1 on Windows — Dune crashes with internal error on Windows (MinGW/Cygwin) during compilation
- **#12431** `S4` `D3` - Can't build ocamlbuild on Windows: `Error: opendir(): No such file or directory` — Build failure on Windows due to symlinks in ocamlbuild source; also `dune clean` fails afterwards
- **#12429** `S4` `D3` - Error fetching compiler package on Windows relating to directory targets — Dune fails to recognize directory targets it created on Windows, claiming the action didn't produce them
- **#12122** `S4` `D3` - Hardlinks on Haiku not allowed — Package management fails on Haiku because hardlinks for cookies fail and there is no way to change sandbox mode
- **#12063** `S2` `D3` - Dune segfaults during bootstrap on ppc64 — Generated dune.exe is corrupt and segfaults on ppc64 Darwin during bootstrap
- **#11590** `S4` `D3` - Support MSVC command-line flags syntax with pkg-config in dune-configurator — pkg-config returns Unix-style flags to MSVC compiler, causing build failures on Windows
- **#11574** `S4` `D4` - Cannot install dune using opam on Windows due to non-exist directory/file — Bug: dune compilation fails on Windows due to missing directory/file during bootstrap.
- **#11303** `S4` `D3` - Too easy to reach MAX_PATH on windows — Bug: dune generates paths that are too long on Windows, hitting the MAX_PATH limit.
- **#10940** `S4` `D3` - Compilation of Dune 3.16.0 Fails on macOS M2 (ARM64) During `opam install` — Bug: dune 3.16.0 fails to compile on macOS ARM64.
- **#10874** `S5` `D3` - macos: ld: warning: ignoring duplicate libraries: '-lunixbyt' — Bug: regression since #10763; duplicate library warnings appear on macOS.
- **#10872** `S2` `D2` - CRAM tests on windows — Bug: CRAM tests crash with internal error on Windows when `sh` is not found, instead of giving a clear error message.
- **#10805** `S4` `D3` - [dune-configurator] PKG_CONFIG_PATH is ignored on macos — Bug: `PKG_CONFIG_PATH` environment variable is ignored on macOS in favor of brew paths.
- **#10799** `S4` `D3` - Dune 3.16 doesn't compile in OCaml 4.08/4.09 on Windows — Bug: dune 3.16 uses `Unix.ftruncate` which is unavailable on Windows before OCaml 4.10.
- **#10764** `S2` `D2` - Dune crash with melange-webapi on Windows — Bug: dune crashes with internal error `Path.drop_prefix_exn` on Windows with melange-webapi.
- **#10177** `S4` `D2` - Tests fail on Windows: dune: PATH argument: no ... directory — Merlin-related tests fail on Windows due to Unix-style vs Windows-style path mismatch
- **#10176** `S2` `D3` - Tests fail on Windows with: Cannot decode build prefix map — Dune crashes on Windows with an internal error because colons in Windows paths are not escaped in the build prefix map
- **#10042** `S4` `D3` - Add MSVC libNAME.lib and dllNAME.dll to stub libraries — On Windows with MSVC, incorrect `-lxdg_stubs` flag is used instead of the proper MSVC format, and -L path is missing, causing link failures
- **#9482** `S4` `D1` - opam files from template generated with carriage return on windows — Opam file generation adds carriage returns on Windows, causing unnecessary diffs and promotions
- **#9396** `S4` `D1` - dune-project parser does not work if dune-project has a UTF-8 byte-order mark — Parser fails with garbled output when a UTF-8 BOM is present, which is valid UTF-8; this is incorrect behavior on Windows where PowerShell writes BOM by default.
- **#9326** `S2` `D3` - freebsd: Error trying to read targets after a rule was run — Build error ("Bad file descriptor") when building on FreeBSD; a crash/failure in the build system.
- **#9128** `S4` `D2` - windows: run cannot find *.cmd — `(run)` fails to find programs with `.cmd` extension on Windows because it only tries `.exe`; programs that should be found are not.
- **#9071** `S5` `D3` - Error "rmdir(...): Directory not empty" on an NFS setup — Regression from dune 3.7.0 to 3.11.1; NFS cache setup that used to work now fails with errors.
- **#8811** `S2` `D3` - dune crashes when passing `-w` after `dune clean` on aarch64-unknown-linux-gnu — Crash with internal error ("Fs_memo.Event.create called on a build path") on a specific platform.
- **#8651** `S2` `D3` - Internal error on tests on windows, hooks failed — Crash/internal error on Windows with "hooks failed" and ENOTEMPTY rmdir errors causing CI timeouts.
- **#8643** `S4` `D3` - Enabling (use_standard_c_and_cxx_flags) fails when paired with C++ stubs on Windows — Build failure on Windows because flexlink doesn't understand `-shared-libgcc` flag passed by dune.
- **#8358** `S4` `D1` - Cram tests on Windows, line termination and Git warning — Cram tests produce incorrect diffs on Windows due to line terminator handling issues; test output contains the entire file as a diff.
- **#8231** `S4` `D3` - Displaying full filenames in dune-site before load — Debugging/diagnostic issue where dune-site fails to load on Cygwin with an opaque "Permission denied" error, providing insufficient information to diagnose the problem.
- **#7917** `S4` `D3` - dune clean fails because of .filesystem-clock and .digest-db (NFS) — `dune clean` fails on NFS because dune creates files in `_build` and then complains the directory is not empty.
- **#7448** `S5` `D3` - Potential bug: dune commands no longer work after updating macOS to Ventura — `dune build` produces `Error: write(): Operation timed out` after macOS Ventura update
- **#6730** `S4` `D3` - Terminal UI is broken on Windows — `--display tui` mode is completely broken on Windows
- **#5659** `S4` `D2` - dune-configurator: `C_define.import` fails on windows when includes are present — Bug: C_define.import fails on Windows when custom header includes are used
- **#5638** `S2` `D3` - Unix.EOPNOTSUPP when trying `dune build --watch` on windows using WSL2 — Bug: uncaught exception (EOPNOTSUPP) when using watch mode on WSL2
- **#5485** `S4` `D2` - Dune 3 cannot delete files named `NUL` on Windows — Bug: dune creates `NUL` files on Windows that it then cannot delete, blocking builds
- **#5467** `S5` `D1` - Dune 3 all generated or promoted files on Windows are set executable — Bug: regression from dune 2.9 where all promoted/generated files on Windows/Cygwin get their executable bit set
- **#5378** `S4` `D2` - wrong call to --ppx flags (slash issue) — Bug: ppx flags have incorrect path separators on Windows, preventing compilation
- **#4547** `S4` `D3` - Too much string escaping in overlapped dependencies error path on Windows — Error messages on Windows show excessively escaped backslashes, making paths unreadable
- **#4482** `S4` `D3` - Random "Permission denied" errors on macOS ARM64 — Random compilation failures specific to macOS ARM64, working fine on other platforms
- **#4194** `S2` `D3` - Crash in Stdune__io.Make.eagerly_input_string — Dune crashes with Invalid_argument("Bytes.create") exception on arm32 when running tests
- **#4130** `S4` `D3` - pkg-config not resolved on windows with dune configurator — C.Pkg_config.get always returns None on Windows even when pkg-config works correctly
- **#4018** `S5` `D3` - Cannot add absolute paths to CRAM sanitizer on Windows — Path sanitization is broken on Windows because colons in absolute paths conflict with the separator format
- **#4017** `S4` `D3` - Sanitized paths for CRAM tests in Windows mix `/` and `\` — Path sanitization fails on Windows due to inconsistent forward/back slash mixing
- **#3322** `S4` `D1` - dune exec needs to add .exe on Windows — `dune exec -- foo` on Windows doesn't consider `foo.exe`, leading to stale execution or errors
- **#3040** `S4` `D3` - Dune does not correctly handle c_compiler using a shim — Dune incorrectly splits a C compiler shim command (e.g., `xcrun -sdk macosx10.14 clang`) and passes parts as separate `-ccopt` arguments
- **#2991** `S4` `D2` - Error "The command line is too long" for very short command line (<250 characters) on Cygwin/Windows — Build fails with "command line too long" error even for very short command lines on Windows/Cygwin
