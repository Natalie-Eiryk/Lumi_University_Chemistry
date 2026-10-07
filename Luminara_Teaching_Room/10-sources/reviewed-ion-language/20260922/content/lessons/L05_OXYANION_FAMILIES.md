---
document_id: LU-IONS-L05
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# The oxygen family wall: a few anchors, carefully bounded rules

[Session map](../05_SESSION_AND_SKILL_GRAPH.md) · [Rules](../03_CHEMISTRY_RULES_AND_BOUNDARIES.md) · [Answer key](../09_ANSWER_KEY.md)

**Lesson ID:** L05  
**Skills:** SK-02, SK-04, SK-09  
**Planning duration:** 12 minutes  
**Prerequisites:** Basic ion notation. This lesson can be opened before L03 if vocabulary is the main obstacle.

## Model change

Before: -ate, -ite, per-, hypo-, and -ide feel like unrelated syllables or universal atom counters.

After: Families have remembered anchors and local relationships; suffixes do not encode universal oxygen counts or charges.


## Work one family at a time

Start with nitrate NO₃⁻ and nitrite NO₂⁻. Ask what changed and what stayed: one oxygen changes; nitrogen and net −1 remain. The learner may use “ATE ate more oxygen,” but must finish “within this family.”

Next show sulfate SO₄²⁻ and sulfite SO₃²⁻. Compare nitrate and sulfite: both have three oxygens, yet one is -ate and the other -ite. This is the counterexample that prevents the mnemonic becoming a false rule.

## Chlorine staircase

Keep chlorate ClO₃⁻ as the anchor. Reveal the four positions in order:

```text
ClO⁻   hypochlorite
ClO₂⁻  chlorite
ClO₃⁻  chlorate
ClO₄⁻  perchlorate
```

The charge badge stays −1. Moving the interface slider selects a different known ion card; it does not perform a chemical reaction. A “show electrons/oxidation states” extension must explicitly distinguish formal oxidation-state accounting from actual localized charges.

## Other contrast stations

Carbonate CO₃²⁻ versus bicarbonate HCO₃⁻: adding H⁺ to the charge inventory gives −2+1=−1. The H belongs inside the ion; Ca(HCO₃)₂ repeats the whole group.

Oxide O²⁻ versus peroxide O₂²⁻: same net charge; different group identities. Replay the sodium peroxide exception to naive subscript reduction.

Chromate CrO₄²⁻ versus dichromate Cr₂O₇²⁻: recall this pair. Two chromate copies would have different atom totals and total charge. The name is not a command to duplicate the ion card.

Ammonium NH₄⁺ and hydronium H₃O⁺: two useful positive groups. Hydroxide OH⁻ and cyanide CN⁻ demonstrate that -ide is not proof of a monatomic ion.

## Memory micro-cycle

Look → say the name → cover the card → write formula AND charge → reverse the cue later. A drawing or spoken response may replace typing, but a handwritten interpretation requires confirmation before automated feedback. Do not recite the complete 62-ion bank in a single presentation.

## Slow Turn

> **Ástríðr:** “So a pattern can reduce the remembering, but only after we know what family it belongs to.”
>
> **Ms. Luminara:** “Exactly. We keep the anchor and the rule. Throwing away either one sends the bus to the wrong address.”

Have Natalie sort statements into “calculate,” “family pattern,” and “remember.” Sulfate’s −2 charge belongs under remember; the number of sulfate groups with Al³⁺ belongs under calculate.

## Codex hook

`CMP-OXYGEN-FAMILY` reads explicit sibling relationships from the bank. It must never manufacture missing siblings by suffix substitution. `CMP-CONTRAST` can show matching atom counts with different suffixes. Course-sensitive phosphite/silicate/carbide cards stay in the reference tier until source reconciliation, not in automatic first-pass quizzes.


## Acceptance evidence

The lesson must render as readable content without JavaScript. The interactive version must implement its named hook, a non-drag/non-audio fallback, a hint ladder, and one independent transfer opportunity. Preserve raw notes; do not claim software can verify arbitrary free-text reasoning. Source and scientific limits follow [03](../03_CHEMISTRY_RULES_AND_BOUNDARIES.md); the lesson scripts are original design examples, not historical quotations.
