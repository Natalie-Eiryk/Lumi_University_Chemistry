---
document_id: LU-IONS-L06
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Translate both ways, explain a seam, and carry it forward

[Session map](../05_SESSION_AND_SKILL_GRAPH.md) · [Rules](../03_CHEMISTRY_RULES_AND_BOUNDARIES.md) · [Answer key](../09_ANSWER_KEY.md)

**Lesson ID:** L06  
**Skills:** SK-08, SK-09, SK-10  
**Planning duration:** 9 plus 3-minute exit minutes  
**Prerequisites:** Any earlier lesson; use the reference if desired.

## Model change

Before: Success on a familiar example may depend on recognizing the displayed answer.

After: The learner can construct and inspect a translation on a new example, identify missing information, and know which anchor needs review.


## The transfer round

Choose six items: two name→formula, two formula→name, one identity contrast, and one scope/ambiguity item. Avoid simply reversing the item shown a moment ago and counting it as fresh evidence. Change the cation or family while preserving the target skill.

Suggested round: PR-23, PR-34, PR-45, PR-50, PR-62, PR-66. The [bank](../08_PRACTICE_BANK.md) defines prompts; the [key](../09_ANSWER_KEY.md) defines approved interpretations.

## What the learner does

For each item, permit a final answer immediately. Offer optional expandable steps: identify ions → show charges → choose counts → write conventional form → name. Do not force an expert through every intermediate box. When an answer is wrong, expose the earliest supported mismatch rather than requiring the learner to restart a correct section.

After a correct but uncertain response, show a brief contrasting example and ask what is different. After a high-confidence error, show the charge or atom inventory as evidence, not a chastising message.

## Narrative integration without a penalty mechanism

> **Carlos:** “Can I call Fe₂O₃ iron(II) oxide? There are two irons.”
>
> **Natalie:** “That counts the passengers. The numeral labels each passenger’s charge. Three oxides need +6 in total.”
>
> **Jeff:** “Two irons sharing +6: +3 each. The ledger settles it.”
>
> **Ms. Luminara:** “There is the translation. No one needed to appeal to the driver’s authority.”

The story demonstration is unscored. Independent retrieval is a separate chosen mode. No student or learner is punished, trapped, or humiliated for a wrong answer.

## Exit artifact

Create a private three-line field note:

- A rule I can rebuild: ______.
- An identity I still need to retrieve: ______.
- A distinction that helped: ______.

Offer a review queue based on actual attempts, not guessed learner traits. Export the field note only with explicit selection; the public lesson does not contain Natalie’s private responses.

## Codex hook

`buildReviewQueue` combines skill evidence with ion-level direction-specific recall. A final response does not count as unaided if the answer was revealed earlier in that item. Do not mark an item mastered because it was answered correctly immediately after reading its solution. Provide a later-session status and a manual “still shaky” override.


## Acceptance evidence

The lesson must render as readable content without JavaScript. The interactive version must implement its named hook, a non-drag/non-audio fallback, a hint ladder, and one independent transfer opportunity. Preserve raw notes; do not claim software can verify arbitrary free-text reasoning. Source and scientific limits follow [03](../03_CHEMISTRY_RULES_AND_BOUNDARIES.md); the lesson scripts are original design examples, not historical quotations.
