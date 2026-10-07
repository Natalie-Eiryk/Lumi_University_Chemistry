---
document_id: 00_START_HERE
package_id: LU-CHEM-Q13-SCAFFOLDS
version: 0.1.0
status: editorial_draft
created: 2026-09-28
visibility: editorial
integration_mode: additive_scaffold_overlay
assessment_owner: existing_native_exercises
---

# Ms. Luminara — Naming With the Right Questions

## What this packet adds

Six focused teaching scaffolds built from the recent Q13 nomenclature submission. These are **teaching companions to existing exercises**, not a replacement quiz, a new ion bank, or a new scoring system.

The central teaching move is:

> Read the symbols. Choose the naming model. Do that model’s bookkeeping. Check the requested fields separately.

A correct formula paired with the wrong compound-type label is not the same result as a wrong formula. An omitted Roman numeral is not evidence that every step of the calculation failed. The interface should preserve what worked and help with the smallest unresolved step.

The manuscript is an additive companion to the Chemical Language design v1.1.0 and the supplied September 28 content inventory. It does **not** declare a new central doctrine version. The current installed Primer, Adventure Doctrine, reference bank, and native checks remain authoritative. Resolve their current paths in the actual workspace before coding.

## Read in this order

1. [Codex implementation brief](01_CODEX_HANDOFF.md) — integration boundaries, milestones, and completion report.
2. [Session and branching](03_SESSION_AND_BRANCHING.md) — the learner’s route, including a short version.
3. [Existing-ID bindings](06_EXISTING_ID_BINDINGS.md) — exact Q13/CR attachments and related exercises.
4. The six scenes below — reusable story, explanation, guided practice, and feedback.
5. [Feedback and interface contract](05_FEEDBACK_AND_UI_CONTRACT.md) and [acceptance tests](07_ACCEPTANCE_TESTS.md).

## The six scaffolds

| ID | Learner-facing title | The question it repairs |
|---|---|---|
| Q13-SCF-01 | [Two checks, one answer](scaffolds/Q13-SCF-01_TWO_CHECKS.md) | Is the type label being checked separately from the name or formula? |
| Q13-SCF-02 | [Read the badge before naming the passenger](scaffolds/Q13-SCF-02_SYMBOLS.md) | Does P mean phosphorus or potassium? What do capitalization and subscripts do? |
| Q13-SCF-03 | [More passengers, not different passengers](scaffolds/Q13-SCF-03_WHOLE_IONS.md) | How many complete ions make a neutral ratio? |
| Q13-SCF-04 | [The Roman numeral belongs to one ion](scaffolds/Q13-SCF-04_ROMAN_NUMERALS.md) | Which charge must be named, even in a one-to-one formula? |
| Q13-SCF-05 | [Count before you pronounce](scaffolds/Q13-SCF-05_PREFIXES.md) | Which atom count does each molecular prefix encode? |
| Q13-SCF-06 | [Same word, different chemical context](scaffolds/Q13-SCF-06_BOUNDARIES.md) | Why do hydride, peroxide, and a metalloid resist one-word classification rules? |

Each contains an actual Ms. Luminara teaching scene, not merely a promise to add one. Speaker names are explicit. Natalie remains a learner with a notebook. Other students notice, hypothesize, revise, and occasionally panic. No historical guest is introduced: these are short bench scenes, not a new full time-travel adventure.

## The high-value pattern

The worksheet includes correct molecular names/formulas paired with ionic labels, and correct ionic constructions beside other constructions with too few whole ions. This suggests a useful **transfer opportunity**, not a diagnosis of a permanent deficit. We can put the successful and unfinished cases beside each other and ask what transfers.

Detailed personal observations live only in [the private evidence map](private/02_EVIDENCE_MAP.md). Public teaching must not announce a learner’s mistake history. Fictional Natalie’s dialogue in the scenes is newly authored, not a verbatim transcript of private journal content.

## What remains owned elsewhere

- Ion identities and canonical names: existing reference records.
- Worksheet prompts and correctness decisions: existing CR/PR/native engines.
- Saved responses and confidence: existing private progress storage.
- Canon/publication approval: existing Lumi workflow and Natalie.
- Full instructor spelling/alias rules: still an open source gate where the inventory says so.

## Package scope and status

This is a Markdown implementation scaffold, not installed code. JSON blocks are proposed attachment contracts and QA fixtures, not claims about an existing API. The final document records checks actually run on this packet. The application tests are specifications for Codex, not already-passing browser tests.

Source foundation: [S-Q13, S-INDEX, S-MATERIALS](09_SOURCES_DECISIONS_AND_QA.md). No worksheet PDF, original photo, or saved journal is redistributed.
