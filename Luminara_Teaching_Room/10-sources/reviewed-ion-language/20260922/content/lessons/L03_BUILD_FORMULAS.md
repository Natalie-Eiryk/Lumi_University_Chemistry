---
document_id: LU-IONS-L03
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Build the formula without changing the passengers

[Session map](../05_SESSION_AND_SKILL_GRAPH.md) · [Rules](../03_CHEMISTRY_RULES_AND_BOUNDARIES.md) · [Answer key](../09_ANSWER_KEY.md)

**Lesson ID:** L03  
**Skills:** SK-05, SK-06, SK-10  
**Planning duration:** 10 minutes  
**Prerequisites:** Identify or look up the ion cards. Ion recall is not a prerequisite for practicing charge balance.

## Model change

Before: Crossing numbers feels like a magic rule, and every subscript looks reducible.

After: Counts are the smallest whole-number solution; polyatomic internal subscripts stay part of ion identity.


## Core example

Give Al³⁺ and SO₄²⁻. Start at one of each. The ledger reads +1. Allow any attempted counts; show what they imply without rejecting the physical manipulation.

> **Jeff:** “Two aluminums make +6. Three sulfate cards make −6. I will try that.”
>
> **Ms. Luminara:** “The ledger balances. Now let the notation report exactly what you built.”

Reveal Al₂(SO₄)₃ only after counts are confirmed. Preserve the sulfate card as a whole while adding an outer multiplier.

## The derivation Natalie can inspect

`3a − 2b = 0`. The smallest positive integers are a = 2 and b = 3. A table of trial totals, least common multiple, algebra, or a justified crossing shortcut are all valid ways to get there. Do not grade the presentation of multiplication as if it were the chemistry itself.

## Three contrast pairs

- Mg²⁺ + O²⁻ → MgO. Equal charge magnitudes require one of each.
- Al³⁺ + PO₄³⁻ → AlPO₄. Do not write Al₃(PO₄)₃ as the simplest formula.
- Na⁺ + O₂²⁻ → Na₂O₂. Its two sodium ions and one peroxide ion are already the minimum group ratio. Do not simplify the internal O₂ to O.

## Parentheses lens

For Ca(NO₃)₂ reveal nested counts: one calcium; two nitrate groups; each group contains one N and three O. Show Ca = 1, N = 2, O = 6. Then compare:

- Ca(NO₃)₂: conventional grouped result.
- CaN₂O₆: same atom counts, grouping not expressed as requested.
- CaNO₆: wrong atom counts and no correct nitrate decomposition.
- Ca(NO₃)₃: recognizable groups but the charge ledger is −1.

Use different messages for these different situations.

## Fading practice

Fully work calcium nitrate. Leave the sulfate count blank for aluminum sulfate. Then ask for magnesium phosphate with the ions supplied. A subsequent example changes both charges to +3/−3 to test minimum ratio rather than rote crossing.

## Slow Turn

Ask Natalie to complete: “The subscript inside nitrate stayed ___; the subscript outside the parentheses tells me ___.” Expected: three oxygens per nitrate; number of complete nitrate groups. Follow with the peroxide non-reduction test.

## Codex hook

`minimumIonRatio` is pure integer arithmetic. `formatConventionalFormula` applies parentheses when a polyatomic constituent repeats. Neither routine may use global gcd across element atom totals. The representation lens uses the same parsed tree as grading. Support `D-RATIO-NOT-MINIMAL`, `D-GROUP-LOST`, and `D-ION-MUTATED` separately.


## Acceptance evidence

The lesson must render as readable content without JavaScript. The interactive version must implement its named hook, a non-drag/non-audio fallback, a hint ladder, and one independent transfer opportunity. Preserve raw notes; do not claim software can verify arbitrary free-text reasoning. Source and scientific limits follow [03](../03_CHEMISTRY_RULES_AND_BOUNDARIES.md); the lesson scripts are original design examples, not historical quotations.
