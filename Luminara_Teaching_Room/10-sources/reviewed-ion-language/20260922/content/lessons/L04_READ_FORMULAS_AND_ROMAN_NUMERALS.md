---
document_id: LU-IONS-L04
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Read backward: let the known ion constrain the unknown

[Session map](../05_SESSION_AND_SKILL_GRAPH.md) · [Rules](../03_CHEMISTRY_RULES_AND_BOUNDARIES.md) · [Answer key](../09_ANSWER_KEY.md)

**Lesson ID:** L04  
**Skills:** SK-07, SK-08  
**Planning duration:** 8 minutes  
**Prerequisites:** SK-01 and known anion charge; the anion card may be shown.

## Model change

Before: The Roman numeral seems to count metal atoms or to be another fact to memorize.

After: For these salts it states charge per metal ion, derived from the total anion charge and number of metal ions.


## The discriminating example

Show Fe₂O₃ beside FeCl₂. Both contain a written 2 somewhere, but their iron charges differ.

For Fe₂O₃: three O²⁻ total −6; two Fe ions must total +6; each Fe is +3; the name is iron(III) oxide. For FeCl₂: two Cl⁻ total −2; one Fe is +2; iron(II) chloride.

> **Henry:** “The three in iron(III) belongs to each iron, not to the number of irons.”
>
> **Natalie:** “Then I need to divide the total positive charge by the count of metal ions.”

## Repeatable reverse-translation trace

1. Confirm this is an in-scope ionic-formula exercise.
2. Identify the anion as a whole; retrieve its charge.
3. Read the number of anion units and calculate their total charge.
4. Use neutrality to find the total cation charge.
5. Divide by cation count; compare with allowed charge states.
6. Name the cation, including the numeral where needed, followed by the anion.

Use Cu(NO₃)₂ as the polyatomic follow-up. Do not infer the metal numeral from the oxygen count; infer it from the two nitrate charges.

## Productive ambiguity

“Copper sulfate” lacks the copper state in a name-to-formula item. It is reasonable to ask for clarification. By contrast CuSO₄ provides enough information to infer copper(II). This is a lesson in information available, not a speed test.

Fe₃O₄ yields an average +8/3 if every iron is assumed identical. That is a useful boundary marker: the simple single-charge algorithm is insufficient. Show “mixed-valence extension, outside this lesson,” not iron(VIII/III) oxide or an invented integer.

## Fading

Worked: FeCl₃. Completion: Fe₂O₃ with the total −6 supplied. Independent: Cu₂O. Then transfer to Fe₃(PO₄)₂, where two −3 phosphate groups require three +2 irons.

## Slow Turn

Ask: “When did the formula tell us something the bare metal name did not?” Expected idea: the known partner’s charge and the ratio constrained the metal state. Allow a sentence or a completed charge ledger as the response.

## Codex hook

`inferSingleCationCharge` must return integer-state, insufficient-information, or unsupported/mixed-valence outcomes. Never round a fractional result to a convenient allowed state. Reverse translation must also recognize fixed cations and ammonium, not only transition metals.


## Acceptance evidence

The lesson must render as readable content without JavaScript. The interactive version must implement its named hook, a non-drag/non-audio fallback, a hint ladder, and one independent transfer opportunity. Preserve raw notes; do not claim software can verify arbitrary free-text reasoning. Source and scientific limits follow [03](../03_CHEMISTRY_RULES_AND_BOUNDARIES.md); the lesson scripts are original design examples, not historical quotations.
