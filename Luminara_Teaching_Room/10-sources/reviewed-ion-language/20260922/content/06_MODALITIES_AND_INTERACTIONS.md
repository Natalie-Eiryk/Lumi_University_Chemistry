---
document_id: LU-IONS-DESIGN-06
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Interaction blueprints: one model, several ways to inspect it

## Shared state, not seven disconnected mini-apps

Every component reads the same ion records and current count state. Switching from tiles to equations must not reset the learner’s reasoning. The component contracts below describe behavior; Codex should implement them within existing campus components after inspection.

## CMP-FAMILY-WALL — visual recognition and recall

**Purpose:** reduce a flat list to remembered anchors and contrasts.  
**Inputs:** ion IDs, family relationships, tier, direction, mask state.  
**View:** one family at a time, with name/formula/charge as separately labeled fields. Keep related pairs near each other during instruction.  
**Actions:** flip one field; compare two cards; pin shaky; choose name→formula or reverse.  
**Feedback:** a charge mismatch is not a name mismatch.  
**Events:** `reference_opened`, `mask_changed`, `recall_submitted`, `shaky_toggled`.  
**Fallback:** the table in 04 plus paper covering one column.

Acceptance: a learner can compare nitrate and sulfate, notice the oxygen counts differ, and still see that -ate does not fix a count. Opening the reference does not produce a successful retrieval.

## CMP-LEDGER — tangible charge balancing

**Purpose:** link a whole ion to its total contribution.  
**Inputs:** curated cation and anion records; two nonnegative UI counts.  
**View:** count controls, positive subtotal, negative subtotal, total, then formula. Negative and positive labels remain visible even without color.  
**Actions:** drag tiles OR tap +/− OR type counts; undo/reset; inspect why a ratio is nonminimal.  
**Feedback:** `2(+3)+3(−2)=0` appears alongside—not instead of—the tile model.  
**Events:** intermediate edits remain workspace state; only Check produces an attempt.  
**Fallback:** paper cards with printed charges; one row per ion on a ledger.

Do not represent charge balance as an actual reaction simulation. Counts of zero are allowed while exploring but do not form a final two-ion compound. Do not let learners accidentally change SO₄ to SO₃ when adding a sulfate tile.

## CMP-NOTATION-LENS — charge, inner count, outer count

**Purpose:** distinguish what each number modifies.  
**View:** Ca(NO₃)₂ is linked to one calcium and two nitrate groups, each containing one nitrogen and three oxygens. A separate panel totals atoms.  
**Actions:** focus a symbol, group, subscript, or charge; narrate its meaning.  
**Fallback:** a marked-up written formula with labeled brackets.

Acceptance: highlighting the outside 2 selects the nitrate group, not just oxygen. Highlighting nitrate’s internal 3 selects oxygens per group. Do not show a nonexistent overall +2 charge on the final neutral formula.

## CMP-OXYGEN-FAMILY — vocabulary navigation, not chemistry animation

**Purpose:** attach names to members of a known family.  
**View:** chlorine’s four member cards; fixed −1 group-charge badge; oxygen counts 1–4.  
**Actions:** select a named card or step between adjacent cards. Dragging is optional; buttons provide full equivalence.  
**Narration:** “You selected chlorate, a different ion from chlorite.” Avoid “We attached an oxygen and automatically made chlorate.”  
**Transfer:** compare nitrate with sulfite, both with three oxygens.  
**Fallback:** four index cards ordered by oxygen count.

Acceptance: an unknown family returns a reference-needed state instead of applying the chlorine algorithm.

## CMP-TRANSLATOR — bidirectional coached work

**View:** prompt; learner answer; optional staged trace; Check; Hint; Reveal; notebook.  
**Actions:** type ASCII formulas, use subscript UI, speak a name to oneself, or enter a confirmed handwritten transcription.  
**Feedback:** show recognized ion identities and the earliest supported discrepancy. Show a valid alternate representation and its preferred course form separately.  
**Transfer:** both directions exist as distinct items; immediate reversal after reveal is assisted practice.  
**Fallback:** pencil and the decision trees in 14.

## CMP-AUDIO — name-to-formula listening

**Purpose:** practice producing a formula without seeing it.  
**Inputs:** curated `spokenName` and separately curated `spokenFormula`.  
**Example:** name cue “iron three sulfate”; feedback formula “F e, subscript two, open parenthesis, S O, subscript four, close parenthesis, subscript three.” Offer a more natural “two iron ions, three sulfate groups” paraphrase after the literal readout.

No automatic speech until Play. Supply repeat, pause, speed preference if supported, transcript, and a no-audio route. Device text-to-speech is optional capability, not a launch prerequisite. No microphone required. A speech-recognition interpretation, if later added, must be confirmed before grading because “sulfate” versus “sulfite” changes the chemistry.

## CMP-NOTEBOOK — my model alongside the conventional form

Two columns at wide widths; stacked panels on mobile. Preserve raw notes; derived/typed interpretations have an explicit confirmation state. Never auto-publish personal notes. “Compare my model” can show a charge ledger but cannot confidently grade arbitrary handwriting.

Paper fallback: left side for raw thinking; right side for the final conventional representation. The point is explanation, not forced conformity of every scratch mark.

## CMP-REPAIR — error discrimination

Show one intentionally flawed answer and ask the learner to identify the smallest repair. Good flaws: wrong family; incorrect metal state; nonminimal ion ratio; lost group; missing information. Bad flaws: random nonsense or deliberately ambiguous photos treated as definite errors.

Keep the user’s own attempts distinct from supplied examples. Never turn “the example is wrong” into “you are bad at this.”

## CMP-REVIEW — recall across sessions

Show a small chosen queue, direction, and available support. The learner can open a reference or end the queue without losing progress. Include retained versus relearned evidence rather than a single success badge. See [10](10_FEEDBACK_AND_SPACED_REVIEW.md).

## Multimodal lesson invariant

Each interaction must answer: What does the learner notice? What must the learner produce? Which model is being revised? What exact evidence updates the record? What is the keyboard/tap/text equivalent? Which information stays private?

Multiple representations are integrated because they describe the same state, not because more animation is inherently better. The instructional basis is summarized in [SRC-IES](15_SOURCES_AND_DECISIONS.md#src-ies). Accessible alternatives follow [SRC-W3C](15_SOURCES_AND_DECISIONS.md#src-w3c).
