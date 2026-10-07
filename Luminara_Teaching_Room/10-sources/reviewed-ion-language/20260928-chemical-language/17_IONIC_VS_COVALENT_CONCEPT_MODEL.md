---
document_id: LU-CHEM-LANGUAGE-DESIGN-17
module_id: LU-CHEM-BONDING-NAMING-002
package_version: 1.1.0
status: design_candidate
created: 2026-09-28
---

# Ionic vs covalent — classify the boundary before naming

## The learner problem

“Ionic versus covalent” often gets taught as a two-column memorization chart. That works until the learner sees Na₂O₂, LiH, NH₄Cl, or NaNO₃. The module should therefore teach **classification as a boundary decision**, not as a claim that every bond inside a formula has one character.

## The four-layer model

### 1. Composition
What atoms are present and in what counts?

`Na₂O₂` contains two Na and two O atoms.

### 2. Constituents
What objects are treated as persistent units in the naming model?

`Na₂O₂` is modeled as two Na⁺ ions and one peroxide ion O₂²⁻.

### 3. Boundary
Which interaction is the current question classifying?

The salt is classified through the cation/anion boundary as ionic. Inside peroxide, the O–O connection is covalent.

### 4. Naming grammar
Which language convention follows from that constituent/boundary choice?

`Na₂O₂` → **sodium peroxide**, not sodium dioxide.

This four-layer model should be visible in the UI and feedback.

## Course-level classification rules

These are high-value **routing heuristics**, not universal laws of nature.

| Evidence | Default naming route | Why |
|---|---|---|
| reviewed cation + reviewed anion | ionic | compound is represented as a charge-balanced ion assembly |
| metal + monatomic nonmetal | usually ionic | common introductory salt pattern |
| ammonium + anion | ionic | NH₄⁺ is a cation even though no metal is present |
| two nonmetals, no recognized ion/context override | molecular/covalent | atom counts are communicated with prefixes |
| H + strongly electropositive metal in reviewed hydride record | ionic hydride | H is represented as H⁻ |
| acid state/context, hydrate, network solid, metallic material, complex | route elsewhere | different grammar/model is required |

## Ionic route: what the learner should notice

Ionic naming asks **which ions** are present, not how many atoms should receive Greek prefixes.

For Na₂O:

- Na is a fixed +1 cation;
- oxide is O²⁻;
- 2(+1) + (−2) = 0;
- name: sodium oxide.

For Na₂O₂:

- peroxide is O₂²⁻, one recognized ion;
- two Na⁺ balance one O₂²⁻;
- name: sodium peroxide;
- atomic subscripts are not reduced because the **ion ratio** 2 Na⁺ : 1 peroxide is already minimal.

## Molecular route: what the learner should notice

Molecular naming asks how many atoms of each element are in a discrete molecular formula.

For CO₂:

- C and O are both nonmetals;
- no recognized ionic constituent overrides the route;
- one carbon → `carbon` (first-element mono omitted);
- two oxygen → `dioxide`;
- name: carbon dioxide.

For N₂O₄:

- two nitrogen → dinitrogen;
- four oxygen → tetroxide;
- do **not** reduce N₂O₄ to NO₂, because a molecular formula describes molecule identity, not a lowest ion ratio.

## The most important nested case

A polyatomic ion can be **covalently bonded internally and still be an ion**.

NaNO₃ therefore supports both statements:

- nitrate contains covalent N–O bonding/delocalized electron density;
- sodium nitrate is classified/named as an ionic compound made from Na⁺ and NO₃⁻.

These statements describe different boundaries. The UI should never force the learner to choose one as though the other were false.

## Hydrogen is a switch, not a single rule

Hydrogen commonly participates in several models.

### Metal hydride example: LiH

Course model:

```text
Li → Li⁺ + e⁻
H + e⁻ → H⁻
Li⁺ + H⁻ → LiH
```

Name: **lithium hydride**.

Do not prefix-name it “lithium monohydride” in the ordinary ionic naming route.

### Nonmetal example: HCl

Without aqueous acid context, HCl is a covalent molecular compound and is called **hydrogen chloride**. If the course later supplies `HCl(aq)`, acid nomenclature becomes a separate context-sensitive route. Do not silently convert one into the other.

## Under the Floorboards — the binary is a model

At the electronic-structure level, “ionic” and “covalent” are not perfect mutually exclusive boxes. Electron density can be polarized; ions can distort each other; solids are many-particle quantum systems. Electronegativity difference can support intuition but no single cutoff should serve as the software’s truth oracle.

For this module, the question is narrower and pedagogically useful:

> **Which constituent model and naming grammar does this introductory exercise require?**

That keeps the course answer stable without telling the learner a false story about nature being divided by a hard line.

## Misconception catches

### “If it contains a covalent bond, the whole compound must be covalent.”
Upgrade: polyatomic ions contain internal covalent bonding but can form ionic salts.

### “If there is no metal, it cannot be ionic.”
Upgrade: NH₄Cl is ionic because NH₄⁺ is a recognized cation.

### “If there is a metal, every interaction is purely ionic.”
Upgrade: metal + nonmetal is a useful naming heuristic; deeper bonding character is continuous and boundary-dependent.

### “If all atomic subscripts share a factor, reduce them.”
Upgrade: reduce a simple ionic **ion ratio** when appropriate. Do not destroy peroxide/polyatomic identity, and never reduce a molecular formula merely to make smaller integers.

### “Prefixes tell me the charge.”
Upgrade: prefixes count atoms in molecular naming. Ionic charges come from ion identity/oxidation state and charge balance.
