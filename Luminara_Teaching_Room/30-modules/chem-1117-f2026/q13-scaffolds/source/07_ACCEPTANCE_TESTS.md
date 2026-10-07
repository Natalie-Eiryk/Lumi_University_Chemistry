---
document_id: 07_ACCEPTANCE_TESTS
package_id: LU-CHEM-Q13-SCAFFOLDS
version: 0.1.0
status: editorial_draft
created: 2026-09-28
visibility: editorial
integration_mode: additive_scaffold_overlay
assessment_owner: existing_native_exercises
---

# Acceptance and regression tests — implementation specification

## Status

The following **40 tests are specified for Codex**. They are not claimed as executed application tests. The package-level QA in the final document covers only links, IDs, embedded JSON, fixture arithmetic, and artifact construction.

Native checker changes require their own source review. This overlay does not override those checks merely to make these tests pass.

| ID | Behavior | Expected result |
|---|---|---|
| T01 | Type-only repair | CR-329 CS₂ agrees; CR-330 ionic disagrees. Keep the formula and its status; offer SCF-01 for type only. |
| T02 | Boron-halide field split | CR-337 BF₃ agrees; CR-338 ionic disagrees. Do not ask the learner to rebuild BF₃. |
| T03 | P₂O₃ source fidelity | Teach the name of the given P₂O₃ and covalent exercise type; do not replace the printed formula or claim a specific discrete structure. |
| T04 | P/K diagnostic order | PBr₃ named potassium bromide first triggers an identity check. A route hypothesis is not asserted as proven. |
| T05 | Formula case | CO and Co remain distinct. Formula normalization never silently lowercases element tokens. |
| T06 | Hidden one | Cl₂O maps to Cl count 2 and O count 1; prefix practice gives dichlorine monoxide. |
| T07 | Oxygen count | N₂O₅ maps to 5 O, not 4. Preserve the correct nitrogen count and covalent type. |
| T08 | Prefix versus reading probe | A learner who says 5 O but chooses tetra- gets prefix help; one who reads 4 O gets formula-count help. |
| T09 | Molecular formula preservation | N₂O₄ is never automatically reduced to NO₂ in a molecular-formula exercise. |
| T10 | Ammonium sulfide charge | With NH₄⁺ and S²⁻ fixed, one of each gives −1; two ammoniums and one sulfide give zero. |
| T11 | Ammonium grouping | (NH₄)₂S has N=2, H=8, S=1. NH₄S is not an equivalent inventory. |
| T12 | Potassium sulfate charge | K⁺ and SO₄²⁻ require 2:1. KSO₄ leaves −1 in the supported ion model. |
| T13 | Magnesium chlorate charge | Mg²⁺ and ClO₃⁻ require 1:2 and serialize as Mg(ClO₃)₂. |
| T14 | Group notation distinction | MgCl₂O₆ matches Mg(ClO₃)₂ atom counts but not conventional grouped display; MgClO₆ does not match the counts. |
| T15 | Minimal whole-ion ratio | A correct 4:2 K:sulfate pair balances but is not the minimum ion-count ratio. Explain reduction of the pair, not of internal sulfate. |
| T16 | Peroxide identity | Na₂O₂ remains two sodium ions per peroxide group; never canonicalize it as NaO. |
| T17 | Known-charge support | If the learner does not know sulfate’s charge, show a reference explanation/card. Do not repeat “use the correct charge” alone. |
| T18 | Nickel Stock name | In the supported NiS model, q−2=0 gives +2; the prefix-free Stock response is nickel(II) sulfide. |
| T19 | Per-ion numeral | Fe₂O₃ yields Fe(III), not II from the subscript and not VI from the aggregate positive charge. |
| T20 | No fractional numeral rounding | An out-of-scope mixed-state case such as Fe₃O₄ does not round +8/3 to +3; retain PR-67 context handling. |
| T21 | Ammonium without metal | NH₄NO₃ is ionic at the compound level despite covalent bonding within the ions. |
| T22 | LiH scope | LiH is taught as an ionic hydride for the ordinary solid comparison; do not generalize to all compounds containing H. |
| T23 | B₂H₆ scope | B₂H₆ uses the covalent route in this exercise; hydride is not treated as a universal ionic trigger. |
| T24 | Diborane naming variants | Diborane and diboron hexahydride are recognized identity forms. Boron hydride receives a qualified convention note, not “nonexistent compound.” Instructor acceptance remains a separate gate. |
| T25 | No universal electronegativity cutoff | A fixed electronegativity threshold is not the sole classifier; unsupported cases can return needs_context. |
| T26 | Independent fields | Native formula/name and type outcomes remain separate. A wrong field does not reset a correct paired field. |
| T27 | Read is not attempt | Opening a story, card, or hint does not increment graded attempts as a wrong response. |
| T28 | Reveal is not mastery | Viewing a worked solution does not become unaided success or automatic mastery. |
| T29 | Preserve answers | Closing, reopening, or refreshing a scaffold preserves existing entered work according to current storage behavior. |
| T30 | No import of worksheet attempts | Private normalized observations do not populate app attempts, grades, confidence, or journals. |
| T31 | Anchor resolution | Every attached CR/PR/L/WE ID resolves in the live workspace or produces an editorial unresolved-anchor report. |
| T32 | Idempotent integration | Repeating the integration/build does not duplicate items, links, progress events, or generated pages. |
| T33 | No copied answer authority | Tutorial targets remain explanatory/fixture material. Native records stay the source of grading truth. |
| T34 | Public export allowlist | Public output excludes private/02_EVIDENCE_MAP.md, original PDFs/photos, and private note contents; check rendered links as well as files. |
| T35 | Keyboard equivalence | All count-changing and routing actions work without dragging or precise pointer movement; focus is visible. |
| T36 | Semantic formulas | Displays retain subscripts/superscripts and useful accessible descriptions; input/display round-trips preserve formula identity. |
| T37 | Phone reading | At a narrow viewport the current formula, field state, help, and return action remain reachable without clipped charge or forced wide layout. |
| T38 | No forced audio/motion | Text equivalents are complete; narration is opt-in; reduced motion does not remove any explanation. |
| T39 | Scope and consent | No automatic live publication, central-doctrine change, new launcher, or external transfer of private learner data occurs. |
| T40 | Truthful completion report | Implementation report distinguishes passed tests, manual inspections, skipped checks, unavailable source conventions, and remaining work. |

## Small mathematical fixtures

Use the installed ion records where possible. These values are explicit test expectations for the examples, not a replacement reference bank.

```json
{
  "fixtureContract": "proposal.lumi.q13.arithmetic-fixtures.v1",
  "cases": [
    {"target": "(NH4)2S", "cationCharge": 1, "anionCharge": -2, "cationCount": 2, "anionCount": 1, "netCharge": 0, "atoms": {"N": 2, "H": 8, "S": 1}},
    {"target": "K2SO4", "cationCharge": 1, "anionCharge": -2, "cationCount": 2, "anionCount": 1, "netCharge": 0, "atoms": {"K": 2, "S": 1, "O": 4}},
    {"target": "Mg(ClO3)2", "cationCharge": 2, "anionCharge": -1, "cationCount": 1, "anionCount": 2, "netCharge": 0, "atoms": {"Mg": 1, "Cl": 2, "O": 6}},
    {"target": "Na2O2", "cationCharge": 1, "anionCharge": -2, "cationCount": 2, "anionCount": 1, "netCharge": 0, "atoms": {"Na": 2, "O": 2}},
    {"target": "NH4NO3", "cationCharge": 1, "anionCharge": -1, "cationCount": 1, "anionCount": 1, "netCharge": 0, "atoms": {"N": 2, "H": 4, "O": 3}},
    {"target": "NiS", "cationCharge": 2, "anionCharge": -2, "cationCount": 1, "anionCount": 1, "netCharge": 0, "atoms": {"Ni": 1, "S": 1}},
    {"target": "Fe2O3", "cationCharge": 3, "anionCharge": -2, "cationCount": 2, "anionCount": 3, "netCharge": 0, "atoms": {"Fe": 2, "O": 3}}
  ]
}
```

## Suggested execution evidence

Unit tests should cover charge/count computations and parser round-trips. Component tests should cover a correct name/formula with incorrect type. Integration tests should verify reference resolution and saved-answer preservation. Browser checks should cover keyboard, narrow screens, and public-output exclusion.

Screenshots support a visual review but are not substitutes for keyboard and state tests. A screenshot of a formula does not establish that screen-reader labeling works. A JSON file parsing successfully does not establish chemistry correctness. Preserve those distinctions in the report.
