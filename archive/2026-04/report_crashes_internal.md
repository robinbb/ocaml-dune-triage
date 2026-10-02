# Crashes & Internal Errors

## Summary

This category contains 36 open bugs spanning from issue #1819 to #13903, representing years of accumulated crash-related reports. The most prevalent pattern is unhandled internal errors that surface as cryptic messages rather than actionable diagnostics. Specific recurring failure modes include dependency cycle detection errors (#13832, #13500, #5447, #3591), where dune reports spurious cycles that do not actually exist or crashes outright when encountering certain module or stanza configurations involving `virtual_modules`, `enabled_if` with `%{read:...}`, or multi-project workspaces. Another significant cluster involves `link_many: unable to find module` crashes (#12018, #10285), which appear in distinct contexts (ctypes stanzas, certain module layouts) and suggest a fragile module resolution path.

The package management subsystem (`dune pkg`) accounts for a disproportionate share of newer issues. These include a crash when `dune-project` contains `%%VERSION_NUM%%` placeholders (#13108), a hang when `curl` is not installed (#12609), unnecessary full rebuilds when the `-j` flag changes (#12103), and unpredictable dependency updates during normal builds (#13011). The `dune install` path also has its own crash (#13903, "Unexpected build progress state") and a collision error when multiple install stanzas target `share_root` (#13307). Several bugs affect developer tooling workflows: `dune utop` crashes from duplicate `.cma` files (#12551) or from packages in `~/.ocamlinit` (#5312), and `dune format-dune-file` broke compatibility with `opam-dune-lint` (#12897).

A number of long-standing issues remain concerning. Issue #10954 reports a segfault during `opam install dune`, which is a severe first-impression failure. Issue #1819 describes dune unconditionally setting `-no-alias-deps`, which causes runtime crashes in libraries that depend on module initialization side effects (e.g., lablgtk3). Other notable older bugs include uncaught `EACCES` exceptions when `XDG_RUNTIME_DIR` is inaccessible (#5468), a stacktrace when promoting a binary that is in use on Linux (#3484), and corruption of ANSI escape codes in test output (#3160). Taken together, these bugs paint a picture of a system where error handling at boundaries -- file system edge cases, network availability, stanza interactions, and unusual configurations -- needs systematic hardening.


### Severity Breakdown

| Severity | Count |
|----------|-------|
| **S1** — Silent Correctness Failures | 2 |
| **S2** — Crashes & Data Loss | 23 |
| **S3** — Broken Documented Behavior | 3 |
| **S5** — Regressions | 3 |
| **S6** — Misleading Errors & Poor UX | 1 |
| **S7** — Workaroundable Bugs | 4 |

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| **D1** — Straightforward Fix | 1 |
| **D2** — Moderate Investigation | 11 |
| **D3** — Subsystem Rework | 20 |
| **D4** — Cross-Cutting Architectural | 2 |
| **D5** — Design Problem | 2 |

## Issues (36 bugs)

- **#13903** `S2` `D3` - Internal error during `dune install` with pkg-enabled dune-workspace — `dune install` crashes with internal error "Unexpected build progress state" when using pkg-enabled dune-workspace
- **#13832** `S3` `D2` - Dependency cycle with dynamic `enabled_if` on `library` stanza and `package` directive — Build fails with dependency cycle error when using `%{read:...}` in `enabled_if` with a `package` directive present, but works without the directive
- **#13500** `S2` `D3` - Dune 3.21.0 crashes and hangs with "Dependency cycle between ..." — Dune crashes with a spurious dependency cycle error in a multi-project workspace
- **#13307** `S2` `D3` - Crash when multiple install stanzas are targeting share_root for their directory — Dune crashes with internal error "Map.add_exn: key already exists" when multiple install stanzas target share_root
- **#13230** `S2` `D3` - Invalid Variable_name.t error raised — Dune crashes with internal error "Invalid Variable_name.t" due to a typo in dune-project (space in `: with-dev-setup`)
- **#13108** `S2` `D3` - pkg lock fails on repos that need dune subst — `dune pkg lock` crashes with internal error when dune-project contains `%%VERSION_NUM%%` placeholder
- **#13011** `S3` `D5` - pkg: the current dependency update model is unpredictable and impractical — Dependencies update unexpectedly during normal `dune build`/`dune test`, causing builds to break when network is unavailable or upstream APIs change
- **#12897** `S5` `D2` - breakage with `dune format-dune-file` and `opam-dune-lint` — Breaking change requiring `(lang ...)` field breaks existing tools that relied on prior behavior
- **#12866** `S2` `D3` - Adding constraint to `ocamlformat` developer tool fails — Internal crash ("as_outside_build_dir_exn") when adding constraints to dev tool lock directories
- **#12854** `S3` `D3` - `--display=quiet` has no effect on `--root`-changing messages — The `--display=quiet` flag fails to suppress "Entering/Leaving directory" messages, contrary to expected behavior
- **#12700** `S7` `D2` - under-specified dependencies for build env — Package build rules don't account for environment changes, causing incorrect builds
- **#12609** `S2` `D3` - dune build hangs if curl not installed — Build hangs indefinitely after reporting curl is missing instead of exiting with an error
- **#12551** `S2` `D3` - pkg: `dune utop src/...` fails because of duplicate .cmas: tools and pkgs — `dune utop` crashes with "Duplicated implementations" errors due to conflicting .cma files between dev tools and packages
- **#12103** `S7` `D2` - [pkg] Passing `-j` to `dune build` causes the compiler package to be rebuilt — Changing the `-j` parallelism flag causes all dependencies including the compiler to be unnecessarily rebuilt
- **#12075** `S2` `D3` - Building dune crashes with Unexpected_find_result for pp library — `make release` crashes with internal error "Unexpected find result" for the `pp` library
- **#12018** `S2` `D3` - crash when using ctypes stanza — Internal error "link_many: unable to find module" crash when using ctypes stanza with `--profile release`
- **#11923** `S1` `D2` - Dune builds C stubs with `bytecode_cflags` and never `native_cflags` — Wrong compiler flags used for native C stubs; can cause crashes with ThreadSanitizer
- **#11377** `S7` `D3` - dune build @doc doesn't update generated documentation properly — Bug: incremental documentation rebuild is broken; unchanged modules sometimes disappear from index.
- **#11134** `S6` `D2` - Dune shows "Source files changed, restarting current build" for more than 30s — Bug: dune restarts build unnecessarily for 30+ seconds after file changes, causing confusing UX.
- **#10954** `S2` `D3` - 'opam install dune' segfaults — Bug: installing dune via opam causes a segfault.
- **#10285** `S2` `D3` - Internal error: link_many: unable to find module — Dune crashes with an internal error when building a project with certain module configurations
- **#10234** `S1` `D2` - Changes made to the build/install commands of a pinned non-dune package are not picked up until `dune pkg lock` is run — Changes to pinned package build commands are silently ignored until re-locking, leading to stale builds
- **#10038** `S5` `D2` - Undocumented change related to install dir and workspaces — Regression: building packages with different workspaces now deletes previously built install artifacts, changed behavior from dune 3.10
- **#9024** `S2` `D2` - Dune crashes when menhir_flags is in dune-workspace — Unhandled exception/crash when a valid-looking configuration is used; dune should not crash.
- **#8968** `S2` `D3` - Restarting OCaml LSP caused Internal error: attempting to write to a closed channel — Internal error/crash when restarting LSP, dune should handle channel closure gracefully.
- **#8417** `S7` `D2` - Dune sometimes changes *.opam files in release mode — In release mode (`-p`), dune should not modify opam files but it does; this is incorrect behavior.
- **#8281** `S2` `D3` - Exception when secondary .opam with bad name exists while running build doc — Internal error/crash when building documentation with a secondary .opam file that has a bad name.
- **#7962** `S2` `D3` - Crash when depending on source_tree outside workspace — Crash with internal error instead of a proper error message when `source_tree` references a path outside the workspace.
- **#5733** `S5` `D1` - dune 3.2.0 changes mandir from /usr/share/man to /usr/man — Bug: regression where the default mandir changed from `/usr/share/man` to `/usr/man`
- **#5468** `S2` `D2` - Internal error: EACCES exception uncaught, opinions on how to catch it? — Bug: uncaught EACCES exception when XDG_RUNTIME_DIR points to a non-existent/inaccessible directory
- **#5447** `S2` `D4` - dependency cycle that does not involve any files — Bug: internal error / crash with "dependency cycle that does not involve any files" message
- **#5312** `S2` `D3` - dune utop blows up with an exception when cohttp-lwt-unix is present in ~/.ocamlinit — Bug: dune utop crashes with an exception when certain packages are required in ~/.ocamlinit
- **#3591** `S2` `D4` - Internal error: dependency cycle with virtual_modules — Building a project with virtual_modules causes an internal error (dependency cycle crash) instead of proper behavior
- **#3484** `S2` `D3` - stacktrace when trying to promote into a binary in use (linux) — Dune crashes with a stacktrace when trying to promote a binary that is currently running, instead of handling the "Text file busy" error gracefully
- **#3160** `S2` `D3` - Dune runtest incorrectly changes escape codes related to cursor movement — Dune's output processing corrupts ANSI escape codes that involve cursor movement, breaking formatted test output (e.g., Rely)
- **#1819** `S2` `D5` - Dune always sets -no-alias-deps for all files — Bug/misfeature: dune unconditionally sets `-no-alias-deps` which was never intended to be the default, causing runtime crashes for libraries like lablgtk3 that depend on module initialization side effects
