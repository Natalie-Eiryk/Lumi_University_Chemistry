---
document_id: LU-IONS-DESIGN-03
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# The chemistry engine: rules with explicit scope

## Read this before implementing feedback

This is the scientific constraint layer. It refines the preceding conversational lesson; it does not silently replace the course vocabulary. Source-backed clarifications and design choices are separated in the [source ledger](15_SOURCES_AND_DECISIONS.md). The provisional course bank is in [04](04_ION_BANK_AND_FAMILIES.md).

## RULE-01 — charge is not atom count

For a monatomic ion, charge in elementary-charge units equals proton count minus electron count. Gaining an electron changes that number by −1; losing one changes it by +1. An ion may itself contain one atom or multiple bonded atoms. NO₃⁻ has a charge of −1 for the entire group, not −1 on each oxygen. [SRC-IONIC](15_SOURCES_AND_DECISIONS.md#src-ionic)

Teach with Na⁺, Cl⁻, and NO₃⁻ side by side. Keep the subscript and superscript visually distinct. Do not teach “every chemical formula must equal zero”: isolated ions have nonzero charge.

## RULE-02 — neutral ionic formulas balance total charge

For the neutral two-ion formula model used here:

```text
n_c × q_c + n_a × q_a = 0
n_c and n_a are positive integers.
```

If the cation is +p and the anion is −r, divide p and r by their greatest common divisor: cation count = r/gcd(p,r); anion count = p/gcd(p,r). This is our derivation of the shortcut, not a requirement that Natalie use gcd notation.

Example: Al³⁺ and SO₄²⁻ require 2(+3)+3(−2)=0, hence Al₂(SO₄)₃. Charge balance is necessary for this formula task. It does not prove that an arbitrarily invented compound exists, is isolable, is soluble, or forms when two solutions are mixed. [SRC-IONIC](15_SOURCES_AND_DECISIONS.md#src-ionic)

## RULE-03 — simplify the ion ratio, not every atomic subscript

Mg²⁺ with O²⁻ gives MgO, not Mg₂O₂. But Na⁺ with O₂²⁻ gives Na₂O₂. Reducing Na₂O₂ to NaO destroys peroxide identity. The two constituent-ion counts are 2 and 1, already minimal.

This rule is mandatory for the generator, parser, answer key, and charge tiles. A formula must preserve the identity of each polyatomic ion.

## RULE-04 — names identify ions before charge determines quantity

For introductory ionic naming, use cation name followed by anion name. A monatomic cation generally retains the element name; a monatomic anion uses a recognized root with **-ide**. Do not compute the root by blindly deleting characters: oxygen → oxide, nitrogen → nitride, sulfur → sulfide. [SRC-NAMING](15_SOURCES_AND_DECISIONS.md#src-naming)

**-ine is not an ion rule.** Chlorine is an element name; Cl⁻ is chloride. Elemental chlorine is ordinarily represented as Cl₂ when discussing the molecular substance, not as a chloride ion.

The implication goes one way: common monatomic anions end in -ide, but not everything ending in -ide is monatomic. Hydroxide, cyanide, and peroxide are the counterexamples already in the working bank.

## RULE-05 — -ate and -ite compare siblings, not all oxygen-containing ions

Known anchors establish a family. Nitrate NO₃⁻ has one more O than nitrite NO₂⁻; sulfate SO₄²⁻ has one more O than sulfite SO₃²⁻. Neither suffix supplies a universal oxygen count or charge. The shared charge must be learned with each family. The conventional chlorine series is ClO⁻, ClO₂⁻, ClO₃⁻, ClO₄⁻: hypochlorite, chlorite, chlorate, perchlorate. [SRC-NAMING](15_SOURCES_AND_DECISIONS.md#src-naming)

The oxygen elevator navigates labels in a known family. It is NOT an animation claiming that adding a loose oxygen atom mechanically converts one ion into the next. Do not extrapolate hypothetical names such as “carbonite” from the suffix rule.

## RULE-06 — a Roman numeral is not a subscript

In the simple salts used here, iron(III) means each iron ion is Fe³⁺. Fe₂O₃ therefore needs III, not II: three oxide ions total −6, so two irons must each contribute +3.

More generally the Roman numeral expresses an oxidation state. That equals actual charge for a monatomic ion in this model, but an oxidation-state assignment within a covalently bonded group is not an isolated ion. For example, sulfur’s formal +6 in sulfate does not mean sulfate contains a separate S⁶⁺ cation. [SRC-OXIDATION](15_SOURCES_AND_DECISIONS.md#src-oxidation)

Use only the allowed oxidation states in the bank. Do not guess an unprovided charge in “iron chloride”; ask which iron state is intended.

## RULE-07 — parentheses preserve repeated groups

Ca(NO₃)₂ contains two nitrate groups. CaNO₃ is not neutral under the named-ion model. CaNO₆ changes the inventory. CaN₂O₆ preserves the total atom inventory but hides the expected nitrate grouping; diagnose it as composition-equivalent but conventionally ungrouped, not as a wholly different atom count. Request Ca(NO₃)₂ as the conventional answer. Mg(OH)₂ and (NH₄)₂SO₄ work the same way.

Parentheses are notation, not a literal force field or proof a group cannot react. The formula-unit view is not an isolated-molecule claim about an ionic solid. [SRC-IONIC](15_SOURCES_AND_DECISIONS.md#src-ionic)

## RULE-08 — the noble-gas heuristic has a boundary

For selected main-group monatomic ions, group position predicts useful charges: group 1 +1, group 2 +2, Al/Ga +3, halides −1, oxide/sulfide −2, nitride/phosphide −3. This is a restricted pattern, not “all atoms choose the closest noble gas.” It neither determines every transition-metal charge nor supplies polyatomic ion formulas.

Removing an electron from an isolated gaseous atom costs energy. Noble-gas-like occupancy alone is not the energetic argument for compound formation; lattice interactions and the rest of the process matter. Keep this clarification in a short optional aside instead of making the novice solve a Born–Haber cycle. [SRC-ENERGY](15_SOURCES_AND_DECISIONS.md#src-energy)

## RULE-09 — route before translating

This module directly handles a curated set of neutral introductory ionic-formula exercises, plus isolated-ion recall. NH₄Cl is in scope despite containing no metal. CO₂ and N₂O₅ belong to molecular naming; HCl(aq) requires acid context; CuSO₄·5H₂O requires hydrate naming. Mixed-valence Fe₃O₄, complexes, radicals, and unknown formulas go to an explicit unsupported/extension state, not a guessed answer.

Metal + nonmetal is a useful introductory hint, not an infallible classifier. The curated record controls scope. No first-element-only parsing rule.

## RULE-10 — mnemonic vocabulary has limits

“ATE ate more oxygen” is useful only with the same-family qualifier. “Bicarbonate” is an accepted common name for hydrogen carbonate HCO₃⁻; bi- does not mean two carbonate ions. Dichromate Cr₂O₇²⁻ is not two unchanged chromates. Peroxide is not generated by the chlorine per-/hypo- naming algorithm.

## Source-sensitive entries

The earlier conversation’s ion-list transcription includes PO₃³⁻ as phosphite, SiO₄⁴⁻ as silicate, and C⁴⁻ as carbide. Preserve those as **course-profile labels pending original-PDF reconciliation**. Do not present them as exhaustive descriptions of phosphorus, silicate, or carbide chemistry; do not silently substitute a different formula. They are reference/recognition entries, not automatic random-compound ingredients.
