# CHEM 1117 — source-limited teaching pilot and preservation pass

**September 21, 2026 · Teaching Room 1.1.0 · Chemistry 0.1.0 · private local study**

## What is actually known

The request named a Windows OneDrive directory, `Chem_1117_F2026`. That directory has NOT been scanned. Files searches of the conversation and Library recovered one relevant course source: **Chem 1117 - workbook module 1-1.pdf**, seven pages. Its page images were inspected through Files. No syllabus, full directory inventory, official answer key, remaining worksheets, or current course AI policy was retrieved. Connector discovery did not establish a live read of the OneDrive folder. The preliminary plan is based on the recovered workbook, not on an invented full course map.

The original PDF could not be materialized through the authorized Files path. The app therefore includes selected, labeled transcriptions of printed passages and readable learner notes—not a PDF or facsimile. The link between this Library copy and the current Windows-folder version remains unverified.

## What the source suggests for the teaching design

Pages 1–2 supply matter, physical states, and properties; page 3 distinguishes physical and chemical properties; page 4 distinguishes two types of change through chemical composition; page 5 supplies eleven example prompts; pages 6–7 supply a completed classification tree and mixture notes. The organization in the pilot follows these source pages rather than a generic survey of chemistry.

The tree especially rewards a route-based explanation: a short leaf descriptor has a parent branch. A learner can reconstruct the relationship before retrieving its name. The change examples support comparisons within a familiar setting, such as taking a bite of food versus digesting food. These are questions and examples on the actual pages, not newly invented numerical homework.

Handwriting remains attributed to Natalie as learner annotation, according to her prior clarification. It is not promoted to an instructor answer key. The mixed element wording, incomplete compound line, page-5 “always” statement, and handwritten reaction sketch remain visible as clarification points. Nothing is silently repaired or filled from a different textbook.

## Working pilot

The new `/chemistry/` route contains five activities:

- **Find a way in:** six guided routes, with source-page scope and a visible missing-source boundary.
- **Source & thinking:** 18 response stops with pre/post Ms. Luminara guidance, optional three-step handrails, source beside writing, independent pane scrolling, Quiet desk, larger type, and a jump-to-writing control.
- **Name & meaning:** six printed definitions plus six completed-chart associations. Matching checks a displayed source association. Name recall and meaning have separate learner self-ratings; there is no automated semantic grade.
- **Change detective:** eleven exact page-5 prompts. The comparison is with visible learner annotations, not a claimed official key. A mismatch can be saved as a question.
- **Notebook & sources:** private notes, clarification questions, chemistry-only JSON backup/import and a Markdown export of learner writing. Import requires explicit replacement approval and rejects other formats, including Bioethics.

The guides are authored scaffolds, not instructor prose or a live AI tutor. No learning-outcome experiment, ADHD treatment effect, or instructor endorsement is claimed. The prototype supplies conceptual reinforcement, not submission-ready lab reports or assessed work.

## Preservation and integration boundary

The existing Bioethics HTML remains byte-identical:

`bb4410480b38bbd05a4ca3816d63f07829ec17f0c3099e8cb3b1a7a8882afbf7`

All nine original ZIPs, their 594 file members, and 162 exact active source copies passed the retained preservation verifier. The entire previous consolidated assembly contained 243 files: 231 remain identical in place, and 12 revised artifacts have exact original copies under `10-sources/assembly-1-baseline/`. No previous input bytes were discarded.

The new route uses the same loopback origin and its own `luminara-chem1117-workbook-pilot-v1` key. The six Bioethics keys are unchanged. The server still has a closed route list, accepts no data writes, and exposes no archive/source-directory routes. Chemistry has no telemetry or automatic network calls. It adds no cloud service or native Lumi runtime.

## Fresh checks and their limits

**80 grouped checks passed:** 22 existing host/updater tests, 26 preservation/intake tests, 6 portal UI groups, 6 chemistry host tests, 19 chemistry UI groups, and 1 mobile writing-focus group. These contain software assertions, not 80 learners or independent outcome studies. The 131-group internal Bioethics suite was not rerun here; its exact app bytes and earlier receipts are preserved.

The new checks exercise all 18 response stops, all twelve matching associations, all eleven prompt comparisons, note restoration from serialized state, separate ratings, actual download events, import validation/cancellation, failed saves, corrupt previous values, conflicting-tab detection, markup escaping, source changes without textarea replacement, keyboard navigation, and four viewport widths. Desktop and mobile screenshots of the actual app were inspected. Two consecutive chemistry and portal builds are byte-identical.

Real HTTP tests served the exact chemistry and Bioethics bytes and rejected private paths and write methods. A native persistent Chromium profile was attempted without a Storage fixture; the managed environment returned `ERR_BLOCKED_BY_ADMINISTRATOR` before the app could load. That result is **blocked**, not a pass. UI/serialization tests used an explicitly test-only Storage fixture; it is not in the delivered HTML. User Windows launchers, private Firefox notes, native file-origin persistence, and Lumi-Ladybird execution were not accessed or certified.

## Next exact source intake

Attach a ZIP of **only Chem_1117_F2026**, preserving its subfolders. The existing staging tool has a new `Stage-Chemistry.cmd` shortcut pointed at the named location; it creates a separate local snapshot and inventory, does not modify the original, and does not upload it. Reparse points, inaccessible data, and size limits remain stop conditions.

The next source pass should inspect the actual syllabus, worksheet families, instructor examples, annotation layer, solution layouts, feedback, and restrictions. It can then populate the course order and calculation tools from evidence. Presently there is no presumed module sequence, no invented sig-figure/conversion rule set, and no automatic import of unreviewed material.

## Privacy and reproduction

This remains a private master package because it carries the preserved earlier personal archives. The chemistry source has no established public reuse license; the Bioethics CC license does not cover it. Do not upload the whole room to GitHub Pages.

Build with `python scripts/build_chemistry.py` and `python scripts/build_room.py`. Tests require Python Playwright and Chromium; normal launching requires only Python 3.10+ standard library and a browser. The new code is under `30-modules/chem-1117-f2026/source/`.

Source record: Files `file_00000000613c81f78c65434922f809b5`, version 1; inspected page ranges 1–4 and 5–7. This identifier is provenance, not a downloadable original in this package.

Implementation references (not course content):
- https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage
- https://docs.python.org/3/library/http.server.html
