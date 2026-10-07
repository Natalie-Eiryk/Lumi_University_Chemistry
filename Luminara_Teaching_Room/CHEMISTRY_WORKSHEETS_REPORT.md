<!-- @version 2026-09-22 -->
<!-- @lifecycle LOCAL_WORKSHEET_REPLACEMENT -->

# Chemistry worksheets, campus 1.2.0

The Chemistry lesson now opens **Worksheet practice** for a new notebook.
It replaces the 39 scanned study pages with **293 practice prompts and 561
answer fields** covering all 19 source entries. Existing notebooks keep their
current activity selection; choose Worksheet practice to enter the new questions.

The replacement preserves worksheet numbering, table rows and answerable
subparts, including all 72 Chapter 1 problems. Ten of the prompts are explicitly
authored reviews for the periodicity reference sheet. Repeated worksheet
versions retain separate responses. See the full [coverage ledger](evidence/chemistry-questions/COVERAGE.md)
for counts, adaptations, excluded administrative items and verification limits.

Questions provide editable answers, method hints, progress, previous/next and
direct question selection, and a self-review mark. All fields must have a
response before marking a review; changing an answer clears that mark. Progress
is not an automatic grade. Instrument tasks use lightweight authored SVG/text
models; chemistry representation tasks accept typed orbital and Lewis notation.

Answers use the existing Chemistry key and native saving interface. Reasoning
appears in the shared campus journal. Earlier page-linked notes remain accessible
under **Earlier notes about source pages** and in the journal. Older imports
preserve current worksheet records when that section is absent. Current imports
replace their explicit worksheet section only after the existing confirmation.
Export includes worksheet answers and reasoning. Versions before 1.2.0 cannot
read the new optional worksheet section; preserve the earlier revision/backup
before choosing an older program. Selecting a release does not downgrade work.

## Files and preservation

- Existing Chemistry source: `app.js`, `folder.js`, `template.html`, `build-info.json`;
  new `questions.json`, `questions.js`, `questions.css` under
  `30-modules/chem-1117-f2026/source/`.
- Native code: `chemistry_compiler_main.cpp`, `work_api.cpp`, `host_bundle.cpp`,
  new `chemistry_questions.cpp/.hpp` and `chemistry_question_index.hpp`, and CMake.
- Installed generated page: `web/chemistry.html`, now **291,125 bytes**, compared
  with **15,127,189 bytes** before replacement (about **98.1% smaller**).
- Preservation/parity metadata: `COMPREHENSIVE_PRIOR_PRESERVATION.json`,
  `verify_comprehensive.py`, retained reference host `serve_lab.py`, and refreshed
  `evidence/native-host-legacy-reference.json`. Original teaching banks remain
  byte/semantically identical; only the scan payload is retired from the page.
- Tests: `20-shared-kernel/native/tests/chemistry_question_tests.cpp` and
  `tests/test_chemistry_questions.cjs`. Source audit, inert authoring/edit recipes,
  coverage and measured test evidence are under `evidence/chemistry-questions/`.
- Changed pre-existing files are backed up under
  `review-backups/20260922-chemistry-questions/originals/`, with hashes in
  `manifest.json`. The stable desktop executable, shortcut and five launch
  entry points are unchanged. No replacement full campus package was created.

The host, port, routes and browser keys are preserved. The 12 original source
archives and 3,768 members pass preservation verification, as do 378 retained
prior-assembly files. Private learner records are not read or migrated by this
update. Source archives and scanned source evidence remain inert and unserved.

## Verification

- All **12 native suites passed**, including the new worksheet suite, existing
  launch conflict/shutdown identity checks, releases, storage, paths, Ion and
  shared work API. Final content admission and HTTP parity were rerun after
  the method-hint and UI polish changes.
- **15 new browser-function checks**, **7 Chemistry compatibility checks** and
  **55 shared-saving checks** passed: 77 checks in those three suites.
- An owned C++ fixture and the in-app browser rendered all **293 prompts / 561
  fields**. Each source had its expected question count and a reachable final
  question; none rendered an image, iframe, embed or object.
- Live synthetic-work checks covered answer/progress updates, clearing a review
  after editing, canceled/approved native adoption, save/reopen, preserved page
  notes, and a shared-journal edit returning to the same worksheet answer.
- Native tests save all 561 fields and reopen them exactly, reject missing
  subparts, duplicate/unknown IDs, malformed scales, unsupported versions,
  oversized UTF-8 inputs and invalid review marks. They also verify journal
  isolation and stale-save refusal without reading real notebooks.
- Evidence: `native-suites.xml`, `final-content-suites.xml`, `native-tests.json`,
  `browser-function-tests.json`, `live-browser.json`, and the release receipt
  in `evidence/chemistry-questions/`.

## Activation and limits

Version **1.2.0** is delivered through the existing immutable release manager.
It is selected at generation **3**, with **1.1.0** as the previous version.
The desktop link continues to point to the stable root executable. A running
campus session is left running; save/export its study work before accepting the
normal launcher handover to the new version. Selection and a readiness check
do not prove that a running server has switched versions.

Windows/NTFS remains the supported runtime/storage environment. Live UI checks
used the in-app browser on owned fixture ports, not the user's normal browser
profile. Actual private-notebook adoption, touch-device behavior and a real user
session handover were not exercised. The local executable remains unsigned.
The stable 1.0.0 bootstrap also copies its old descriptive `chemistrySourceScope`
text into release manifests; that annotation still mentions 39 facsimiles.
It is stale metadata, not a retained viewer: the sealed Chemistry resource hash
matches the new 291,125-byte page, whose compiled bank has 293 prompts and no
embedded scans. The new native source reports the updated scope when loading
the editable installation; updating that bootstrap annotation is outside this
worksheet replacement. The immutable 1.2.0 manifest was not edited after sealing.
The official answer/convention guide, missing source instrument views and full
semester syllabus remain unavailable; no automatic correctness certification
is claimed. No user process was terminated, privileges escalated, source archive
changed, material published or pushed, or Lumi_OS integration performed.
