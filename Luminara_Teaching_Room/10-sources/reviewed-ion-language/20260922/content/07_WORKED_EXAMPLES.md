---
document_id: LU-IONS-DESIGN-07
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Eighteen worked translations and their reverse checks

## How to use a worked example

Show the whole trace once, then offer a nearby completion task, then a different independent task. Keep ion identity, charge arithmetic, and naming distinct. The exact atom and charge results below were checked by the packet builder; that is not a claim that repository integration or human course review has passed.

The conservation model uses supplied ion identities. It predicts their neutral ratio, not whether a compound is stable in every physical setting. Scientific scope follows [03](03_CHEMISTRY_RULES_AND_BOUNDARIES.md).

## WE-01 — sodium chloride

**Target:** NaCl ⇄ sodium chloride. Related seed: PR-17.

1. Recognize Na⁺ as sodium and Cl⁻ as chloride.
2. Build charge totals: 1 × (+1) = +1; 1 × (−1) = −1.
3. Confirm the minimum ion-count ratio 1:1. The total is zero.
4. Write NaCl; name the cation first and preserve the anion name.

**Atom inventory:** Na = 1, Cl = 1. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-02 — calcium chloride

**Target:** CaCl₂ ⇄ calcium chloride. Related seed: PR-18.

1. Recognize Ca²⁺ as calcium and Cl⁻ as chloride.
2. Build charge totals: 1 × (+2) = +2; 2 × (−1) = −2.
3. Confirm the minimum ion-count ratio 1:2. The total is zero.
4. Write CaCl₂; name the cation first and preserve the anion name.

**Atom inventory:** Ca = 1, Cl = 2. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-03 — magnesium oxide

**Target:** MgO ⇄ magnesium oxide. Related seed: PR-19.

1. Recognize Mg²⁺ as magnesium and O²⁻ as oxide.
2. Build charge totals: 1 × (+2) = +2; 1 × (−2) = −2.
3. Confirm the minimum ion-count ratio 1:1. The total is zero.
4. Write MgO; name the cation first and preserve the anion name.

**Atom inventory:** Mg = 1, O = 1. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-04 — aluminum oxide

**Target:** Al₂O₃ ⇄ aluminum oxide. Related seed: PR-20.

1. Recognize Al³⁺ as aluminum and O²⁻ as oxide.
2. Build charge totals: 2 × (+3) = +6; 3 × (−2) = −6.
3. Confirm the minimum ion-count ratio 2:3. The total is zero.
4. Write Al₂O₃; name the cation first and preserve the anion name.

**Atom inventory:** Al = 2, O = 3. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-05 — magnesium nitride

**Target:** Mg₃N₂ ⇄ magnesium nitride. Related seed: PR-22.

1. Recognize Mg²⁺ as magnesium and N³⁻ as nitride.
2. Build charge totals: 3 × (+2) = +6; 2 × (−3) = −6.
3. Confirm the minimum ion-count ratio 3:2. The total is zero.
4. Write Mg₃N₂; name the cation first and preserve the anion name.

**Atom inventory:** Mg = 3, N = 2. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-06 — calcium nitrate

**Target:** Ca(NO₃)₂ ⇄ calcium nitrate. Related seed: PR-23.

1. Recognize Ca²⁺ as calcium and NO₃⁻ as nitrate.
2. Build charge totals: 1 × (+2) = +2; 2 × (−1) = −2.
3. Confirm the minimum ion-count ratio 1:2. The total is zero.
4. Write Ca(NO₃)₂; name the cation first and preserve the anion name.

**Group check:** the multiplier outside each parenthesis counts complete copies of that polyatomic ion, not only the final element.

**Atom inventory:** Ca = 1, N = 2, O = 6. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-07 — aluminum sulfate

**Target:** Al₂(SO₄)₃ ⇄ aluminum sulfate. Related seed: PR-24.

1. Recognize Al³⁺ as aluminum and SO₄²⁻ as sulfate.
2. Build charge totals: 2 × (+3) = +6; 3 × (−2) = −6.
3. Confirm the minimum ion-count ratio 2:3. The total is zero.
4. Write Al₂(SO₄)₃; name the cation first and preserve the anion name.

**Group check:** the multiplier outside each parenthesis counts complete copies of that polyatomic ion, not only the final element.

**Atom inventory:** Al = 2, S = 3, O = 12. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-08 — aluminum phosphate

**Target:** AlPO₄ ⇄ aluminum phosphate. Related seed: PR-25.

1. Recognize Al³⁺ as aluminum and PO₄³⁻ as phosphate.
2. Build charge totals: 1 × (+3) = +3; 1 × (−3) = −3.
3. Confirm the minimum ion-count ratio 1:1. The total is zero.
4. Write AlPO₄; name the cation first and preserve the anion name.

**Do not blindly cross:** both charge magnitudes are 3. One of each is enough; no visible subscript 1 or unnecessary parentheses are needed.

**Atom inventory:** Al = 1, P = 1, O = 4. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-09 — ammonium sulfate

**Target:** (NH₄)₂SO₄ ⇄ ammonium sulfate. Related seed: PR-27.

1. Recognize NH₄⁺ as ammonium and SO₄²⁻ as sulfate.
2. Build charge totals: 2 × (+1) = +2; 1 × (−2) = −2.
3. Confirm the minimum ion-count ratio 2:1. The total is zero.
4. Write (NH₄)₂SO₄; name the cation first and preserve the anion name.

**Group check:** the multiplier outside each parenthesis counts complete copies of that polyatomic ion, not only the final element.

**Atom inventory:** N = 2, H = 8, S = 1, O = 4. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-10 — copper(II) nitrate

**Target:** Cu(NO₃)₂ ⇄ copper(II) nitrate. Related seed: PR-30.

1. Recognize Cu²⁺ as copper(II) and NO₃⁻ as nitrate.
2. Build charge totals: 1 × (+2) = +2; 2 × (−1) = −2.
3. Confirm the minimum ion-count ratio 1:2. The total is zero.
4. Write Cu(NO₃)₂; name the cation first and preserve the anion name.

**Reverse check:** the anions total −2; distribute +2 across 1 metal ion(s). Each is +2, which supplies the Roman numeral.

**Group check:** the multiplier outside each parenthesis counts complete copies of that polyatomic ion, not only the final element.

**Atom inventory:** Cu = 1, N = 2, O = 6. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-11 — iron(II) phosphate

**Target:** Fe₃(PO₄)₂ ⇄ iron(II) phosphate. Related seed: PR-31.

1. Recognize Fe²⁺ as iron(II) and PO₄³⁻ as phosphate.
2. Build charge totals: 3 × (+2) = +6; 2 × (−3) = −6.
3. Confirm the minimum ion-count ratio 3:2. The total is zero.
4. Write Fe₃(PO₄)₂; name the cation first and preserve the anion name.

**Reverse check:** the anions total −6; distribute +6 across 3 metal ion(s). Each is +2, which supplies the Roman numeral.

**Group check:** the multiplier outside each parenthesis counts complete copies of that polyatomic ion, not only the final element.

**Atom inventory:** Fe = 3, P = 2, O = 8. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-12 — iron(III) sulfate

**Target:** Fe₂(SO₄)₃ ⇄ iron(III) sulfate. Related seed: PR-32.

1. Recognize Fe³⁺ as iron(III) and SO₄²⁻ as sulfate.
2. Build charge totals: 2 × (+3) = +6; 3 × (−2) = −6.
3. Confirm the minimum ion-count ratio 2:3. The total is zero.
4. Write Fe₂(SO₄)₃; name the cation first and preserve the anion name.

**Reverse check:** the anions total −6; distribute +6 across 2 metal ion(s). Each is +3, which supplies the Roman numeral.

**Group check:** the multiplier outside each parenthesis counts complete copies of that polyatomic ion, not only the final element.

**Atom inventory:** Fe = 2, S = 3, O = 12. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-13 — calcium bicarbonate

**Target:** Ca(HCO₃)₂ ⇄ calcium bicarbonate. Related seed: PR-33.

1. Recognize Ca²⁺ as calcium and HCO₃⁻ as bicarbonate.
2. Build charge totals: 1 × (+2) = +2; 2 × (−1) = −2.
3. Confirm the minimum ion-count ratio 1:2. The total is zero.
4. Write Ca(HCO₃)₂; name the cation first and preserve the anion name.

**Group check:** the multiplier outside each parenthesis counts complete copies of that polyatomic ion, not only the final element.

**Atom inventory:** Ca = 1, H = 2, C = 2, O = 6. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-14 — potassium chlorite

**Target:** KClO₂ ⇄ potassium chlorite. Related seed: PR-34.

1. Recognize K⁺ as potassium and ClO₂⁻ as chlorite.
2. Build charge totals: 1 × (+1) = +1; 1 × (−1) = −1.
3. Confirm the minimum ion-count ratio 1:1. The total is zero.
4. Write KClO₂; name the cation first and preserve the anion name.

**Atom inventory:** K = 1, Cl = 1, O = 2. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-15 — sodium peroxide

**Target:** Na₂O₂ ⇄ sodium peroxide. Related seed: PR-38.

1. Recognize Na⁺ as sodium and O₂²⁻ as peroxide.
2. Build charge totals: 2 × (+1) = +2; 1 × (−2) = −2.
3. Confirm the minimum ion-count ratio 2:1. The total is zero.
4. Write Na₂O₂; name the cation first and preserve the anion name.

**Do not reduce:** the peroxide group is O₂²⁻. The minimum ion ratio is 2 sodium : 1 peroxide; NaO is not the desired representation.

**Atom inventory:** Na = 2, O = 2. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-16 — iron(III) oxide

**Target:** Fe₂O₃ ⇄ iron(III) oxide. Related seed: PR-45.

1. Recognize Fe³⁺ as iron(III) and O²⁻ as oxide.
2. Build charge totals: 2 × (+3) = +6; 3 × (−2) = −6.
3. Confirm the minimum ion-count ratio 2:3. The total is zero.
4. Write Fe₂O₃; name the cation first and preserve the anion name.

**Reverse check:** the anions total −6; distribute +6 across 2 metal ion(s). Each is +3, which supplies the Roman numeral.

**Atom inventory:** Fe = 2, O = 3. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-17 — copper(I) oxide

**Target:** Cu₂O ⇄ copper(I) oxide. Related seed: PR-46.

1. Recognize Cu⁺ as copper(I) and O²⁻ as oxide.
2. Build charge totals: 2 × (+1) = +2; 1 × (−2) = −2.
3. Confirm the minimum ion-count ratio 2:1. The total is zero.
4. Write Cu₂O; name the cation first and preserve the anion name.

**Reverse check:** the anions total −2; distribute +2 across 2 metal ion(s). Each is +1, which supplies the Roman numeral.

**Atom inventory:** Cu = 2, O = 1. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?

## WE-18 — potassium dichromate

**Target:** K₂Cr₂O₇ ⇄ potassium dichromate. Related seed: PR-57.

1. Recognize K⁺ as potassium and Cr₂O₇²⁻ as dichromate.
2. Build charge totals: 2 × (+1) = +2; 1 × (−2) = −2.
3. Confirm the minimum ion-count ratio 2:1. The total is zero.
4. Write K₂Cr₂O₇; name the cation first and preserve the anion name.

**Atom inventory:** K = 2, Cr = 2, O = 7. This is a second representation check, not a replacement for charge balance.

**Reflection:** Which information came from an ion anchor, and which part did charge balance determine?


## Two derivations of the same ratio

For aluminum sulfate, use either a common multiple (+6 and −6) or `3a = 2b`. Both establish a = 2 and b = 3 as the smallest positive integers. The app must accept either coherent explanation. “Criss-cross” may be offered after the derivation, but always follow it by a ratio-reduction and group-identity check.

## Contrast worth keeping visible

- FeCl₂ versus FeCl₃: same element names, different iron state.
- KClO₂ versus KClO₃: same cation charge and same anion charge, different anion identity/name.
- MgO versus Na₂O₂: least whole-number **ion** ratio is not least whole-number **atom** ratio in every formula.
- Ca(NO₃)₂ versus CaN₂O₆: distinguish atom-equivalent notation from the preferred grouped representation; teach the improvement without denying what is already correct.
