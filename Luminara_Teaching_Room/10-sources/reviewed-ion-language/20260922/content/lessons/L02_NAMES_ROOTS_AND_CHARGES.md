---
document_id: LU-IONS-L02
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Name badges: what you can predict and what you must recall

[Session map](../05_SESSION_AND_SKILL_GRAPH.md) · [Rules](../03_CHEMISTRY_RULES_AND_BOUNDARIES.md) · [Answer key](../09_ANSWER_KEY.md)

**Lesson ID:** L02  
**Skills:** SK-02, SK-03, SK-09  
**Planning duration:** 8 minutes  
**Prerequisites:** SK-01 helps; reference cards remain available.

## Model change

Before: The end of a word is expected to reveal everything about an ion.

After: Names are parsed into recognized identities; selected periodic patterns help with charges but do not replace the ion bank.


## Opening contrast

Show “chlorine,” “chloride,” and “chlorate.” Do not initially ask for all three formulas. Ask which part of each word seems informative. Then reveal: element name; monatomic anion Cl⁻; known oxyanion ClO₃⁻.

> **Natalie:** “I was hoping the ending would be a complete decoder.”
>
> **Ms. Luminara:** “It is a clue to the family, not the full address.”

## Teaching sequence

1. Cations first: Na⁺ sodium, Ca²⁺ calcium, Al³⁺ aluminum. Then the nonmetal exception to the metal cue: NH₄⁺ ammonium.
2. Common monatomic anions: Cl⁻ chloride, O²⁻ oxide, N³⁻ nitride. Store names as dictionary entries, not string surgery.
3. Show hydroxide OH⁻ and cyanide CN⁻. Both end in -ide; both contain two elements. Ask what failed in “-ide always means one atom.”
4. Preview only two polyatomic anchors needed next: nitrate NO₃⁻ and sulfate SO₄²⁻. Keep them visible through L03.
5. Contrast fixed-course charges with variable-metal entries Fe²⁺/Fe³⁺. A blank “iron” card cannot choose its charge without context.

## Periodic mini-map

Use clickable group labels, not a complete periodic-table app rebuild. Group 1’s selected entries show +1; group 2 +2. Show Al/Ga specifically rather than asserting every group-13 ion is always +3. Halides −1, oxide/sulfide −2, nitride/phosphide −3 are a scoped introductory set. Transition-metal area displays “use supplied charge or infer from the compound.”

## Memory actions

See Cl⁻, say chloride, cover it, write it back. Repeat later in reverse. Offer the spoken cue “single-atom negative: recognized root plus -ide,” immediately followed by the caveat that the converse is false. Do not let the mnemonic erase hydroxide or peroxide.

## Fading and transfer

Worked: sodium sulfide is made from Na⁺ and S²⁻. Completion: supply the ion cards for magnesium oxide. Independent: identify the two cards in ammonium chloride. The objective here is identity selection, not yet independent ratio derivation.

## Slow Turn

Create two notebook columns, “derived from a pattern” and “retrieved from an anchor.” Place calcium’s +2 in the first, nitrate’s NO₃⁻ identity in the second. Ask: “Which uncertainty do you actually have right now?”

## Codex hook

`CMP-FAMILY-WALL` supports independent masking of name, formula, and charge. `resolveIonName` must return an ambiguity result for iron without a numeral. Do not silently add unsupported charges or convert chlorine to chloride. Confusing chlorine/chloride is `D-ION-IDENTITY`, not a typo.


## Acceptance evidence

The lesson must render as readable content without JavaScript. The interactive version must implement its named hook, a non-drag/non-audio fallback, a hint ladder, and one independent transfer opportunity. Preserve raw notes; do not claim software can verify arbitrary free-text reasoning. Source and scientific limits follow [03](../03_CHEMISTRY_RULES_AND_BOUNDARIES.md); the lesson scripts are original design examples, not historical quotations.
