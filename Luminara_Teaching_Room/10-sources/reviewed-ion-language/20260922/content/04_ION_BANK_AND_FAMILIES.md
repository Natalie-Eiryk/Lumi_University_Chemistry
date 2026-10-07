---
document_id: LU-IONS-DESIGN-04
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Ion bank and the family wall

## Provenance and release boundary

This is a **62-entry working bank reconstructed from the ion-list transcription already present in the conversation**, including entries omitted from the shorter study proposal. The original `1117 Ion List.pdf` was located by Files metadata, but content reads returned no readable text/images and materialization returned no downloadable backing file during this build. Therefore this bank is not claimed to be newly checked against that PDF. [SRC-COURSE-IONS](15_SOURCES_AND_DECISIONS.md#src-course-ions)

Common instructional conventions were checked against the publisher and IUPAC sources identified in [03](03_CHEMISTRY_RULES_AND_BOUNDARIES.md). Exact course completeness and special-entry labels remain a Codex/Natalie source-reconciliation gate. Do not add ions because they happen to occur elsewhere in a textbook.

## Table contract

The rows below are the single bank authority inside this design packet. `formula_ascii` excludes charge; `charge` is a signed integer for the complete ion. `id` is stable; never key records only by formula, because Fe²⁺/Fe³⁺ and H⁺/H⁻ must remain distinct.

Tier 1 = first learning route; tier 2 = later retrieval expansion; tier 3 = explicitly source-sensitive or special-context reference. Tiers are proposed learning order, not instructor importance. A tier-1 designation does not mean the learner must memorize all tier-1 entries in one sitting.

| id | formula_ascii | charge | English label | Family | Tier |
|---|---|---:|---|---|---:|
| ION-H-PLUS | `H` | +1 | hydrogen ion | special | 3 |
| ION-LI | `Li` | +1 | lithium | group-1 | 2 |
| ION-NA | `Na` | +1 | sodium | group-1 | 1 |
| ION-K | `K` | +1 | potassium | group-1 | 1 |
| ION-RB | `Rb` | +1 | rubidium | group-1 | 2 |
| ION-CS | `Cs` | +1 | cesium | group-1 | 2 |
| ION-AMMONIUM | `NH4` | +1 | ammonium | polyatomic-cation | 1 |
| ION-HYDRONIUM | `H3O` | +1 | hydronium | polyatomic-cation | 3 |
| ION-AG | `Ag` | +1 | silver | fixed-course | 2 |
| ION-BE | `Be` | +2 | beryllium | group-2 | 2 |
| ION-MG | `Mg` | +2 | magnesium | group-2 | 1 |
| ION-CA | `Ca` | +2 | calcium | group-2 | 1 |
| ION-SR | `Sr` | +2 | strontium | group-2 | 2 |
| ION-BA | `Ba` | +2 | barium | group-2 | 2 |
| ION-ZN | `Zn` | +2 | zinc | fixed-course | 2 |
| ION-CD | `Cd` | +2 | cadmium | fixed-course | 2 |
| ION-AL | `Al` | +3 | aluminum | fixed-course | 1 |
| ION-GA | `Ga` | +3 | gallium | fixed-course | 2 |
| ION-CU-I | `Cu` | +1 | copper(I) | variable-metal | 1 |
| ION-CU-II | `Cu` | +2 | copper(II) | variable-metal | 1 |
| ION-AU-I | `Au` | +1 | gold(I) | variable-metal | 2 |
| ION-AU-III | `Au` | +3 | gold(III) | variable-metal | 2 |
| ION-CR-II | `Cr` | +2 | chromium(II) | variable-metal | 2 |
| ION-CR-III | `Cr` | +3 | chromium(III) | variable-metal | 2 |
| ION-FE-II | `Fe` | +2 | iron(II) | variable-metal | 1 |
| ION-FE-III | `Fe` | +3 | iron(III) | variable-metal | 1 |
| ION-CO-II | `Co` | +2 | cobalt(II) | variable-metal | 2 |
| ION-CO-III | `Co` | +3 | cobalt(III) | variable-metal | 2 |
| ION-SN-II | `Sn` | +2 | tin(II) | variable-metal | 2 |
| ION-SN-IV | `Sn` | +4 | tin(IV) | variable-metal | 2 |
| ION-PB-II | `Pb` | +2 | lead(II) | variable-metal | 2 |
| ION-PB-IV | `Pb` | +4 | lead(IV) | variable-metal | 2 |
| ION-FLUORIDE | `F` | -1 | fluoride | monatomic | 2 |
| ION-CHLORIDE | `Cl` | -1 | chloride | monatomic | 1 |
| ION-BROMIDE | `Br` | -1 | bromide | monatomic | 2 |
| ION-IODIDE | `I` | -1 | iodide | monatomic | 2 |
| ION-NITRATE | `NO3` | -1 | nitrate | nitrogen-oxyanion | 1 |
| ION-NITRITE | `NO2` | -1 | nitrite | nitrogen-oxyanion | 1 |
| ION-HYDROXIDE | `OH` | -1 | hydroxide | polyatomic-anchor | 1 |
| ION-PERMANGANATE | `MnO4` | -1 | permanganate | polyatomic-anchor | 2 |
| ION-ACETATE | `C2H3O2` | -1 | acetate | polyatomic-anchor | 2 |
| ION-HYDRIDE | `H` | -1 | hydride | monatomic | 3 |
| ION-PERCHLORATE | `ClO4` | -1 | perchlorate | chlorine-oxyanion | 2 |
| ION-CHLORATE | `ClO3` | -1 | chlorate | chlorine-oxyanion | 1 |
| ION-CHLORITE | `ClO2` | -1 | chlorite | chlorine-oxyanion | 1 |
| ION-HYPOCHLORITE | `ClO` | -1 | hypochlorite | chlorine-oxyanion | 2 |
| ION-CYANIDE | `CN` | -1 | cyanide | polyatomic-anchor | 2 |
| ION-HYDROGEN-CARBONATE | `HCO3` | -1 | bicarbonate | carbonate-family | 1 |
| ION-OXIDE | `O` | -2 | oxide | monatomic | 1 |
| ION-PEROXIDE | `O2` | -2 | peroxide | special-polyatomic | 2 |
| ION-SULFIDE | `S` | -2 | sulfide | monatomic | 2 |
| ION-SULFATE | `SO4` | -2 | sulfate | sulfur-oxyanion | 1 |
| ION-SULFITE | `SO3` | -2 | sulfite | sulfur-oxyanion | 1 |
| ION-CARBONATE | `CO3` | -2 | carbonate | carbonate-family | 1 |
| ION-CHROMATE | `CrO4` | -2 | chromate | chromium-oxyanion | 2 |
| ION-DICHROMATE | `Cr2O7` | -2 | dichromate | chromium-oxyanion | 2 |
| ION-PHOSPHIDE | `P` | -3 | phosphide | monatomic | 2 |
| ION-NITRIDE | `N` | -3 | nitride | monatomic | 1 |
| ION-PHOSPHATE | `PO4` | -3 | phosphate | phosphorus-oxyanion | 1 |
| ION-PHOSPHITE | `PO3` | -3 | phosphite | course-specific | 3 |
| ION-CARBIDE | `C` | -4 | carbide | course-specific | 3 |
| ION-SILICATE | `SiO4` | -4 | silicate | course-specific | 3 |


## Recognition cards: three fields, two retrieval directions

Each ion card has a name, a formula, and a charge. Name → formula+charge and formula+charge → name are separate retrieval skills. A recognized name with an uncertain charge should not count as fully recalled.

For example: sulfate ⇄ SO₄²⁻. Initially cover only the charge, then cover the whole formula, then reverse the prompt. Keep “sulfite SO₃²⁻” adjacent during explanation but interleave it with other families after a short delay.

## The family wall

| Anchor | Neighbor or contrast | What can be inferred after the anchor is known |
|---|---|---|
| nitrate NO₃⁻ | nitrite NO₂⁻ | one fewer O within this pair; same −1 charge |
| sulfate SO₄²⁻ | sulfite SO₃²⁻ | one fewer O within this pair; same −2 charge |
| phosphate PO₄³⁻ | course-listed phosphite PO₃³⁻ | course-pair pattern; special scope label stays visible |
| chlorate ClO₃⁻ | chlorite ClO₂⁻; hypochlorite ClO⁻; perchlorate ClO₄⁻ | positions on this specific four-member family |
| carbonate CO₃²⁻ | hydrogen carbonate/bicarbonate HCO₃⁻ | adding H⁺ changes the net charge by +1 |
| oxide O²⁻ | peroxide O₂²⁻ | one O atom versus an O₂ group; same total charge, different identity |
| chromate CrO₄²⁻ | dichromate Cr₂O₇²⁻ | recall as a linked pair; do not simply double chromate |
| ammonium NH₄⁺ | ammonia NH₃ | charged cation versus neutral molecule; ammonia is a contrast, not a bank ion |
| H⁺ | H⁻; H₃O⁺ | different charged species; hydrogen is not “always +1” |

## Explicit aliases

Accept `hydrogen carbonate` and `bicarbonate` as the same ion; present the course label on the answer card. Accept `aluminium` for aluminum and `caesium` for cesium as spelling variants, without changing the displayed course form. Allow `CH3COO` and `CH3CO2` as reviewed acetate formula aliases with charge −1. Allow `OCl` as a reviewed hypochlorite ordering alias. Do not automatically accept every permutation of symbols.

Optional traditional names such as ferric/ferrous should not be generated or graded until an explicit alias map and course policy are supplied. A missing Roman numeral is ambiguous for a variable metal even if the learner intended a familiar salt.

## Completeness and use policy

32 cations/charge-specific cation records + 30 anions = 62. A formula syntax validator may recognize all these ion records; an exercise generator must draw from the reviewed item bank, not the 32×30 Cartesian product. A charge-balanced combination alone is not evidence of a real stable material.

No real mixing, tasting, heating, or medical dosing accompanies these tiles. They are representations for naming and charge arithmetic.
