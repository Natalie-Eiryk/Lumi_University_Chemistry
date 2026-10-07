---
document_id: LU-IONS-DESIGN-01
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Codex: integrate a chemistry learning module, not a document viewer

## The task

Implement **LU-CHEM-IONS-001 — Ion Language: Name ↔ Formula** inside the existing Lumi University / teaching-campus system. Use this packet as a scaffolded design and seed-content source. Build a stronger interactive experience than static Markdown: coordinated models, reusable chemistry logic, staged hints, bidirectional practice, private notes, and evidence-aware review.

The desired product is not a new standalone website, a competing launcher, a copied doctrine, or an LLM that improvises answer keys. The deliverable should feel like an existing campus lesson with a new chemistry capability.

Read [00](00_START_HERE.md), [03](03_CHEMISTRY_RULES_AND_BOUNDARIES.md), [11](11_DATA_AND_ENGINE_CONTRACTS.md), [13](13_TESTS_AND_ACCEPTANCE.md), and [15](15_SOURCES_AND_DECISIONS.md) before designing the adapter. Use lesson files and the example bank during implementation.

## Phase 0 — inspect, map, then touch code

Read the workspace’s current `AGENTS.md` and relevant local instructions. Identify the actual university/campus shell, module registry, canonical source location, current lesson schema, renderer, formula renderer, learner storage, export/import, privacy boundary, test runner, and launcher. Preserve uncommitted changes and existing subject tools.

The repository surfaces inspected for this design are listed with Git blob SHAs in 15. They are useful starting evidence, not a license to assume the local workspace is identical. Specifically, the observed v2 LearningItem schema supports teaching/scaffold objects, but the current local campus may have a newer adapter.

Produce an integration map before broad edits:

| Concern | Actual existing symbol/path | Reuse / extend / blocked | Planned change |
|---|---|---|---|
| module registration | resolve locally | decide after inspection | register one stable module ID |
| source content ownership | resolve locally | prefer reuse | one canonical editable content source |
| lesson/rendering shell | resolve locally | prefer reuse | map the six lesson specifications |
| formula parsing/notation | resolve locally | extend only if needed | domain logic from 11 |
| learner progress/notes | resolve locally | prefer reuse | private event/projection adapter |
| local launcher | resolve locally | reuse | no new competing server |
| publication | resolve locally | separate gate | no default public release |
| tests | resolve locally | reuse | matrix in 13 |

Do not fill unresolved cells with guessed code symbols. A genuinely missing hook requires a small documented adapter or a blocking question, not an entire replacement architecture.

## Phase 1 — one useful vertical slice

Implement L01 + L03 with CaCl₂ and Al₂(SO₄)₃, plus the Na₂O₂ non-reduction regression test. This slice must support: readable lesson, ion cards, counts, charge ledger, conventional formula, one hint, Check, explanation, and private progress. It must work with keyboard and tap controls, with no model service.

Include one conventional-grouping diagnosis: CaN₂O₆ for Ca(NO₃)₂. Preserve the correct atom inventory while showing the representation repair. This slice tests the hardest architectural distinction early instead of leaving it for polish.

## Phase 2 — content and translation engine

Compile the 62-entry provisional ion bank and 44 curated compound records into the existing data system. Reconcile the actual instructor source when available; retain provenance flags until then. Add all six lesson routes, 18 worked examples, and 72 seed prompts with separated answer keys and hint states.

Implement the pure functions in 11. Reuse the existing frontend language; keep any native core aligned with the repository’s C++ policy. Do not introduce Rust, an unrelated framework, or a Python service just to support these lesson interactions.

## Phase 3 — modalities and feedback

Connect family wall, charge tiles, equation ledger, notation lens, translator, and repair tasks through shared state. Add optional spoken-name practice with a transcript. Add notebook separation and confirmed transcription, not silent OCR-based grading.

Implement component-level feedback and unsupported/ambiguous states. A missing ion is a content gap, not a hallucination opportunity. A correct alternate derivation is not wrong because it uses a different arithmetic layout.

## Phase 4 — review and persistence

Add direction-specific recall, hints/reveal accounting, optional confidence, shaky flags, and an adjustable bounded review queue. Resolve the legacy confidence-schema mismatch explicitly. Preserve existing subject records and export/import formats where possible; use versioned migration with backups when necessary.

No automatic notifications, cloud synchronization, or learner-note publication. Design timestamps and IDs must come from actual events; do not copy illustrative dates into runtime histories.

## Phase 5 — validate and hand back

Run actual unit, content, integration, accessibility, and visual checks. Test at desktop and iPad-sized widths, in keyboard-only and tap-only use, and with offline/no-audio fallback. Report commands and observed results. Label manual accessibility/science review separately from automated tests.

A local integrated preview may be delivered under the user’s authorized workspace request. Public publishing, commits/pushes outside the agreed workflow, canonical adventure promotion, changing the central doctrine, and changing site/DNS/security settings are separate actions, not implied by reading this packet.

## Invariants Codex must preserve

- Topic-first public identity; course sources and personal notes stay backstage.
- Charge is separate from counts; whole-ion ratios are reduced without mutating ions.
- All generated compound exercises come from the reviewed pair pool.
- -ate/-ite is a local family rule; -ide is not a monatomic detector; Roman numerals are not atom counts.
- Known source simplifications remain visibly scoped rather than silently rewritten.
- Core answer checking is deterministic and testable; an LLM is optional explanation assistance.
- Alternate valid mathematics is accepted; conventional formatting can still be requested as a separate outcome.
- Dragging, audio, a mouse, or a cloud model must not be required to learn.
- Private data does not become public by hiding it in a collapsed panel.
- No new launcher or ad hoc process killing. Reuse the existing explicit conflict-confirmation flow; cancel remains the default and active study work must be preserved.
- “Compiled a design” is not “implemented the module,” and schema validity is not proof of scientific correctness.

## Definition of done for the first integration

The module appears in the existing local teaching navigation. Every lesson is readable. At least the core interactive components operate from shared data. All 72 items resolve to explicit keys; all 44 compound records pass arithmetic/structural checks. The named boundary tests pass. Notes and progress survive an ordinary reload and can be exported. Existing subjects and launch behavior still work. Public output contains no private material. Remaining source or human-review gates are plainly reported.

## Handback format

Return the real local route/launch path, changed files, architectural mapping, implementation scope, tests run with outcomes, screenshots of actual UI, source-reconciliation status, unresolved gaps, and exact actions still requiring approval. Do not return only “done,” a plan, or a mocked-up page.

## Suggested work-ticket IDs

`IONS-100` inspect adapters. `IONS-110` compile content. `IONS-120` domain engine. `IONS-130` core lessons/ledger. `IONS-140` family/audio/repair views. `IONS-150` diagnostics/review. `IONS-160` persistence/privacy. `IONS-170` regression/accessibility. `IONS-180` review/release handback.

Each ticket links to this module ID, the governing design sections, and the tests it satisfies. Preserve the project’s existing ticket system rather than creating another tracker.
