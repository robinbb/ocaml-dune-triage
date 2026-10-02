# ocaml/dune Bug To-Do List (Core)

Prioritized by easiest high-impact first.
Excludes Windows/platform, Coq/Rocq, and package management issues.
**271 bugs** after filtering.

## Tier 1: Quick Wins (D1)

| # | Issue | S | D | Area | Title |
|---|-------|---|---|------|-------|
| 1 | [#6148](https://github.com/ocaml/dune/issues/6148) | S1 | D1 | Build | `root_module` generates duplicate module definition when `logs.lwt` is a dependency |
| 2 | [#10707](https://github.com/ocaml/dune/issues/10707) | S3 | D1 | Build | Add correct lower bound to menhir |
| 3 | [#3349](https://github.com/ocaml/dune/issues/3349) | S3 | D1 | Build | `(disable_dynamically_linked_foreign_archives true)` should not try to build js targets |
| 4 | [#10141](https://github.com/ocaml/dune/issues/10141) | S5 | D1 | Build | git describe is incorrect for Dune's main branch since 3.12 |
| 5 | [#5733](https://github.com/ocaml/dune/issues/5733) | S5 | D1 | Crashes | dune 3.2.0 changes mandir from /usr/share/man to /usr/man |
| 6 | [#2370](https://github.com/ocaml/dune/issues/2370) | S5 | D1 | Errors/UX | Hygiene issue in _build with .h files |
| 7 | [#11542](https://github.com/ocaml/dune/issues/11542) | S6 | D1 | Errors/UX | `dune subst` inferred version is totally misleading and wrong |
| 8 | [#2353](https://github.com/ocaml/dune/issues/2353) | S6 | D1 | Errors/UX | Dune installs empty META file for package with no library |
| 9 | [#11631](https://github.com/ocaml/dune/issues/11631) | S7 | D1 | Watch/RPC | dune watch rpc is sending off by minus one lines inconsistently |
| 10 | [#11110](https://github.com/ocaml/dune/issues/11110) | S7 | D1 | Build | Custom `libexec` sites install does not set executable bit |
| 11 | [#10360](https://github.com/ocaml/dune/issues/10360) | S7 | D1 | Build | (executables_implicit_empty_intf ...) expects dune >= 2.9 but was only added in 3.0 |
| 12 | [#8970](https://github.com/ocaml/dune/issues/8970) | S7 | D1 | Errors/UX | dune build accepts trailing slashes |

## Tier 2: High-Impact Moderate Fixes (D2, S1-S2)

| # | Issue | S | D | Area | Title |
|---|-------|---|---|------|-------|
| 1 | [#11941](https://github.com/ocaml/dune/issues/11941) | S1 | D2 | Build | Dune overwrites the user provided debug flag in foreign stubs |
| 2 | [#11923](https://github.com/ocaml/dune/issues/11923) | S1 | D2 | Crashes | Dune builds C stubs with `bytecode_cflags` and never `native_cflags` |
| 3 | [#11774](https://github.com/ocaml/dune/issues/11774) | S1 | D2 | Paths | `dune install` with an out-of-workspace build directory produces absolute paths in dune-package files |
| 4 | [#9979](https://github.com/ocaml/dune/issues/9979) | S1 | D2 | Build | Dune links against wrong cstubs in byte mode |
| 5 | [#9757](https://github.com/ocaml/dune/issues/9757) | S1 | D2 | Errors/UX | `dune runtest` compiles but does not execute `(inline_tests) (modes byte)` |
| 6 | [#9650](https://github.com/ocaml/dune/issues/9650) | S1 | D2 | Vendoring | ppx is skipped when `(modes byte)` |
| 7 | [#7460](https://github.com/ocaml/dune/issues/7460) | S1 | D2 | Build | Cache hits "hide" warnings |
| 8 | [#7222](https://github.com/ocaml/dune/issues/7222) | S1 | D2 | Paths | compiler errors have wrong relative path |
| 9 | [#6481](https://github.com/ocaml/dune/issues/6481) | S1 | D2 | Build | ctypes: flags are added twice |
| 10 | [#6128](https://github.com/ocaml/dune/issues/6128) | S1 | D2 | Vendoring | Warnings leak through `vendored_dirs` subpath |
| 11 | [#6012](https://github.com/ocaml/dune/issues/6012) | S1 | D2 | Build | Cram tests can access OCaml libraries not in deps, if they are compiled |
| 12 | [#5992](https://github.com/ocaml/dune/issues/5992) | S1 | D2 | Paths | Usability/Documentation issues with copy_files/glob |
| 13 | [#5313](https://github.com/ocaml/dune/issues/5313) | S1 | D2 | Paths | `(dirs ..` with paths of depth >= 2 are just ignored |
| 14 | [#5238](https://github.com/ocaml/dune/issues/5238) | S1 | D2 | Vendoring | Bad ppx annotations are not reported |
| 15 | [#9024](https://github.com/ocaml/dune/issues/9024) | S2 | D2 | Crashes | Dune crashes when menhir_flags is in dune-workspace |
| 16 | [#5468](https://github.com/ocaml/dune/issues/5468) | S2 | D2 | Crashes | Internal error: EACCES exception uncaught, opinions on how to catch it? |

## Tier 3: Broken Features (D2, S3)

| # | Issue | S | D | Area | Title |
|---|-------|---|---|------|-------|
| 1 | [#13832](https://github.com/ocaml/dune/issues/13832) | S3 | D2 | Crashes | Dependency cycle with dynamic `enabled_if` on `library` stanza and `package` directive |
| 2 | [#13825](https://github.com/ocaml/dune/issues/13825) | S3 | D2 | Build | archives are incorrectly detected by inspecting the extension |
| 3 | [#13782](https://github.com/ocaml/dune/issues/13782) | S3 | D2 | Build | `dune show targets` does not work on build-only directories |
| 4 | [#13638](https://github.com/ocaml/dune/issues/13638) | S3 | D2 | Paths | `diff` action directive isn't working as expected with a non-existent file |
| 5 | [#13418](https://github.com/ocaml/dune/issues/13418) | S3 | D2 | Tooling | `dune runtest --force` does not work for `(mdx)` stanza |
| 6 | [#13225](https://github.com/ocaml/dune/issues/13225) | S3 | D2 | Errors/UX | `:standard` in an `:include`d file is ignored |
| 7 | [#12975](https://github.com/ocaml/dune/issues/12975) | S3 | D2 | Errors/UX | running `dune tools exec <p>` when `p` is not already installed as a dev tool should suggest users run `dune tools install <p>` |
| 8 | [#12439](https://github.com/ocaml/dune/issues/12439) | S3 | D2 | Errors/UX | Confusing message with erroneous rules |
| 9 | [#12322](https://github.com/ocaml/dune/issues/12322) | S3 | D2 | Errors/UX | Don't include .output files with "default" targets |
| 10 | [#12104](https://github.com/ocaml/dune/issues/12104) | S3 | D2 | Errors/UX | Cram tests don't pick up env variables |
| 11 | [#11932](https://github.com/ocaml/dune/issues/11932) | S3 | D2 | Errors/UX | baffling error message when a "dune lang" version is too new |
| 12 | [#11518](https://github.com/ocaml/dune/issues/11518) | S3 | D2 | Errors/UX | [BUG] dune build @check fails mysteriously with overlapping executables |
| 13 | [#11506](https://github.com/ocaml/dune/issues/11506) | S3 | D2 | Errors/UX | error message on failing copy action is unclear |
| 14 | [#11500](https://github.com/ocaml/dune/issues/11500) | S3 | D2 | Tooling | `@ocaml-index` is empty when not built from the root of a project |
| 15 | [#11418](https://github.com/ocaml/dune/issues/11418) | S3 | D2 | Build | dune-build-info is not working on flambda1 switch |
| 16 | [#11042](https://github.com/ocaml/dune/issues/11042) | S3 | D2 | Build | Using (enabled_if %{read:...}) |
| 17 | [#10792](https://github.com/ocaml/dune/issues/10792) | S3 | D2 | Build | Doc for building byte code incorrect |
| 18 | [#10588](https://github.com/ocaml/dune/issues/10588) | S3 | D2 | Build | --ignore-promoted-rules has no effect on copy_files |
| 19 | [#10578](https://github.com/ocaml/dune/issues/10578) | S3 | D2 | Tooling | `dune build @fmt` exits with 1 if `ocamlformat` is not installed |
| 20 | [#10423](https://github.com/ocaml/dune/issues/10423) | S3 | D2 | Vendoring | GCC and GLIBC supported minimums for Dune on Linux |
| 21 | [#10158](https://github.com/ocaml/dune/issues/10158) | S3 | D2 | Errors/UX | The `pin` stanza requires a `name` when it appears in `dune-workspace` but not in `dune-project` |
| 22 | [#9943](https://github.com/ocaml/dune/issues/9943) | S3 | D2 | Tooling | dune fmt should not fail to format when depopt isn't available / `and` isn't lazy |
| 23 | [#9759](https://github.com/ocaml/dune/issues/9759) | S3 | D2 | Paths | data_only_dirs documentation seems to imply that ordered set language applies |
| 24 | [#9724](https://github.com/ocaml/dune/issues/9724) | S3 | D2 | Build | `dune build @check` should pass if `dune build @all` does |
| 25 | [#9662](https://github.com/ocaml/dune/issues/9662) | S3 | D2 | Build | dune-site: use string list instead of Location.t |
| 26 | [#8626](https://github.com/ocaml/dune/issues/8626) | S3 | D2 | Tooling | `#use_output "dune ocaml top"` fails in a project where `dune utop` works |
| 27 | [#8587](https://github.com/ocaml/dune/issues/8587) | S3 | D2 | Vendoring | Add support for `staged_pps` in `dune describe pp` |
| 28 | [#8352](https://github.com/ocaml/dune/issues/8352) | S3 | D2 | Errors/UX | (allow_empty) rules and messages are confusing |
| 29 | [#8075](https://github.com/ocaml/dune/issues/8075) | S3 | D2 | Paths | Fail to promote over a non-existing file |
| 30 | [#7831](https://github.com/ocaml/dune/issues/7831) | S3 | D2 | Paths | Install fails for a directory with symlinks to a directory |
| 31 | [#7811](https://github.com/ocaml/dune/issues/7811) | S3 | D2 | Vendoring | Vendoring of foreign source trees with leading underscores |
| 32 | [#7800](https://github.com/ocaml/dune/issues/7800) | S3 | D2 | Build | `(byte shared_object)` linking mode does not allow linking C stubs |
| 33 | [#7573](https://github.com/ocaml/dune/issues/7573) | S3 | D2 | Vendoring | Build failing due to existence of broken symbolic link (unused in build) |
| 34 | [#7571](https://github.com/ocaml/dune/issues/7571) | S3 | D2 | Errors/UX | env not supported in enabled_if Boolean language in library stanza |
| 35 | [#7135](https://github.com/ocaml/dune/issues/7135) | S3 | D2 | Paths | Hidden folders are ignored in source_tree dep |
| 36 | [#7073](https://github.com/ocaml/dune/issues/7073) | S3 | D2 | Build | ld: Error: unable to disambiguate: -shared-libgcc |
| 37 | [#6830](https://github.com/ocaml/dune/issues/6830) | S3 | D2 | Vendoring | Rule collision when multiple vendored projects contain executables with matching names |
| 38 | [#6680](https://github.com/ocaml/dune/issues/6680) | S3 | D2 | Tooling | OCaml toplevel sometimes fails to load default implementation for a virtual library |
| 39 | [#6568](https://github.com/ocaml/dune/issues/6568) | S3 | D2 | Errors/UX | Preprocessing with actions and future syntax cannot be used in conjunction with (instrumentation ...) |
| 40 | [#6263](https://github.com/ocaml/dune/issues/6263) | S3 | D2 | Build | C archive for byte target not built to include dynamic dependencies |
| 41 | [#6133](https://github.com/ocaml/dune/issues/6133) | S3 | D2 | Paths | The new dir install feature does not work on existing directories |
| 42 | [#6074](https://github.com/ocaml/dune/issues/6074) | S3 | D2 | Errors/UX | "Error: Pure bytecode executables cannot contain foreign stubs." is misleading |
| 43 | [#6073](https://github.com/ocaml/dune/issues/6073) | S3 | D2 | Paths | test stanza does not work with bytecode compiled with foreign_stubs |
| 44 | [#5946](https://github.com/ocaml/dune/issues/5946) | S3 | D2 | Tooling | `dune fmt` ignores `--disable-promotion` flag |
| 45 | [#5833](https://github.com/ocaml/dune/issues/5833) | S3 | D2 | Paths | [dune engine] [bug] Error file unavailable when an absolute path points to a symlink |
| 46 | [#5789](https://github.com/ocaml/dune/issues/5789) | S3 | D2 | Errors/UX | Got this error message while trying to build Hello_world project |
| 47 | [#5647](https://github.com/ocaml/dune/issues/5647) | S3 | D2 | Paths | Moving a file as a previously existing directory |
| 48 | [#5460](https://github.com/ocaml/dune/issues/5460) | S3 | D2 | Build | Project initialized with `init exec` does not build (cannot find root) |
| 49 | [#5229](https://github.com/ocaml/dune/issues/5229) | S3 | D2 | Tooling | @doc "Couldn't find the following modules: Stdlib" |
| 50 | [#5081](https://github.com/ocaml/dune/issues/5081) | S3 | D2 | Build | Use of (modes c) does not work |
| 51 | [#4971](https://github.com/ocaml/dune/issues/4971) | S3 | D2 | Tooling | MDX stanza not causing dependencies to be built |
| 52 | [#4892](https://github.com/ocaml/dune/issues/4892) | S3 | D2 | Tooling | Private modules cause missing build path (in the ocaml-merlin dump) |
| 53 | [#4531](https://github.com/ocaml/dune/issues/4531) | S3 | D2 | Build | Issues with --action-stdxxx-on-success |
| 54 | [#4123](https://github.com/ocaml/dune/issues/4123) | S3 | D2 | Build | -opaque option breaks equivalence between release and dev compilation in presence of [@inline always] |
| 55 | [#4039](https://github.com/ocaml/dune/issues/4039) | S3 | D2 | Build | flambda with -nostdlib and transitive stdlib not finding cmx |
| 56 | [#3908](https://github.com/ocaml/dune/issues/3908) | S3 | D2 | Build | does dune enforce complete cmxs files? |
| 57 | [#3805](https://github.com/ocaml/dune/issues/3805) | S3 | D2 | Paths | No such file or directory when DUNE_BUILD_DIR is set during test |
| 58 | [#3779](https://github.com/ocaml/dune/issues/3779) | S3 | D2 | Errors/UX | %{lib-private} and multiple packages |
| 59 | [#3755](https://github.com/ocaml/dune/issues/3755) | S3 | D2 | Errors/UX | %{env:FOO=<val>} does not accept spaces in <val> |
| 60 | [#3645](https://github.com/ocaml/dune/issues/3645) | S3 | D2 | Vendoring | "The module X is an alias for module Y.X, which is missing" when X comes from a virtual library |
| 61 | [#3467](https://github.com/ocaml/dune/issues/3467) | S3 | D2 | Build | modes not respected in combination with library with public_name |
| 62 | [#3382](https://github.com/ocaml/dune/issues/3382) | S3 | D2 | Vendoring | "Unknown constructor vendored_dirs" when using OCaml syntax |
| 63 | [#3362](https://github.com/ocaml/dune/issues/3362) | S3 | D2 | Build | Cannot use `%{lib:...}` in the `flags` stanza |
| 64 | [#3214](https://github.com/ocaml/dune/issues/3214) | S3 | D2 | Vendoring | Fl_dynload.load_packages in a PPX |
| 65 | [#3173](https://github.com/ocaml/dune/issues/3173) | S3 | D2 | Paths | can't promote into a directory start with underscore |
| 66 | [#3025](https://github.com/ocaml/dune/issues/3025) | S3 | D2 | Paths | dune install: ocamlfind point to the wrong directory in a local switch |
| 67 | [#2938](https://github.com/ocaml/dune/issues/2938) | S3 | D2 | Paths | (dirs ...) not recognised in dune2 |
| 68 | [#2144](https://github.com/ocaml/dune/issues/2144) | S3 | D2 | Paths | Error in documentation for dirs stanza |
| 69 | [#2003](https://github.com/ocaml/dune/issues/2003) | S3 | D2 | Build | Ability to use sub-extensions for virtual modules |
| 70 | [#1645](https://github.com/ocaml/dune/issues/1645) | S3 | D2 | Tooling | Odoc: valid module name clashes cause issues |
| 71 | [#1415](https://github.com/ocaml/dune/issues/1415) | S3 | D2 | Build | Implementations of virtual libraries aren't installed correctly |
| 72 | [#1187](https://github.com/ocaml/dune/issues/1187) | S3 | D2 | Tooling | $ dune utop doesn't work for dune itself |
| 73 | [#108](https://github.com/ocaml/dune/issues/108) | S3 | D2 | Build | bytecode + c stubs not working as expected |

## Tier 4: Regressions & UX (D2, S5-S6)

| # | Issue | S | D | Area | Title |
|---|-------|---|---|------|-------|
| 1 | [#14085](https://github.com/ocaml/dune/issues/14085) | S5 | D2 | Build | 3.22.0 regression: error about non-existent excluded module from `(select)` in a different stanza |
| 2 | [#13891](https://github.com/ocaml/dune/issues/13891) | S5 | D2 | Errors/UX | Revert the behavior of --diff-command wrt to non-existent files |
| 3 | [#12897](https://github.com/ocaml/dune/issues/12897) | S5 | D2 | Crashes | breakage with `dune format-dune-file` and `opam-dune-lint` |
| 4 | [#12544](https://github.com/ocaml/dune/issues/12544) | S5 | D2 | Errors/UX | The error message "optional with unavailable dependencies" is hard to digest |
| 5 | [#10732](https://github.com/ocaml/dune/issues/10732) | S5 | D2 | Build | menhir option `--only-tokens` does not work |
| 6 | [#10038](https://github.com/ocaml/dune/issues/10038) | S5 | D2 | Crashes | Undocumented change related to install dir and workspaces |
| 7 | [#9873](https://github.com/ocaml/dune/issues/9873) | S5 | D2 | Paths | Error with directory symlink: Unexpected file kind "S_DIR" |
| 8 | [#8727](https://github.com/ocaml/dune/issues/8727) | S5 | D2 | Build | The issues of `--ignore-promote-rules` |
| 9 | [#8709](https://github.com/ocaml/dune/issues/8709) | S5 | D2 | Build | Generate cmi files that match the input |
| 10 | [#8242](https://github.com/ocaml/dune/issues/8242) | S5 | D2 | Build | Very slow emacs compilation buffer updates |
| 11 | [#7664](https://github.com/ocaml/dune/issues/7664) | S5 | D2 | Build | program output from `exec -w` and rule actions interspersed with repeated dune status output |
| 12 | [#6106](https://github.com/ocaml/dune/issues/6106) | S5 | D2 | Vendoring | dune 3.0 cannot find file through relative path during ppx preprocessing |
| 13 | [#6099](https://github.com/ocaml/dune/issues/6099) | S5 | D2 | Errors/UX | No error is raised when building an empty package not defined in the dune-project file |
| 14 | [#5104](https://github.com/ocaml/dune/issues/5104) | S5 | D2 | Build | Possible regression in the `select` stanza |
| 15 | [#4816](https://github.com/ocaml/dune/issues/4816) | S5 | D2 | Build | Optional argument for --promote-install-files breaks CLI compatibility |
| 16 | [#4479](https://github.com/ocaml/dune/issues/4479) | S5 | D2 | Tooling | interop between dune and merlin since 2.8 does not work with ppx_expect |
| 17 | [#3910](https://github.com/ocaml/dune/issues/3910) | S5 | D2 | Build | Mode `(byte shared_object)` cannot find stubs in Dune >= 2.1 |
| 18 | [#3618](https://github.com/ocaml/dune/issues/3618) | S5 | D2 | Build | Test "github660" does not pass with flambda |
| 19 | [#13815](https://github.com/ocaml/dune/issues/13815) | S6 | D2 | Paths | patch action should fail without source stanza |
| 20 | [#12317](https://github.com/ocaml/dune/issues/12317) | S6 | D2 | Errors/UX | User-defined rules cannot be added to the 'empty' alias |
| 21 | [#11501](https://github.com/ocaml/dune/issues/11501) | S6 | D2 | Build | dune doesn't reset DUNE_CACHE_ROOT inside cram tests |
| 22 | [#11134](https://github.com/ocaml/dune/issues/11134) | S6 | D2 | Crashes | Dune shows "Source files changed, restarting current build" for more than 30s |
| 23 | [#10029](https://github.com/ocaml/dune/issues/10029) | S6 | D2 | Errors/UX | Building the cmo of a module of a disabled library gives a bad error |
| 24 | [#6598](https://github.com/ocaml/dune/issues/6598) | S6 | D2 | Errors/UX | Confusing 'Module ... is used in several stanzas' error |
| 25 | [#5486](https://github.com/ocaml/dune/issues/5486) | S6 | D2 | Build | no-cmx-file warning emitted for external dependency after adding internal library |
| 26 | [#5044](https://github.com/ocaml/dune/issues/5044) | S6 | D2 | Build | Warning 58 with virtual_modules |
| 27 | [#4445](https://github.com/ocaml/dune/issues/4445) | S6 | D2 | Paths | action plugin: trying to read empty / non-existing directory raises |
| 28 | [#3487](https://github.com/ocaml/dune/issues/3487) | S6 | D2 | Tooling | Hinted `external-lib-deps` for `dune utop` does not include Odoc |
| 29 | [#2818](https://github.com/ocaml/dune/issues/2818) | S6 | D2 | Errors/UX | Cycles reported by dune are cryptic |

## Tier 5: Minor Bugs (D2, S7)

| # | Issue | S | D | Area | Title |
|---|-------|---|---|------|-------|
| 1 | [#13551](https://github.com/ocaml/dune/issues/13551) | S7 | D2 | Vendoring | Dune should respect user-specified PPX order in `(preprocess (pps ...))` stanza |
| 2 | [#13001](https://github.com/ocaml/dune/issues/13001) | S7 | D2 | Build | modules of library using ctypes without (modules) field are incorrectly validated |
| 3 | [#12700](https://github.com/ocaml/dune/issues/12700) | S7 | D2 | Crashes | under-specified dependencies for build env |
| 4 | [#12611](https://github.com/ocaml/dune/issues/12611) | S7 | D2 | Tooling | [Merlin] Curious Unbound module issue |
| 5 | [#12309](https://github.com/ocaml/dune/issues/12309) | S7 | D2 | Build | `--cache=disabled` is triggering some re-compilation |
| 6 | [#12103](https://github.com/ocaml/dune/issues/12103) | S7 | D2 | Crashes | [pkg] Passing `-j` to `dune build` causes the compiler package to be rebuilt |
| 7 | [#12007](https://github.com/ocaml/dune/issues/12007) | S7 | D2 | Tooling | dune build @ocaml-index builds too many files |
| 8 | [#11848](https://github.com/ocaml/dune/issues/11848) | S7 | D2 | Errors/UX | Test stanza allows expectation files to be generated |
| 9 | [#11633](https://github.com/ocaml/dune/issues/11633) | S7 | D2 | Tooling | odoc required by cram depending on objs/byte |
| 10 | [#11593](https://github.com/ocaml/dune/issues/11593) | S7 | D2 | Errors/UX | dune takes >2GB of RAM building some targets of frama-c.30.0 |
| 11 | [#11523](https://github.com/ocaml/dune/issues/11523) | S7 | D2 | Paths | symlinks in directory targets don't go in shared cache |
| 12 | [#11163](https://github.com/ocaml/dune/issues/11163) | S7 | D2 | Build | dune cache |
| 13 | [#11038](https://github.com/ocaml/dune/issues/11038) | S7 | D2 | Tooling | `dune fmt` requires `ocamlc` to be in path but does not guarantee that this is the case |
| 14 | [#10678](https://github.com/ocaml/dune/issues/10678) | S7 | D2 | Paths | Dangling internal path when using virtual library |
| 15 | [#10144](https://github.com/ocaml/dune/issues/10144) | S7 | D2 | Vendoring | All Recursive Aliases are broken in vendored directories |
| 16 | [#10111](https://github.com/ocaml/dune/issues/10111) | S7 | D2 | Errors/UX | Using ambiguous hash references for git repos leads to unexpected results |
| 17 | [#9775](https://github.com/ocaml/dune/issues/9775) | S7 | D2 | Errors/UX | glob_file_rec is not recursive on generated folder |
| 18 | [#9744](https://github.com/ocaml/dune/issues/9744) | S7 | D2 | Tooling | @doc-new's index.html might be missing a link to `/local/index.html` |
| 19 | [#9687](https://github.com/ocaml/dune/issues/9687) | S7 | D2 | Vendoring | Inconsistent assumptions over interface when additional copy of library is present in vendored_dirs |
| 20 | [#9672](https://github.com/ocaml/dune/issues/9672) | S7 | D2 | Vendoring | Bug/Request `--context` should work the same with dune build and dune exec |
| 21 | [#8989](https://github.com/ocaml/dune/issues/8989) | S7 | D2 | Paths | Menhir parsers as module group interfaces |
| 22 | [#8770](https://github.com/ocaml/dune/issues/8770) | S7 | D2 | Build | TUI captures clicks when using inside vscode |
| 23 | [#8417](https://github.com/ocaml/dune/issues/8417) | S7 | D2 | Crashes | Dune sometimes changes *.opam files in release mode |
| 24 | [#8073](https://github.com/ocaml/dune/issues/8073) | S7 | D2 | Errors/UX | Cannot promote empty files over a non-existing file |
| 25 | [#7464](https://github.com/ocaml/dune/issues/7464) | S7 | D2 | Paths | `preprocess` `per_module` dependencies are not relative |
| 26 | [#7454](https://github.com/ocaml/dune/issues/7454) | S7 | D2 | Tooling | `dune fmt` unexpectedly triggers menhir rules |
| 27 | [#7170](https://github.com/ocaml/dune/issues/7170) | S7 | D2 | Errors/UX | Folders excluded from `dirs` are visited when calling `dune build @my_alias` |
| 28 | [#7043](https://github.com/ocaml/dune/issues/7043) | S7 | D2 | Vendoring | Dune tests are being executed in unexpected dir while vendoring |
| 29 | [#6607](https://github.com/ocaml/dune/issues/6607) | S7 | D2 | Build | Test suite is broken when CLICOLOR_FORCE=1 |
| 30 | [#5899](https://github.com/ocaml/dune/issues/5899) | S7 | D2 | Build | Incorrect implementation of Workspace_root |
| 31 | [#5735](https://github.com/ocaml/dune/issues/5735) | S7 | D2 | Build | cmxs should not be installed in libexec |
| 32 | [#5566](https://github.com/ocaml/dune/issues/5566) | S7 | D2 | Tooling | Error: Reference to undefined global `Build_info__Build_info_data' |
| 33 | [#5417](https://github.com/ocaml/dune/issues/5417) | S7 | D2 | Build | `grep -z` causes files to diff as binary |
| 34 | [#4957](https://github.com/ocaml/dune/issues/4957) | S7 | D2 | Build | Using `findlib.dynload` shouldn't imply `-linkall` for executables |
| 35 | [#4895](https://github.com/ocaml/dune/issues/4895) | S7 | D2 | Errors/UX | The documentation/value of %{system} is not consistent |
| 36 | [#4866](https://github.com/ocaml/dune/issues/4866) | S7 | D2 | Tooling | dune doesn't cleanup all .merlin files and doesn't inform user of using them |
| 37 | [#4525](https://github.com/ocaml/dune/issues/4525) | S7 | D2 | Build | Making (setenv) easy to test |
| 38 | [#4468](https://github.com/ocaml/dune/issues/4468) | S7 | D2 | Paths | Error: Invalid dune file on Unicode in dune file |
| 39 | [#4457](https://github.com/ocaml/dune/issues/4457) | S7 | D2 | Build | Documentation for determining package version is incorrect |
| 40 | [#4347](https://github.com/ocaml/dune/issues/4347) | S7 | D2 | Build | Byte target can't be debugged with ocamldebug |
| 41 | [#4111](https://github.com/ocaml/dune/issues/4111) | S7 | D2 | Tooling | Dune doesn't generate correct .merlin file when directory path contains space |
| 42 | [#4021](https://github.com/ocaml/dune/issues/4021) | S7 | D2 | Build | auto-formatting of dune files does not preserve end-of-line strings |
| 43 | [#3642](https://github.com/ocaml/dune/issues/3642) | S7 | D2 | Tooling | Adding new formatters can break older projects |
| 44 | [#3638](https://github.com/ocaml/dune/issues/3638) | S7 | D2 | Errors/UX | env-vars ignored under exec |
| 45 | [#3549](https://github.com/ocaml/dune/issues/3549) | S7 | D2 | Errors/UX | dune not checking modules in modules_before_stdlib |
| 46 | [#3516](https://github.com/ocaml/dune/issues/3516) | S7 | D2 | Tooling | dune format-dune-file doesn't respect the formatting stanza |
| 47 | [#3474](https://github.com/ocaml/dune/issues/3474) | S7 | D2 | Paths | bootstrap does not properly search PATH |
| 48 | [#3230](https://github.com/ocaml/dune/issues/3230) | S7 | D2 | Errors/UX | Long form target inference is not properly versioned |
| 49 | [#3223](https://github.com/ocaml/dune/issues/3223) | S7 | D2 | Tooling | dune-project not formatted with @fmt |
| 50 | [#3182](https://github.com/ocaml/dune/issues/3182) | S7 | D2 | Errors/UX | The @all alias does not produce .cmt files which are produced by @check |
| 51 | [#2913](https://github.com/ocaml/dune/issues/2913) | S7 | D2 | Build | Dune should not look up other sub-directories when given `-p` |
| 52 | [#2757](https://github.com/ocaml/dune/issues/2757) | S7 | D2 | Build | dune install ignores --for-release-of-packages |
| 53 | [#2445](https://github.com/ocaml/dune/issues/2445) | S7 | D2 | Build | dune forwards signal to process but sends SIGKILL right away |
| 54 | [#1974](https://github.com/ocaml/dune/issues/1974) | S7 | D2 | Paths | `@all` target doesn't interact well with `(include_subdirs ...)` |
| 55 | [#1371](https://github.com/ocaml/dune/issues/1371) | S7 | D2 | Paths | -nostdlib in flags field, but forgotten when building stubs files |

## Tier 6: Subsystem Rework (D3)

| # | Issue | S | D | Area | Title |
|---|-------|---|---|------|-------|
| 1 | [#11225](https://github.com/ocaml/dune/issues/11225) | S1 | D3 | Build | dune-build-info: spurious `git describe` output instead of version string |
| 2 | [#8025](https://github.com/ocaml/dune/issues/8025) | S1 | D3 | Vendoring | dune-build-info reports wrong library version in vendored dir |
| 3 | [#5749](https://github.com/ocaml/dune/issues/5749) | S1 | D3 | Paths | Incorrect value when installing a relocatable binary with dune-site |
| 4 | [#13903](https://github.com/ocaml/dune/issues/13903) | S2 | D3 | Crashes | Internal error during `dune install` with pkg-enabled dune-workspace |
| 5 | [#13500](https://github.com/ocaml/dune/issues/13500) | S2 | D3 | Crashes | Dune 3.21.0 crashes and hangs with "Dependency cycle between ..." |
| 6 | [#13307](https://github.com/ocaml/dune/issues/13307) | S2 | D3 | Crashes | Crash when multiple install stanzas are targeting share_root for their directory |
| 7 | [#13230](https://github.com/ocaml/dune/issues/13230) | S2 | D3 | Crashes | Invalid Variable_name.t error raised |
| 8 | [#12609](https://github.com/ocaml/dune/issues/12609) | S2 | D3 | Crashes | dune build hangs if curl not installed |
| 9 | [#12108](https://github.com/ocaml/dune/issues/12108) | S2 | D3 | Build | Poor error reporting in cram tests, take 2 |
| 10 | [#12075](https://github.com/ocaml/dune/issues/12075) | S2 | D3 | Crashes | Building dune crashes with Unexpected_find_result for pp library |
| 11 | [#12018](https://github.com/ocaml/dune/issues/12018) | S2 | D3 | Crashes | crash when using ctypes stanza |
| 12 | [#11444](https://github.com/ocaml/dune/issues/11444) | S2 | D3 | Paths | ERROR while compiling dune.3.17.2 ($HOME/.cache/dune perms problem?) |
| 13 | [#11229](https://github.com/ocaml/dune/issues/11229) | S2 | D3 | Tooling | Dune developer preview: ocamllsp cannot read stdlib.cmi (corrupted compiled interface) |
| 14 | [#10393](https://github.com/ocaml/dune/issues/10393) | S2 | D3 | Errors/UX | Improve error message when git is not found |
| 15 | [#10335](https://github.com/ocaml/dune/issues/10335) | S3 | D4 | Paths | Cannot build executable in a target directory (architectural: module discovery vs build-time timing) |
| 16 | [#10285](https://github.com/ocaml/dune/issues/10285) | S2 | D3 | Crashes | Internal error: link_many: unable to find module |
| 17 | [#9963](https://github.com/ocaml/dune/issues/9963) | S2 | D3 | Paths | Aborted `init` command leaves empty directory |
| 18 | [#8968](https://github.com/ocaml/dune/issues/8968) | S2 | D3 | Crashes | Restarting OCaml LSP caused Internal error: attempting to write to a closed channel |
| 19 | [#8281](https://github.com/ocaml/dune/issues/8281) | S2 | D3 | Crashes | Exception when secondary .opam with bad name exists while running build doc |
| 20 | [#7962](https://github.com/ocaml/dune/issues/7962) | S2 | D3 | Crashes | Crash when depending on source_tree outside workspace |
| 21 | [#5312](https://github.com/ocaml/dune/issues/5312) | S2 | D3 | Crashes | dune utop blows up with an exception when cohttp-lwt-unix is present in ~/.ocamlinit |
| 22 | [#3484](https://github.com/ocaml/dune/issues/3484) | S2 | D3 | Crashes | stacktrace when trying to promote into a binary in use (linux) |
| 23 | [#3463](https://github.com/ocaml/dune/issues/3463) | S2 | D3 | Errors/UX | Dune is mangling qtest/ounit output |
| 24 | [#3160](https://github.com/ocaml/dune/issues/3160) | S2 | D3 | Crashes | Dune runtest incorrectly changes escape codes related to cursor movement |
| 25 | [#13566](https://github.com/ocaml/dune/issues/13566) | S3 | D3 | Tooling | @ocaml-index fails when multiple executables in a directory don't specify (modules) |
| 26 | [#12854](https://github.com/ocaml/dune/issues/12854) | S3 | D3 | Crashes | `--display=quiet` has no effect on `--root`-changing messages |
| 27 | [#11583](https://github.com/ocaml/dune/issues/11583) | S3 | D3 | Build | packages depending on a toolchain-provided compiler can't cache the first time |
| 28 | [#11440](https://github.com/ocaml/dune/issues/11440) | S3 | D3 | Build | ctypes' `deps` field doesn't follow the dependency specification language |
| 29 | [#10974](https://github.com/ocaml/dune/issues/10974) | S3 | D3 | Paths | "Shared cache miss" error while building project on different filesystem to cache directory |
| 30 | [#10731](https://github.com/ocaml/dune/issues/10731) | S3 | D3 | Errors/UX | Many noisy shared cache miss messages when using multiple filesystems |
| 31 | [#10697](https://github.com/ocaml/dune/issues/10697) | S3 | D3 | Build | Dynamic loading of packages: linking issues |
| 32 | [#10466](https://github.com/ocaml/dune/issues/10466) | S3 | D3 | Paths | Packaging a library with `extra_objects` |
| 33 | [#7761](https://github.com/ocaml/dune/issues/7761) | S3 | D3 | Watch/RPC | `dune build --passive-watch-mode` ignores its argument |
| 34 | [#7720](https://github.com/ocaml/dune/issues/7720) | S3 | D3 | Tooling | `dune build @doc` does not rebuild pages |
| 35 | [#7470](https://github.com/ocaml/dune/issues/7470) | S3 | D3 | Tooling | `dune-site` cannot be used in top-level REPL |
| 36 | [#7146](https://github.com/ocaml/dune/issues/7146) | S3 | D3 | Paths | Linker is invoked from unexpected directory |
| 37 | [#6086](https://github.com/ocaml/dune/issues/6086) | S3 | D3 | Build | The `embed_in_plugin_libraries` stanza fails with libraries requiring link-time code |
| 38 | [#5809](https://github.com/ocaml/dune/issues/5809) | S3 | D3 | Build | ctypes stanza does not compile cstubs .o files with -fPIC |
| 39 | [#5322](https://github.com/ocaml/dune/issues/5322) | S3 | D3 | Tooling | Relocatable site does not work when the install directory is outside the build directory |
| 40 | [#2909](https://github.com/ocaml/dune/issues/2909) | S3 | D3 | Tooling | Virtual Libraries: Dune files don't include required source entries when relying on virtual modules |
| 41 | [#2565](https://github.com/ocaml/dune/issues/2565) | S3 | D3 | Watch/RPC | Minor improvements for Build_info and install |
| 42 | [#9773](https://github.com/ocaml/dune/issues/9773) | S5 | D3 | Build | Ctypes and foreign bindings won't bundle library properly |
| 43 | [#11377](https://github.com/ocaml/dune/issues/11377) | S7 | D3 | Crashes | dune build @doc doesn't update generated documentation properly |
| 44 | [#11281](https://github.com/ocaml/dune/issues/11281) | S7 | D3 | Build | Dune site (without plugins) forces `-linkall` |
| 45 | [#7413](https://github.com/ocaml/dune/issues/7413) | S7 | D3 | Paths | Debug mapping is sometimes inconsistent with installed locations |
| 46 | [#2420](https://github.com/ocaml/dune/issues/2420) | S7 | D3 | Vendoring | Configurator does not have access to C flags set in (env) |
| 47 | [#1593](https://github.com/ocaml/dune/issues/1593) | S7 | D3 | Paths | Watermarking works only in the GIT root, not dune root |

## Tier 7: Architectural & Design (D4-D5)

| # | Issue | S | D | Area | Title |
|---|-------|---|---|------|-------|
| 1 | [#13492](https://github.com/ocaml/dune/issues/13492) | S1 | D4 | Errors/UX | install stanza in dynamic_include is ignored |
| 2 | [#12715](https://github.com/ocaml/dune/issues/12715) | S1 | D4 | Watch/RPC | RPC system hanging non-deterministically on eager watch mode |
| 3 | [#11138](https://github.com/ocaml/dune/issues/11138) | S1 | D4 | Vendoring | Promotion and cross-compilation |
| 4 | [#4070](https://github.com/ocaml/dune/issues/4070) | S1 | D4 | Vendoring | Undesired conflict between vendored library and public library by the same name |
| 5 | [#12900](https://github.com/ocaml/dune/issues/12900) | S2 | D4 | Watch/RPC | dune hangs in mdx tests waiting for _build/default/_build/.rpc/dune |
| 6 | [#12660](https://github.com/ocaml/dune/issues/12660) | S2 | D4 | Watch/RPC | dune forwarding rpc occasionally gets EINVAL backtrace |
| 7 | [#11010](https://github.com/ocaml/dune/issues/11010) | S2 | D4 | Watch/RPC | Dune crashes when editing a file in exec watch mode |
| 8 | [#7568](https://github.com/ocaml/dune/issues/7568) | S2 | D4 | Watch/RPC | Dune doesn't respond to RPC methods when run in watch mode in the dune repository |
| 9 | [#5447](https://github.com/ocaml/dune/issues/5447) | S2 | D4 | Crashes | dependency cycle that does not involve any files |
| 10 | [#3591](https://github.com/ocaml/dune/issues/3591) | S2 | D4 | Crashes | Internal error: dependency cycle with virtual_modules |
| 11 | [#13080](https://github.com/ocaml/dune/issues/13080) | S3 | D4 | Watch/RPC | dune build --watch + dune exec + DUNE_BUILD_DIR does not work |
| 12 | [#10896](https://github.com/ocaml/dune/issues/10896) | S3 | D4 | Tooling | Using `@ocaml-index` with vendored libraries: `Error: Conflict between the following libraries` |
| 13 | [#7223](https://github.com/ocaml/dune/issues/7223) | S3 | D4 | Watch/RPC | "I/O error" with `.pp.ml` file when running `dune build . -w` |
| 14 | [#4156](https://github.com/ocaml/dune/issues/4156) | S3 | D4 | Vendoring | ppxs are built in the target context in cross-compilation settings |
| 15 | [#3917](https://github.com/ocaml/dune/issues/3917) | S3 | D4 | Vendoring | Explicit executable dependencies and cross-compilation |
| 16 | [#3569](https://github.com/ocaml/dune/issues/3569) | S3 | D4 | Errors/UX | Expect tests with (implicit_transitive_deps false) |
| 17 | [#13525](https://github.com/ocaml/dune/issues/13525) | S5 | D4 | Watch/RPC | Formatting dune files on save while the build is running |
| 18 | [#7034](https://github.com/ocaml/dune/issues/7034) | S5 | D4 | Tooling | Dune treats warnings as errors according to the workspace `lang dune` version when building vendored packages with a more permissive `lang dune` version |
| 19 | [#7624](https://github.com/ocaml/dune/issues/7624) | S6 | D4 | Watch/RPC | In `dune_rpc_lwt` closing the output channel should also close the input channel |
| 20 | [#13788](https://github.com/ocaml/dune/issues/13788) | S7 | D4 | Watch/RPC | with RPC/watch: short job waits for long job to return |
| 21 | [#13768](https://github.com/ocaml/dune/issues/13768) | S7 | D4 | Vendoring | Usability issues with Dune contexts |
| 22 | [#12752](https://github.com/ocaml/dune/issues/12752) | S7 | D4 | Watch/RPC | RPC builds don't transfer warnings to the client |
| 23 | [#12725](https://github.com/ocaml/dune/issues/12725) | S7 | D4 | Watch/RPC | [RPC] Eager watch mode doesn't register promotions at all |
| 24 | [#10268](https://github.com/ocaml/dune/issues/10268) | S7 | D4 | Vendoring | Module name conflict with vendored library |
| 25 | [#10173](https://github.com/ocaml/dune/issues/10173) | S7 | D4 | Vendoring | Percent forms are allowed to escape from one context to another |
| 26 | [#6817](https://github.com/ocaml/dune/issues/6817) | S7 | D4 | Watch/RPC | `dune utop --watch` Appears to be broken |
| 27 | [#5549](https://github.com/ocaml/dune/issues/5549) | S7 | D4 | Watch/RPC | dune build -w restricting job number for no reason |
| 28 | [#3913](https://github.com/ocaml/dune/issues/3913) | S7 | D4 | Vendoring | Dune finds non existing library conflict without (implicit_transitive_deps false) |
| 29 | [#12996](https://github.com/ocaml/dune/issues/12996) | S2 | D5 | Build | `dune exec` doesn't perform install stanza |
| 30 | [#1819](https://github.com/ocaml/dune/issues/1819) | S2 | D5 | Crashes | Dune always sets -no-alias-deps for all files |
| 31 | [#9690](https://github.com/ocaml/dune/issues/9690) | S3 | D5 | Paths | `default` alias usability issues for projects with nested folders |
| 32 | [#7583](https://github.com/ocaml/dune/issues/7583) | S3 | D5 | Build | What should happen when exposing code from a private package? |
| 33 | [#5697](https://github.com/ocaml/dune/issues/5697) | S3 | D5 | Build | env stanza should support variables `%{...}` |
| 34 | [#5621](https://github.com/ocaml/dune/issues/5621) | S3 | D5 | Build | (optional) in executables doesn't work |
| 35 | [#5122](https://github.com/ocaml/dune/issues/5122) | S5 | D5 | Build | Package dependency check doesn't take into account recursive dependencies |
| 36 | [#8291](https://github.com/ocaml/dune/issues/8291) | S7 | D5 | Build | Please honor CFLAGS |
| 37 | [#3634](https://github.com/ocaml/dune/issues/3634) | S7 | D5 | Build | foreign archive handling |
| 38 | [#3151](https://github.com/ocaml/dune/issues/3151) | S7 | D5 | Vendoring | Recursive alias in vendored directories are not well defined |
| 39 | [#1920](https://github.com/ocaml/dune/issues/1920) | S7 | D5 | Build | Detect case-insensitive filesystems and prevent double-linking |
