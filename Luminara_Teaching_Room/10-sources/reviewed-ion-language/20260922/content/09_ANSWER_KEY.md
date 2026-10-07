---
document_id: LU-IONS-DESIGN-09
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Answer key, reasoning, and compiler fixtures

## Key contract

These answers are for the supplied curated items and ion conventions. They are not a general chemical-name resolver. Canonical formulas use case-sensitive ASCII for machine storage and semantic sub/superscripts in the reader. The lessons explain acceptable alternate reasoning; the engine tracks correctness and presentation separately.

A free-text explanation matching the meaning below should not be marked wrong because its wording differs. When semantic grading is uncertain, request clarification or offer self-review; do not invent confidence in an automated verdict.

[Prompts](08_PRACTICE_BANK.md) · [Diagnostics](10_FEEDBACK_AND_SPACED_REVIEW.md) · [Engine contract](11_DATA_AND_ENGINE_CONTRACTS.md)

## PR-01

**Answer:** Three oxygen atoms in one nitrate ion; net charge −1 on the complete ion.

Atom inventory and group charge are different quantities.

**Evidence tags:** SK-01. **First diagnostic to consider:** `D-NOTATION-CONFLATION`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-02

**Answer:** N = 2; O = 6; charge = −2.

Multiply the complete ion inventory and its charge by two.

**Evidence tags:** SK-01. **First diagnostic to consider:** `D-GROUP-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-03

**Answer:** chloride

The element name chlorine is not the name of its monatomic negative ion.

**Evidence tags:** SK-02. **First diagnostic to consider:** `D-ION-IDENTITY`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-04

**Answer:** NH₄⁺

Ammonium is a remembered polyatomic cation. It is not neutral ammonia NH₃.

**Evidence tags:** SK-02. **First diagnostic to consider:** `D-ION-IDENTITY`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-05

**Answer:** Net +1; add one more Cl⁻.

One +2 cation needs two −1 anions for a neutral formula.

**Evidence tags:** SK-01, SK-05. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-06

**Answer:** No. It represents an ion with charge −1; neutrality is required for the neutral compound task.

Do not generalize a neutral-salt rule to isolated ions.

**Evidence tags:** SK-09. **First diagnostic to consider:** `D-SCOPE-NEUTRALITY`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-07

**Answer:** +2; calcium is a group-2 element.

Use the scoped main-group pattern, not a universal noble-gas rule.

**Evidence tags:** SK-03. **First diagnostic to consider:** `D-ION-CHARGE`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-08

**Answer:** sulfate, −2; sulfite, −2

The oxygen count changes by one within the sulfur pair; the group charge does not.

**Evidence tags:** SK-02, SK-04. **First diagnostic to consider:** `D-FAMILY-SUFFIX`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-09

**Answer:** NO₂⁻

Use the known nitrogen family; one fewer oxygen retains its family charge of −1.

**Evidence tags:** SK-04. **First diagnostic to consider:** `D-FAMILY-SUFFIX`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-10

**Answer:** No. You need a known family anchor or an ion reference.

Nitrate and sulfate already show that -ate does not specify one universal oxygen count or charge.

**Evidence tags:** SK-04, SK-09. **First diagnostic to consider:** `D-FAMILY-OVERGENERALIZED`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-11

**Answer:** hypochlorite → chlorite → chlorate → perchlorate

This is the known chlorine series: ClO⁻, ClO₂⁻, ClO₃⁻, ClO₄⁻.

**Evidence tags:** SK-04. **First diagnostic to consider:** `D-FAMILY-SUFFIX`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-12

**Answer:** No. Both are polyatomic ions.

The -ide rule for monatomic anions does not work as a reversible definition.

**Evidence tags:** SK-09. **First diagnostic to consider:** `D-FAMILY-OVERGENERALIZED`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-13

**Answer:** The +3 charge of each iron ion in this simple ionic model.

It is not the number of iron atoms or the chloride charge.

**Evidence tags:** SK-07. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-14

**Answer:** No. Use a supplied Roman numeral, formula context, or other explicit information.

Iron has more than one allowed charge in the bank.

**Evidence tags:** SK-07, SK-09. **First diagnostic to consider:** `D-AMBIGUOUS-NAME`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-15

**Answer:** CO₃²⁻ and HCO₃⁻

A hydrogen cation added to the bookkeeping changes the charge from −2 to −1. Bi- does not mean two carbonate ions.

**Evidence tags:** SK-02, SK-04. **First diagnostic to consider:** `D-ION-IDENTITY`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-16

**Answer:** Name, formula, and net charge.

Recognizing a name is insufficient for formula construction if the charge is missing.

**Evidence tags:** SK-02. **First diagnostic to consider:** `D-ION-CHARGE`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-17

**Answer:** NaCl

Use Na⁺ and Cl⁻. The ion-count ratio is 1:1; 1(+1) + 1(−1) = 0.

**Evidence tags:** SK-02, SK-05, SK-08. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `NaCl`; `ION-NA` × 1; `ION-CHLORIDE` × 1.

## PR-18

**Answer:** CaCl₂

Use Ca²⁺ and Cl⁻. The ion-count ratio is 1:2; 1(+2) + 2(−1) = 0.

**Evidence tags:** SK-02, SK-05, SK-08. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `CaCl2`; `ION-CA` × 1; `ION-CHLORIDE` × 2.

## PR-19

**Answer:** MgO

Use Mg²⁺ and O²⁻. The ion-count ratio is 1:1; 1(+2) + 1(−2) = 0.

**Evidence tags:** SK-02, SK-05, SK-08. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `MgO`; `ION-MG` × 1; `ION-OXIDE` × 1.

## PR-20

**Answer:** Al₂O₃

Use Al³⁺ and O²⁻. The ion-count ratio is 2:3; 2(+3) + 3(−2) = 0.

**Evidence tags:** SK-02, SK-05, SK-08. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Al2O3`; `ION-AL` × 2; `ION-OXIDE` × 3.

## PR-21

**Answer:** K₂S

Use K⁺ and S²⁻. The ion-count ratio is 2:1; 2(+1) + 1(−2) = 0.

**Evidence tags:** SK-02, SK-05, SK-08. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `K2S`; `ION-K` × 2; `ION-SULFIDE` × 1.

## PR-22

**Answer:** Mg₃N₂

Use Mg²⁺ and N³⁻. The ion-count ratio is 3:2; 3(+2) + 2(−3) = 0.

**Evidence tags:** SK-02, SK-05, SK-08. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Mg3N2`; `ION-MG` × 3; `ION-NITRIDE` × 2.

## PR-23

**Answer:** Ca(NO₃)₂

Use Ca²⁺ and NO₃⁻. The ion-count ratio is 1:2; 1(+2) + 2(−1) = 0.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06, SK-04. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Ca(NO3)2`; `ION-CA` × 1; `ION-NITRATE` × 2.

## PR-24

**Answer:** Al₂(SO₄)₃

Use Al³⁺ and SO₄²⁻. The ion-count ratio is 2:3; 2(+3) + 3(−2) = 0.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06, SK-04. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Al2(SO4)3`; `ION-AL` × 2; `ION-SULFATE` × 3.

## PR-25

**Answer:** AlPO₄

Use Al³⁺ and PO₄³⁻. The ion-count ratio is 1:1; 1(+3) + 1(−3) = 0.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06, SK-04. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `AlPO4`; `ION-AL` × 1; `ION-PHOSPHATE` × 1.

## PR-26

**Answer:** NH₄Cl

Use NH₄⁺ and Cl⁻. The ion-count ratio is 1:1; 1(+1) + 1(−1) = 0.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `NH4Cl`; `ION-AMMONIUM` × 1; `ION-CHLORIDE` × 1.

## PR-27

**Answer:** (NH₄)₂SO₄

Use NH₄⁺ and SO₄²⁻. The ion-count ratio is 2:1; 2(+1) + 1(−2) = 0.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06, SK-04. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `(NH4)2SO4`; `ION-AMMONIUM` × 2; `ION-SULFATE` × 1.

## PR-28

**Answer:** Mg(OH)₂

Use Mg²⁺ and OH⁻. The ion-count ratio is 1:2; 1(+2) + 2(−1) = 0.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Mg(OH)2`; `ION-MG` × 1; `ION-HYDROXIDE` × 2.

## PR-29

**Answer:** Cu₂O

Use Cu⁺ and O²⁻. The ion-count ratio is 2:1; 2(+1) + 1(−2) = 0. The total negative charge has magnitude 2; dividing the required positive total by 2 gives +1 per metal ion.

**Evidence tags:** SK-02, SK-05, SK-08, SK-07. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Cu2O`; `ION-CU-I` × 2; `ION-OXIDE` × 1.

## PR-30

**Answer:** Cu(NO₃)₂

Use Cu²⁺ and NO₃⁻. The ion-count ratio is 1:2; 1(+2) + 2(−1) = 0. The total negative charge has magnitude 2; dividing the required positive total by 1 gives +2 per metal ion.

**Evidence tags:** SK-02, SK-05, SK-08, SK-07, SK-06, SK-04. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Cu(NO3)2`; `ION-CU-II` × 1; `ION-NITRATE` × 2.

## PR-31

**Answer:** Fe₃(PO₄)₂

Use Fe²⁺ and PO₄³⁻. The ion-count ratio is 3:2; 3(+2) + 2(−3) = 0. The total negative charge has magnitude 6; dividing the required positive total by 3 gives +2 per metal ion.

**Evidence tags:** SK-02, SK-05, SK-08, SK-07, SK-06, SK-04. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Fe3(PO4)2`; `ION-FE-II` × 3; `ION-PHOSPHATE` × 2.

## PR-32

**Answer:** Fe₂(SO₄)₃

Use Fe³⁺ and SO₄²⁻. The ion-count ratio is 2:3; 2(+3) + 3(−2) = 0. The total negative charge has magnitude 6; dividing the required positive total by 2 gives +3 per metal ion.

**Evidence tags:** SK-02, SK-05, SK-08, SK-07, SK-06, SK-04. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Fe2(SO4)3`; `ION-FE-III` × 2; `ION-SULFATE` × 3.

## PR-33

**Answer:** Ca(HCO₃)₂

Use Ca²⁺ and HCO₃⁻. The ion-count ratio is 1:2; 1(+2) + 2(−1) = 0. Also accept calcium hydrogen carbonate.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Ca(HCO3)2`; `ION-CA` × 1; `ION-HYDROGEN-CARBONATE` × 2.

## PR-34

**Answer:** KClO₂

Use K⁺ and ClO₂⁻. The ion-count ratio is 1:1; 1(+1) + 1(−1) = 0.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06, SK-04. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `KClO2`; `ION-K` × 1; `ION-CHLORITE` × 1.

## PR-35

**Answer:** NaClO₃

Use Na⁺ and ClO₃⁻. The ion-count ratio is 1:1; 1(+1) + 1(−1) = 0.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06, SK-04. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `NaClO3`; `ION-NA` × 1; `ION-CHLORATE` × 1.

## PR-36

**Answer:** NaClO

Use Na⁺ and ClO⁻. The ion-count ratio is 1:1; 1(+1) + 1(−1) = 0.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06, SK-04. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `NaClO`; `ION-NA` × 1; `ION-HYPOCHLORITE` × 1.

## PR-37

**Answer:** KClO₄

Use K⁺ and ClO₄⁻. The ion-count ratio is 1:1; 1(+1) + 1(−1) = 0.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06, SK-04. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `KClO4`; `ION-K` × 1; `ION-PERCHLORATE` × 1.

## PR-38

**Answer:** Na₂O₂

Use Na⁺ and O₂²⁻. The ion-count ratio is 2:1; 2(+1) + 1(−2) = 0. Keep the O₂ peroxide group; do not reduce to NaO.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Na2O2`; `ION-NA` × 2; `ION-PEROXIDE` × 1.

## PR-39

**Answer:** Zn(C₂H₃O₂)₂

Use Zn²⁺ and C₂H₃O₂⁻. The ion-count ratio is 1:2; 1(+2) + 2(−1) = 0.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Zn(C2H3O2)2`; `ION-ZN` × 1; `ION-ACETATE` × 2.

## PR-40

**Answer:** Ag₂CO₃

Use Ag⁺ and CO₃²⁻. The ion-count ratio is 2:1; 2(+1) + 1(−2) = 0.

**Evidence tags:** SK-02, SK-05, SK-08, SK-06. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Ag2CO3`; `ION-AG` × 2; `ION-CARBONATE` × 1.

## PR-41

**Answer:** sodium sulfide

Use Na⁺ and S²⁻. The ion-count ratio is 2:1; 2(+1) + 1(−2) = 0.

**Evidence tags:** SK-02, SK-08. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Na2S`; `ION-NA` × 2; `ION-SULFIDE` × 1.

## PR-42

**Answer:** magnesium bromide

Use Mg²⁺ and Br⁻. The ion-count ratio is 1:2; 1(+2) + 2(−1) = 0.

**Evidence tags:** SK-02, SK-08. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `MgBr2`; `ION-MG` × 1; `ION-BROMIDE` × 2.

## PR-43

**Answer:** iron(II) chloride

Use Fe²⁺ and Cl⁻. The ion-count ratio is 1:2; 1(+2) + 2(−1) = 0. The total negative charge has magnitude 2; dividing the required positive total by 1 gives +2 per metal ion.

**Evidence tags:** SK-02, SK-08, SK-07. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `FeCl2`; `ION-FE-II` × 1; `ION-CHLORIDE` × 2.

## PR-44

**Answer:** iron(III) chloride

Use Fe³⁺ and Cl⁻. The ion-count ratio is 1:3; 1(+3) + 3(−1) = 0. The total negative charge has magnitude 3; dividing the required positive total by 1 gives +3 per metal ion.

**Evidence tags:** SK-02, SK-08, SK-07. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `FeCl3`; `ION-FE-III` × 1; `ION-CHLORIDE` × 3.

## PR-45

**Answer:** iron(III) oxide

Use Fe³⁺ and O²⁻. The ion-count ratio is 2:3; 2(+3) + 3(−2) = 0. The total negative charge has magnitude 6; dividing the required positive total by 2 gives +3 per metal ion.

**Evidence tags:** SK-02, SK-08, SK-07. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Fe2O3`; `ION-FE-III` × 2; `ION-OXIDE` × 3.

## PR-46

**Answer:** copper(I) oxide

Use Cu⁺ and O²⁻. The ion-count ratio is 2:1; 2(+1) + 1(−2) = 0. The total negative charge has magnitude 2; dividing the required positive total by 2 gives +1 per metal ion.

**Evidence tags:** SK-02, SK-08, SK-07. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Cu2O`; `ION-CU-I` × 2; `ION-OXIDE` × 1.

## PR-47

**Answer:** copper(II) oxide

Use Cu²⁺ and O²⁻. The ion-count ratio is 1:1; 1(+2) + 1(−2) = 0. The total negative charge has magnitude 2; dividing the required positive total by 1 gives +2 per metal ion.

**Evidence tags:** SK-02, SK-08, SK-07. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `CuO`; `ION-CU-II` × 1; `ION-OXIDE` × 1.

## PR-48

**Answer:** copper(II) sulfate

Use Cu²⁺ and SO₄²⁻. The ion-count ratio is 1:1; 1(+2) + 1(−2) = 0. The total negative charge has magnitude 2; dividing the required positive total by 1 gives +2 per metal ion.

**Evidence tags:** SK-02, SK-08, SK-07, SK-06, SK-04. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `CuSO4`; `ION-CU-II` × 1; `ION-SULFATE` × 1.

## PR-49

**Answer:** copper(II) nitrate

Use Cu²⁺ and NO₃⁻. The ion-count ratio is 1:2; 1(+2) + 2(−1) = 0. The total negative charge has magnitude 2; dividing the required positive total by 1 gives +2 per metal ion.

**Evidence tags:** SK-02, SK-08, SK-07, SK-06, SK-04. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Cu(NO3)2`; `ION-CU-II` × 1; `ION-NITRATE` × 2.

## PR-50

**Answer:** iron(II) phosphate

Use Fe²⁺ and PO₄³⁻. The ion-count ratio is 3:2; 3(+2) + 2(−3) = 0. The total negative charge has magnitude 6; dividing the required positive total by 3 gives +2 per metal ion.

**Evidence tags:** SK-02, SK-08, SK-07, SK-06, SK-04. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Fe3(PO4)2`; `ION-FE-II` × 3; `ION-PHOSPHATE` × 2.

## PR-51

**Answer:** tin(IV) chloride

Use Sn⁴⁺ and Cl⁻. The ion-count ratio is 1:4; 1(+4) + 4(−1) = 0. The total negative charge has magnitude 4; dividing the required positive total by 1 gives +4 per metal ion.

**Evidence tags:** SK-02, SK-08, SK-07. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `SnCl4`; `ION-SN-IV` × 1; `ION-CHLORIDE` × 4.

## PR-52

**Answer:** lead(IV) oxide

Use Pb⁴⁺ and O²⁻. The ion-count ratio is 1:2; 1(+4) + 2(−2) = 0. The total negative charge has magnitude 4; dividing the required positive total by 1 gives +4 per metal ion.

**Evidence tags:** SK-02, SK-08, SK-07. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `PbO2`; `ION-PB-IV` × 1; `ION-OXIDE` × 2.

## PR-53

**Answer:** cobalt(III) oxide

Use Co³⁺ and O²⁻. The ion-count ratio is 2:3; 2(+3) + 3(−2) = 0. The total negative charge has magnitude 6; dividing the required positive total by 2 gives +3 per metal ion.

**Evidence tags:** SK-02, SK-08, SK-07. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Co2O3`; `ION-CO-III` × 2; `ION-OXIDE` × 3.

## PR-54

**Answer:** chromium(III) chloride

Use Cr³⁺ and Cl⁻. The ion-count ratio is 1:3; 1(+3) + 3(−1) = 0. The total negative charge has magnitude 3; dividing the required positive total by 1 gives +3 per metal ion.

**Evidence tags:** SK-02, SK-08, SK-07. **First diagnostic to consider:** `D-ROMAN-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `CrCl3`; `ION-CR-III` × 1; `ION-CHLORIDE` × 3.

## PR-55

**Answer:** ammonium carbonate

Use NH₄⁺ and CO₃²⁻. The ion-count ratio is 2:1; 2(+1) + 1(−2) = 0.

**Evidence tags:** SK-02, SK-08, SK-06. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `(NH4)2CO3`; `ION-AMMONIUM` × 2; `ION-CARBONATE` × 1.

## PR-56

**Answer:** potassium chromate

Use K⁺ and CrO₄²⁻. The ion-count ratio is 2:1; 2(+1) + 1(−2) = 0.

**Evidence tags:** SK-02, SK-08, SK-06, SK-04. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `K2CrO4`; `ION-K` × 2; `ION-CHROMATE` × 1.

## PR-57

**Answer:** potassium dichromate

Use K⁺ and Cr₂O₇²⁻. The ion-count ratio is 2:1; 2(+1) + 1(−2) = 0.

**Evidence tags:** SK-02, SK-08, SK-06, SK-04. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `K2Cr2O7`; `ION-K` × 2; `ION-DICHROMATE` × 1.

## PR-58

**Answer:** potassium permanganate

Use K⁺ and MnO₄⁻. The ion-count ratio is 1:1; 1(+1) + 1(−1) = 0.

**Evidence tags:** SK-02, SK-08, SK-06. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `KMnO4`; `ION-K` × 1; `ION-PERMANGANATE` × 1.

## PR-59

**Answer:** calcium bicarbonate

Use Ca²⁺ and HCO₃⁻. The ion-count ratio is 1:2; 1(+2) + 2(−1) = 0. Also accept calcium hydrogen carbonate.

**Evidence tags:** SK-02, SK-08, SK-06. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Ca(HCO3)2`; `ION-CA` × 1; `ION-HYDROGEN-CARBONATE` × 2.

## PR-60

**Answer:** cadmium nitrate

Use Cd²⁺ and NO₃⁻. The ion-count ratio is 1:2; 1(+2) + 2(−1) = 0.

**Evidence tags:** SK-02, SK-08, SK-06, SK-04. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

**Compiled target:** `Cd(NO3)2`; `ION-CD` × 1; `ION-NITRATE` × 2.

## PR-61

**Answer:** Al₂(SO₄)₃

Al³⁺ + SO₄²⁻ totals +1. Two aluminums and three sulfate groups give +6 and −6.

**Evidence tags:** SK-05, SK-06, SK-10. **First diagnostic to consider:** `D-CHARGE-TOTAL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-62

**Answer:** No. Na₂O₂ has two sodium ions and one peroxide ion; that ion ratio is already minimal.

Reducing all atom subscripts would replace the O₂²⁻ ion with a different assumed constituent.

**Evidence tags:** SK-05, SK-06, SK-10. **First diagnostic to consider:** `D-ION-MUTATED`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-63

**Answer:** Ca(NO₃)₂. CaN₂O₆ has the same atom totals but omits the conventional grouping; CaNO₆ has the wrong N count.

Recognize composition equivalence without pretending all representations communicate the ion grouping equally well.

**Evidence tags:** SK-06, SK-10. **First diagnostic to consider:** `D-GROUP-LOST`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-64

**Answer:** No. Route to molecular naming.

The nonmetal/nonmetal compound in this curated boundary item does not supply the two ion cards used by this module.

**Evidence tags:** SK-09. **First diagnostic to consider:** `D-SCOPE-ROUTING`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-65

**Answer:** No. Route to the acid-context extension.

The state/context matters; do not pretend this module covers all hydrogen-containing formulas.

**Evidence tags:** SK-09. **First diagnostic to consider:** `D-SCOPE-ROUTING`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-66

**Answer:** Request the copper oxidation state; CuCl and CuCl₂ correspond to different choices.

Do not guess a missing Roman numeral from familiarity.

**Evidence tags:** SK-07, SK-09. **First diagnostic to consider:** `D-AMBIGUOUS-NAME`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-67

**Answer:** No. Mark the single-charge model insufficient; route to a mixed-valence extension.

A noninteger average is not a valid integer charge to round or invent in this introductory translator.

**Evidence tags:** SK-07, SK-09. **First diagnostic to consider:** `D-UNSUPPORTED-MODEL`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-68

**Answer:** Keep nitrate NO₃⁻ and use two groups: Ca(NO₃)₂.

Changing the oxygen count changes ion identity and does not change the −1 charge within this nitrate/nitrite pair.

**Evidence tags:** SK-04, SK-06, SK-10. **First diagnostic to consider:** `D-ION-MUTATED`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-69

**Answer:** -ate has more oxygen than -ite within specified families; nitrate has three O, sulfate four.

Oxygen count and charge must come from a known anchor, not from the suffix alone.

**Evidence tags:** SK-04, SK-09. **First diagnostic to consider:** `D-FAMILY-OVERGENERALIZED`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-70

**Answer:** (NH₄)₂SO₄; N = 2, H = 8, S = 1, O = 4.

One ammonium and one sulfate total −1. Two ammonium ions balance one sulfate.

**Evidence tags:** SK-05, SK-06, SK-10. **First diagnostic to consider:** `D-GROUP-COUNT`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-71

**Answer:** No. Return unknown ion / reference needed, without inventing a species.

A lookup gap is not a learner misconception and is not solved by guessing chemistry.

**Evidence tags:** SK-09. **First diagnostic to consider:** `D-UNKNOWN-ION`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.

## PR-72

**Answer:** No. CO and Co mean different things. Show a case-sensitive clarification.

Chemical symbol case is meaningful; typography normalization must not erase element boundaries.

**Evidence tags:** SK-01, SK-09. **First diagnostic to consider:** `D-PARSE-CASE`. The diagnostic is a candidate based on an observed error, not an automatic label assigned to the learner.


## Fixed-pair compiler records

The records below are normative design fixtures for the 44 compound translation prompts. Convert to the existing content format; do not use Markdown prose as the production chemical parser. Formula spelling aliases must be curated in a separate reviewed map, not generated through unrestricted atom sorting.

```json
[
  {
    "id": "PR-17",
    "direction": "name_to_formula",
    "formula_ascii": "NaCl",
    "name": "sodium chloride",
    "cation_id": "ION-NA",
    "anion_id": "ION-CHLORIDE",
    "cation_count": 1,
    "anion_count": 1
  },
  {
    "id": "PR-18",
    "direction": "name_to_formula",
    "formula_ascii": "CaCl2",
    "name": "calcium chloride",
    "cation_id": "ION-CA",
    "anion_id": "ION-CHLORIDE",
    "cation_count": 1,
    "anion_count": 2
  },
  {
    "id": "PR-19",
    "direction": "name_to_formula",
    "formula_ascii": "MgO",
    "name": "magnesium oxide",
    "cation_id": "ION-MG",
    "anion_id": "ION-OXIDE",
    "cation_count": 1,
    "anion_count": 1
  },
  {
    "id": "PR-20",
    "direction": "name_to_formula",
    "formula_ascii": "Al2O3",
    "name": "aluminum oxide",
    "cation_id": "ION-AL",
    "anion_id": "ION-OXIDE",
    "cation_count": 2,
    "anion_count": 3
  },
  {
    "id": "PR-21",
    "direction": "name_to_formula",
    "formula_ascii": "K2S",
    "name": "potassium sulfide",
    "cation_id": "ION-K",
    "anion_id": "ION-SULFIDE",
    "cation_count": 2,
    "anion_count": 1
  },
  {
    "id": "PR-22",
    "direction": "name_to_formula",
    "formula_ascii": "Mg3N2",
    "name": "magnesium nitride",
    "cation_id": "ION-MG",
    "anion_id": "ION-NITRIDE",
    "cation_count": 3,
    "anion_count": 2
  },
  {
    "id": "PR-23",
    "direction": "name_to_formula",
    "formula_ascii": "Ca(NO3)2",
    "name": "calcium nitrate",
    "cation_id": "ION-CA",
    "anion_id": "ION-NITRATE",
    "cation_count": 1,
    "anion_count": 2
  },
  {
    "id": "PR-24",
    "direction": "name_to_formula",
    "formula_ascii": "Al2(SO4)3",
    "name": "aluminum sulfate",
    "cation_id": "ION-AL",
    "anion_id": "ION-SULFATE",
    "cation_count": 2,
    "anion_count": 3
  },
  {
    "id": "PR-25",
    "direction": "name_to_formula",
    "formula_ascii": "AlPO4",
    "name": "aluminum phosphate",
    "cation_id": "ION-AL",
    "anion_id": "ION-PHOSPHATE",
    "cation_count": 1,
    "anion_count": 1
  },
  {
    "id": "PR-26",
    "direction": "name_to_formula",
    "formula_ascii": "NH4Cl",
    "name": "ammonium chloride",
    "cation_id": "ION-AMMONIUM",
    "anion_id": "ION-CHLORIDE",
    "cation_count": 1,
    "anion_count": 1
  },
  {
    "id": "PR-27",
    "direction": "name_to_formula",
    "formula_ascii": "(NH4)2SO4",
    "name": "ammonium sulfate",
    "cation_id": "ION-AMMONIUM",
    "anion_id": "ION-SULFATE",
    "cation_count": 2,
    "anion_count": 1
  },
  {
    "id": "PR-28",
    "direction": "name_to_formula",
    "formula_ascii": "Mg(OH)2",
    "name": "magnesium hydroxide",
    "cation_id": "ION-MG",
    "anion_id": "ION-HYDROXIDE",
    "cation_count": 1,
    "anion_count": 2
  },
  {
    "id": "PR-29",
    "direction": "name_to_formula",
    "formula_ascii": "Cu2O",
    "name": "copper(I) oxide",
    "cation_id": "ION-CU-I",
    "anion_id": "ION-OXIDE",
    "cation_count": 2,
    "anion_count": 1
  },
  {
    "id": "PR-30",
    "direction": "name_to_formula",
    "formula_ascii": "Cu(NO3)2",
    "name": "copper(II) nitrate",
    "cation_id": "ION-CU-II",
    "anion_id": "ION-NITRATE",
    "cation_count": 1,
    "anion_count": 2
  },
  {
    "id": "PR-31",
    "direction": "name_to_formula",
    "formula_ascii": "Fe3(PO4)2",
    "name": "iron(II) phosphate",
    "cation_id": "ION-FE-II",
    "anion_id": "ION-PHOSPHATE",
    "cation_count": 3,
    "anion_count": 2
  },
  {
    "id": "PR-32",
    "direction": "name_to_formula",
    "formula_ascii": "Fe2(SO4)3",
    "name": "iron(III) sulfate",
    "cation_id": "ION-FE-III",
    "anion_id": "ION-SULFATE",
    "cation_count": 2,
    "anion_count": 3
  },
  {
    "id": "PR-33",
    "direction": "name_to_formula",
    "formula_ascii": "Ca(HCO3)2",
    "name": "calcium bicarbonate",
    "cation_id": "ION-CA",
    "anion_id": "ION-HYDROGEN-CARBONATE",
    "cation_count": 1,
    "anion_count": 2
  },
  {
    "id": "PR-34",
    "direction": "name_to_formula",
    "formula_ascii": "KClO2",
    "name": "potassium chlorite",
    "cation_id": "ION-K",
    "anion_id": "ION-CHLORITE",
    "cation_count": 1,
    "anion_count": 1
  },
  {
    "id": "PR-35",
    "direction": "name_to_formula",
    "formula_ascii": "NaClO3",
    "name": "sodium chlorate",
    "cation_id": "ION-NA",
    "anion_id": "ION-CHLORATE",
    "cation_count": 1,
    "anion_count": 1
  },
  {
    "id": "PR-36",
    "direction": "name_to_formula",
    "formula_ascii": "NaClO",
    "name": "sodium hypochlorite",
    "cation_id": "ION-NA",
    "anion_id": "ION-HYPOCHLORITE",
    "cation_count": 1,
    "anion_count": 1
  },
  {
    "id": "PR-37",
    "direction": "name_to_formula",
    "formula_ascii": "KClO4",
    "name": "potassium perchlorate",
    "cation_id": "ION-K",
    "anion_id": "ION-PERCHLORATE",
    "cation_count": 1,
    "anion_count": 1
  },
  {
    "id": "PR-38",
    "direction": "name_to_formula",
    "formula_ascii": "Na2O2",
    "name": "sodium peroxide",
    "cation_id": "ION-NA",
    "anion_id": "ION-PEROXIDE",
    "cation_count": 2,
    "anion_count": 1
  },
  {
    "id": "PR-39",
    "direction": "name_to_formula",
    "formula_ascii": "Zn(C2H3O2)2",
    "name": "zinc acetate",
    "cation_id": "ION-ZN",
    "anion_id": "ION-ACETATE",
    "cation_count": 1,
    "anion_count": 2
  },
  {
    "id": "PR-40",
    "direction": "name_to_formula",
    "formula_ascii": "Ag2CO3",
    "name": "silver carbonate",
    "cation_id": "ION-AG",
    "anion_id": "ION-CARBONATE",
    "cation_count": 2,
    "anion_count": 1
  },
  {
    "id": "PR-41",
    "direction": "formula_to_name",
    "formula_ascii": "Na2S",
    "name": "sodium sulfide",
    "cation_id": "ION-NA",
    "anion_id": "ION-SULFIDE",
    "cation_count": 2,
    "anion_count": 1
  },
  {
    "id": "PR-42",
    "direction": "formula_to_name",
    "formula_ascii": "MgBr2",
    "name": "magnesium bromide",
    "cation_id": "ION-MG",
    "anion_id": "ION-BROMIDE",
    "cation_count": 1,
    "anion_count": 2
  },
  {
    "id": "PR-43",
    "direction": "formula_to_name",
    "formula_ascii": "FeCl2",
    "name": "iron(II) chloride",
    "cation_id": "ION-FE-II",
    "anion_id": "ION-CHLORIDE",
    "cation_count": 1,
    "anion_count": 2
  },
  {
    "id": "PR-44",
    "direction": "formula_to_name",
    "formula_ascii": "FeCl3",
    "name": "iron(III) chloride",
    "cation_id": "ION-FE-III",
    "anion_id": "ION-CHLORIDE",
    "cation_count": 1,
    "anion_count": 3
  },
  {
    "id": "PR-45",
    "direction": "formula_to_name",
    "formula_ascii": "Fe2O3",
    "name": "iron(III) oxide",
    "cation_id": "ION-FE-III",
    "anion_id": "ION-OXIDE",
    "cation_count": 2,
    "anion_count": 3
  },
  {
    "id": "PR-46",
    "direction": "formula_to_name",
    "formula_ascii": "Cu2O",
    "name": "copper(I) oxide",
    "cation_id": "ION-CU-I",
    "anion_id": "ION-OXIDE",
    "cation_count": 2,
    "anion_count": 1
  },
  {
    "id": "PR-47",
    "direction": "formula_to_name",
    "formula_ascii": "CuO",
    "name": "copper(II) oxide",
    "cation_id": "ION-CU-II",
    "anion_id": "ION-OXIDE",
    "cation_count": 1,
    "anion_count": 1
  },
  {
    "id": "PR-48",
    "direction": "formula_to_name",
    "formula_ascii": "CuSO4",
    "name": "copper(II) sulfate",
    "cation_id": "ION-CU-II",
    "anion_id": "ION-SULFATE",
    "cation_count": 1,
    "anion_count": 1
  },
  {
    "id": "PR-49",
    "direction": "formula_to_name",
    "formula_ascii": "Cu(NO3)2",
    "name": "copper(II) nitrate",
    "cation_id": "ION-CU-II",
    "anion_id": "ION-NITRATE",
    "cation_count": 1,
    "anion_count": 2
  },
  {
    "id": "PR-50",
    "direction": "formula_to_name",
    "formula_ascii": "Fe3(PO4)2",
    "name": "iron(II) phosphate",
    "cation_id": "ION-FE-II",
    "anion_id": "ION-PHOSPHATE",
    "cation_count": 3,
    "anion_count": 2
  },
  {
    "id": "PR-51",
    "direction": "formula_to_name",
    "formula_ascii": "SnCl4",
    "name": "tin(IV) chloride",
    "cation_id": "ION-SN-IV",
    "anion_id": "ION-CHLORIDE",
    "cation_count": 1,
    "anion_count": 4
  },
  {
    "id": "PR-52",
    "direction": "formula_to_name",
    "formula_ascii": "PbO2",
    "name": "lead(IV) oxide",
    "cation_id": "ION-PB-IV",
    "anion_id": "ION-OXIDE",
    "cation_count": 1,
    "anion_count": 2
  },
  {
    "id": "PR-53",
    "direction": "formula_to_name",
    "formula_ascii": "Co2O3",
    "name": "cobalt(III) oxide",
    "cation_id": "ION-CO-III",
    "anion_id": "ION-OXIDE",
    "cation_count": 2,
    "anion_count": 3
  },
  {
    "id": "PR-54",
    "direction": "formula_to_name",
    "formula_ascii": "CrCl3",
    "name": "chromium(III) chloride",
    "cation_id": "ION-CR-III",
    "anion_id": "ION-CHLORIDE",
    "cation_count": 1,
    "anion_count": 3
  },
  {
    "id": "PR-55",
    "direction": "formula_to_name",
    "formula_ascii": "(NH4)2CO3",
    "name": "ammonium carbonate",
    "cation_id": "ION-AMMONIUM",
    "anion_id": "ION-CARBONATE",
    "cation_count": 2,
    "anion_count": 1
  },
  {
    "id": "PR-56",
    "direction": "formula_to_name",
    "formula_ascii": "K2CrO4",
    "name": "potassium chromate",
    "cation_id": "ION-K",
    "anion_id": "ION-CHROMATE",
    "cation_count": 2,
    "anion_count": 1
  },
  {
    "id": "PR-57",
    "direction": "formula_to_name",
    "formula_ascii": "K2Cr2O7",
    "name": "potassium dichromate",
    "cation_id": "ION-K",
    "anion_id": "ION-DICHROMATE",
    "cation_count": 2,
    "anion_count": 1
  },
  {
    "id": "PR-58",
    "direction": "formula_to_name",
    "formula_ascii": "KMnO4",
    "name": "potassium permanganate",
    "cation_id": "ION-K",
    "anion_id": "ION-PERMANGANATE",
    "cation_count": 1,
    "anion_count": 1
  },
  {
    "id": "PR-59",
    "direction": "formula_to_name",
    "formula_ascii": "Ca(HCO3)2",
    "name": "calcium bicarbonate",
    "cation_id": "ION-CA",
    "anion_id": "ION-HYDROGEN-CARBONATE",
    "cation_count": 1,
    "anion_count": 2
  },
  {
    "id": "PR-60",
    "direction": "formula_to_name",
    "formula_ascii": "Cd(NO3)2",
    "name": "cadmium nitrate",
    "cation_id": "ION-CD",
    "anion_id": "ION-NITRATE",
    "cation_count": 1,
    "anion_count": 2
  }
]
```

## Hint ladder for every compiled pair

H1: Identify or look up the complete negative ion.  
H2: Reveal the two ion identities and charges.  
H3: Show positive and negative charge totals for the learner’s current counts.  
H4: Reveal the minimum ratio and conventional name/formula with explanation.

H4 exposure marks the current attempt as assisted/revealed. Never issue an independent-success event for copying that answer back.
