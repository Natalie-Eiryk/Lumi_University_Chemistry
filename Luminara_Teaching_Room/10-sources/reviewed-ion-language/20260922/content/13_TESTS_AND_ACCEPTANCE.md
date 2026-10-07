---
document_id: LU-IONS-DESIGN-13
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Acceptance tests and the evidence required to call it done

## Separate test kinds

1. **Packet integrity:** internal links, data count, fixture arithmetic, answer/prompt IDs. These can be checked while authoring these Markdown files.
2. **Implementation behavior:** parser, feedback, UI, persistence, registry integration. These remain future Codex tests until real software executes them.
3. **Human review:** science scope, course-list reconciliation, accessibility usability, narrative tone, and learner usefulness. A passing schema or keyword lint cannot certify these.

Do not label level 2 or 3 passed because level 1 passed.

## Acceptance matrix

| Test | Rule / area | Given / when | Required result |
|---|---|---|---|
| T-01 | RULE-01 | NO3^− / NO₃⁻ entered in ion mode | Recognize one N, three O, and group charge −1; preserve the source text. |
| T-02 | RULE-01 | Two selected nitrate cards | Compute N=2, O=6, charge=−2. |
| T-03 | RULE-02 | Ca²⁺ + Cl⁻ | Minimum counts 1:2; CaCl2. |
| T-04 | RULE-02 | Al³⁺ + SO₄²⁻ | Minimum counts 2:3; Al2(SO4)3. |
| T-05 | RULE-03 | Mg²⁺ + O²⁻ | MgO; reject Mg2O2 as nonminimal for the named constituent model. |
| T-06 | RULE-03 | Al³⁺ + PO₄³⁻ | AlPO4; no subscript 1 or redundant parentheses. |
| T-07 | RULE-03 | Na⁺ + O₂²⁻ | Na2O2 remains unreduced; not NaO. |
| T-08 | RULE-07 | Mg(OH)2 parsed | Mg=1, O=2, H=2; two hydroxide groups. |
| T-09 | RULE-07 | (NH4)2SO4 parsed | N=2, H=8, S=1, O=4; net constituent charge zero. |
| T-10 | RULE-07 | CaN2O6 for calcium nitrate | Acknowledge atom equivalence; explain conventional nitrate grouping. |
| T-11 | RULE-07 | CaNO6 for calcium nitrate | Identify wrong atom inventory; do not equate with Ca(NO3)2. |
| T-12 | RULE-07 | Ca(NO3)3 for calcium nitrate | Recognized groups, net −1; diagnose charge/counts. |
| T-13 | RULE-06 | Fe2O3 | iron(III) oxide; +3 per Fe. |
| T-14 | RULE-06 | Cu2O | copper(I) oxide; +1 per Cu. |
| T-15 | RULE-06 | Fe3(PO4)2 | iron(II) phosphate; +2 per Fe. |
| T-16 | RULE-06 | bare name copper chloride | Ask I or II; do not choose from popularity. |
| T-17 | RULE-09 | Fe3O4 | No rounding +8/3; route to mixed-valence extension. |
| T-18 | RULE-09 | NH4Cl | In scope despite no metal; ammonium chloride. |
| T-19 | RULE-09 | CO2 | Molecular route; not calcium/cobalt ionic interpretation. |
| T-20 | RULE-09 | HCl(aq) | Acid-context route; do not silently remove state. |
| T-21 | RULE-09 | CuSO4·5H2O | Hydrate route; no silent omission of water. |
| T-22 | RULE-05 | NO3− versus SO4²− | Same -ate suffix does not force identical O count/charge. |
| T-23 | RULE-05 | chlorine-family navigation | Exactly four reviewed sibling entries; no synthetic ion beyond ends. |
| T-24 | RULE-04 | hydroxide/cyanide/peroxide | -ide does not trigger monatomic-only classification. |
| T-25 | RULE-10 | hydrogen carbonate / bicarbonate | Resolve to one reviewed ion and accepted compound-name aliases. |
| T-26 | RULE-10 | dichromate | Cr2O7, charge −2; not two chromate copies. |
| T-27 | RULE-08 | noble-gas explanation panel | States its main-group scope and electron-removal energy cost. |
| T-28 | RULE-09 | unlisted name | reference-needed; no invented formula. |
| T-29 | ENGINE | CO versus Co | Case preserved; no silent recasing. |
| T-30 | ENGINE | SO42- | Clarification in ion entry; no guessed charge/subscript split. |
| T-31 | ENGINE | unbalanced parentheses / zero atom count | Localized syntax feedback; no chemistry verdict from invalid parse. |
| T-32 | ENGINE | huge counts / excessive nesting | Bounded rejection; no overflow, hang, or unsafe allocation. |
| T-33 | ENGINE | HTML/script text in answer field | Rendered as text; no execution or injected markup. |
| T-34 | TEACH-03 | valid alternate algebraic balance | Accept chemical reasoning; do not require one visual fence layout. |
| T-35 | TEACH-02 | ambiguous handwriting interpretation | Require confirmation before grading; preserve original. |
| T-36 | REVIEW | Reveal then copy answer | Assisted/revealed event; not independent success. |
| T-37 | REVIEW | correct response with confidence omitted | Unknown stays unknown; do not write confidence=0 as a substitute. |
| T-38 | REVIEW | repeated Check / retried sync | One logical event per submission identity; no double-counting. |
| T-39 | REVIEW | immediate inverse after example | Not evidence of later retained transfer. |
| T-40 | REVIEW | two similar errors | Offer a different representation or reference, not endless same-item repeats. |
| T-41 | ACCESS | keyboard-only use | All lesson, tile, hint, and answer actions usable; focus visible. |
| T-42 | ACCESS | touch with no dragging | Tap steppers/select-and-place provide all tile functionality. |
| T-43 | ACCESS | audio unavailable or muted | Full content usable with text; no blocked progress. |
| T-44 | ACCESS | screen reader / 200% zoom / narrow width | Correct chemical reading, headings, controls, no hidden required fields. |
| T-45 | PRIVACY | public export | No personal notes, source PDFs, confidence, attempts, local paths, or tokens. |
| T-46 | STORAGE | storage quota/failure | Visible unsaved state; usable workspace and explicit export. |
| T-47 | STORAGE | import replay / bad version | Validate before merge; preserve existing history; no duplicates. |
| T-48 | INTEGRATION | new module installed | Existing subjects, launch flow, progress and site navigation still work. |
| T-49 | INTEGRATION | repeat content build | Stable IDs and deterministic output; no duplicate registry entries. |
| T-50 | RELEASE | design build or local preview completed | No automatic public publish, canon promotion, or new notification schedule. |


## Corpus tests

Every one of the 44 curated compound records must satisfy: positive cation count, positive anion count, gcd(counts)=1, net charge zero, atom inventory matching the rendered formula, correct ion IDs, and name-to-record/formula-to-record round-trip behavior. The minimum-ratio test operates on ion counts, not every element count.

Every PR-01–72 must have exactly one answer-key section. Each generated ion-recall variant must resolve to one of the 62 reviewed-or-provisional bank IDs with provenance preserved. Special tier-3 entries may not leak into default random compound generation.

## Human review prompts

Can Natalie tell at a glance whether a mismatch concerns recall, algebra, or notation? Does the system allow “I know the chemistry but need the conventional display”? Does a low-confidence correct answer lead to useful explanation rather than dismissal? Are nitrate/nitrite and oxide/peroxide differences visible without color? Can a user complete the same lesson with a keyboard, a finger, or paper?

Do not claim cognitive mastery, historical accuracy, accessibility conformance, or classroom grading equivalence from a simple keyword checker. Preserve actual reviewer, date, version, and evidence in review records.

## Regression and handback

Use the repository’s existing validation framework and test runners. The currently inspected registry names `node tools/validate-questions.js` and `node tools/verify-teaching-v2.js`; confirm they still exist and fit the implementation before execution. These are discovered integration hooks, not commands run by this packet.

Return: changed files; schema migrations; exact commands and results; local route; screenshots at desktop and iPad-sized widths; keyboard/tap test notes; storage/export checks; source-reconciliation gaps; anything still blocked. Screenshots must come from the built software, not design mock-ups labeled as working functionality.
