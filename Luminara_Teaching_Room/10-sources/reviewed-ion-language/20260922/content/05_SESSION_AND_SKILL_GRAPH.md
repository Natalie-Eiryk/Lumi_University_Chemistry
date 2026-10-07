---
document_id: LU-IONS-DESIGN-05
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Session routes and skill evidence

## The default route: about 60 minutes, with a natural break

These durations are planning defaults, not countdowns or evidence-based optimums. A learner can pause, skip ahead, return to an earlier bridge, or use reference aids at any time.

| Segment | Target minutes | Evidence or artifact |
|---|---:|---|
| Orientation and three low-stakes probes | 3 | prior confidence; no score deduction |
| L01 Charge and representation | 7 | distinguishes atom count, ion charge, and group count |
| L02 Names, roots, and common charges | 8 | retrieves selected ions in both directions |
| L03 Build a neutral formula | 10 | constructs counts without changing ion identity |
| L04 Read a formula and infer a metal charge | 8 | Roman numeral justified by a charge ledger |
| L05 Oxygen families and contrast anchors | 12 | names siblings and states what cannot be inferred |
| L06 Mixed translation and reflection | 9 | transfers to different items; explains one choice |
| Exit note and chosen review route | 3 | one secure rule, one shaky anchor, next step |

Break after L03 for two sessions of roughly 28 and 32 minutes. The full 62-ion bank is available as a reference, not a one-session memory demand. The initial teaching examples repeatedly use Na⁺, Ca²⁺, Al³⁺, Fe²⁺/Fe³⁺, Cl⁻, O²⁻, nitrate, and sulfate; later segments broaden this set.

## Other entry routes

**Ten-minute reset:** L01 notation contrast → WE-02 calcium chloride → one nitrate/sulfate contrast → two fresh translations. Do not relabel it “mastery.”

**Twenty-minute formula clinic:** L03 → L04 → six mixed examples selected by current uncertainty. Reference cards may stay open; record that assistance honestly.

**Reference mode:** family wall + translation trees + cheat sheet. Viewing references creates no successful-retrieval event.

**Independent retrieval:** hide answers until a deliberate reveal; hints remain available. An exposed answer converts the event to assisted study, not an unaided pass.

## Skill identifiers

| ID | Skill | A useful observable check | Prerequisites |
|---|---|---|---|
| SK-01 | separate charge/subscript/coefficient | explains NO₃⁻ versus three nitrate ions | none |
| SK-02 | retrieve ion identity and charge | sulfate → SO₄²⁻ and the reverse | SK-01 |
| SK-03 | use scoped periodic charge hints | Ca → Ca²⁺; knows Fe needs more information | SK-01 |
| SK-04 | discriminate oxyanion family labels | nitrite versus nitrate without changing charge | SK-02 |
| SK-05 | derive minimum neutral ratio | Al³⁺ + O²⁻ → 2:3 | SK-01, SK-02 |
| SK-06 | preserve group identity in notation | calcium nitrate → Ca(NO₃)₂ | SK-05 |
| SK-07 | infer variable-metal charge | Fe₂O₃ → +3 per Fe | SK-01, SK-02 |
| SK-08 | translate name ↔ formula | both directions on different examples | SK-02, SK-05, SK-06, SK-07 |
| SK-09 | identify a rule’s scope | routes CO₂ away from the ionic translator | SK-01 |
| SK-10 | explain and repair a model | detects why NaO is not sodium peroxide | SK-05, SK-06 |

This is a recommendation graph, not a lock graph. Never block the learner from a reference because a prerequisite probe was missed.

## Scaffolding levels

- `S3 worked`: all ion identities, charge totals, ratio, and naming are shown.
- `S2 completion`: identities shown; learner supplies one missing count or numeral.
- `S1 cue`: a prompt such as “What is the charge on the whole sulfate group?”
- `S0 independent`: no content revealed before response.

Store the highest assistance actually used. A learner-requested step back is normal. Do not force faster fading because of a degree or earlier success in another topic.

## Required telemetry distinctions

A click on Check is not necessarily a completed attempt. Save the submitted response, which hints were already exposed, recognition versus production direction, optional confidence, component-level diagnosis, and content version. No keystroke surveillance. No emotional inference from pauses.

## First three probes

1. Point to the atom count and charge in NO₃⁻. (`PR-01`)
2. Explain why Ca²⁺ and one Cl⁻ do not make the requested neutral formula. (`PR-05`)
3. Choose whether “nitrate” contains enough information without a remembered ion identity. (`PR-10`)

Missing a probe routes to a bridge, not a failure screen. The [practice bank](08_PRACTICE_BANK.md) and [answer key](09_ANSWER_KEY.md) use stable IDs so routing can be deterministic.

## Completion language

Prefer “You translated three different salts independently today” over “You mastered chemistry.” A later successful retrieval supports “retained on review.” Confidence and performance can disagree; show that gently and let Natalie mark an item shaky herself.
