<!-- @version 2026-09-22 @lifecycle LOCAL_SOFTWARE_COMPLETE_REVIEW_PENDING -->
# Ion Language in the installed campus

The complete local Ion Language software module is installed in the existing
campus. Open `Launch-Teaching-Campus.cmd`, then the **Ion Language** link beside
Chemistry, or use `http://127.0.0.1:47831/websites/chemistry/ion-language/`.

The module includes all **six lessons, 18 worked examples, 72 keyed practice
prompts and 62 provisional ion cards**, plus both translation directions, family
comparisons, the existing count builder and a bounded review queue. The readable
`lessons.html` page keeps the full lesson sequence available without JavaScript.

The existing C++ runtime owns content compilation, formula/name checking and
review scheduling. It accepts only the curated compound pool, distinguishes
atom inventory from conventional grouping and charge, preserves ion identity,
and asks for clarification on ambiguous notation. Unsupported acids, hydrates,
mixed valence, complexes and unlisted pairs receive an explicit boundary response.
Free explanations are self-reviewed against the supplied key, not keyword-graded.

## Private work and recovery

The unchanged browser key is `luminara-ion-language-v1`. Earlier workshop records
are readable without an automatic overwrite. **Review the record upgrade** shows
a preview; Cancel is the default. Approval retains the exact earlier JSON inside
the versioned full-module record. Other subjects' keys and private notebooks are
untouched. This is browser persistence, not shared native notebook migration.

Full-module export includes lessons' practice history, drafts, notes and optional
confidence. Missing confidence remains null. Import validates the module/version,
previews additions, deduplicates identical event IDs, refuses changed data under
the same event ID and retains different notes separately. Conflicting drafts keep
the current version and remain recoverable in the original import file.

Saving requires a Web Lock and byte-for-byte readback. Stale tabs, denied locks,
quota failures and malformed records cannot silently overwrite existing work.
Failed saves leave the session exportable; size limits refuse additions without
truncating earlier history. Download requested does not prove that a file reached
disk. Keep the original import/export files until you have checked the result.

Hints and revealed examples remain support evidence. Both translation directions
have separate history; immediate inverse answers and repeated early checks do not
advance delayed-recall intervals. Review prioritizes shaky/overdue work and offers
optional retained practice. The default 1/3/7/14-day intervals are a study baseline,
not a mastery certificate or a measured learning result.

## Verification

Measured test results, changed-file hashes, installed runtime identity and browser
observations are recorded in `evidence/ion-completion-update.json`. The complete
before-edit backup inventory is
`review-backups/20260922-ion-complete/BACKUP_MANIFEST.json`.

| Checks | Passed |
| --- | --- |
| Native seed/compiler | 18 |
| Native domain and review | 31 |
| Native stateless HTTP API | 33 |
| Shared native launch controller | 38 |
| Native private store regression | 61 |
| Native host parity | 35 |
| Native Windows paths | 16 |
| Production private-store smoke | 8 |
| Browser count-builder boundary | 30 |
| Full-module browser state and UI | 35 |
| Curriculum/source/projection integration | 11 |
| Retained host regression | 22 |
| Retained launcher regression | 32 |
| Campus navigation | 18 |
| Campus progress display | 14 |
| Compiler CLI failure and determinism | 11 |
| Installed read-only launch views | 5 |

Browser checks use disposable study text on an owned temporary native listener.
The source packet remains exact: all 23 files and the OneDrive originals are
verified. Preservation also covers 12 original archives, 3,768 archive members
and 378 retained earlier files. No full distribution package was rebuilt.

## Remaining gates and Windows limits

- The original instructor `1117 Ion List.pdf` has not been located. All ion entries
  remain `courseSourceVerified: false`; phosphite, silicate and carbide retain
  explicit course-profile scope. Human course/science approval remains open.
- Actual screen-reader and iPad/device checks, and retained-learning assessment,
  remain unassessed. Desktop viewport checks are not hardware certification.
- Browser storage, Web Locks, download permissions and installed voices depend on
  the browser. Text remains available when speech is unavailable; no microphone
  or automatic cloud synchronization is used.
- The full production-port restart on an actual user's server was not exercised.
  The installed executable uses the existing shared confirmation flow: save/export
  active study work before approving an older instance's shutdown. All development
  shutdown/termination tests used owned fixtures, never a user's process.
- Runtime paths retain the existing NTFS safeguards. Unicode compiler paths were
  tested; extended-length compiler paths and external editor limits remain
  unassessed by this update.

The campus development bar remains **4/6**: shared native saving and the full
campus journey review remain U05/U06. There was no publication, push, Lumi_OS
integration, source-archive replacement or access to real learner notebooks.

## Editable files and regeneration

Module source is under `30-modules/chem-1117-f2026/ion-language/source/`; its six
served files are under `40-projections/chemistry/ion-language/`. Native ownership
is in `20-shared-kernel/native/`, including `ion_compiler`, `ion_domain` and
`ion_api_http`. `ION_LANGUAGE_INTEGRATION_MAP.md` records the connections.

Build the existing native CMake project, then run:

```text
luminara_ion_compiler INPUT.json OUTPUT.json CURRICULUM.json READER.html
```

Inputs are `source/ion-seed.json` and `source/curriculum-seed.json`; outputs are
`source/ion-data.json` and `source/lessons.html`. Review and admit the exact public
projection hashes afterward. The one-time `.py.txt` files in the backup directory
are editing/test evidence, not an interpreted production backend.

This report supersedes the first-slice scope in `evidence/ion-language-update.json`.
Earlier receipts remain historical evidence; they do not describe today's bytes.
