# 03 · Chemistry reference and validation contract

## Status and boundaries

This is an authored chemistry-content contract, not a working native API, a compiled runtime data package, a chemical simulation, or proof that future C++ validation has passed. `reference_data.json` is the concrete reference deliverable. Schema `1.0.0`; content version `2026-10-06.1`; sources accessed 6 October 2026. The 118 reference elements are distinct from the packet's activity inventory.

Included: 118 element identities and layout positions, 20 neutral ground-state configurations with explicit occupancy and neutral main-group valence/core counts, 23 selected monatomic teaching-ion charge choices, 12 polyatomic ions, and the Cr/Cu exception examples. Excluded: atomic masses, universal oxidation-state lists, exhaustive stable ions, blanket material classification, isotope calculations, excited states, transition-metal ion configuration generation, and unsupported predictions about superheavy-element chemistry. Omitted fields are unavailable, not zero.

## 1. Element identity and table layout

`atomic_number` is the stable identity, an integer 1–118. Symbols are unique and case-sensitive. Names use IUPAC spellings; aluminium/aluminum and caesium/cesium can be search synonyms without changing canonical content. An atom or ion retains its element identity when electrons change. Never change the atomic number to make a charged atom resemble a noble gas.

`period` is 1–7. `group` is 1–18 for main-body cells. All La–Lu and Ac–Lr records intentionally have `group: null` and `block: null`; `display_region` names the detached series. This classroom convention avoids declaring one universal group-3 boundary or calling all 15 entries a 14-position orbital block. It does not imply that their chemistry is unknown. Main-body placeholders at period 6/7, group 3 link to these series and do not duplicate an element. Detached display rows 8 and 9, columns 3–17, are screen coordinates, not chemical periods or groups. A future 32-column view may use different screen coordinates while retaining identities.

Hydrogen is a nonmetal placed in group 1; it is not an alkali metal. Helium is group 18 and has configuration 1s²: it is an s-block element with two valence electrons, not a p-block octet. The dataset distinguishes chemical block from display column. Use family names only with a documented mapping; do not infer every group-1 element is a metal. Do not infer a transition-element definition simply from a d-region color. Group numbering and series terminology are grounded in [IUPAC's periodic-table guidance](https://iupac.org/what-we-do/periodic-table-of-elements/); identities were checked against [IUPAC's element selector](https://iupac.org/periodic-table-challenge/).

## 2. Electrons and configuration grading

The concrete configuration records cover neutral H through Ca only. Occupancy is machine-readable, while `configuration_ascii` is a display/export convenience. Sum occupancy to get the electron total. A neutral atom has Z electrons; an ion with signed charge q has Z − q electrons. Reject negative electron totals. A positive charge means fewer electrons, never more protons.

For these neutral main-group records, valence means electrons at the largest occupied principal quantum number n; core = Z − valence. Thus H: 1/0, He: 2/0, Na: 1/10, Cl: 7/10, Ar: 8/10, Ca: 2/18 (valence/core). Helium is the explicit group-18 exception. These are not universal valence rules for d/f elements; transition-metal bonding may involve ns and (n−1)d electrons, with context-dependent bookkeeping.

The occupancy validator must enforce valid subshells and capacities (s ≤ 2, p ≤ 6, d ≤ 10, f ≤ 14), nonnegative integral counts, electron total, and equality to the supported reference ground state. Correct total alone is insufficient: an excited configuration can have the right electron count. Compare maps, not whitespace or written orbital ordering. Expand recognised noble-gas shorthand before comparison. H has no preceding noble-gas core. Use [NIST reference configurations](https://www.nist.gov/pml/atomic-reference-data-electronic-structure-calculations/atomic-reference-data-electronic-8) as factual ground-state references, not a simple filling algorithm extrapolated to every atom.

Chromium is [Ar] 3d⁵ 4s¹; copper is [Ar] 3d¹⁰ 4s¹. These illustrate that a naive Aufbau generator is not authoritative. For introductory cation examples remove highest-n electrons first, so Fe loses 4s before 3d; do not simply reverse the displayed filling order. This is a teaching procedure with a bounded species set, not a universal ion ground-state engine. NIST records include rearrangements for some singly charged transition-metal ions. Before adding a graded ion configuration, store and review that specific species' reference. [OpenStax 6.4](https://openstax.org/books/chemistry-2e/pages/6-4-electronic-structure-of-atoms-electron-configurations) supplies the introductory convention.

Never copy a neutral atom's valence/core numbers onto its ion. For Na⁺ the electron count is 10 and Z remains 11. A question about the ion's outermost occupied shell has a different convention from a question about the electrons removed from neutral Na. MVP ion tasks grade charge and electron count only unless the prompt explicitly supplies an ionic-shell convention and species-specific answer key.

## 3. Selected ion library and bonding scope

The monatomic list contains selected instructional charges, not all possible oxidation states or all ions an element can form. An empty selection is not proof that no ion exists. Fe(II)/Fe(III) and Cu(I)/Cu(II) require an explicit charge/name choice. Never infer the intended Fe charge from its group. Roman numerals in ion names specify oxidation state in the named compound; do not equate oxidation state with an atom count or universally with a local physical charge.

The 12 polyatomic records are ammonium, hydroxide, nitrate, nitrite, sulfate, sulfite, carbonate, hydrogen carbonate, phosphate, acetate, hydrogen sulfate, and permanganate. Each stores formula, integral net charge, atom map and atom total separately. Acetate's approved CH3COO alias maps to the same ion ID as C2H3O2. Other same-composition formulas are not automatically declared the same species or structure. Names/formulas/charges are checked against [OpenStax's common-ion table](https://openstax.org/books/chemistry-2e/pages/2-6-ionic-and-molecular-compounds).

Bonding tiles may say “often ionic” for common selected metal/nonmetal pairs and “often covalent” for selected nonmetal pairs. This is a heuristic with curated exceptions, not an authoritative binary classifier. NH4Cl is ionic overall despite containing only nonmetal elements, and contains covalent bonds within NH4⁺. Pure aluminium chloride is a caution case with substantial covalent character and phase-dependent structures; it must not be stamped universally ionic merely from Al + Cl. OsO4 is a molecular metal-containing counterexample, not evidence for free Os⁸⁺ ions. References: [OpenStax's explicit heuristic limits and AlCl3 example](https://openstax.org/books/chemistry-2e/pages/2-6-ionic-and-molecular-compounds) and [NIST's osmium tetraoxide record and gas-phase studies](https://webbook.nist.gov/cgi/cbook.cgi?ID=C20816120&Mask=20&Units=CAL). Unreviewed formulas return “outside this activity's model,” not a confident guess. No reaction, toxicity, experimental feasibility or synthesis claims follow from a valid formula.

## 4. Formula representation and parsing contract

Store three different things: original entered text, a parsed syntax tree retaining groups, and a computed atom map. A species also has an explicit signed net charge and a curated ion ID when applicable. A formula's text and atom map alone cannot reveal all charge, bonding, structure, phase or species identity.

The core formula grammar accepts case-sensitive element symbols and positive decimal integer multiplicities, with balanced parentheses for grouped repeats. Missing count means one. Formula input is not a chemical equation: no leading coefficient, plus-separated reactants, arrows, hydrate dot, isotope prefix, oxidation-state label or coordination-bracket syntax in MVP. Unsupported valid chemistry gets an unsupported-format message rather than “chemically impossible.” Reject unknown symbols, empty groups, zero/negative/fractional subscripts, unbalanced groups and trailing garbage. Set deterministic input, nesting, count and arithmetic-overflow limits before release, with separately tested limit errors.

### Normalization is syntax-aware

1. Trim outer whitespace. Reject internal whitespace in element formulas rather than silently joining tokens. Configuration fields have a separate whitespace policy.
2. Convert Unicode subscript digits to count tokens while retaining their original source spans. Do not apply blind NFKC first: that can collapse superscript charge digits into atom counts.
3. Recognise terminal Unicode superscript charges, e.g. Fe²⁺ and SO₄²⁻. Map superscript signs and Unicode minus to signed charge tokens only in the charge position.
4. Canonical ASCII charge syntax is a caret followed by optional positive magnitude and terminal sign: Fe^2+, SO4^2-, NH4^+. A terminal bare sign may be accepted only after a formula ending in a letter or closing parenthesis (Na+, Cl-); a digit immediately before a bare sign is rejected as ambiguous and receives a rewrite suggestion. Thus NH4+ is requested as NH4^+ or NH₄⁺, not guessed.
5. Fe2 means two iron atoms with no explicit charge. Never repair it to Fe²⁺. Fe2+ is rejected as ambiguous; ask for Fe^2+ for a single iron(II) ion. A separate charge control is the preferred beginner path.
6. Co is cobalt; CO is one C and one O. Never case-fold symbols. Reject co, suggesting that symbol case matters without silently choosing an intent.
7. Display can render counts as subscripts and charges as superscripts, but accessibility text says “two plus charge,” distinctly from “two atoms.” Preserve source spans for useful errors.

## 5. Mathematical validators

### Atom count

Walk the syntax tree recursively. An element node contributes its multiplicity; a group multiplies every child contribution by its repeat count. Ca(NO3)2 gives Ca:1, N:2, O:6, total 9. (NH4)2SO4 gives N:2, H:8, S:1, O:4, total 15. Charge is stored separately and never included in an atom total. NH4⁺ has five atoms and net charge +1.

### Ionic formula construction

Given a selected cation with q+ > 0 and anion with q− < 0, let g = gcd(q+, |q−|), cation count a = |q−|/g, anion count b = q+/g. Require a*q+ + b*q− = 0 and gcd(a,b) = 1. Reduce the ratio of whole ions, never the internal formula of either ion. Keep polyatomic IDs in the tree; parentheses are required around a polyatomic ion when its multiplicity exceeds one. Omit displayed count 1. Ca²⁺ and NO3⁻ yield Ca(NO3)2. NH4⁺ and SO4²⁻ yield (NH4)2SO4. Do not claim neutrality proves actual compound existence.

A wrong expanded formula such as CaN2O6 has the same atom map as Ca(NO3)2 but loses the nitrate group representation. In a “write the ionic formula preserving ions” exercise return a grouping-specific correction, not a correct score based solely on the atom map. An atom-count exercise can still count it correctly. Rubrics explicitly choose which equivalence they test.

### Molecular formula construction

Use the problem's specified molecular subscripts or naming rules. Never automatically reduce a molecular formula: N2O4 and NO2 are different formulas; H2O2 must not become HO. Atom ratios alone do not identify the molecule. “Empirical formula” must be a separately named task with a separate validator. Polyatomic ionic formulas likewise cannot be reduced by taking the gcd of all atomic subscripts.

### Outcome contract

Return structured outcomes: `correct`, `incorrect`, `needs_clarification`, `invalid_syntax`, `unsupported_scope`, plus a stable reason code, the offending source span when applicable, and a next-step explanation. Do not conflate parsing, mathematical consistency, chemical reference agreement, pedagogical notation and real-world existence. Retry feedback should identify the earliest relevant misconception without replacing the student's whole answer immediately.

## 6. Required future acceptance tests

These are requirements for the implementation, not claims of executed native tests.

| Input/task | Required result |
|---|---|
| H family | Nonmetal, not alkali metal |
| He group/block/configuration | 18 / s / 1s²; valence 2 |
| La or Lu group in this layout | null; detached-series explanation |
| Ca neutral configuration | 20 electrons; valence 2; core 18 |
| Ca 1s²2s²2p⁶3s²3p⁶3d² | Right total but wrong neutral ground state |
| Cr / Cu naive filling outputs | Reject against exception reference |
| Na⁺ particle count | 11 protons, 10 electrons |
| Fe²⁺ configuration exercise without reference | Unsupported scope, not guessed |
| Co / CO | Distinct element maps |
| co | Invalid case; no silent normalization |
| Fe2 | Fe:2, no explicit charge |
| Fe2+ | Needs clarification; suggest caret/superscript |
| Fe^2+ / Fe²⁺ | Same one-Fe, +2 species |
| SO4^2- / SO₄²⁻ | S:1, O:4, charge −2 |
| NH4⁺ | Five atoms; charge +1 |
| NH4+ | Needs unambiguous charge notation |
| Ca(NO3)2 | Nine atoms, retains nitrate grouping |
| (NH4)2SO4 | Fifteen atoms, retains ammonium grouping |
| CaN2O6 in nitrate-builder | Atom map equal, notation/grouping correction |
| Al³⁺ + O²⁻ | Al2O3; 2(+3)+3(−2)=0 |
| Ca²⁺ + O²⁻ | CaO, not Ca2O2 |
| N2O4 molecular task | Preserve N2O4, no gcd reduction |
| H2O2 molecular task | Preserve H2O2 |
| NH4Cl heuristic task | Curated ionic compound; polyatomic covalent bonds |
| AlCl3 / OsO4 heuristic | Show reviewed caveat/counterexample |
| Qq2 / H0 / (OH / ()2 | Syntax error with useful location |
| 2H2O / CuSO4·5H2O | Unsupported coefficient/hydrate format |
| Huge count/deep nesting | Bounded, deterministic limit error; no crash |
| Absent oxidation-state field | Unavailable; never infer universal 0 or impossible |

## 7. Provenance, rights and change control

All prose, schema choices, feedback rules and test cases here are newly authored. Reference facts are minimally transcribed with citations. No third-party table image, bulk numeric database, textbook passage or scientific artwork is packaged. This packet does not claim a universal open license over cited material or endorse copying whole source databases. IUPAC, NIST and OpenStax have source-specific terms; inspect them before expanding data imports or redistributing their figures/prose. In particular, a government-hosted compilation is not automatically a blanket license for every included item.

A production import must pin source edition/date, record field-level provenance and review status, validate schema and referential integrity, generate any native read-only table reproducibly, and expose content version for bug reports. A reviewed content update changes the dataset version; a breaking field/meaning change also changes the schema version. Do not fetch chemistry facts live during a graded exercise. Source corrections trigger affected answer-key and regression-test review, not silent replacement mid-session.

## 8. Actual packet-level checks completed

The authored JSON was parsed successfully and checked for 118 unique atomic numbers/symbols, continuous Z = 1–118, valid periods and layout positions, 20 configuration electron totals, correct valence-plus-core totals, 12 polyatomic formula/count/charge records, and finite integer charge choices. The reference contains 23 selected monatomic ion entries. First-20 configuration records and Cr/Cu examples were checked against the NIST table; all 118 names/symbols were cross-checked with IUPAC's selector. These are content checks only. Parsing, C++ behavior, rendering, accessibility, educational assessment and integration remain to be implemented and tested by the future application.
