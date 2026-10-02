# Paths, Files & Symlinks

## Summary

This category contains 39 bugs spanning from issue #1371 to #13815, representing some of the oldest unresolved issues in the Dune tracker alongside relatively recent reports. A dominant theme is **symlink mishandling**: Dune fails when encountering symlinks in directory targets (#11523, #9873), during install (#7831), when resolving absolute paths (#5833), and during promotion (#8075). The `diff` action incorrectly reports "Unable to resolve symlink" instead of treating a missing file as empty (#13638). These symlink issues are particularly impactful because they block caching (#11523), break installs (#7831), and cause spurious build failures (#9873).

A second major cluster involves **incorrect path resolution and leaking of internal paths**. Absolute build paths leak into installed `dune-package` files, rendering distributed packages unusable (#11774). The `preprocess per_module` stanza resolves paths relative to the workspace root instead of the dune file (#7464). The linker runs from an unexpected directory, breaking relative `-L` paths in `c_library_flags` (#7146). Compiler error messages show paths relative to the wrong project root when building from submodules (#7222). Relocatable installs produce doubled path prefixes like `/tmp/bla//tmp/bla/share/` (#5749). Debug mappings via `BUILD_PATH_PREFIX_MAP` omit package names, causing wrong source locations after installation (#7413). These path bugs collectively degrade the developer experience and break cross-project consumption of installed libraries.

The third significant pattern is **silent failures and confusing error messages around directory handling**. The `(dirs ...)` stanza silently ignores paths of depth >= 2 with no warning (#5313). Hidden directories like `.cargo/` are silently excluded from `source_tree` dependencies (#7135). The `copy_files` glob silently does nothing when it matches a directory (#5992). The `data_only_dirs` documentation is misleading about ordered set language support (#9759), and its interaction with `(dirs ...)` is undocumented (#2144). The `@all` alias omits targets from subdirectories when `include_subdirs` is used (#1974). Several issues also involve filesystem boundary problems: the shared cache fails with `EXDEV` when the project and cache live on different filesystems (#10974), and cache directory permissions cause compilation failures (#11444). The `dune subst` watermarking feature looks for `.git` rather than `dune-project` to find the project root (#1593), a design mismatch that has remained unfixed for years.


### Severity Breakdown

| Severity | Count |
|----------|-------|
| **S1** — Silent Correctness Failures | 5 |
| **S2** — Crashes & Data Loss | 3 |
| **S3** — Broken Documented Behavior | 18 |
| **S5** — Regressions | 1 |
| **S6** — Misleading Errors & Poor UX | 2 |
| **S7** — Workaroundable Bugs | 10 |

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| **D2** — Moderate Investigation | 29 |
| **D3** — Subsystem Rework | 9 |
| **D5** — Design Problem | 1 |

## Issues (39 bugs)

- **#13815** `S6` `D2` - patch action should fail without source stanza — Patch action on packages without a source stanza gives confusing "No such file or directory" error instead of an informative message
- **#13638** `S3` `D2` - `diff` action directive isn't working as expected with a non-existent file — diff action with a non-existent file gives "Unable to resolve symlink" error instead of comparing with empty file as documented
- **#11774** `S1` `D2` - `dune install` with an out-of-workspace build directory produces absolute paths in dune-package files — Absolute build paths leak into installed dune-package files, making distributed packages unusable
- **#11523** `S7` `D2` - symlinks in directory targets don't go in shared cache — Bug: symlinks in directory targets prevent caching, which is incorrect behavior.
- **#11444** `S2` `D3` - ERROR while compiling dune.3.17.2 ($HOME/.cache/dune perms problem?) — Bug: dune compilation fails due to cache directory permissions issue.
- **#10974** `S3` `D3` - "Shared cache miss" error while building project on different filesystem to cache directory — Bug: shared cache fails with EXDEV error when project and cache are on different filesystems.
- **#10678** `S7` `D2` - Dangling internal path when using virtual library — Bug: using a pinned virtual library (sexplib0) causes dangling internal path errors during compilation.
- **#10466** `S3` `D3` - Packaging a library with `extra_objects` — Installed library with extra_objects fails to link when consumed by downstream projects; the .o file path is wrong at link time
- **#10335** `S3` `D4` - Cannot build executable in a target directory — Architectural: module discovery happens at rule-generation time but directory target contents are only known after execution; fix requires bridging this timing gap (see dir_contents.ml CR-someday comment)
- **#9963** `S2` `D3` - Aborted `init` command leaves empty directory — `dune init proj` with an invalid name creates an empty directory that should be cleaned up on failure
- **#9873** `S5` `D2` - Error with directory symlink: Unexpected file kind "S_DIR" — Directory symlinks in directory targets cause build errors; regression from a specific commit
- **#9759** `S3` `D2` - data_only_dirs documentation seems to imply that ordered set language applies — Documentation is misleading about ordered set language support in data_only_dirs, causing confusion
- **#9690** `S3` `D5` - `default` alias usability issues for projects with nested folders — Custom `default` alias in a subdirectory is ignored when building from a parent directory; the `all` alias overrides it
- **#8989** `S7` `D2` - Menhir parsers as module group interfaces — When `(include_subdirs qualified)` is enabled, menhir parser files cannot serve as group interfaces, which is a limitation that prevents a valid use case from working.
- **#8075** `S3` `D2` - Fail to promote over a non-existing file — Promotion fails with a symlink resolution error even though documentation/tests show it should work; broken functionality.
- **#7831** `S3` `D2` - Install fails for a directory with symlinks to a directory — `dune install` fails when the directory contains symlinks to directories; broken install functionality.
- **#7464** `S7` `D2` - `preprocess` `per_module` dependencies are not relative — Preprocessing with action `run` in `preprocess` stanza resolves paths relative to workspace root instead of the dune file directory
- **#7413** `S7` `D3` - Debug mapping is sometimes inconsistent with installed locations — `BUILD_PATH_PREFIX_MAP` in compiled libraries is missing package name information, causing incorrect debug source mappings after installation
- **#7222** `S1` `D2` - compiler errors have wrong relative path — Compiler errors show paths relative to the parent project root instead of the current project when building from a submodule
- **#7146** `S3` `D3` - Linker is invoked from unexpected directory — Linker cannot find libraries referenced with relative paths in `c_library_flags` because the linker runs from an unexpected directory
- **#7135** `S3` `D2` - Hidden folders are ignored in source_tree dep — Files in hidden directories (e.g. `.cargo/`) are silently excluded from `source_tree` dependencies with no way to include them
- **#6133** `S3` `D2` - The new dir install feature does not work on existing directories — Bug: the `(dirs ...)` install stanza fails with "No rule found for existing-dir" when using existing directories
- **#6073** `S3` `D2` - test stanza does not work with bytecode compiled with foreign_stubs — Bug: test stanza fails to set up LD_LIBRARY_PATH correctly for bytecode executables with foreign_stubs
- **#5992** `S1` `D2` - Usability/Documentation issues with copy_files/glob — Bug (partially): copy_files silently does nothing when glob matches a directory or non-existing file instead of reporting an error
- **#5833** `S3` `D2` - [dune engine] [bug] Error file unavailable when an absolute path points to a symlink — Bug: dune errors on `dune build $file` when `$file` is an absolute path pointing to a symlink
- **#5749** `S1` `D3` - Incorrect value when installing a relocatable binary with dune-site — Bug: relocatable install produces incorrect doubled path prefix (e.g., `/tmp/bla//tmp/bla/share/...`)
- **#5647** `S3` `D2` - Moving a file as a previously existing directory — Bug: renaming a cram test from a directory to a file causes shared cache errors due to stale directory entries
- **#5313** `S1` `D2` - `(dirs ..` with paths of depth >= 2 are just ignored — Bug: paths with depth >= 2 in the `(dirs ...)` stanza are silently ignored without any error message
- **#4468** `S7` `D2` - Error: Invalid dune file on Unicode in dune file — Dune incorrectly rejects Unicode characters in paths within dune files
- **#4445** `S6` `D2` - action plugin: trying to read empty / non-existing directory raises — read_directory_with_glob raises an unhelpful error on empty or non-existing directories instead of returning empty
- **#3805** `S3` `D2` - No such file or directory when DUNE_BUILD_DIR is set during test — `dune runtest` fails when `DUNE_BUILD_DIR` environment variable is set
- **#3474** `S7` `D2` - bootstrap does not properly search PATH — Dune bootstrap incorrectly assumes all `ocaml*` programs live next to the first one found, instead of properly searching PATH for each
- **#3173** `S3` `D2` - can't promote into a directory start with underscore — Promoting output into a directory starting with underscore fails with "directory does not exist" even though the directory exists
- **#3025** `S3` `D2` - dune install: ocamlfind point to the wrong directory in a local switch — In a local switch without ocamlfind, dune uses the global switch's ocamlfind and tries to install to the wrong location
- **#2938** `S3` `D2` - (dirs ...) not recognised in dune2 — `(dirs *)` works in a static dune file but is rejected with "Unknown constructor" when used via OCaml-syntax dune file generation
- **#2144** `S3` `D2` - Error in documentation for dirs stanza — Bug: the documentation claims files in ignored sub-directories can be depended on, but this does not work; also `(data_only_dirs)` requires listing dirs in both `(dirs)` and `(data_only_dirs)` which is undocumented and confusing
- **#1974** `S7` `D2` - `@all` target doesn't interact well with `(include_subdirs ...)` — Bug: targets generated by subdirs are not included in the `@all` alias, which should contain all buildable targets
- **#1593** `S7` `D3` - Watermarking works only in the GIT root, not dune root — Bug: `dune subst` looks for `.git` directory rather than `dune-project` to determine the project root, preventing watermarking from working when OCaml code is in a subdirectory of a git repository
- **#1371** `S7` `D2` - -nostdlib in flags field, but forgotten when building stubs files — Bug: when `-nostdlib` is specified in flags, dune does not pass it when building C stubs, causing unwanted include paths to be passed to gcc
