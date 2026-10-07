---
document_id: LU-IONS-DESIGN-02
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# The learner, the method, and the boundaries

## The learning problem to solve

Natalie is not starting without algebra. She wants to reconstruct chemistry from a small set of meaningful relationships rather than memorize a flat list. Her present difficulty is deciding which part of a chemical name supplies identity, which supplies charge, and which must be retrieved as vocabulary. A correct answer accompanied by uncertainty is useful evidence, not an invitation to remove all scaffolding.

The design separates three jobs:

1. **Remember an identity:** nitrate means NO₃⁻, not an arbitrary collection of nitrogen and oxygen.
2. **Reason about a relationship:** given Al³⁺ and SO₄²⁻, derive a 2:3 ratio by balancing charge.
3. **Express it in a notation:** write Al₂(SO₄)₃ and say aluminum sulfate.

Do not diagnose a difficulty in one job as failure in all three.

## Teaching contract

Use the current Ms. Luminara Primer and central Adventure Doctrine, not a copied replacement. This packet is a study module, not automatically a canonical adventure. Small teaching scenes do not require a historical guest; a later full adventure does require the central guest research and continuity process. [SRC-DOCTRINE in the source ledger](15_SOURCES_AND_DECISIONS.md#src-doctrine)

Ms. Luminara speaks precisely and warmly. She begins with an observable mismatch, allows a prediction, reveals the mechanism, and pauses for a model revision. She never treats hesitation as stupidity. Natalie is the Notebook Learner: “Here is what I think this notation means.” Jeff may be the one to try the next move, not simply the person who panics. Two or three active characters are enough per teaching beat; every speaker is labeled.

Useful opening exchange:

> **Natalie:** “I think I keep trying to derive the word and the number at the same time.”
>
> **Ms. Luminara:** “Then we shall give them separate desks. The name identifies our passengers. Their charges determine the seating ratio.”
>
> **Henry:** “And the seating chart is not a molecular structure?”
>
> **Ms. Luminara:** “Correct. It is an ion-count ledger. We label the metaphor before it escapes.”

## Three visible explanation depths

- **Quick map:** the ion identity, the balance, and the conventional answer.
- **Walk beside me:** one worked example, one partially completed example, then a fresh attempt.
- **Under the Floorboards:** why the model works and where it stops working.

Let the learner open any depth voluntarily. Do not require a long derivation before every simple answer. “Show me the bridge” expands an explanation; “Let it breathe” removes timed prompts and allows a notebook pause. Neither changes the chemistry answer.

## Capture the reasoning without overwriting it

Provide two visibly distinct spaces: **My model** and **Conventional solution**. Preserve original notebook input separately from later corrections. A typed interpretation of handwriting is a proposal the learner confirms; it is not automatically a fact, a grade, or an exportable public note.

Feedback follows: notice what worked → identify one load-bearing seam → test it → translate the repaired idea back to chemistry. Example: “You kept sulfate intact. One Al³⁺ plus one sulfate still totals +1. Which counts could make the two charge totals equal?”

## Multiple modalities, not assigned learning styles

The same underlying ion/count model powers text, tiles, spoken names, handwriting, and equations. The point is to connect representations and practice retrieval, not to classify Natalie as a visual or kinesthetic learner. Spacing, worked-example/problem alternation, and connected verbal/concrete/abstract representations inform the design; the exact timing and thresholds here are proposed product settings, not established optimums. [SRC-IES](15_SOURCES_AND_DECISIONS.md#src-ies)

## Definition of success

A learner can retrieve or look up an ion, construct the least whole-number ratio, translate in both directions, detect a misleading suffix or Roman numeral, and explain one step. Later, she can repeat that on a different item without a revealed answer. Time spent, correct clicking, and a single repeated success are not substitutes for those observations.

## Hooks

`TEACH-01`: separate ion recall, balance, and notation feedback.  
`TEACH-02`: preserve raw notebook text and explicitly confirmed interpretation.  
`TEACH-03`: permit alternate valid arithmetic/equation methods.  
`TEACH-04`: offer non-scored exploration and optional retrieval; no lives, streak penalties, or locked exits.  
`TEACH-05`: collect optional confidence without using it as correctness.
