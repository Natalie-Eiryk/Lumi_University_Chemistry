---
document_id: LU-IONS-DESIGN-00
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Ion Language — the Lumi University design packet

## Start with this outcome

Given **aluminum sulfate**, the learner recognizes Al³⁺ and SO₄²⁻, balances 2(+3)+3(−2)=0, and writes **Al₂(SO₄)₃**. Given the formula, she reads the same model backward and names it. She can distinguish what she calculated from what she remembered and can identify when the available information is insufficient.

This packet provides the content, teaching flow, interaction behavior, data contracts, examples, diagnostics, and acceptance criteria needed to build that capability into Lumi University. It is a **design candidate**, not an installed app or replacement central doctrine. Its version 1.0.0 is the packet version; the referenced Adventure Doctrine is v1.1.0.

## Hand to Codex

Give Codex the entire folder and tell it to start with [01_CODEX_IMPLEMENTATION_BRIEF.md](01_CODEX_IMPLEMENTATION_BRIEF.md). It should inspect the actual workspace first, reuse the existing campus, and implement in vertical slices. Native/frontend languages, registry paths, and persistence interfaces must be mapped to what is actually present.

## Contents

| Read | Purpose |
|---|---|
| [01 Codex brief](01_CODEX_IMPLEMENTATION_BRIEF.md) | bounded implementation work, milestones, handback |
| [02 Learner and teaching contract](02_LEARNER_AND_TEACHING_CONTRACT.md) | Ms. Luminara posture; multiple representations; personal thinking |
| [03 Scientific rules and limits](03_CHEMISTRY_RULES_AND_BOUNDARIES.md) | what the software may and may not infer |
| [04 Ion bank and family wall](04_ION_BANK_AND_FAMILIES.md) | 62 charge-specific ion records; anchors and scope |
| [05 Session and skills](05_SESSION_AND_SKILL_GRAPH.md) | roughly 60-minute route; short routes; prerequisite suggestions |
| [L01 Charge and representation](lessons/L01_CHARGE_AND_REPRESENTATION.md) | charge versus inner/outer counts |
| [L02 Names and charges](lessons/L02_NAMES_ROOTS_AND_CHARGES.md) | roots, remembered identities, periodic hints |
| [L03 Build formulas](lessons/L03_BUILD_FORMULAS.md) | neutral ratios and group preservation |
| [L04 Read formulas](lessons/L04_READ_FORMULAS_AND_ROMAN_NUMERALS.md) | Roman numerals and reverse inference |
| [L05 Oxygen families](lessons/L05_OXYANION_FAMILIES.md) | anchors, local patterns, contrasts |
| [L06 Transfer and reflection](lessons/L06_TRANSFER_AND_REFLECTION.md) | both directions and a learner-owned exit note |
| [06 Interaction blueprints](06_MODALITIES_AND_INTERACTIONS.md) | connected visual, verbal, tactile, written, and symbolic modes |
| [07 Worked examples](07_WORKED_EXAMPLES.md) | 18 complete traces and reverse checks |
| [08 Practice prompts](08_PRACTICE_BANK.md) | 72 authored items, separate from answers |
| [09 Answer key and fixtures](09_ANSWER_KEY.md) | explanations and 44 structured pair targets |
| [10 Feedback and review](10_FEEDBACK_AND_SPACED_REVIEW.md) | error distinctions, hints, confidence, later retrieval |
| [11 Data and engine](11_DATA_AND_ENGINE_CONTRACTS.md) | proposed domain objects and actual-schema adaptation |
| [12 Interface and privacy](12_INTERFACE_ACCESSIBILITY_AND_PRIVACY.md) | local/public boundaries, accessible notation and controls |
| [13 Acceptance tests](13_TESTS_AND_ACCEPTANCE.md) | 50 behavior cases plus content/human-review gates |
| [14 Exam/reference card](14_EXAM_CARD_AND_REVIEW.md) | compact study map and short review routine |
| [15 Sources and decisions](15_SOURCES_AND_DECISIONS.md) | source quality, explicit refinements, unresolved gates |
| [16 File manifest and QA](16_FILE_MANIFEST_AND_QA.md) | what this package actually contains and what was checked |

## Three layers of knowledge

**Reconstruct:** charge balance, minimum ion ratios, metal charge from context.  
**Recognize a local pattern:** nitrate/nitrite, sulfate/sulfite, chlorine’s four-member series.  
**Retrieve:** a family anchor’s name, formula, and charge; exceptions and conventional names.

The interaction should keep these visible. A vocabulary gap should lead to an ion card; an algebra gap to a ledger; a notation gap to a group lens. Never collapse all three into “wrong.”

## Defaults worth preserving

Local/private learning first. Topic-first public presentation later. No new launcher or competing curriculum store. Answer keys are explicit, not generated on the fly. The core module functions without a model service. Valid alternate reasoning survives. Optional deeper physics explains the rule without burying the introductory answer.

## One source limitation to resolve

The original ion-list attachment was found but did not yield readable content or a downloadable backing file in this build. The complete working bank therefore preserves the earlier conversation transcription and marks course verification pending. Most ordinary chemistry rules were externally checked; exact instructor-list completeness is a separate gate. See [15](15_SOURCES_AND_DECISIONS.md#src-course-ions). This does not require rebuilding the lesson design or stopping implementation of the local candidate.

## Scope of the handoff

The Markdown files are a scaffold for the software and a useful fallback for human study. They are not the final limit of the experience. Codex should turn the same underlying model into synchronized cards, charge totals, formulas, spoken/written practice, targeted feedback, and review that is explainable to the learner.
