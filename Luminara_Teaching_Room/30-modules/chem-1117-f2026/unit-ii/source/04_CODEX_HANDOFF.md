# Handoff to LumiUniversityCodex

## Copy-ready request

Please use this packet to implement the Chem. 1117 Unit II review teaching content in the existing Luminara teaching-room module. First inspect the current module, active release, schemas, question IDs, existing Q13 scaffold documentation, and persistence behavior. Report any mismatch before changing content bindings or release state. Preserve the existing notebook, routes, question identities, drafts, and save behavior. Reuse the existing six companion surfaces and campus adapters wherever they fit. Map source-sheet labels to verified existing question anchors; the packet’s labels are only candidate bindings until you inspect them. Keep explanations hidden behind staged hints/reveals. Do not automatically upgrade ModuleV2 or add a parallel notebook. Use the campus’s authoritative validation and normal release/rollback process. Show the implementation diff, verification evidence, remaining instructor decisions, and acceptance-test results before any release action beyond the user-authorized scope.

## Boundary and current evidence

The present deliverable is content only. No app code or campus file changes were made to produce it. The user's next step is to hand this packet to LumiUniversityCodex. This document is a work brief; it does not grant authority to change security settings, credentials, accounts, or any unrelated system.

Planning supplied the following target and contracts:

- Target module: `F:\Luminara_Campus\Luminara_Teaching_Room\30-modules\chem-1117-f2026`
- Existing data surfaces: `content.json`, `folder-content.json`, `questions.json`
- Existing adapters: `app.js`, `folder.js`, `questions.js`, `practice.js`, `factors.js`, `isotopes.js`, `template.html`
- Existing Q13 scaffold/source documents: `00_START_HERE`, `01_CODEX_HANDOFF`, `03_SESSION_AND_BRANCHING`, `04_FADING_AND_TRANSFER`, `05_FEEDBACK_AND_UI_CONTRACT`, `06_EXISTING_ID_BINDINGS`, `07_ACCEPTANCE_TESTS`, `09_SOURCES_DECISIONS_AND_QA`, and `PROVENANCE`
- Shared surfaces: `CampusQuestionFields.html` / `mount`; `feedback.set`, `label`, `focusFeedback`; `CampusStudyWorkspace.mount` / `setContext`; `CampusWork` / `apiwork`
- Existing notebook: `luminara-chem1117-workbook-pilot-v1`
- Existing origin: `127.0.0.1:47831`
- ModuleV2 planning baseline: active `0.2.0`; `0.3.0` is not an automatic migration target

These are supplied integration constraints, not a claim that this packet inspected those files or confirmed the currently running release. Current-release inspection was unverified/access denied in the preceding environment work. Existing question anchors were not inspected. Resolve those gaps through the authorized campus environment before editing or admission.

## Required inspection before implementation

1. Identify the current module root, ownership, editable authoring sources, active release, and version contracts
2. Read the existing Q13 scaffold/source documents and prefer their established semantics where this packet is merely descriptive
3. Inspect the real data schemas and adapter contracts. Do not insert the packet's JSON directly into a native schema
4. Match each worksheet label to an existing question ID, source anchor, lesson/folder route, and prior content. Produce an explicit mapping for review
5. Establish a baseline of existing working/drafts and notebook round-trip behavior without exporting private learner data into test fixtures
6. Identify the native validation, admission, release manager, root dispatcher, rollback procedure, and user-authorized execution boundary
7. If access remains denied, stop that dependent work and report the exact blocker. Do not bypass the restriction or claim successful inspection

## Binding and preservation contract

Worksheet labels such as Q7l and Q14f are pedagogical references, not verified campus IDs. Prefix supplemental items clearly so they cannot collide with source items. Verify all identifiers before choosing names or writing adapters. Keep source numbering and source-page association visible to the learner even when the native ID differs.

Do not overwrite established lesson content simply because a packet file shares a title. Reconcile deliberately with prior content. Preserve existing routes, IDs, user drafts, attempts, annotations, notebook content, and journal return context. Do not create a new notebook, dual-write path, migration, or alternate persistence endpoint. Reuse the notebook and APIs listed above only after confirming their current contract.

The six companion roles are two-check, symbol, whole-ion, Roman, prefix, and chemical context. Inspect and reuse their existing implementations. This packet does not authorize an additional competing companion system.

## Content rendering and grading

- Bind learner prompts, hints, explanations, transfer items, and checker notes as separate fields in the native supported schema
- Keep teacher/checker answers out of the default learner view; individual reveals are intentional
- Preserve full worked reasoning and every ion's internal identity, electron count, lone pair, charge, and domain distinction
- Definitions/drawings need concept checks or transparent self-assessment when reliable evaluation is unavailable
- Flag Q10, Q14 SO₃ conventions, the meaning of “orbital geometry,” and Q15 OsO₄ course preference for instructor alignment
- Accept equivalent notation and established synonyms without silently accepting a chemically different species
- Do not claim a model can interpret an arbitrary drawing unless that capability has actually been tested
- The coverage manifest and any content-bank JSON are content-only authoring aids, **not native admissions schemas**

## Validation and release guardrails

C++20 validation is authoritative for the campus pipeline. Discover and run the actual documented command; no command is invented here. Generated or sealed releases must not be edited directly. Use the native release manager and root dispatcher with the documented rollback path. Record the starting release and the result of any authorized release change.

Respect the development guard: one job at a time, at most two build workers, bounded logs. Do not launch parallel build/test jobs that violate the single-job limit. Native authoring validation must pass before admission; admission must pass before any authorized release action. Failed validation is a blocker to publication, not a reason to weaken the checks.

## Future acceptance tests

These are required future tests, not completed test results. Record setup, action, expected result, actual result, evidence, and pass/fail/block status for each.

| ID | Test | Expected result |
|---|---|---|
| A01 | Coverage | Every source Q1–16 task appears exactly once as a mapped source item; supplemental content is labeled; Q7/Q8 retain all 16 cells |
| A02 | Native validation and admission | Authoritative C++20 validation and native admission pass against the inspected schemas; no invented admissions record |
| A03 | Prior content regression | Existing lessons, Q13 scaffolds, routes, IDs, and journal navigation remain available |
| A04 | Attempts and hints | First attempt and revisions remain distinguishable; hints/reveals produce assisted status and never erase work |
| A05 | Feedback | Each error family yields a targeted next check; valid notation/synonyms are accepted; convention-sensitive items are not falsely rejected |
| A06 | Draft retention | Navigate among lesson, companion, hint, feedback, and practice; unsaved/retained state behaves exactly as the existing contract requires |
| A07 | Save/readback/reopen | Save a test entry to the existing notebook, read it back, close/reopen, and verify exact authorized persistence without duplicate writing |
| A08 | Stale conflict Cancel | Create a supported stale-edit conflict; choose Cancel; no local or remote work is silently overwritten and the user can recover their draft |
| A09 | Journal return | Return from a study item to the existing journal with correct context, retained draft, and stable item identity |
| A10 | Keyboard and narrow layout | All answer fields, companions, reveal controls, and feedback work without a pointer; meaningful labels/focus remain; formulas and tables fit narrow layouts |
| A11 | Lewis/geometry chemistry | Electron budgets, shared pairs, lone pairs, formal charges, resonance, and domain-vs-bond distinctions survive rendering |
| A12 | Release and rollback | If a release is authorized, verify native dispatcher activation and documented rollback; no direct sealed-release edit or implicit 0.3.0 upgrade |

Suggested focused content probes: N₂ remains an element in the supplemental classification; NH₄⁺ is an ion; (NH₄)₂CO₃ retains intact ions; Cu₃(PO₄)₂ names copper(II), not copper(III); negative charge adds to the NO₂⁻ electron budget; NO₂⁻ is bent with trigonal-planar electron geometry; CO₂ double bonds still give two domains; molecular formulas are not reduced; AlCl₃ is assessed in the stated monomer model.

## Completion report to the user

State what was implemented, where it appears, what was preserved, which tests passed/failed/were blocked, and what still needs instructor input. Distinguish authored content, local validation, native admission, active release, and runtime persistence verification. Do not claim deployment merely because files were produced or a content validator passed.
