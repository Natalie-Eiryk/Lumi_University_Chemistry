---
document_id: LU-CHEM-LANGUAGE-DESIGN-28
package_id: LU-CHEMICAL-LANGUAGE
package_version: 1.1.0
status: design_candidate
created: 2026-09-28
---

# Copy/paste handoff prompt for Codex

Use the entire `Lumi_University_Chemical_Language_Design_v1.1.0` packet as a **design scaffold** for the existing Lumi University chemistry work.

First read `00_START_HERE.md`, `01_CODEX_IMPLEMENTATION_BRIEF.md`, `17_IONIC_VS_COVALENT_CONCEPT_MODEL.md`, `18_NAMING_ROUTER_AND_DECISION_TREES.md`, `23_CHEMICAL_LANGUAGE_DATA_CONTRACTS.md`, `24_CHEMICAL_LANGUAGE_TESTS.md`, and `25_CODEX_DELTA_IMPLEMENTATION_PLAN.md`.

Then inspect the current workspace before editing. Reuse the existing teaching-campus shell, chemistry/ion data, formula renderer/parser, learner progress storage, review system, launchers, and deployment pipeline. Do not create a competing application, launcher, learner database, or public site.

The implementation goal is to extend the existing ion-language capability with a deterministic **naming-route classifier** and teaching experience that distinguishes:

- ionic naming from molecular-prefix naming;
- constituent identity from raw atom count;
- internal covalent bonding in polyatomic ions from the ionic salt-level naming boundary;
- hydride H⁻ from hydrogen in molecular compounds;
- oxide O²⁻ from peroxide O₂²⁻;
- ionic formula-unit reduction from molecular formulas that must not be empirically reduced;
- variable-metal Roman numerals from molecular numerical prefixes;
- supported naming tasks from acid/hydrate/network/material cases that need another grammar or more context.

Start with the six-anchor vertical slice: `NaCl`, `CO2`, `NH4Cl`, `LiH`, `Na2O2`, `NaNO3`. Make the same parsed/recognized chemistry state flow through classifier -> boundary lens -> naming gate -> feedback -> learner progress.

Preserve the course-facing answer first. Deeper quantum/bonding nuance belongs in an optional `Under the Floorboards` layer and must not overwrite the expected introductory nomenclature.

Implement the smallest coherent adapters required by the current codebase. Stable existing learner/item IDs must not be silently renamed if progress may reference them. Runtime answer keys must come from reviewed deterministic records, not free-form LLM generation.

Run the repository's actual current validation/test commands plus the CLT-01–50 cases in `24_CHEMICAL_LANGUAGE_TESTS.md`. Return:

1. integration map and architecture choice;
2. changed files;
3. schema/data migrations;
4. exact test commands and results;
5. local route and screenshots at desktop/iPad widths;
6. keyboard/touch/accessibility notes;
7. source/course-convention gates still unresolved;
8. any deviations from the packet and the reason;
9. confirmation that no automatic public deployment or competing launcher was created.
