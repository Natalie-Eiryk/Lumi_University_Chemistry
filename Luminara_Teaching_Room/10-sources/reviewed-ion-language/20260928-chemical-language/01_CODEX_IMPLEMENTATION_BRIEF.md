---
document_id: LU-CHEM-LANGUAGE-DESIGN-01
package_id: LU-CHEMICAL-LANGUAGE
package_version: 1.1.0
status: design_candidate
created: 2026-09-28
implementation_status: not_implemented_by_this_packet
---

# Codex implementation brief — extend Ion Language into a Chemical Language router

## Mission

Extend the existing Lumi University ion-language work. Do **not** replace it. The new capability should let the learner classify an introductory formula/name into the correct naming route and explain the boundary used to make that decision.

The implementation must support the contrast among:

- `Na₂O` — sodium oxide;
- `Na₂O₂` — sodium peroxide, where O₂²⁻ is a constituent ion and the formula must not be reduced to NaO;
- `CO₂` — carbon dioxide, where `di-` is molecular-prefix grammar;
- `LiH` — lithium hydride, modeled as Li⁺ + H⁻ in this introductory ionic context;
- `HCl` — molecular hydrogen chloride when no aqueous-acid context is supplied;
- `NaNO₃` — an ionic salt built from Na⁺ and NO₃⁻ even though nitrate has internal covalent N–O bonding;
- `NH₄Cl` — ionic despite containing no metal because ammonium is a recognized cation.

## Phase 0 — inspect current workspace

Before edits, inspect current `AGENTS.md`, module registry, chemistry data, ion-language implementation state, formula parser, renderer, learner-progress store, review scheduler, tests, launcher, and any work-in-progress branches. Build an integration map. Do not assume the September design packet is identical to current code.

Required questions:

| Concern | Resolve before implementation |
|---|---|
| Existing ion module status | Was `LU-CHEM-IONS-001` implemented, renamed, partially implemented, or still design-only? |
| Chemistry content root | What Dewey/content path is canonical now? |
| Formula AST | Can it preserve polyatomic constituents and distinguish Na₂O₂ from a reducible monatomic-ion ratio? |
| Compound classifier | Is there already a task router? Extend it rather than creating a second classifier. |
| Learner evidence | Can classification, naming, and explanation be recorded as separate evidence? |
| Audio | Is browser speech/audio already available? Reuse; do not add a cloud dependency just for this module. |
| Privacy | Where are notebook text and attempts stored? Keep learner-owned notes private by default. |

## Phase 1 — vertical slice

Build one connected route using six anchors:

1. NaCl — obvious ionic binary;
2. CO₂ — obvious molecular binary;
3. NH₄Cl — ionic without metal;
4. LiH — metal hydride;
5. Na₂O₂ — peroxide identity lock;
6. NaNO₃ — nested covalent-inside-ionic boundary.

For each anchor, the learner should be able to:

- classify the naming route;
- reveal the evidence used;
- name formula → English;
- reverse English → formula where appropriate;
- inspect a boundary lens;
- receive targeted feedback on the smallest broken step.

## Phase 2 — naming router

Implement the reviewed decision tree in [18](18_NAMING_ROUTER_AND_DECISION_TREES.md). Route order matters. **Known constituent identity outranks a crude metal/nonmetal heuristic.** In particular:

- O₂²⁻ must resolve as peroxide before a generic oxygen parser reduces or prefix-names the formula;
- NH₄⁺ must route ionic even though there is no metallic element;
- H with a metal may route to hydride when the reviewed compound record supports it;
- HCl must retain state/context sensitivity and must not be silently converted to acid naming.

No runtime LLM should invent the route or answer key for assessed items.

## Phase 3 — molecular prefix grammar

Add reviewed prefix support: mono, di, tri, tetra, penta, hexa, hepta, octa, nona, deca. The first element ordinarily omits `mono-`; the second element gets prefix + modified root + `-ide`. Support reviewed spelling forms such as monoxide and pentoxide. Use explicit answer records rather than a naive string chop for irregular roots.

Molecular formulas are **not reduced to empirical ratios** for naming. `N₂O₄` remains dinitrogen tetroxide, not NO₂.

## Phase 4 — boundary lens

The UI should be able to show nested structure without pretending the diagram is a complete quantum calculation.

Example Na₂O₂:

```text
[Na⁺]   [ O—O ]²⁻   [Na⁺]
  \_______ ionic bookkeeping ______/
            ↑
      O—O bond is internal
```

Example NaNO₃:

```text
Na⁺  |  NO₃⁻
ionic|  nitrate has internal covalent bonding/resonance
boundary
```

Use language such as “course-level classification of this boundary,” not “all bonding everywhere in the substance is purely ionic.”

## Phase 5 — adaptive practice

Compile the new prompt bank and route evidence separately:

- classification accuracy;
- naming grammar selection;
- constituent recognition;
- charge reasoning;
- prefix/count reasoning;
- special-case recognition;
- confidence/support use.

A learner may know the name but classify for the wrong reason; store that separately when the interaction elicits reasoning.

## Non-goals

Do not build a full valence-bond/MO solver, crystal-structure simulator, acid nomenclature course, organic nomenclature engine, or exhaustive materials classifier. Do not use electronegativity cutoff alone as a truth oracle. Do not automatically publish or canonize.

## Required handback

Return changed paths, adapters added, schemas touched, exact tests run/results, local route, screenshots at desktop/iPad widths, keyboard/touch behavior, any source/course-convention gates, and explicit deviations from this packet with rationale.
