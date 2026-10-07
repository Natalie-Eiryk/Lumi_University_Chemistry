# Codex Integration Handoff

## Copy ready brief

Use this design/content packet to plan and, only within my separately authorized implementation scope, integrate a periodic-table workbench into the existing Chem. 1117 teaching room. First inspect the actual repository, Q13 scaffolds, chemistry domain API, active release, native schemas, and shared UI/persistence contracts. Show a small mapping and capability plan before changing bindings. Preserve existing IDs, routes, notebook, drafts, and journal behavior. Treat this packet's JSON as a declared authoring contract to map deliberately, not a native API. Build no parallel grader or data store. Use authoritative native C++20 validation, admission, release management, and rollback. Record blocked assumptions and test evidence honestly. Do not migrate to ModuleV2 0.3.0 or release merely because the packet discusses them.

## Target and verification boundary

Supplied target: `F:\Luminara_Campus\Luminara_Teaching_Room\30-modules\chem-1117-f2026`.

The authoring workspace had no inspection of that target. The following names are supplied integration context, not verified signatures or proof of present availability:

- Existing authoring surfaces `content.json`, `folder-content.json`, `questions.json`
- Existing adapters `app.js`, `folder.js`, `questions.js`, `practice.js`, `factors.js`, `isotopes.js`, `template.html`
- Existing Q13 scaffold documents covering session/branching, fading/transfer, feedback/UI, existing ID bindings, acceptance, sources/QA, and provenance
- Chem ion-domain/API and existing chemistry validation services
- `CampusQuestionFields.html` / `mount`; feedback `set`, `label`, `focusFeedback`
- `CampusStudyWorkspace.mount` / `setContext`; `CampusWork` / `apiwork`; shared Save and journal
- Notebook `luminara-chem1117-workbook-pilot-v1`, origin `127.0.0.1:47831`
- Planning baseline active `0.2.0`; `0.3.0` is a proposal only

If any name differs from the current repository, report the difference and use the established native contract. Do not create a same-named replacement to satisfy this brief. If access is denied, pause dependent work and report the exact blocker without using another path to evade it.

## Inspection and mapping deliverable

Before implementation, provide a concise record of the verified module root and authoring entry points, active version, existing question/source anchors, Q13 conventions, chemistry domain responsibilities, field and feedback contracts, study workspace/journal navigation, Save semantics, and native validation/admission commands. Include the owner's supported development and release boundary.

Map each packet activity ID to a proposed native destination without overwriting an existing item. Packet IDs are candidate supplemental authoring identities, not established question IDs. Where content extends existing source-sheet work, retain the old identity and visible source association rather than replacing it with a new packet ID. Resolve collisions explicitly.

Produce a field map from every consumed packet field to a real native field, derived value, display-only field, or intentionally unsupported field. Unsupported data must not silently disappear. Explain where reference values originate, how provenance remains accessible, how unavailable values render, and how source updates would be reviewed.

## Architecture responsibilities

The table is the persistent learning surface. Selection, comparison, lenses, manipulatives, and activity context should cooperate rather than each creating a separate activity application. Reuse existing Q13 session/scaffolding and six companion roles where they apply: two-check, symbol, whole-ion, Roman, prefix, and chemical context. Names and mechanics must be verified in the repository.

Use the existing Chem ion-domain/API as the authoritative boundary for chemistry evaluation wherever it already supports the required rules. Extend that domain through the owner's normal process if authorized; do not introduce a second JavaScript grader that can disagree with C++ validation. Presentation code may normalize supported input and render state, but correctness must follow the documented native domain contract. Reference lookup is not by itself a chemistry grader.

Use `CampusQuestionFields` for native response entry when suitable, shared feedback for targeted correction and focus, `CampusStudyWorkspace` for study context, and `CampusWork`/`apiwork` for the existing Save/journal flow. Confirm signatures before calling them. Packet examples do not establish these signatures.

No alternate notebook, localStorage answer store, duplicate save endpoint, dual-write journal, silent migration, replacement question system, or telemetry backend is part of this brief. Temporary UI state must follow the existing draft and privacy contracts.

## Concrete C++20 validation expectations

The owner must locate and run the actual documented C++20 validator. This packet intentionally supplies no guessed command, header name, class signature, ABI, or admissions schema. The data specification defines the packet JSON boundary; a proposed adapter should parse it explicitly and validate before producing native authoring records.

Required validation responsibilities are concrete: reject malformed or unknown required fields; enforce supported schema version; ensure stable unique record IDs; check atomic numbers and element symbols against the full reference; verify count, charge, formula, and accepted-answer invariants under stated models; reject dangling activity/data references; identify missing provenance; distinguish unavailable data from numeric zero; and reject invalid hint or transfer references. Unsupported chemistry cases must return a transparent unsupported/needs-review result, never guessed correctness.

Keep schema errors, scientific inconsistency, notation ambiguity, missing source/convention, learner misconception, and runtime/persistence failure separate. Content-import rejection is not learner feedback. Native acceptance of a transformed record and educational correctness of its contents require separate evidence.

## Capability slices for owner selection

### First candidate slice

All 118 tiles and accessible list/search; element detail with honest unavailable fields; up to two-element comparison; neutral atom and ion electron ledger; species notation and common-ion/formula reasoning; staged hints and revision; existing Save and journal return. Admit only fields and cases supported by verified native contracts.

### Expanded candidate workbench

Add validated property lenses, broader comparisons, carefully modeled configurations, mystery clues with ambiguity handling, and richer activity routes as their data and native support pass acceptance. Advanced candidate modes must not hold basic table lookup hostage. The activity bank is reusable content, not a promise that all modes ship together.

### Later optional enrichment

Consider richer visual representations or instructor-curated extensions only after confirming accessibility, data provenance, chemistry validity, and current user authorization. Do not infer an autonomous adaptive learner model, external AI dependency, new analytics, or persistent Lumi memory from this proposal.

These slices express scope choices, not a calendar, project milestones, or release authorization.

## Persistence and conflict behavior

Observe the current Save state machine before changing UI: clean, dirty, saving, saved, error, stale conflict, and cancellation may have existing names and semantics. Preserve the real behavior rather than implementing guessed equivalents. Keep first attempt, revision, hints/reveals, and learner reflection distinct only to the extent the current supported schema permits; propose unsupported additions for review.

Test a safe test entry in the existing notebook, read it back, reopen it, and verify stable activity/context binding. Verify supported stale-edit Cancel does not overwrite remote state or lose the local draft. Verify journal return restores the appropriate work context. Do not use real private learner work as packaged test data.

## Release and completion boundaries

Use native admission and the existing release manager/root dispatcher. Never edit generated/sealed releases directly. Respect the supplied development guard: one job at a time, no more than two build workers, bounded logs; verify current owner rules before executing. Do not launch parallel build jobs.

Before an authorized release, record baseline and rollback procedure. If release is outside authorization, stop at reviewable implementation and tests. Report separately: packet mapped, application changed, local/native validation passed, admission passed, runtime tests passed, release activated, and rollback verified. A content packet review proves none of the latter automatically.

Completion should include the diff, field/ID mapping, source/convention decisions, actual acceptance results, remaining limitations, preserved baseline evidence, and any separate release decision needed.

## Optional future teacher animation anchors

A later design may add an animated HD-pixel Ms. Luminara who walks in eight directions and points to workbench evidence. No sprite, animation system, operating-system autonomy, or native Lumi capability is implemented by this packet. This idea does not enlarge the current implementation or release authorization.

If inexpensive during ordinary layout work, reserve logical anchor names that a future presentation adapter could resolve: `element-cell:<atomic_number>` for the 118 elements; `charge-control`; `formula-tray`; and `hint-region`. These are proposed semantic anchor identifiers, not verified DOM IDs or native APIs. The owner should map them to existing stable controls without renaming existing identities. A future pointing request must resolve the anchor's current visible bounds and return unavailable when absent, collapsed, scrolled out of view, or unsupported. Do not guess screen coordinates or trigger an action merely because a character points.

Any future character must avoid obscuring controls, formula glyphs, feedback or keyboard focus; remain pointer-transparent when decorative; respect reduced motion with a static/hidden alternative; and be optional. Teaching guidance should also exist as readable text. Requests for LumiOS actions would need a separate capability and authorization review; animation never confers system access or autonomy.
