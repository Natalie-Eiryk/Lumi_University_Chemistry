---
document_id: 09_SOURCES_DECISIONS_AND_QA
package_id: LU-CHEM-Q13-SCAFFOLDS
version: 0.1.0
status: editorial_draft
created: 2026-09-28
visibility: editorial
integration_mode: additive_scaffold_overlay
assessment_owner: existing_native_exercises
---

# Sources, decisions, open gates, and package checks

## Source-derived foundation

### S-Q13 — the actual attempt

**File:** `Ionic_cov_nom_q13.pdf`  
**Visible identity:** Chemistry 1117, Q13 Ionic and Covalent Nomenclature, printed page 265; one submitted page.  
**Conversation citation:** `turn68file0`; the rendered source page is available alongside extracted lines 1–39.

Use the rendered handwriting to distinguish printed prompts from the learner’s responses. Core observation ranges: rows 2–7 (extracted lines 8–16); rows 14–21 (lines 26–37). The private evidence map holds a normalized transcription with the limits stated. This is not an instructor key.

### S-INDEX — existing exercise and reference snapshot

**File:** `CHEMISTRY_QUESTION_AND_REFERENCE_INDEX_2026-09-28.md`  
**Conversation citation:** `turn68file1`.

Relevant anchors:

- L01–L06 and WE-01–18: lines 7–37.
- Ion identities: lines 57–96 and 314–383.
- Whole-ion builder: lines 121–157.
- Prefix/molecular fields: lines 195–226.
- Q13 row and field bindings: lines 284–312.
- Comparison compound targets: lines 447–470.
- Original PR prompts and boundary cases: lines 472–549.
- Source boundaries and installed-file snapshot: lines 1086–1110.

The snapshot explicitly distinguishes reference answers from an instructor-confirmed answer key and does not include saved learner responses. The existing CR fields already belong to the practice collection; attaching this packet must not count them again as new questions.

### S-MATERIALS — teaching needs and ownership boundaries

**File:** `CHEMISTRY_STUDY_MATERIALS_2026-09-28.md`  
**Conversation citation:** `turn68file2`.

Primary sections: MAT-06 charge/subscripts/copies; MAT-07 ion identity; MAT-08 ammonium charge; MAT-09 oxygen patterns; MAT-10 neutral formulas; MAT-11 Stock naming; MAT-12 model selection; MAT-13 prefixes; MAT-15 diagnosis without overclaiming.

Especially important: lines 177–185 distinguish partial success, learning with a reveal, and unsupported claims about misconceptions. Lines 227–231 reserve assessment ownership to existing native questions and checks.

## External scientific checks and explicit extensions

These are limited supplements. They do not replace the worksheet, dictate a classroom grade, or provide a new unrestricted nomenclature engine. Links identify the checked sources; no source images or long passages are reproduced.

### S-NAMING — ordinary naming and spelling examples

OpenStax, *Chemistry 2e*, §2.7, “Chemical Nomenclature.”

https://openstax.org/books/chemistry-2e/pages/2-7-chemical-nomenclature

Used to cross-check the separation of ionic/Stock and molecular-prefix naming, and the example forms **dinitrogen pentoxide**, **dinitrogen tetroxide**, and **monoxide**. The section distinguishes classroom contraction practices from stricter conventions; therefore the implementation must not equate every alternate spelling with a wrong atom count. Full instructor acceptance remains unverified.

### S-IONIC — constituent/group scope

OpenStax, *Chemistry 2e*, §2.6, “Ionic and Molecular Compounds.”

https://openstax.org/books/chemistry-2e/pages/2-6-ionic-and-molecular-compounds

Used as a limited scope check: polyatomic ions may be constituents of neutral salts; formulas can preserve whole-ion groups; periodic-position shortcuts have exceptions. The packet’s detailed examples and lesson sequence are grounded primarily in the supplied course inventory and independently authored scenes.

### S-DIBORANE — identity and synonym correction

NIOSH, *Pocket Guide to Chemical Hazards*, “Diborane,” CAS 19287-45-7.

https://www.cdc.gov/niosh/npg/npgd0183.html

The record identifies B₂H₆ and lists **boron hydride** and **diboron hexahydride** as synonyms. NIST Chemistry WebBook search results also associate those names with B₂H₆, but direct-page retrieval was unavailable during this build; NIOSH provides the accessible checked record used here.

This qualifies the preceding spot check: the learner’s “boron hydride” should not become a hard-coded claim of chemically meaningless naming. The count-prefix response is more explicit for the requested exercise, while instructor alias acceptance remains a separate issue. This packet does not reproduce handling guidance or propose experiments with the compound.

### S-BORON — covalent boron compounds

OpenStax, *Chemistry: Atoms First 2e*, §18.3, “Structure and General Properties of the Metalloids.”

https://openstax.org/books/chemistry-atoms-first-2e/pages/18-3-structure-and-general-properties-of-the-metalloids

Used narrowly to verify that boron forms covalent compounds and to keep boron hydrides outside a universal monatomic-ion shortcut. No complete advanced borane structure or d-orbital bonding model is imported into the beginner scaffold.

### S-HYDRIDE — LiH as an ion-based solid model

Khang Hoang and Chris G. Van de Walle, “LiH as a Li⁺ and H⁻ ion provider,” research preprint, 2014.

https://arxiv.org/abs/1412.6208

This primary study of defects and ionic behavior in LiH supports the deliberately scoped Li⁺/H⁻ solid-state comparison. The short scaffold does not assert that an exact integer-charge picture is a complete quantum description or that all hydrides behave alike.

### S-IONIC-CHARACTER — the binary model has limits

IUPAC Gold Book, “ionic bond,” entry IT07058.

https://goldbook.iupac.org/terms/view/IT07058

Used for the limited qualification that degree of ionic character is preferable to treating all bonds as physically pure endpoints. No electronegativity formula or fixed numerical threshold is implemented here.

External checks were performed September 28, 2026. Scientific descriptions are separate from teacher-confirmed conventions.

## Design decisions

| Decision | Reason | What is not being claimed |
|---|---|---|
| Six focused scaffolds | The observed errors cluster around repeatable decisions | Six permanent deficits or six proven diagnoses |
| Use successful rows as bridges | The same worksheet contains useful near-transfer examples | Unaided, permanent mastery from one correct answer |
| Two-field feedback | Name/formula and type are separate in the source | Authority to change an instructor’s grade |
| Keep private evidence separate | Teaching may use personal context without publishing it | Permission to place worksheet mistakes in public content |
| No new graded bank | Native IDs and checks already exist | That staged self-checks create additional course questions |
| Qualified B₂H₆ naming | Recognized identity and requested format are different issues | Instructor acceptance of every synonym |
| No guest/canon addition | These are short companion scenes, not a new historical epic | A new canonical adventure event |
| Choice, text, voice, and tiles | Different supports for the same reasoning | A fixed “learning-style” diagnosis or optimal timing claim |

## Open gates for Codex/editorial review

1. Resolve the current working-tree paths and component interfaces. This turn did not inspect the live application.
2. Confirm full instructor ion-list and molecular-spelling/alias conventions; the snapshot already marks these as unresolved.
3. Decide how the native checker reports scientifically recognized but differently formatted names without overwriting source policy.
4. Confirm the existing progress schema’s hint/reveal semantics before adding events.
5. Validate all public export exclusions and accessibility behavior in the actual application.
6. Keep existing grading and data intact. Pause for review if source records and scaffold examples disagree.

## QA performed on this packet

- Confirmed **16 Markdown documents**, including **six scaffold documents** and one explicitly private evidence map.
- Checked **43 relative Markdown links**, including the generated file manifest; all destinations existed.
- Parsed **3 embedded JSON examples** successfully.
- Matched every primary Q13 field binding to its exact row in the supplied index; verified all 21 private row/field pairs.
- Verified all referenced CR, PR, WE, L, and MAT attachment IDs against the supplied snapshots.
- Verified **7 charge-balanced minimal whole-ion fixtures** and **26 atom-inventory cases** with a small independent arithmetic/parser check.
- Checked the equal-inventory grouping contrast, three unequal-inventory contrasts, two incomplete-charge examples, and Ni/Fe per-metal arithmetic.
- Checked unique IDs for **6 scaffolds** and **40 specified application tests**.
- Checked balanced Markdown code fences and parsed/rendered all **16 Markdown documents** as HTML fragments without errors; each has one top-level title. This was a syntax check, not a visual browser or accessibility test.
- No application test suite, live workspace validation, browser rendering, screen-reader test, or deployment was executed in this build. These remain Codex gates.
- Numerical and link checks do not establish learner mastery, instructor acceptance, chemical existence for arbitrary formulas, or flawless prose.

### Input snapshot hashes

These identify the exact mounted inputs used for packet QA. Hashing does not create a new citation or prove that a snapshot is the current live source.

- `Ionic_cov_nom_q13.pdf`: SHA-256 `d31ab284c009cc093378575b44cfd1a1ba619cd4ccf65564b4e50e6493973d44`
- `CHEMISTRY_QUESTION_AND_REFERENCE_INDEX_2026-09-28.md`: SHA-256 `29af7eaaaab608e85a8eae9c64fd00e8ba06f3522b20bc6c6c2b8a1916f24350`
- `CHEMISTRY_STUDY_MATERIALS_2026-09-28.md`: SHA-256 `5fe9fea466dcf0b7798bc0a0475ae00af5b4f12297a7763f81d2139e59ffa36c`

## File manifest

- [`00_START_HERE.md`](00_START_HERE.md) — editorial / implementation guidance
- [`01_CODEX_HANDOFF.md`](01_CODEX_HANDOFF.md) — editorial / implementation guidance
- [`03_SESSION_AND_BRANCHING.md`](03_SESSION_AND_BRANCHING.md) — editorial / implementation guidance
- [`04_FADING_AND_TRANSFER.md`](04_FADING_AND_TRANSFER.md) — editorial / implementation guidance
- [`05_FEEDBACK_AND_UI_CONTRACT.md`](05_FEEDBACK_AND_UI_CONTRACT.md) — editorial / implementation guidance
- [`06_EXISTING_ID_BINDINGS.md`](06_EXISTING_ID_BINDINGS.md) — editorial / implementation guidance
- [`07_ACCEPTANCE_TESTS.md`](07_ACCEPTANCE_TESTS.md) — editorial / implementation guidance
- [`08_CARRY_CARD.md`](08_CARRY_CARD.md) — authored teaching content
- [`09_SOURCES_DECISIONS_AND_QA.md`](09_SOURCES_DECISIONS_AND_QA.md) — editorial / implementation guidance
- [`private/02_EVIDENCE_MAP.md`](private/02_EVIDENCE_MAP.md) — PRIVATE: do not deploy
- [`scaffolds/Q13-SCF-01_TWO_CHECKS.md`](scaffolds/Q13-SCF-01_TWO_CHECKS.md) — authored teaching content
- [`scaffolds/Q13-SCF-02_SYMBOLS.md`](scaffolds/Q13-SCF-02_SYMBOLS.md) — authored teaching content
- [`scaffolds/Q13-SCF-03_WHOLE_IONS.md`](scaffolds/Q13-SCF-03_WHOLE_IONS.md) — authored teaching content
- [`scaffolds/Q13-SCF-04_ROMAN_NUMERALS.md`](scaffolds/Q13-SCF-04_ROMAN_NUMERALS.md) — authored teaching content
- [`scaffolds/Q13-SCF-05_PREFIXES.md`](scaffolds/Q13-SCF-05_PREFIXES.md) — authored teaching content
- [`scaffolds/Q13-SCF-06_BOUNDARIES.md`](scaffolds/Q13-SCF-06_BOUNDARIES.md) — authored teaching content

The archive is a handoff package. It has not been installed in Lumi, deployed to GitHub Pages, or canonized. Content completeness and chemistry review are not equivalent to runtime validation.
