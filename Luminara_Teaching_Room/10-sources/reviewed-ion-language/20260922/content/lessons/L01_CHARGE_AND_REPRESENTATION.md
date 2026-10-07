---
document_id: LU-IONS-L01
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# The charge ledger: three different numbers

[Session map](../05_SESSION_AND_SKILL_GRAPH.md) · [Rules](../03_CHEMISTRY_RULES_AND_BOUNDARIES.md) · [Answer key](../09_ANSWER_KEY.md)

**Lesson ID:** L01  
**Skills:** SK-01, SK-09  
**Planning duration:** 7 minutes  
**Prerequisites:** None; a periodic table and ion card may remain visible.

## Model change

Before: A superscript, a subscript, and a coefficient all feel like numbers attached to symbols.

After: Each number has a different referent: atoms inside a group, charge of a group, or number of groups.


## Situated opening

> **Ms. Luminara:** “One nitrate ion has arrived. The three is its oxygen inventory. The minus sign is its net charge. They have been filling out different forms.”
>
> **Natalie:** “So I cannot read the three as three charges.”
>
> **Henry:** “And putting three nitrates on the ledger means three complete copies.”

Show NO₃⁻, then three identical nitrate tiles. Under the tiles show N = 3, O = 9, total charge = −3. The tiles represent complete ions; a negative icon does not belong separately to each oxygen.

## Teaching sequence

1. Label the subscript 3 and superscript −1 with words before colors. Ask what each describes.
2. Add a second nitrate tile. Keep the individual tile formula unchanged; update group count to 2 and total charge to −2.
3. Place Ca²⁺ beside one Cl⁻. Show `+2 + (−1) = +1` immediately as a ledger, not as a failed experiment.
4. Add the second chloride. Show `+2 + 2(−1) = 0`, then CaCl₂.
5. Return to one NO₃⁻ tile. Explain why that ion is permitted to have nonzero charge even though a neutral compound formula is not.

## Representation links

Spoken: “two chloride ions for one calcium ion.” Written: CaCl₂. Algebra: `1(+2)+2(−1)=0`. Tiles: one +2 card and two −1 cards. Tap each representation and highlight the corresponding whole group in the others, without making color the only cue.

## Fading practice

Worked: CaCl₂. Completion: Na⁺ with O²⁻, where one sodium is already on the ledger. Independent: Mg²⁺ with Cl⁻. Do not reveal final subscripts while asking the learner to retrieve them.

## Misconception catch

If Natalie says “everything has to add to zero,” show NO₃⁻ alone next to neutral NaNO₃. Ask which object the neutrality condition describes. Repair the scope, not the arithmetic. Use `D-SCOPE-NEUTRALITY`.

## Under the Floorboards

Show `q/e = Z − N_e` only for a monatomic ion. Polyatomic net charge is the charge on the group, not simply a count of visible oxygen atoms. No bond-formation energy claim is needed yet.

## Slow Turn

Prompt: “What stayed fixed when we added another nitrate tile?” Expected idea: its internal formula and charge; only the number of copies changed. Save an optional notebook sentence locally, without grading its prose.

## Codex hook

Implement `CMP-LEDGER` and `CMP-NOTATION-LENS`; a tile add/remove event recalculates counts and charge from structured data. Output SK-01 evidence only after a submitted identification or explanation, not after a drag. Keyboard and tap stepper are equivalent to drag. Static fallback: a four-column ion/count/charge/subtotal table.


## Acceptance evidence

The lesson must render as readable content without JavaScript. The interactive version must implement its named hook, a non-drag/non-audio fallback, a hint ladder, and one independent transfer opportunity. Preserve raw notes; do not claim software can verify arbitrary free-text reasoning. Source and scientific limits follow [03](../03_CHEMISTRY_RULES_AND_BOUNDARIES.md); the lesson scripts are original design examples, not historical quotations.
