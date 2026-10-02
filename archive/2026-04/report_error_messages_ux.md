# Error Messages & UX

## Summary

This category contains 44 bugs spanning from issue #2353 to #13891, representing some of the oldest unresolved issues in the Dune tracker. The problems cluster around several recurring themes: misleading or confusing error messages that point users in the wrong direction, silent failures where Dune accepts invalid input or ignores configuration without any warning, and inconsistencies between documented behavior and actual behavior. These issues collectively degrade the developer experience and make Dune harder to debug and reason about.

A prominent theme is error messages that actively mislead. For example, #12544 reports that the "optional with unavailable dependencies" message fails to identify the actual missing transitive dependency. Issue #12439 shows users the cryptic "You cannot use %{target} with inferred rules" when the real problem is a missing `(target ...)` field. Issue #6598 reports a "Module ... is used in several stanzas" error that names a module not present in the listed stanza. Issue #6074 tells users that "pure bytecode executables cannot contain foreign stubs" when the operation is in fact possible by wrapping stubs in a library. Issue #11932 produces a baffling error when a `(lang dune X)` version is unsupported, and #12317 triggers an error with no location information at all upon upgrading to lang dune 3.20, making it impossible to diagnose. Several issues (#10393, #12975, #10029) show cases where error messages fail to suggest actionable next steps, such as explaining why git is needed or why a target is missing because a library is disabled.

Equally damaging are the silent failures. Issue #9757 is particularly severe: inline tests with `(modes byte)` are compiled but never executed, with no warning. Issue #13492 silently ignores install stanzas in `dynamic_include` files. Issue #13225 silently drops `:standard` flags inside `:include`d files. Issue #10111 silently resolves an ambiguous git hash reference to the wrong branch. Issue #3638 silently ignores `env-vars` set in the `(env)` stanza when running `dune exec`. Issue #8970 silently accepts and misinterprets trailing slashes in build targets. Issue #6099 silently accepts empty packages not defined in `dune-project`. And issue #3549 silently accepts invalid module names in `modules_before_stdlib`. These silent failures are arguably worse than bad error messages because users have no indication that anything is wrong until they encounter downstream symptoms. Additional UX problems include garbled test output from escape code corruption (#3463), excessive memory usage building certain targets (#11593), noisy cache miss spam (#10731), and inconsistencies between `@all` and `@check` aliases (#3182, #11518). Several variable-expansion issues (#7571, #4895, #3755, #3779) also contribute to a frustrating experience where the templating system does not behave as documented.


### Severity Breakdown

| Severity | Count |
|----------|-------|
| **S1** — Silent Correctness Failures | 2 |
| **S2** — Crashes & Data Loss | 2 |
| **S3** — Broken Documented Behavior | 18 |
| **S5** — Regressions | 4 |
| **S6** — Misleading Errors & Poor UX | 6 |
| **S7** — Workaroundable Bugs | 12 |

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| **D1** — Straightforward Fix | 4 |
| **D2** — Moderate Investigation | 35 |
| **D3** — Subsystem Rework | 3 |
| **D4** — Cross-Cutting Architectural | 2 |

## Issues (44 bugs)

- **#13891** `S5` `D2` - Revert the behavior of --diff-command wrt to non-existent files — Documented behavior of diff with non-existent files (comparing against empty file) no longer works as documented
- **#13492** `S1` `D4` - install stanza in dynamic_include is ignored — Install stanza inside a `dynamic_include` file is silently ignored, contrary to what documentation implies should work
- **#13225** `S3` `D2` - `:standard` in an `:include`d file is ignored — Using `:standard` inside an `:include`d file silently ignores environment flags instead of working or raising an error
- **#12975** `S3` `D2` - running `dune tools exec <p>` when `p` is not already installed as a dev tool should suggest users run `dune tools install <p>` — Unhelpful/confusing error messages when running `dune tools exec` for a tool that is not installed
- **#12544** `S5` `D2` - The error message "optional with unavailable dependencies" is hard to digest — Error message is misleading and does not point to the actual missing transitive dependency
- **#12439** `S3` `D2` - Confusing message with erroneous rules — Error message "You cannot use %{target} with inferred rules" is confusing when the actual issue is a missing `(target ...)` field
- **#12322** `S3` `D2` - Don't include .output files with "default" targets — `dune build` unnecessarily executes test binaries (building `.output` files) causing confusing error reports for failing tests
- **#12317** `S6` `D2` - User-defined rules cannot be added to the 'empty' alias — Upgrading lang dune to 3.20 triggers an error with no location information, making it impossible to diagnose
- **#12104** `S3` `D2` - Cram tests don't pick up env variables — Inline environment variable assignments (e.g., `VAR=val command`) are not picked up by commands in cram tests
- **#11932** `S3` `D2` - baffling error message when a "dune lang" version is too new — Error message when `(lang dune X)` version is unsupported is confusing and misleading
- **#11848** `S7` `D2` - Test stanza allows expectation files to be generated — This breaks promotion in the test stanza
- **#11593** `S7` `D2` - dune takes >2GB of RAM building some targets of frama-c.30.0 — Excessive memory usage (>2GB) when building certain targets, suggesting a resource leak or inefficiency
- **#11542** `S6` `D1` - `dune subst` inferred version is totally misleading and wrong — Bug/misfeature: `dune subst` uses `git describe` which produces misleading version strings that confuse users.
- **#11518** `S3` `D2` - [BUG] dune build @check fails mysteriously with overlapping executables — Bug: `dune build @check` fails with confusing errors while `dune build @all` succeeds in the same project.
- **#11506** `S3` `D2` - error message on failing copy action is unclear — Bug: unclear/misleading error message when a copy action fails.
- **#10731** `S3` `D3` - Many noisy shared cache miss messages when using multiple filesystems — Bug: dune spams many cache miss error messages instead of showing a single warning when cache is on a different filesystem.
- **#10393** `S2` `D3` - Improve error message when git is not found — Build aborts with unhelpful "git: command not found" without explaining the cause or suggesting a fix
- **#10158** `S3` `D2` - The `pin` stanza requires a `name` when it appears in `dune-workspace` but not in `dune-project` — Inconsistent behavior between the same stanza in different files, with a confusing error message
- **#10111** `S7` `D2` - Using ambiguous hash references for git repos leads to unexpected results — A branch name formatted like a SHA1 hash silently resolves to the default branch instead of the correct branch, without any warning
- **#10029** `S6` `D2` - Building the cmo of a module of a disabled library gives a bad error — Error message is unhelpful; should indicate that the target is missing because the library is disabled
- **#9775** `S7` `D2` - glob_file_rec is not recursive on generated folder — `glob_files_rec` behaves as non-recursive glob inside generated directories, which is unexpected
- **#9757** `S1` `D2` - `dune runtest` compiles but does not execute `(inline_tests) (modes byte)` — Inline tests are compiled but silently not executed when library has `(modes byte)`, which is a serious bug
- **#8970** `S7` `D1` - dune build accepts trailing slashes — Incorrect argument parsing; `dune build abc/` is silently accepted and misinterpreted even if `abc` is a file.
- **#8352** `S3` `D2` - (allow_empty) rules and messages are confusing — Confusing/incorrect error message for a valid project setup (executable with `(modes js)`); the error message is misleading and the `(allow_empty)` workaround is itself confusing.
- **#8073** `S7` `D2` - Cannot promote empty files over a non-existing file — Empty files cannot be promoted when the target doesn't exist; dune logs that files differ but doesn't create the promoted file.
- **#7571** `S3` `D2` - env not supported in enabled_if Boolean language in library stanza — `%{env:...}` variable not allowed in `enabled_if` despite documentation saying it should be supported; documentation and behavior mismatch
- **#7170** `S7` `D2` - Folders excluded from `dirs` are visited when calling `dune build @my_alias` — Directories excluded via `dirs` stanza are still visited (stat'd) during alias builds
- **#6598** `S6` `D2` - Confusing 'Module ... is used in several stanzas' error — Error message mentions a module name that is not in the listed stanza, making the error confusing and misleading
- **#6568** `S3` `D2` - Preprocessing with actions and future syntax cannot be used in conjunction with (instrumentation ...) — Cannot combine `preprocess` action with `instrumentation` stanza despite no inherent conflict
- **#6099** `S5` `D2` - No error is raised when building an empty package not defined in the dune-project file — Bug: regression where dune stopped raising an error for empty packages, a feature that was lost when tests were removed
- **#6074** `S3` `D2` - "Error: Pure bytecode executables cannot contain foreign stubs." is misleading — Bug: misleading/incorrect error message implies something is impossible when it can be done by wrapping stubs in a library
- **#5789** `S3` `D2` - Got this error message while trying to build Hello_world project — Bug: confusing/undocumented error message about `(allow_empty)` when building a new hello world project; the error message references a stanza not documented
- **#4895** `S7` `D2` - The documentation/value of %{system} is not consistent — The %{system} variable value does not match what the documentation claims it should be
- **#3779** `S3` `D2` - %{lib-private} and multiple packages — `%{lib-private}` does not work when used across packages defined in the same project
- **#3755** `S3` `D2` - %{env:FOO=<val>} does not accept spaces in <val> — Spaces in default values for env variable expansion cause a parse error, which is a limitation/misfeature
- **#3638** `S7` `D2` - env-vars ignored under exec — `env-vars` set in the `(env)` stanza are not applied when running executables with `dune exec`
- **#3569** `S3` `D4` - Expect tests with (implicit_transitive_deps false) — Setting `(implicit_transitive_deps false)` causes `Unbound module Expect_test_common` when using expect tests, even though the dependency should be resolved
- **#3549** `S7` `D2` - dune not checking modules in modules_before_stdlib — Dune doesn't validate/complain about invalid module names in `modules_before_stdlib`
- **#3463** `S2` `D3` - Dune is mangling qtest/ounit output — Dune's output buffering corrupts escape codes related to cursor movement, producing garbled test output
- **#3230** `S7` `D2` - Long form target inference is not properly versioned — Target inference for long-form actions lacks a `since` version check, allowing it in `(lang dune 1.2)` when it should only work in >= 2.0
- **#3182** `S7` `D2` - The @all alias does not produce .cmt files which are produced by @check — `dune build` produces only `.cmti` but not `.cmt`, while `dune build @check` produces both, which is inconsistent
- **#2818** `S6` `D2` - Cycles reported by dune are cryptic — Module cycle errors reported by dune don't correspond to actual user code, likely due to over-approximation of the dependency graph
- **#2370** `S5` `D1` - Hygiene issue in _build with .h files — Bug/regression: since Dune 1.9.0, .h files are copied eagerly into _build even when no C compilation is needed, creating misleading build artifacts
- **#2353** `S6` `D1` - Dune installs empty META file for package with no library — Bug: dune generates and installs a blank META file for executable-only packages, causing confusing output from ocamlfind (version: n/a)
