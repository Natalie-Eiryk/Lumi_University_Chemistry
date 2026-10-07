---
document_id: 05_FEEDBACK_AND_UI_CONTRACT
package_id: LU-CHEM-Q13-SCAFFOLDS
version: 0.1.0
status: editorial_draft
created: 2026-09-28
visibility: editorial
integration_mode: additive_scaffold_overlay
assessment_owner: existing_native_exercises
---

# Feedback, interaction, and privacy contract

## One rule for the UI

**Preserve every part of the learner’s work that remains useful.**

The type field and the name/formula field must retain separate native results. Scaffold observations are additional explanations, not replacements for those results.

## Proposed presentation states

These are adapter-level suggestions; reuse existing equivalents instead of adding a competing state system.

| State | Meaning | Example message |
|---|---|---|
| matches_reference | This requested part agrees | “CS₂ matches carbon disulfide.” |
| revisit_type | Name/formula can stand; type needs attention | “Keep CS₂. Check only the compound type.” |
| check_symbol | A token/name correspondence differs | “P is phosphorus; potassium is K. Read the first symbol again.” |
| check_atom_count | Prefix or formula count differs | “The formula has five O atoms. Which word means five?” |
| check_charge_ratio | Known-ion inventory is nonneutral | “One K⁺ and one sulfate give −1. What copy is missing?” |
| check_group_notation | Atom counts match but conventional grouping differs | “Your inventory matches. Show two chlorate groups as (ClO₃)₂.” |
| specify_metal_state | Constituent names are present; Stock specificity missing | “Sulfide is −2; what state must Ni have?” |
| naming_mode_review | Recognized identity and requested convention differ | “Diborane is recognized. The requested count-prefix form is diboron hexahydride.” |
| needs_context | Supported reference cannot settle the result | “This case needs a reference or a naming-mode clarification.” |

Never use these labels to overwrite the native checker’s stored outcome silently. A discrepancy between native grading and a scientifically recognized alias is a content review item.

## Hint ladder

0. **No hint:** preserve the original exercise.
1. **Orient:** identify the relevant decision: type, charge, count, or symbol.
2. **Represent:** show ions, counts, or periodic identities without completing the response.
3. **Work one step:** demonstrate one charge subtotal or one prefix mapping.
4. **Walk through:** reveal the full explanation and conventional target.

The learner can choose a level directly or read the complete scene. This is learning support, not a forced failure ladder. Avoid locks that require intentional wrong answers to unlock teaching.

## Example structured observation

This is a **proposed overlay record**, not a claimed current API. It belongs to transient UI state or existing private help storage; it does not create an assessment attempt.

```json
{
  "contract": "proposal.lumi.q13.scaffold-observation.v1",
  "rowId": "q13-q-15",
  "nativeFields": {
    "CR-329": "matches_reference",
    "CR-330": "revisit_type"
  },
  "preserveFieldIds": ["CR-329"],
  "suggestedScaffoldIds": ["Q13-SCF-01"],
  "claimScope": "this_observed_attempt_only",
  "inferredCause": null,
  "createsAttempt": false,
  "mutatesAnswer": false,
  "exportsPrivateText": false
}
```

The actual typed value remains in the app’s existing response record. Do not duplicate it into a new telemetry channel just to explain it.

## Component proposals

### Two-field check panel

Separate formula/name and type indicators, each with a text explanation. A correct field stays visible while the other opens help. Do not rely on color to communicate status.

### Symbol lens

Tap/focus an element token to show its exact symbol and name. Preserve capitalization. If an input is ambiguous, show the interpretation and ask for confirmation. No silent CO-to-Co normalization.

### Whole-ion counter

Cation and anion cards show formula and signed charge separately. Plus/minus controls change complete copies. A ledger sums charge. An optional inventory expands atom counts without changing the ion record.

### Prefix strip

Display 1–10 with their prefixes; highlight the **count being read**, not an answer selected behind the learner’s back. Stage the count check before the prefix check.

### Boundary lens

Toggle between whole salt constituents and internal bonds in a polyatomic ion. Labels must state the boundary. Use these as explanatory models, not a live simulation claiming quantum accuracy.

### Private model note

Two fields, “What I first thought” and “What I think now,” are optional and stored locally through existing note facilities. Prose is not automatically scored or exported.

## Formula parsing boundaries

Use the existing parser/renderer if available. If a small extension is necessary, document it and test it. Separate:

- element symbols and their case;
- atom counts;
- grouped constituents;
- whole-ion charges;
- coefficient/copy counts;
- target naming model.

Do not derive the charge of nitrate from its three oxygens alone. Do not reduce Na₂O₂ to NaO. Do not reduce N₂O₄ to NO₂. Do not evaluate names by lowercasing formulas. Do not claim that equal atom inventories imply identical structures.

Name matching can normalize ordinary capitalization and spacing in English names. Formula normalization must retain chemical case. Roman-numeral variants and alternate molecular spellings require a defined naming policy, not unbounded fuzzy matching.

## Semantic rendering

For public display use true subscript/superscript markup or the existing equivalent:

```html
<span class="chemical-formula" aria-label="two complete ammonium groups and one sulfur atom">
  (NH<sub>4</sub>)<sub>2</sub>S
</span>
```

Editable plain-text input may remain `(NH4)2S`; display and input are linked views, not different answers. Accessible labels describe what the notation encodes. Do not call the neutral grouped formula a free ion or add a charge not in the input.

## Accessibility and data boundaries

Provide keyboard alternatives to dragging, visible focus, readable text labels, no automatic narration, and reduced-motion alternatives. A phone-width view must keep the formula and explanation usable without a wide-table dependency. Keep long formulas scrollable without clipping charges.

A help panel must restore focus to the field or button that opened it. Refreshing must not reset work. Browser storage can be cleared, so preserve the app’s explicit export/import route; do not promise permanent memory.

No original scans, worksheet mistakes, personal notes, or private evidence-map files enter public builds. Rendering the private evidence filename in a local editorial index does not authorize deploying that file. Use an explicit content allowlist.

## Instructional honesty

A scene is fiction. An equation is a model. A source claim is attributable. A software behavior not yet coded is a proposal. A model-assisted prose response is not a verified grade. Keep those boundaries visible during implementation.

Sources: S-MATERIALS MAT-06, MAT-10, MAT-15, publication boundaries; S-INDEX PR-62, PR-63, PR-67, PR-72. [Source register](09_SOURCES_DECISIONS_AND_QA.md).
