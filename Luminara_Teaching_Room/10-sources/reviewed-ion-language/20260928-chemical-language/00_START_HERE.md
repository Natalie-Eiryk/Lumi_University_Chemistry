---
document_id: LU-CHEM-LANGUAGE-DESIGN-00
package_id: LU-CHEMICAL-LANGUAGE
package_version: 1.1.0
status: design_candidate
created: 2026-09-28
supersedes_packet: Lumi_University_Ion_Language_Design_v1.0.0
implementation_status: not_implemented_by_this_packet
---

# Chemical Language — Lumi University design packet v1.1

## What changed

Version 1.1 keeps the complete **Ion Language: Name ↔ Formula** foundation and adds a second scaffold: **Ionic vs Covalent: classify the boundary before choosing the naming grammar**.

The new design exists because three learner questions expose one missing layer:

- Why is **Na₂O₂** *sodium peroxide* rather than *sodium dioxide*?
- Why is **LiH** *lithium hydride* instead of a prefix-named molecule?
- How can a compound such as **NaNO₃** be called ionic when nitrate itself contains covalent N–O bonding?

The answer is that naming depends first on **what kind of chemical objects the formula is assembling**. The learner must identify the relevant boundary before applying a suffix or prefix.

## North-star capability

Given a formula or English name, the learner should be able to:

1. identify the likely constituent objects: monatomic ions, polyatomic ions, or covalently bonded atoms;
2. classify the **course-level naming route** as ionic, molecular/covalent, or context-dependent;
3. state why that route was chosen instead of merely pattern matching;
4. apply the correct grammar:
   - ionic: cation + anion, charge balance, Roman numeral when required, no molecular prefixes;
   - molecular: prefixes communicate atom counts, second element ends in `-ide`, no charge balancing;
5. preserve special constituent identity such as peroxide O₂²⁻ or hydride H⁻;
6. recognize nested cases where a polyatomic ion is covalently bonded internally but participates as an ion in an ionic solid;
7. route acids, hydrates, network solids, metals, and ambiguous/out-of-scope cases rather than guessing.

## One model, two linked modules

| Module | Stable design ID | Primary question |
|---|---|---|
| Ion Language | `LU-CHEM-IONS-001` | What ions are present, what are their charges, and how do they balance? |
| Bonding & Naming Router | `LU-CHEM-BONDING-NAMING-002` | Which naming grammar applies, and at what structural boundary? |

Do **not** implement these as isolated apps. They should share ion records, compound records, formula parsing, learner evidence, and rendering.

## Read order for Codex

1. [01_CODEX_IMPLEMENTATION_BRIEF.md](01_CODEX_IMPLEMENTATION_BRIEF.md)
2. [17_IONIC_VS_COVALENT_CONCEPT_MODEL.md](17_IONIC_VS_COVALENT_CONCEPT_MODEL.md)
3. [18_NAMING_ROUTER_AND_DECISION_TREES.md](18_NAMING_ROUTER_AND_DECISION_TREES.md)
4. [19_SPECIAL_CASES_AND_BOUNDARY_OBJECTS.md](19_SPECIAL_CASES_AND_BOUNDARY_OBJECTS.md)
5. [23_CHEMICAL_LANGUAGE_DATA_CONTRACTS.md](23_CHEMICAL_LANGUAGE_DATA_CONTRACTS.md)
6. [24_CHEMICAL_LANGUAGE_TESTS.md](24_CHEMICAL_LANGUAGE_TESTS.md)
7. Then inspect the inherited ion-language files 02–16 and lessons L01–L06.

## New lesson sequence

| Lesson | Purpose |
|---|---|
| [L07](lessons/L07_CLASSIFY_THE_BOUNDARY.md) | Decide what kind of objects the formula is assembling. |
| [L08](lessons/L08_IONIC_NAMING_ROUTE.md) | Use ionic grammar, including hydride and peroxide. |
| [L09](lessons/L09_MOLECULAR_NAMING_ROUTE.md) | Use prefix grammar for molecular compounds. |
| [L10](lessons/L10_NESTED_BONDING_AND_TRANSFER.md) | Polyatomic ions, mixed boundaries, continuum, and transfer. |

## High-value distinction

The software and teaching language should repeatedly separate:

```text
COMPOSITION        What atoms are present?
CONSTITUENTS       What chemical units are being treated as units?
BOUNDARY           Which interaction are we classifying/naming?
GRAMMAR            Ionic names or molecular-prefix names?
```

This prevents `Na₂O₂ → sodium dioxide` and prevents “contains covalent bonds” from being treated as equivalent to “must be a molecular compound.”

## Course-first, deeper layer second

The course-facing classifier is intentionally practical:

- recognized cation + recognized anion → ionic naming route;
- metal + monatomic nonmetal in the covered domain → usually ionic route;
- ammonium + anion → ionic route even though no metal is present;
- two nonmetals, no recognized ion/context override → molecular route;
- acid/hydrate/network/metallic/unsupported → explicit route gate.

An optional **Under the Floorboards** layer then explains that ionic/covalent character is not a perfect binary in quantum mechanics, that electron density can be polarized, and that polyatomic ions contain internal covalent bonding.

## Handoff intent

This packet is a scaffold and data-design contract, not a mandate to reproduce Markdown verbatim. Codex should turn it into connected visual, symbolic, auditory, tactile, and retrieval experiences using the existing Lumi University infrastructure. No competing launcher, no parallel learner database, no automatic public deployment.
