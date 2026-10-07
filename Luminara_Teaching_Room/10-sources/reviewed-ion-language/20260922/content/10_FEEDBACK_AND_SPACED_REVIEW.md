---
document_id: LU-IONS-DESIGN-10
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Feedback, diagnosis, and revisiting what matters

## Three questions before giving feedback

What can the response actually establish? Which earlier steps were correct? What is the smallest next question that distinguishes possible explanations?

An incorrect formula can have several causes. Do not infer an internal misconception solely from an answer string when more than one explanation fits. Report the observable mismatch and ask a short diagnostic follow-up.

## Diagnostic catalog

| Code | Observable evidence | Response / next move |
|---|---|---|
| D-PARSE-SYNTAX | unclosed parentheses or invalid count | show the location; ask for a syntax repair before judging chemistry |
| D-PARSE-CASE | `CO` versus `Co`, `ca` versus `Ca` | identify case ambiguity; do not silently recase |
| D-UNKNOWN-ION | no reviewed ion-name match | reference needed; not a chemistry mistake by itself |
| D-AMBIGUOUS-NAME | variable metal with no specified/inferable state | ask which oxidation state was intended |
| D-UNSUPPORTED-MODEL | mixed valence, complex, or unsupported grammar | explain the scope boundary; no fabricated answer |
| D-SCOPE-ROUTING | molecular/acid/hydrate case in simple-salt translator | route to the right extension |
| D-SCOPE-NEUTRALITY | demands zero charge for an isolated ion | distinguish ion from neutral compound |
| D-NOTATION-CONFLATION | oxygen subscript read as charge | identify the referent of each number |
| D-ION-IDENTITY | nitrate selected for nitrite, ammonia for ammonium | compare the two complete identities |
| D-ION-CHARGE | correct formula/name, wrong net charge | keep identity success; retrieve the charge anchor |
| D-CHARGE-TOTAL | right ions, counts do not balance | show signed subtotals for the learner’s counts |
| D-ROMAN-COUNT | metal count substituted for metal charge | total anion charge → divide by cation count |
| D-GROUP-COUNT | outer multiplier applied to only one inner element | open the group tree and count copies |
| D-GROUP-LOST | matching atom inventory without conventional grouping | acknowledge composition; request grouped representation |
| D-ION-MUTATED | internal ion subscript changed to balance | restore ion identity, then change copies |
| D-RATIO-NOT-MINIMAL | correct ions and neutrality, reducible ion counts | divide whole-ion counts by common factor |
| D-FAMILY-SUFFIX | wrong sibling selected | compare O counts within that named family |
| D-FAMILY-OVERGENERALIZED | suffix treated as universal formula rule | show a counterexample from a different family |
| D-SPELLING | unambiguous nonchemical spelling slip | show conventional spelling; separate from chemistry outcome |

## Outcome separation

A result records identity, charge, ratio, grouping, name, and syntax components where assessable. Example CaN₂O₆ for calcium nitrate: atom inventory matches; grouping needs a notation repair. Avoid both extremes: do not label all of it correct for a grouping task, and do not deny its correct composition.

Possible top-level outcomes: `correct`, `correct_with_notation_note`, `needs_revision`, `needs_clarification`, `unsupported`, `unassessed`. The item contract determines whether a representation repair prevents a completed conventional-form task. It never erases correct intermediate reasoning.

## Feedback examples

**Submitted AlSO₄:** “You selected aluminum and sulfate correctly. With one of each, +3−2 leaves +1. How many complete sulfate groups and aluminum ions would balance?”

**Submitted iron(II) oxide for Fe₂O₃:** “You identified oxide. The 2 counts iron ions; three oxides total −6. What charge must each of those two irons have?”

**Submitted sodium nitrite for NaNO₃:** “The sodium portion is right. Compare the nitrogen-family anchors: nitrate has three oxygens, nitrite has two.”

**Submitted NaO for sodium peroxide:** “Your reduction changed the peroxide group. Keep O₂²⁻ as one ion and balance sodium ions around it.”

**Unclear handwriting:** “I read your formula as Ca(NO₃)₃. Is that the subscript you intended?” No error diagnosis until confirmation.

## Hint and reveal behavior

A reference look is assistance, not misconduct. Store assistance honestly. Provide H1 a targeted question; H2 relevant ion cards; H3 charge ledger with a gap; H4 full solution. One click advances at most one step unless Reveal was explicitly selected. Resetting an item does not erase prior exposure from that item’s independence classification.

## Proposed spaced-review policy

This is an adjustable baseline, not a medical or cognitive prescription. On an independent correct response, offer a new variant after a delay rather than repeat the identical item immediately. Default later reviews: about 1, 3, 7, and 14 days. On a miss, teach the seam, practice one supported contrast, then revisit independently after other items or in the next session. Do not schedule an endless same-session punishment loop.

The evidence supports spacing and retrieval generally, not these exact intervals. [SRC-IES](15_SOURCES_AND_DECISIONS.md#src-ies)

## Scheduling logic to implement

- Separate ion-recall direction from formula-construction skill.
- An assisted completion updates practice history, not independent-success count.
- A notation-only issue strengthens the relevant representation review; it should not reset every mastered ion.
- Two similar misses trigger a different representation or a reference, not more identical prompts.
- Favor overdue items, shaky anchors, and underrepresented skills; keep some retained items in the mix.
- Prevent adjacent inverse duplicates from being counted as independent generalization.
- Do not erase an item permanently after a streak.
- Let the learner pin an item as shaky even after success.
- Default session queue cap: eight items, adjustable. No automatic notification permission requests.

Suggested descriptive threshold: three independent successes on at least two distinct examples, including a later-session success, can support `retained_in_observed_tasks`. It is not proof of global mastery. Track direction separately and make threshold settings visible.

## Confidence and privacy

Confidence is optional. `null` means not supplied; never reinterpret it as 0% or 50%. High confidence + error calls for a discriminating counterexample, not a reprimand. Low confidence + success calls for a short explanation or a fresh transfer opportunity.

Only explicit responses and minimal events are recorded. No hidden emotion scoring, microphone recording, fine-grained keystroke tracking, or cross-course personality inference.
