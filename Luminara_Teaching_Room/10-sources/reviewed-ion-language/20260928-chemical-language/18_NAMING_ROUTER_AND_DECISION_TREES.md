---
document_id: LU-CHEM-LANGUAGE-DESIGN-18
module_id: LU-CHEM-BONDING-NAMING-002
package_version: 1.1.0
status: design_candidate
created: 2026-09-28
---

# Naming router — choose the grammar before translating

## Router invariant

**Recognized chemical identity outranks a crude heuristic.** If the reviewed data says O₂²⁻ is peroxide, the engine must not call Na₂O₂ “sodium dioxide” merely because it sees two oxygens.

## Formula → name route

```text
START: formula
  |
  +-- Does the reviewed record identify a special/polyatomic ion?
  |       |
  |       +-- yes --> ionic constituent route
  |       |           identify cation + anion
  |       |           infer variable-metal charge if needed
  |       |           name without molecular prefixes
  |       |
  |       +-- no
  |
  +-- Does it match a supported metal + monatomic nonmetal salt?
  |       |
  |       +-- yes --> ionic route
  |
  +-- Is ammonium a constituent?
  |       |
  |       +-- yes --> ionic route
  |
  +-- Are all participating elements nonmetals in a supported binary molecular record?
  |       |
  |       +-- yes --> molecular prefix route
  |
  +-- Does H/state/context invoke acid or another future grammar?
  |       |
  |       +-- yes --> route/context gate
  |
  +-- otherwise --> unsupported / ask for context
```

## Name → formula route

```text
START: English name
  |
  +-- Roman numeral present?
  |      --> variable-charge ionic cation candidate
  |
  +-- Known polyatomic ion name present?
  |      --> ionic route; retrieve ion formula + charge
  |
  +-- Known fixed-charge metal + -ide anion?
  |      --> ionic route; balance charge
  |
  +-- Molecular numerical prefixes present?
  |      --> molecular route; prefixes become atom counts
  |
  +-- Known hydride/peroxide name?
  |      --> preserve that ion identity
  |
  +-- acid/hydrate/unsupported context?
         --> route elsewhere, do not guess
```

## Ionic grammar

1. Name cation first.
2. If variable-charge monatomic metal, include Roman numeral for its charge/oxidation state in this course model.
3. Name anion second.
4. Monatomic anion generally uses root + `-ide`.
5. Polyatomic anion keeps its reviewed ion name.
6. **No di-/tri-/tetra- prefixes to state ion counts.** Charge balance already determines the ratio.

Examples:

| Formula | Reasoning | Name |
|---|---|---|
| NaCl | Na⁺ + Cl⁻ | sodium chloride |
| CaCl₂ | Ca²⁺ + 2Cl⁻ | calcium chloride |
| FeCl₃ | 3Cl⁻ requires Fe³⁺ | iron(III) chloride |
| NH₄NO₃ | NH₄⁺ + NO₃⁻ | ammonium nitrate |
| LiH | Li⁺ + H⁻ | lithium hydride |
| Na₂O₂ | 2Na⁺ + O₂²⁻ | sodium peroxide |

## Molecular/covalent grammar

For the supported binary molecular domain:

1. first element keeps its element name;
2. first element uses a numerical prefix when count > 1; `mono-` is ordinarily omitted on the first element;
3. second element always gets a count prefix and an `-ide` form;
4. prefix indicates **atom count**, not charge;
5. do not reduce the molecular formula.

### Prefix bank

| Count | Prefix |
|---:|---|
| 1 | mono- |
| 2 | di- |
| 3 | tri- |
| 4 | tetra- |
| 5 | penta- |
| 6 | hexa- |
| 7 | hepta- |
| 8 | octa- |
| 9 | nona- |
| 10 | deca- |

Examples:

| Formula | Name |
|---|---|
| CO | carbon monoxide |
| CO₂ | carbon dioxide |
| N₂O | dinitrogen monoxide |
| N₂O₄ | dinitrogen tetroxide |
| N₂O₅ | dinitrogen pentoxide |
| PCl₃ | phosphorus trichloride |
| PCl₅ | phosphorus pentachloride |
| SF₆ | sulfur hexafluoride |
| CCl₄ | carbon tetrachloride |
| SO₃ | sulfur trioxide |

## Spelling handling

Do not implement molecular names by mechanical concatenation alone. Store or generate reviewed elisions:

- mono + oxide → monoxide;
- tetra + oxide → tetroxide;
- penta + oxide → pentoxide.

Accept pedagogically reasonable input variants only if the instructor/course convention permits them; preferred output should remain canonical.

## Two formulas that must never share a naming algorithm

### Na₂O₂

If a naive atom counter sees “two oxygens” and emits `dioxide`, the router failed. The constituent resolver must recognize peroxide O₂²⁻ and select ionic grammar.

### N₂O₄

If a “reduce to lowest terms” step changes N₂O₄ to NO₂, the router failed. Molecular identity preserves the full atom counts.

These should be permanent regression tests.

## Confidence language

The UI should say:

- “This matches the ionic naming route because…”
- “This matches the molecular prefix route because…”
- “This needs state/context before naming…”

Avoid absolute claims such as “all metal/nonmetal bonds are 100% ionic.”
