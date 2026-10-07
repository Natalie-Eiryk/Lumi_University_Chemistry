---
document_id: LU-IONS-DESIGN-16
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# File manifest and actual package checks

## Build status

This package contains 23 Markdown design files. No application code was installed, repository file modified, site deployed, automation scheduled, or learner data uploaded by this build.

## Checks actually performed

- PASS — UTF-8 read/write of every Markdown file.
- PASS — All internal relative Markdown file links resolve inside the packet.
- PASS — Every fenced code block is closed.
- PASS — 5 fenced JSON examples/fixture arrays parse as JSON.
- PASS — 62 ion IDs are unique; the provisional transcription contains 32 cation records and 30 anion records.
- PASS — All PR-01 through PR-72 exist and have exactly one answer-key section.
- PASS — 44 compound fixture records have positive integer constituent counts, minimum whole-ion ratios, zero net charge, and matching formula/constituent atom inventories.
- PASS — 18 worked-example targets come from the same checked fixture records.
- PASS — Sodium peroxide is retained as Na2O2; aluminum phosphate reduces to AlPO4.
- PASS — 50 proposed behavioral acceptance cases have unique IDs.

## Checks not performed here

Actual campus runtime/schema adapter validation; browser rendering; keyboard/touch/screen-reader testing; storage migrations; test runner execution inside Lumi; exact instructor-list reconciliation; public export/deployment; formal scientific/editorial approval. These remain Codex and human review work.

The generated fixture checks demonstrate internal arithmetic consistency. They do not establish chemical existence/stability for arbitrary pairings and do not certify the pending source transcription.

## File map

| File | Document ID | Purpose |
|---|---|---|
| [00_START_HERE.md](00_START_HERE.md) | `LU-IONS-DESIGN-00` | Ion Language — the Lumi University design packet |
| [01_CODEX_IMPLEMENTATION_BRIEF.md](01_CODEX_IMPLEMENTATION_BRIEF.md) | `LU-IONS-DESIGN-01` | Codex: integrate a chemistry learning module, not a document viewer |
| [02_LEARNER_AND_TEACHING_CONTRACT.md](02_LEARNER_AND_TEACHING_CONTRACT.md) | `LU-IONS-DESIGN-02` | The learner, the method, and the boundaries |
| [03_CHEMISTRY_RULES_AND_BOUNDARIES.md](03_CHEMISTRY_RULES_AND_BOUNDARIES.md) | `LU-IONS-DESIGN-03` | The chemistry engine: rules with explicit scope |
| [04_ION_BANK_AND_FAMILIES.md](04_ION_BANK_AND_FAMILIES.md) | `LU-IONS-DESIGN-04` | Ion bank and the family wall |
| [05_SESSION_AND_SKILL_GRAPH.md](05_SESSION_AND_SKILL_GRAPH.md) | `LU-IONS-DESIGN-05` | Session routes and skill evidence |
| [06_MODALITIES_AND_INTERACTIONS.md](06_MODALITIES_AND_INTERACTIONS.md) | `LU-IONS-DESIGN-06` | Interaction blueprints: one model, several ways to inspect it |
| [07_WORKED_EXAMPLES.md](07_WORKED_EXAMPLES.md) | `LU-IONS-DESIGN-07` | Eighteen worked translations and their reverse checks |
| [08_PRACTICE_BANK.md](08_PRACTICE_BANK.md) | `LU-IONS-DESIGN-08` | Practice prompts: the 72-item seed bank |
| [09_ANSWER_KEY.md](09_ANSWER_KEY.md) | `LU-IONS-DESIGN-09` | Answer key, reasoning, and compiler fixtures |
| [10_FEEDBACK_AND_SPACED_REVIEW.md](10_FEEDBACK_AND_SPACED_REVIEW.md) | `LU-IONS-DESIGN-10` | Feedback, diagnosis, and revisiting what matters |
| [11_DATA_AND_ENGINE_CONTRACTS.md](11_DATA_AND_ENGINE_CONTRACTS.md) | `LU-IONS-DESIGN-11` | Data contracts and the deterministic chemistry core |
| [12_INTERFACE_ACCESSIBILITY_AND_PRIVACY.md](12_INTERFACE_ACCESSIBILITY_AND_PRIVACY.md) | `LU-IONS-DESIGN-12` | Campus interface, accessibility, and private/public separation |
| [13_TESTS_AND_ACCEPTANCE.md](13_TESTS_AND_ACCEPTANCE.md) | `LU-IONS-DESIGN-13` | Acceptance tests and the evidence required to call it done |
| [14_EXAM_CARD_AND_REVIEW.md](14_EXAM_CARD_AND_REVIEW.md) | `LU-IONS-DESIGN-14` | The small map to carry into practice |
| [15_SOURCES_AND_DECISIONS.md](15_SOURCES_AND_DECISIONS.md) | `LU-IONS-DESIGN-15` | Source ledger, corrections, and open decisions |
| [16_FILE_MANIFEST_AND_QA.md](16_FILE_MANIFEST_AND_QA.md) | `LU-IONS-DESIGN-16` | File manifest and actual package checks |
| [lessons/L01_CHARGE_AND_REPRESENTATION.md](lessons/L01_CHARGE_AND_REPRESENTATION.md) | `LU-IONS-L01` | The charge ledger: three different numbers |
| [lessons/L02_NAMES_ROOTS_AND_CHARGES.md](lessons/L02_NAMES_ROOTS_AND_CHARGES.md) | `LU-IONS-L02` | Name badges: what you can predict and what you must recall |
| [lessons/L03_BUILD_FORMULAS.md](lessons/L03_BUILD_FORMULAS.md) | `LU-IONS-L03` | Build the formula without changing the passengers |
| [lessons/L04_READ_FORMULAS_AND_ROMAN_NUMERALS.md](lessons/L04_READ_FORMULAS_AND_ROMAN_NUMERALS.md) | `LU-IONS-L04` | Read backward: let the known ion constrain the unknown |
| [lessons/L05_OXYANION_FAMILIES.md](lessons/L05_OXYANION_FAMILIES.md) | `LU-IONS-L05` | The oxygen family wall: a few anchors, carefully bounded rules |
| [lessons/L06_TRANSFER_AND_REFLECTION.md](lessons/L06_TRANSFER_AND_REFLECTION.md) | `LU-IONS-L06` | Translate both ways, explain a seam, and carry it forward |

## Content hashes

SHA-256 hashes below cover the other 22 Markdown files at this build. The manifest does not hash itself. These are file-integrity hashes, not Atlas codons, repository commits, or approval signatures.

| File | SHA-256 |
|---|---|
| `00_START_HERE.md` | `ced61fe0615f24fd4c12cbf3ecef0e11981ecdb0bcfaaf06397a7cf28d432f08` |
| `01_CODEX_IMPLEMENTATION_BRIEF.md` | `709beb85ccfb3bcc1c866886caee7b491a1fc14a60482b5d15e5cc0323bb8f1a` |
| `02_LEARNER_AND_TEACHING_CONTRACT.md` | `4becb5df56ae1aa8bca5bedc381b72d4da9f17fe37ee05f08ecc8e53658c23d0` |
| `03_CHEMISTRY_RULES_AND_BOUNDARIES.md` | `95fe4e94c1daca016134f99d1657728adf9af6178badbecb9f801952875029f1` |
| `04_ION_BANK_AND_FAMILIES.md` | `fa1b13d7c0cdc0320440dff34df9fd5549427ea24f2e7047c67843669dcd7faa` |
| `05_SESSION_AND_SKILL_GRAPH.md` | `5daa847995e0de1e07dcc7ac820bbc5c76fff79588151b980f95781229c06f0b` |
| `06_MODALITIES_AND_INTERACTIONS.md` | `898acc0af28ae6295b228c52c4a9bf3e44cffbd5a137797cd8706330cf8f5a77` |
| `07_WORKED_EXAMPLES.md` | `81580a4c875b42eb71e712bb4648143d8a1463868560f0ba817a9346984e4357` |
| `08_PRACTICE_BANK.md` | `afb369bfd9e3cb5ab32602ced5582bf585a65ee4226dfc7f73b8ad2edcd279d9` |
| `09_ANSWER_KEY.md` | `2eca0837a1ab6b47eb949c18d6f2fe40f627bc4986bbfc24c3b77f0e95e1aa68` |
| `10_FEEDBACK_AND_SPACED_REVIEW.md` | `739421a38b58cd057158019f0ad1e57e756a36694bbfad35e9cab784f9092be2` |
| `11_DATA_AND_ENGINE_CONTRACTS.md` | `d699b76a6cac0afcf0096cf3b1def384feedc2611824897a6fe402299002c14d` |
| `12_INTERFACE_ACCESSIBILITY_AND_PRIVACY.md` | `46cab279e3ee4dc231fa724279cbb109f0b214bc9f4b864ff3944270ec969292` |
| `13_TESTS_AND_ACCEPTANCE.md` | `13dba1e5ae65bd4143f81631ffb4643ea9137c9e31bd355ce732099a411b46c0` |
| `14_EXAM_CARD_AND_REVIEW.md` | `52ff0d47b1a55f3c677f88fd0945be384168a9bf46de75243b08155dc4c2d838` |
| `15_SOURCES_AND_DECISIONS.md` | `1bccc8816cafb4246c4109025183499d6f169a989ab00e131d1962327e8c5f58` |
| `lessons/L01_CHARGE_AND_REPRESENTATION.md` | `4706fb6239022a6ac16ab35a86caf94053a3961c29865a4581d45d62331c194a` |
| `lessons/L02_NAMES_ROOTS_AND_CHARGES.md` | `d44369ded0885ec721ab9a5bc6f24ebcc0a0dce80efaf883b1bc6a8093037c28` |
| `lessons/L03_BUILD_FORMULAS.md` | `3156ebff59f518a95c8d9ae9a0a6e18b3276efd17fa8d604f9a3188454882df0` |
| `lessons/L04_READ_FORMULAS_AND_ROMAN_NUMERALS.md` | `195ec017fb21c82f3fa7fc8264fbae7749d5dcc4420071037f7b53135a97c4b4` |
| `lessons/L05_OXYANION_FAMILIES.md` | `7ff90bc053f869bd9db124531df678fbd2b86ab8722524571318348f6d3fb255` |
| `lessons/L06_TRANSFER_AND_REFLECTION.md` | `e04a2d0e511d2cc3bde2dd65cfab0083a24637548fabe6f594b143c65da6b5ca` |
