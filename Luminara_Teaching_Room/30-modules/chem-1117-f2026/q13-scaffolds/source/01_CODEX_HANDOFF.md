---
document_id: 01_CODEX_HANDOFF
package_id: LU-CHEM-Q13-SCAFFOLDS
version: 0.1.0
status: editorial_draft
created: 2026-09-28
visibility: editorial
integration_mode: additive_scaffold_overlay
assessment_owner: existing_native_exercises
---

# Codex implementation brief — attach help at the failed step

## The task

Integrate these six teaching scaffolds into the **existing Chemistry → Ion Language** experience. Attach them beside the current Q13 rows and the related native activities. Do not rebuild the university, recreate the ion table, or replace the source-owned answer bank.

The supplied inventory identifies the existing source locations as:

```text
30-modules/chem-1117-f2026/ion-language/source/ion-data.json
30-modules/chem-1117-f2026/source/questions.json
30-modules/chem-1117-f2026/source/content.json
30-modules/chem-1117-f2026/source/folder-content.json
```

These are **September 28 snapshot paths**, not verified current paths in this turn. Inspect the working checkout, its instructions, and its actual data loaders first. Prefer existing components and language choices. Do not introduce a new service, launcher, language runtime, or external model dependency merely for this feature.

## Phase 0 — inspect before modifying

Locate the live equivalents of:

- the Q13 `q13-naming` set and CR-301 through CR-342;
- the activity registry and the reading/scaffold presentation component;
- native answer evaluation and name/formula normalization;
- existing ion/compound identity records, especially PR-85, PR-96, PR-101, PR-104;
- L01–L06, the current story reader, and any existing Loom chapter associations;
- saved-answer storage, attempt tracking, hints/reveal state, and note export;
- formula rendering, mobile layout, keyboard navigation, and test commands;
- current Primer, Adventure Doctrine, and source/licensing boundaries.

Produce a short integration note listing **found, renamed, absent, and ambiguous** items. A missing anchor should disable only that link with an editorial warning, not justify inventing an assessment ID.

## Phase 1 — small working slice

Start with `q13-q-07` (potassium sulfate) and `q13-q-15` (carbon disulfide).

For CR-313: open Q13-SCF-03, preserve the entered formula, show K⁺ and SO₄²⁻ as reference identities, allow whole-ion counts to change, and return to the same native formula field without overwriting it.

For CR-330: when the native checker reports a wrong type but CR-329’s CS₂ is correct, show Q13-SCF-01. State that the formula is correct; help only with the type. No reset, no global “everything wrong,” and no formula correction inserted without action.

A single vertical slice must support keyboard-only use, narrow-screen reading, closing and reopening the help panel, and preserved entered work.

## Phase 2 — attach the other scaffolds

Use [the binding contract](06_EXISTING_ID_BINDINGS.md). Add scene, concise rule, guided representation, optional deeper layer, and return-to-exercise actions using the existing UI conventions.

Do not assign Q13-SCF IDs as new graded questions. They are content/assistance IDs. Existing CR IDs remain the owners of answers. New staged probes are ungraded self-checks unless a separately reviewed assessment migration authorizes otherwise.

## Phase 3 — diagnostic support, not mind reading

Use observable field results and explicit learner actions to offer a scaffold. Suggested help is not a diagnosis.

Examples:

- PBr₃ → “potassium bromide”: first ask what P means. Do not assume an ionic-bonding misconception before checking symbol identity.
- N₂O₅ → a four-oxygen name: ask for the oxygen count, then ask which prefix means five. A count-reading slip and a prefix-recall gap need different help.
- KSO₄: show reference ion charges and ask for net charge. Do not claim the learner forgot sulfate if SO₄ is already present.
- Correct BF₃ + “ionic”: retain the correct formula and focus the return on classification.

Use transparent hint levels: orientation, representation, one worked step, full walkthrough. Record a reveal only through the existing help mechanism. Opening help is not a failed attempt; reading a solution is not unaided mastery.

## Phase 4 — conventional wording versus chemical identity

Keep these outcomes distinct:

1. incorrect chemical identity or atom count;
2. chemically recognized identity but not the requested naming convention;
3. accepted conventional spelling/name;
4. instructor alias policy not yet confirmed.

In particular, `boron hydride` occurs as a synonym for diborane in authoritative chemical records. For a count-prefix exercise, teach **diboron hexahydride**, and show **diborane** as the common name. Do not call the broad synonym chemically nonexistent. Do not silently change native grading or promise that a particular instructor will accept every synonym. Flag the gap for content-owner review. See S-DIBORANE in the source register.

Likewise, contracted classroom forms such as pentoxide/tetroxide must not become an unreviewed global spelling algorithm. Resolve the configured naming mode and alias policy.

## Phase 5 — regression, privacy, and delivery

Use [acceptance tests](07_ACCEPTANCE_TESTS.md). Run current repo tests plus focused coverage for:

- separate name/formula and type feedback;
- positive whole-ion integer ratios;
- grouping versus total atom inventory;
- Roman numerals per metal ion;
- symbol case and molecular subscript preservation;
- the boundary cases that simple heuristics mishandle;
- state retention on all scaffold interactions;
- no annotated worksheet or private evidence in public output.

Do not infer enrollment, intelligence, mood, or long-term misconception status from a wrong response. Do not populate saved answers from this packet or import the handwritten worksheet as app attempts.

## Placement and publication

Store authored scaffold content in the current content system. Use an attachment map in the existing extension mechanism; if no such mechanism exists, propose a small versioned adapter rather than a parallel data architecture. The public page is topic-first, without course codes in the visible title. Backstage source IDs remain intact.

The private evidence file must remain outside deployable/public roots. Public examples are anonymous pedagogical cases. The packet authorizes preparing a reviewed implementation, not pushing a live site, changing a grade, modifying central doctrine, or canonizing a new adventure.

## Deliver back

Report changed paths, reused components, final resolved attachments, before/after tests, desktop and phone checks, keyboard checks, note/answer persistence checks, source gaps, and any unimplemented items. Identify what was actually executed versus only inspected.

## Copy/paste launch instruction

> Read this packet’s START_HERE and CODEX_HANDOFF, inspect the current Lumi University workspace, and attach the six Q13 scaffolds through the existing reading/help system. Implement the CR-313 whole-ion and CR-330 type-only vertical slice first. Preserve native questions, answers, progress, private notes, and all existing IDs. Use the binding map as a snapshot to resolve, not a new question bank. Keep the private evidence map out of public output. Run the acceptance tests and report actual results; stop before live publication or canonization.
