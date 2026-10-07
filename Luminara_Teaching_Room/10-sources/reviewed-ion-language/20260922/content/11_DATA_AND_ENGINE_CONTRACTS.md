---
document_id: LU-IONS-DESIGN-11
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Data contracts and the deterministic chemistry core

## Status and ownership

The existing repository exposes `LearningItem`, `TeachingModuleManifest`, and `LearnerProgressRecord` schemas. Their inspected fields are summarized below; the actual files must be reopened at implementation time. This packet’s ion structures and engine functions are **proposed domain contracts**, not claims that these functions already exist. [Repository evidence](15_SOURCES_AND_DECISIONS.md#src-repo)

Keep three layers separate: reviewed content data → pure chemistry/feedback functions → campus UI and storage adapters. The LLM may help explain, but never supplies an unverified answer key at runtime.

## Existing-schema mapping

| Existing object | Reuse | Proposed extension point / caution |
|---|---|---|
| LearningItem | `id`, `kind`, `moduleId`, `deweyPath`, `system`, `topic`, `prompt`, `answer`, `tags` | existing `teaching` object can carry a reviewed `ionLanguage` payload |
| TeachingModuleManifest | title, version, route, sourceRefs, itemCollections | inspect runtime semantics of diagnostics/lumiSync before setting options |
| LearnerProgressRecord | itemId, attempts, lastOutcome, lastSeenAt, nextReviewAt | optional confidence conflicts with currently required numeric confidence; resolve without inventing a value |
| Adventure packet contracts | only if a full canonical story is later produced | a practice module is not automatically an Adventure or a canon event |

Use existing kinds such as `vocabulary`, `scaffold`, `station`, and `retrieval`; do not invent a new kind without a versioned integration change. Do not transplant `.forge` fields into strict canonical adventure schemas.

## Proposed IonRecord

```json
{
  "id": "ION-SULFATE",
  "formulaAscii": "SO4",
  "charge": -2,
  "atoms": {"S": 1, "O": 4},
  "preferredName": "sulfate",
  "nameAliases": [],
  "formulaAliases": [],
  "familyId": "sulfur-oxyanion",
  "scope": "introductory_ion_bank",
  "sourceRefs": ["SRC-COURSE-IONS", "SRC-IONIC"],
  "courseSourceVerified": false,
  "spokenName": "sulfate",
  "spokenFormula": "S O, subscript four, charge two minus"
}
```

Store charge separately from atom counts. Render it as SO₄²⁻, not as a third number in the formula parser’s atom sequence.

## Proposed constituent model

```json
{
  "itemId": "PR-24",
  "formulaAscii": "Al2(SO4)3",
  "constituents": [
    {"ionId": "ION-AL", "count": 2},
    {"ionId": "ION-SULFATE", "count": 3}
  ],
  "netCharge": 0,
  "atomCounts": {"Al": 2, "S": 3, "O": 12},
  "preferredName": "aluminum sulfate",
  "acceptedNames": ["aluminum sulfate", "aluminium sulfate"],
  "scope": "reviewed_naming_exercise"
}
```

The constituent model is essential: atom counts alone cannot represent the distinction between oxide and peroxide or establish a unique ionic decomposition for arbitrary formulas.

## A valid-shaped LearningItem candidate

```json
{
  "id": "LU-CHEM-IONS-001:PR-24",
  "kind": "retrieval",
  "moduleId": "LU-CHEM-IONS-001",
  "deweyPath": "540/ion-language",
  "system": "chemistry",
  "topic": "ionic-formula-translation",
  "prompt": "Write the formula for aluminum sulfate.",
  "answer": "Al2(SO4)3",
  "tags": ["SK-05", "SK-06", "name_to_formula"],
  "source": {"refs": ["SRC-CHAT", "SRC-IONIC"]},
  "teaching": {
    "ionLanguage": {
      "contractVersion": "1.0.0-candidate",
      "cationId": "ION-AL",
      "anionId": "ION-SULFATE",
      "expectedCounts": [2, 3],
      "requireConventionalGrouping": true,
      "acceptedNames": ["aluminum sulfate", "aluminium sulfate"]
    }
  }
}
```

Do not assert this payload is runtime-supported merely because it validates structurally. Add an explicit adapter and feature test. The deweyPath and route are proposed values; reconcile with the workspace’s current registry.

## Pure engine hooks

| Hook | Input → output | Non-negotiable behavior |
|---|---|---|
| `parseFormula` | text + grammar mode → tree or parse issue | case-sensitive; bounded counts/depth; no eval |
| `parseIonInput` | formula + explicit charge → candidate ion | preserve superscript/charge distinction |
| `resolveIonName` | reviewed name/alias → IDs or ambiguity | no unlisted-ion invention |
| `classifyTaskScope` | item scope + candidate → in-scope/route/referral | ammonium is supported; acids/complexes not guessed |
| `minimumIonRatio` | +p, −r → positive integer counts | gcd over ion charges, not atom counts |
| `composeConstituents` | ion IDs + counts → tree/counts/charge | preserve polyatomic atoms |
| `inferSingleCationCharge` | known anion, ion counts → charge or boundary | no rounding mixed-valence averages |
| `formatConventionalFormula` | constituent tree → display/string | conditional parentheses; omitted subscript 1 |
| `evaluateResponse` | item + confirmed response → component results | distinguish syntax, identity, charge, representation |
| `buildFeedback` | diagnostic evidence → hint text | acknowledge correct components; no unsupported mind-reading |
| `selectReview` | minimal learner state + content versions → queue | bounded, reproducible, assistance-aware |

## Parser scope

MVP grammar supports element symbols, positive integer atom counts, and parentheses for neutral formulas. Standalone-ion entry additionally accepts a separate charge control or an unambiguous suffix such as `SO4^2-`. Display Unicode subscript/superscript input is supported through a position-aware tokenizer. Plain `SO42-` is ambiguous; request clarification rather than treating 42 as an oxygen count or guessing intent.

Leading whole-formula coefficients, state symbols, hydrate dots, brackets for complexes, and equations must be explicitly recognized as unsupported or routed—not silently stripped. Known names are whitespace-tolerant; formula symbols remain case-sensitive. Normalize Unicode minus to a minus sign without flattening superscripts into subscripts. Never uppercase or lowercase an entire formula.

Example: `Al2(SO4)3` parses to Al count 2 and a group containing S count 1/O count 4 repeated 3 times. `Na2O2` stays sodium peroxide when that reviewed target is selected. Generic atom parsing alone does not choose oxide versus peroxide chemistry.

Resource limits: bound input length, nesting depth, and count magnitude; reject overflows; fail gracefully. The count validator must not allocate one object per enormous user-entered atom count.

## Response assessment example

```json
{
  "itemId": "LU-CHEM-IONS-001:PR-23",
  "submitted": "CaN2O6",
  "outcome": "needs_revision",
  "components": {
    "syntax": "valid",
    "atomInventory": "correct",
    "conventionalGrouping": "needs_revision",
    "ionIdentityEvidence": "requires_confirmation"
  },
  "diagnosticCode": "D-GROUP-LOST",
  "feedback": "Your atom totals match calcium nitrate. Show the two complete nitrate groups as Ca(NO3)2.",
  "independent": true
}
```

## Events and storage

Use a domain event record with unique event ID, item ID/version, confirmed response, outcome components, hint level, answer-revealed flag, optional confidence, and timestamp. Keep raw notebook material separate. App restarts and sync retries must not create duplicate attempts. An event is not a canonical story event; do not append study clicks to the Adventure Chronicle.

The inspected legacy progress schema requires numeric `confidence`. Before projecting unanswered-confidence events, choose an explicit compatible strategy: a versioned nullable-confidence migration, or retain the detailed local event and defer that legacy projection. Do not encode “not asked” as zero and thereby claim the learner was unconfident. Do not force confidence entry just to satisfy storage.

## Generators and answer validation

Compile the 62 ion rows and the 44 approved compound records from the design packet into reviewed data. Create ion recall variants only from approved entries; compound variants only from the approved pair pool. If a target is unknown or ambiguous, produce `needs_clarification` or `unsupported`, not a scientifically invented answer.

Prove name→record→formula and formula→record→preferred-name round trips on the curated domain, including reviewed aliases. Matching atom inventory is necessary for many comparisons but is not sufficient to assert identical chemical identity in the general case.
