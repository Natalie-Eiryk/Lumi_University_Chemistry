---
document_id: LU-CHEM-LANGUAGE-DESIGN-19
module_id: LU-CHEM-BONDING-NAMING-002
package_version: 1.1.0
status: design_candidate
created: 2026-09-28
---

# Special cases and boundary objects

## Why this file exists

Special cases are not pedagogical clutter. They reveal **which level of description the rule actually applies to**. Lumi should use them after a basic pattern has formed, not before.

## Case 1 — peroxide: Na₂O₂

### Course-facing model

Peroxide is the polyatomic ion:

```text
O₂²⁻
```

Sodium is Na⁺. Two sodium ions balance one peroxide ion:

```text
2(+1) + (−2) = 0
```

Therefore:

```text
Na₂O₂ = sodium peroxide
```

### Why not sodium dioxide?

`di-` belongs to molecular-prefix grammar. This compound is being represented as ions. The two oxygens are part of the **peroxide ion's identity**, not an atom count that triggers molecular naming.

### Why not reduce Na₂O₂ to NaO?

The constituent ratio is:

```text
2 Na⁺ : 1 O₂²⁻
```

which is already minimal. Reducing atomic subscripts would mutate peroxide into a different constituent model.

### Under the Floorboards

Peroxide contains an O–O covalent bond internally. The salt still uses ionic naming because the boundary between Na⁺ and O₂²⁻ is the constituent boundary relevant to the formula unit.

## Case 2 — hydride: LiH

### Course-facing model

```text
Li⁺ + H⁻ → LiH
```

H⁻ is **hydride**. The name is lithium hydride.

### Learner bridge

Hydrogen is not permanently “+1.” Its formal role depends on chemical environment. With an electropositive alkali/alkaline-earth metal in these reviewed binary hydrides, hydrogen is represented as H⁻.

### Contrast

```text
LiH  -> ionic hydride route -> lithium hydride
HCl  -> molecular route when no aqueous context -> hydrogen chloride
```

If later presented as HCl(aq), route to the acid module rather than reusing the binary molecular name blindly.

## Case 3 — nitrate: NaNO₃

### Two boundaries

Inside nitrate, N and O share covalent bonding/delocalized electron density. At the compound level, Na⁺ and NO₃⁻ form the ionic constituent model.

```text
Na⁺ | NO₃⁻
     | internal N–O bonding
```

Name: sodium nitrate.

### Misconception catch

“Contains covalent bonds” does not imply “molecular naming prefixes should be used.”

## Case 4 — ammonium chloride: NH₄Cl

No metal is present, yet the compound is ionic in the introductory constituent model:

```text
NH₄⁺ + Cl⁻
```

This is the standard counterexample to a simplistic “metal = ionic, no metal = covalent” classifier.

## Case 5 — hydroxide salts

Ca(OH)₂ is calcium hydroxide.

- O–H bonding exists inside hydroxide;
- OH⁻ is treated as a polyatomic ion;
- Ca²⁺ requires two hydroxides;
- parentheses preserve two whole OH⁻ groups.

Again, internal covalent bonding and ionic compound classification coexist.

## Case 6 — variable-charge metal versus molecular prefix

```text
FeCl₃ = iron(III) chloride
PCl₃  = phosphorus trichloride
```

Both formulas contain three chlorines, but the names encode different things.

- In FeCl₃, chloride charge constrains Fe to +3; Roman numeral identifies the metal state.
- In PCl₃, `tri-` simply counts three chlorine atoms in the molecular formula.

This should be a side-by-side interaction.

## Case 7 — molecular formulas are not empirical formulas

```text
N₂O₄ = dinitrogen tetroxide
```

The learner may notice the atom ratio reduces to NO₂. That reduced ratio is an empirical composition, not the same molecular formula. The naming worksheet is asking for molecular identity/counts, so keep N₂O₄.

## Case 8 — elemental diatomic substances are not binary compounds

Cl₂, O₂, N₂, H₂, F₂, Br₂, and I₂ are elemental forms, not “dichloride,” “dioxygenide,” etc. If the task is naming compounds, route these to an elemental-substance state rather than forcing compound grammar.

## Cases deliberately deferred

These require later modules or explicit course context:

- acids (`HCl(aq)`, `H₂SO₄` in acid context);
- hydrates (`CuSO₄·5H₂O`);
- network covalent solids (`SiO₂` requires careful course convention);
- metallic/intermetallic materials;
- coordination complexes;
- organic nomenclature;
- mixed-valence solids;
- superoxide and other oxygen species unless added to the course bank.

The router should say **needs another naming model**, not guess.
