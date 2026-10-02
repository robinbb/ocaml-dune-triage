# Watch Mode & RPC

## Summary

The 17 open bugs in this category reveal a system where watch mode and the RPC interface are both individually fragile and deeply problematic in combination. The most severe class of issues involves hangs and deadlocks: the RPC server stops answering requests non-deterministically in eager watch mode (#12715), dune hangs indefinitely in mdx tests waiting for an RPC socket (#12900), and RPC ping hangs forever when dune is running in watch mode within its own repository (#7568). A closely related pattern is unwanted blocking, where short-running RPC operations like `dune format-dune-file` are forced to wait for long-running watch-mode builds to complete (#13788, #13525), breaking editor integrations that rely on fast format-on-save.

A second major theme is silent data loss and incorrect output. RPC builds swallow non-fatal warnings entirely, reporting "Success" when warnings should be surfaced (#12752). Promotions are completely ignored during eager watch mode (#12725). Diagnostic line numbers sent over the RPC protocol are off by one compared to compiler output, and the offset is inconsistent (#11631). These bugs mean that even when the system does not hang, users cannot trust the information it provides.

The remaining bugs span outright crashes (editing a file during `exec --watch` crashes dune, #11010; uncaught `EINVAL` exception during RPC forwarding, #12660), broken subcommands (`dune utop --watch` never rebuilds, #6817; `--passive-watch-mode` silently ignores its arguments, #7761), and performance regressions (watch-mode rebuilds are slower than fresh builds due to unnecessary job number restriction, #5549). The issues range from #2565 (opened in 2019) to #13788, indicating that some of these problems have persisted for years without resolution. The oldest bug, #2565, bundles multiple issues including `--watch` being advertised but ignored by `dune install`. The concentration of hangs and non-deterministic failures suggests fundamental architectural challenges in coordinating the watch-mode file watcher, the build engine's lock management, and the RPC server's concurrency model.


### Severity Breakdown

| Severity | Count |
|----------|-------|
| **S1** — Silent Correctness Failures | 1 |
| **S2** — Crashes & Data Loss | 4 |
| **S3** — Broken Documented Behavior | 4 |
| **S5** — Regressions | 1 |
| **S6** — Misleading Errors & Poor UX | 1 |
| **S7** — Workaroundable Bugs | 6 |

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| **D1** — Straightforward Fix | 1 |
| **D3** — Subsystem Rework | 2 |
| **D4** — Cross-Cutting Architectural | 14 |

## Issues (17 bugs)

- **#13788** `S7` `D4` - with RPC/watch: short job waits for long job to return — When using `dune build --watch` with RPC, a short formatting command blocks until the watch process finishes its current work
- **#13525** `S5` `D4` - Formatting dune files on save while the build is running — `dune format-dune-file` conflicts with build locks when a watch-mode build is running, breaking editor format-on-save workflows
- **#13080** `S3` `D4` - dune build --watch + dune exec + DUNE_BUILD_DIR does not work — `dune exec` fails with "Don't know how to build" when DUNE_BUILD_DIR is set and watch mode is active
- **#12900** `S2` `D4` - dune hangs in mdx tests waiting for _build/default/_build/.rpc/dune — Dune hangs indefinitely when background process is used in mdx tests; regression in behavior
- **#12752** `S7` `D4` - RPC builds don't transfer warnings to the client — Non-fatal warnings are silently swallowed; RPC client reports "Success" without showing build warnings
- **#12725** `S7` `D4` - [RPC] Eager watch mode doesn't register promotions at all — Promotions via `dune promote` are completely ignored during eager watch mode
- **#12715** `S1` `D4` - RPC system hanging non-deterministically on eager watch mode — Server stops answering requests and clients hang forever in eager watch mode
- **#12660** `S2` `D4` - dune forwarding rpc occasionally gets EINVAL backtrace — Uncaught exception (Unix.EINVAL from setsockopt) during RPC forwarding causes crash
- **#11631** `S7` `D1` - dune watch rpc is sending off by minus one lines inconsistently — Diagnostic line numbers are off by one compared to compiler output, and the offset is inconsistent
- **#11010** `S2` `D4` - Dune crashes when editing a file in exec watch mode — Bug: dune crashes when editing a file during `exec --watch` mode.
- **#7761** `S3` `D3` - `dune build --passive-watch-mode` ignores its argument — Command silently ignores arguments instead of erroring; incorrect behavior.
- **#7624** `S6` `D4` - In `dune_rpc_lwt` closing the output channel should also close the input channel — Closing the output channel raises `Unix.Unix_error(Unix.EBADF)` instead of returning `None` on the input channel
- **#7568** `S2` `D4` - Dune doesn't respond to RPC methods when run in watch mode in the dune repository — RPC ping command hangs forever when dune is running in watch mode within its own repository
- **#7223** `S3` `D4` - "I/O error" with `.pp.ml` file when running `dune build . -w` — Watch mode intermittently fails with I/O error on `.pp.ml` files that resolves on restart
- **#6817** `S7` `D4` - `dune utop --watch` Appears to be broken — `dune utop --watch` does not rebuild/reload when source files change
- **#5549** `S7` `D4` - dune build -w restricting job number for no reason — Bug: watch mode rebuilds are observably slower than fresh builds due to unnecessary job number restriction during rule finding
- **#2565** `S3` `D3` - Minor improvements for Build_info and install — Multiple bugs: documentation example code doesn't compile (wrong API usage), `--display=quiet` is not respected by install messages, `dune install --help` claims `--watch` support but ignores it, and setting `--prefix=_build/install/...` silently produces empty executables
