# Ms Luminara Periodic Table Workbench

## A design and content packet for Codex integration

Prepared 6 October 2026 for Natalie and LumiUniversityCodex.

The periodic table becomes a working surface for chemistry: select an element, inspect evidence, predict a relationship, manipulate a small model, explain a choice, then revise it. A learner can explore freely or ask Ms. Luminara for one purposeful next move. The table remains visible and useful throughout. The centerpiece is an interactive workbench, with authored practice supporting it rather than replacing it with a quiz catalogue.

This packet describes the experience, supplies chemistry reference/content contracts and 60 authored activity cases, and gives the integration owner a bounded implementation brief. It contains no application implementation. Nothing has been installed, admitted, migrated, or released in Luminara Campus. The existing campus repository was not inspected in this workspace.

## How to read the packet

1. Read [01_WORKBENCH_UX.md](01_WORKBENCH_UX.md), the experience design for the intended layout, direct manipulation, teaching voice, modes, and accessibility.
2. Read [03_CHEMISTRY_DATA_AND_VALIDATION.md](03_CHEMISTRY_DATA_AND_VALIDATION.md), the chemistry data and validation specification before mapping fields or designing a checker.
3. Read [02_LEARNING_PATHS.md](02_LEARNING_PATHS.md) and sample [activities.json](activities.json) as concrete workbench sessions. Each case needs an actionable response surface, staged assistance, correction, and transfer, not only a prompt and answer.
4. Give Codex the entire folder and begin with [04_CODEX_INTEGRATION_HANDOFF.md](04_CODEX_INTEGRATION_HANDOFF.md).
5. Use [05_ACCEPTANCE_TESTS.md](05_ACCEPTANCE_TESTS.md), [PROVENANCE.md](PROVENANCE.md), and [QA_STATUS.md](QA_STATUS.md) to separate reviewed packet content from future runtime evidence.

The final inventory and exact filenames are in [packet_manifest.json](packet_manifest.json). The coverage index is in [coverage_manifest.json](coverage_manifest.json).

## What the learner should be able to do

- Find any of the 118 elements by name, symbol, or atomic number and move through the table by keyboard or touch
- Use position, groups, periods, and selected property overlays to form and test a chemistry explanation
- Compare elements side by side, while keeping each property's definition, units, availability, and limitations visible
- Build a neutral atom or ion using proton and electron counts; see that changing electrons changes charge, while changing protons changes identity
- Distinguish an element symbol from a formula, a subscript from a charge, and a monatomic ion from an intact polyatomic ion
- Use configurations and periodic patterns at an explicitly stated level of detail; see exception and ambiguity notices rather than a falsely universal rule
- Save meaningful work through the existing Campus shared Save/journal flow, return to it, and explain a correction

These are target capabilities. Their presence in this packet does not mean they already exist in the application.

## A short first visit

Open the table and select sodium. Ask “What can I know from this square, and what would I need more information to know?” Compare sodium with chlorine. Keep atomic number, electron count, and typical introductory ion behavior separate. Build Na⁺ by removing one electron from a neutral sodium atom; build Cl⁻ by adding one to a neutral chlorine atom. Combine the ions as a neutral formula unit of NaCl. Return to the table and explain why a tile alone cannot represent the whole compound.

This route can be brief. There is no timer, streak penalty, forced completion of all cases, or claim that a single correct click demonstrates mastery.

## Full design and a practical first slice

The full candidate design supports an all-118 table, reference drawer, comparison, property lenses, atom/ion reasoning, configuration work, formula/species reasoning, mystery clues, and journal connections. The authors have supplied 60 concrete activity cases across the specified learning families. That is authored instructional coverage, not 60 elements and not exhaustive exercise coverage for every element or property.

An MVP candidate should keep the whole 118-element table navigable while limiting the first interactive teaching slice to element lookup, comparison, neutral-atom/ion counts, species notation, targeted hints, and the existing Save/journal flow. Advanced overlays and more complex configuration/clue modes can follow only after their data, pedagogy, and native support are verified. These are capability slices for owner selection, not dates, promised project milestones, or authorization to release.

## Teaching relationship

Ms. Luminara speaks clearly to an adult learner: ask for an observation, point to evidence, suggest one next check, and let the learner revise. Physics-style conservation and counting can help bridge the concepts without assuming chemistry vocabulary is already fluent. Optional real-world contexts should reinforce the chemistry rather than introduce medical advice or dosing exercises.

“Let’s give that number one job. Is it counting atoms, or telling us about charge?”

The proposed companion behavior is authored interaction design. This packet makes no claim that native Lumi has persistent memory, autonomous learning, or a new tutoring backend. Any retained learning evidence must use the real campus contracts and visible, authorized state.

## Boundaries to preserve

Keep existing question identities, drafts, notebook `luminara-chem1117-workbook-pilot-v1`, origin `127.0.0.1:47831`, shared Save/journal behavior, and prior Q13 scaffolds intact after verifying their actual current contracts. Active `0.2.0` and proposed `0.3.0` are supplied planning context; do not interpret the proposal as permission to migrate. The campus owner must inspect the current state.

JSON files are declared packet authoring contracts, examples, or reference data as individually labeled. They do not claim to be native campus APIs, admissions records, or runtime validation results. A future C++20 adapter and native validation path must be established by the integration owner.

An optional Ms. Luminara icon was delivered separately. This packet does not copy or relicense that binary. The owner may reuse the previously authorized asset if appropriate and available.

## Files at a glance

| File | Role |
|---|---|
| 01_WORKBENCH_UX.md | Detailed workbench interaction and accessibility design |
| interaction_contract.json | Proposed UI state/event and adapter semantics, not a native API |
| 02_LEARNING_PATHS.md | Six worked routes and activity-bank teaching guidance |
| activities.json | 60 learner-facing authored case records with staged assistance |
| answer_keys.json | Separate teacher/checker answers, explanations and grading notes |
| 03_CHEMISTRY_DATA_AND_VALIDATION.md | Scientific conventions, notation and validation requirements |
| reference_data.json | All-118 identity/layout reference plus explicitly limited deeper data |
| 04_CODEX_INTEGRATION_HANDOFF.md | Copy-ready bounded integration brief |
| 05_ACCEPTANCE_TESTS.md | 52 future table, chemistry, teaching and integration tests |
| PROVENANCE.md | Sources, originality, limitations and maintenance responsibilities |
| coverage_manifest.json | Exact authored/reference coverage |
| QA_STATUS.md and packet_structural_checks.json | Packet review status and actual local checks |
| packet_manifest.json and SHA256SUMS.txt | Final file inventory and integrity checks |
