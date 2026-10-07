# Codex integration handoff — attach a story, do not rebuild the course

## Requested result

Integrate `ADV-CHEM-LOOM-001` as a connected Ms. Luminara narrative beside the existing chemistry activities. This packet supplies authored teaching content, not permission to replace the assessment engine, re-key answers, migrate private journals, or deploy publicly.

## Read order

1. `00_START_HERE.md`.
2. The current repository's Ms. Luminara Primer and central Adventure Doctrine. This packet does not supply replacement copies.
3. `01_THE_ADVENTURE.md`.
4. `02_SOURCE_AND_ACTIVITY_MAP.md` and `04_SOURCES_LIMITS_AND_REVIEW.md`.
5. The current workspace entry points, story/readings components, movable study windows, and native exercise-opening APIs.

## Inspect before changing paths

The supplied September 28 question index identifies these installed content locations:

```text
30-modules/chem-1117-f2026/ion-language/source/ion-data.json
30-modules/chem-1117-f2026/source/questions.json
30-modules/chem-1117-f2026/source/content.json
30-modules/chem-1117-f2026/source/folder-content.json
```

These are **snapshot paths**, not a newly verified checkout or a requested replacement tree. Find their current workspace equivalents. Record any differences in the integration report. Do not invent a URL query protocol such as `?question=...` unless the current app actually supports it.

## Content contract

- Keep one canonical editable story body, with stable anchors `scene-00` through `scene-15`.
- Preserve `ADV-CHEM-LOOM-001` and its draft status unless the owner deliberately changes them.
- Store source/workbook relationships backstage. Public titles remain topic-first; do not expose course numbers as the story's identity.
- Add chapter navigation, a pause/resume affordance if already supported, and links to relevant native exercise/reference windows.
- Use the supplied scene map to resolve existing L/WE/PR/CR/source IDs. Exact item IDs remain the assessment system's IDs; do not manufacture a second set of questions.
- Where native APIs cannot open a field directly, link its existing parent activity and show the field name. Document this downgrade rather than guessing a deep link.
- An activity-set link is conceptual coverage, not a claim the narrative supplies every answer in that set.

Illustrative adapter intent, **not an existing runtime schema**:

```json
{
  "storyId": "ADV-CHEM-LOOM-001",
  "anchor": "scene-07",
  "inventoryTopics": ["MAT-08", "MAT-06", "MAT-14"],
  "existingActivity": "course-ions",
  "existingFields": ["CR-053", "CR-054"],
  "assessmentOwner": "existing_native_activity",
  "onRead": "no_grade_or_mastery_change"
}
```

## First integration slice

Start with Chapter 7 alongside ammonium formula/charge fields CR-053 and CR-054. Keep the periodic reference and Chapter 6 Lewis comparison reachable beside it. The reader must see the **reason**—eleven protons and ten electrons after proton transfer—not just an expected-charge comparison.

Then attach Chapters 9, 11, and 12 beside formula construction and mixed naming. Finally add the broad-foundation and laboratory chapters. This is a delivery sequence, not permission to discard the remaining manuscript.

## Required presentation behavior

- Preserve explicit speaker names, paragraph breaks, and quiet reflection. Do not collapse the prose into cards that reveal only definitions.
- Keep each worked ledger close to the reasoning that motivates it.
- All formulas must display subscripts/superscripts semantically; plain data strings and signed ion charges remain distinct fields in the application.
- Never normalize CO into Co, NO3^- into NO3, or Na2O2 into NaO.
- Provide keyboard-accessible tables/sections, sensible heading order, visible focus, readable contrast, scalable text, and reduced-motion support. No auto-start audio.
- Keep the charge explanation in the main story, not locked behind a deep panel. Formal-charge and broader bonding qualifications may be expandable, but the basic causal bridge must remain present.
- A read-aloud mode must speak speaker names as needed and distinguish “subscript four” from “charge plus one”; use the existing speech layer or leave it unimplemented, not a fictitious enabled button.
- `READER.html` is an offline review artifact. Reuse the university's reader/design components for production. Do not deploy an unrelated site shell or launcher.

## Evidence and assessment safeguards

- No new quiz bank. Do not duplicate 342 fields already counted within the 414-entry practice collection.
- Do not copy reviewed answers out of this prose into the native key as an automatic update.
- Do not auto-grade freehand drawings or infer understanding from arbitrary prose without an explicitly supported human-review design.
- Do not overwrite saved answers, histories, handwritten notes, journals, or photographs. Reading a chapter cannot change an existing score or mark an exercise mastered.
- Fictional Natalie dialogue is not a learner answer record. Never persist it as one.
- Unresolved NO^- source material stays unresolved and unscored.
- B/C/Ge universal monatomic-charge questions stay reference-only.
- Course-specific phosphite/carbide/silicate labels remain qualified; no universal charge derivation is added.
- Keep given P2O5/P2O3 naming tasks while preserving the formula-versus-actual-structure qualification.
- No unperformed experiment becomes an observation. The polymer story supplies no bounce-height answers or lab-completion attestations.
- LiH is a targeted supplemental example, not a newly discovered assignment row.

## Acceptance checks for the installed result

| Check | Observable result |
|---|---|
| Story integrity | All sixteen anchors resolve; all fourteen teaching chapters and the opening/return are available |
| Immediate need | Ammonium field links open Chapter 7 without losing the current exercise |
| Ammonium ledger | NH3 10p/10e; H+ 1p/0e; NH4+ 11p/10e; valence counts remain separately eight |
| Whole-ion display | 2 NO3^- shows two N, six O, total charge -2, each ion still -1 |
| Peroxide | The prose and any native links preserve Na2O2/O2^2-, not reduced NaO |
| Naming boundary | NH4Cl uses ionic naming while its N–H bonds remain covalent internally |
| Molecular preservation | N2O4 is not simplified to NO2 |
| No guessing | “copper chloride” and the simple Fe3O4 average do not receive an invented unique/rounded cation answer |
| Qualified sources | NO^- and instructor spelling/list gates remain visible |
| Private state | Before/after saved-answer export is unchanged by story integration |
| Accessibility | Keyboard and zoom testing pass; dialogue attribution is not color-only |
| Mobile/offline | Existing supported reading behavior remains usable at iPad/phone widths; no hidden remote dependency is added |
| Idempotence | Re-running attachment integration does not duplicate story entries or links |
| Deployment boundary | Local preview and validation report returned; no unsolicited public deployment or canon promotion |

The package QA proves only the checks named in `QA_REPORT.json`. These application acceptance checks remain work to execute and report; they are not pre-certified by the manuscript.

## Final report expected from Codex

Return changed paths, resolved attachment APIs/IDs, screenshots or verified preview routes, tests actually run, remaining source/editorial gates, and confirmation that prior progress was preserved. Ask Natalie for the separate release/canon decision rather than assuming it.
