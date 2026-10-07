---
document_id: 06_EXISTING_ID_BINDINGS
package_id: LU-CHEM-Q13-SCAFFOLDS
version: 0.1.0
status: editorial_draft
created: 2026-09-28
visibility: editorial
integration_mode: additive_scaffold_overlay
assessment_owner: existing_native_exercises
---

# Existing exercise bindings — additive, not a second bank

## Authority and interpretation

S-INDEX explicitly lists the Q13 row IDs and their two fields. The **first field** in each pair holds the missing name or formula; the **second field** holds type. The attachment map below uses those identities. It does not introduce a new assessment ID or another canonical answer key.

The known native source paths are recorded in the implementation brief. Resolve them in the current workspace. If a field was renamed, record the alias or migration rather than silently assigning a similar-looking ID.

## Primary binding summary

| Scaffold | Fields that directly benefit | Related existing support |
|---|---|---|
| Q13-SCF-01 | CR-328, CR-330, CR-338 | L06; MAT-12, MAT-15 |
| Q13-SCF-02 | CR-307, CR-308 | P/K identity; NBr₃ CR-315; PR-72 |
| Q13-SCF-03 | CR-309, CR-313, CR-333 | L01/L03; whole-ion builder; WE-06/07/09 |
| Q13-SCF-04 | CR-303 | L04; NiS CR-291; Fe₂O₃ WE-16 |
| Q13-SCF-05 | CR-305, CR-307, CR-311 | Prefixes CR-226–235; N₂O₄ CR-331 |
| Q13-SCF-06 | CR-338, CR-341, CR-342 | L02/L06; ammonium nitrate CR-325/326; WE-15 peroxide |

## Proposed serialized attachment contract

All fields below belong to a proposed scaffold attachment adapter. Reuse the current system’s equivalent structures where they exist. These are **not undeclared additions to the central adventure manifest**.

```json
{
  "contract": "proposal.lumi.q13.scaffold-bindings.v1",
  "packageId": "LU-CHEM-Q13-SCAFFOLDS",
  "version": "0.1.0",
  "snapshotDate": "2026-09-28",
  "liveWorkspaceVerified": false,
  "assessmentOwner": "existing_native_exercises",
  "authorizesPublication": false,
  "bindings": [
    {
      "scaffoldId": "Q13-SCF-01",
      "contentPath": "scaffolds/Q13-SCF-01_TWO_CHECKS.md",
      "primaryAnchors": [
        {
          "setId": "q13-naming",
          "rowId": "q13-q-14",
          "fieldIds": [
            "CR-328"
          ]
        },
        {
          "setId": "q13-naming",
          "rowId": "q13-q-15",
          "fieldIds": [
            "CR-330"
          ]
        },
        {
          "setId": "q13-naming",
          "rowId": "q13-q-19",
          "fieldIds": [
            "CR-338"
          ]
        }
      ],
      "relatedFieldIds": [
        "CR-306",
        "CR-308",
        "CR-342",
        "CR-316",
        "CR-340"
      ],
      "lessonRefs": [
        "L06"
      ],
      "materialRefs": [
        "MAT-12",
        "MAT-15"
      ],
      "practiceRefs": [],
      "workedExampleRefs": [],
      "offerWhen": "native_type_disagrees_and_paired_translation_matches_or_learner_request",
      "offerIsDiagnosis": false,
      "autoFillAnswers": false,
      "changesNativeScoring": false
    },
    {
      "scaffoldId": "Q13-SCF-02",
      "contentPath": "scaffolds/Q13-SCF-02_SYMBOLS.md",
      "primaryAnchors": [
        {
          "setId": "q13-naming",
          "rowId": "q13-q-04",
          "fieldIds": [
            "CR-307",
            "CR-308"
          ]
        }
      ],
      "relatedFieldIds": [
        "CR-315",
        "CR-316"
      ],
      "lessonRefs": [
        "L02",
        "L06"
      ],
      "materialRefs": [
        "MAT-01",
        "MAT-12",
        "MAT-13"
      ],
      "practiceRefs": [
        "PR-72"
      ],
      "workedExampleRefs": [],
      "offerWhen": "confirmed_symbol_name_mismatch_or_learner_request",
      "offerIsDiagnosis": false,
      "autoFillAnswers": false,
      "changesNativeScoring": false
    },
    {
      "scaffoldId": "Q13-SCF-03",
      "contentPath": "scaffolds/Q13-SCF-03_WHOLE_IONS.md",
      "primaryAnchors": [
        {
          "setId": "q13-naming",
          "rowId": "q13-q-05",
          "fieldIds": [
            "CR-309"
          ]
        },
        {
          "setId": "q13-naming",
          "rowId": "q13-q-07",
          "fieldIds": [
            "CR-313"
          ]
        },
        {
          "setId": "q13-naming",
          "rowId": "q13-q-17",
          "fieldIds": [
            "CR-333"
          ]
        }
      ],
      "relatedFieldIds": [
        "CR-158",
        "CR-159",
        "CR-160",
        "CR-294",
        "CR-296",
        "CR-298",
        "CR-325",
        "CR-321",
        "CR-323"
      ],
      "lessonRefs": [
        "L01",
        "L03"
      ],
      "materialRefs": [
        "MAT-06",
        "MAT-10"
      ],
      "practiceRefs": [
        "PR-27",
        "PR-62",
        "PR-63",
        "PR-70"
      ],
      "workedExampleRefs": [
        "WE-06",
        "WE-07",
        "WE-09"
      ],
      "offerWhen": "known_ion_ratio_nonzero_or_grouping_differs_or_learner_request",
      "offerIsDiagnosis": false,
      "autoFillAnswers": false,
      "changesNativeScoring": false
    },
    {
      "scaffoldId": "Q13-SCF-04",
      "contentPath": "scaffolds/Q13-SCF-04_ROMAN_NUMERALS.md",
      "primaryAnchors": [
        {
          "setId": "q13-naming",
          "rowId": "q13-q-02",
          "fieldIds": [
            "CR-303"
          ]
        }
      ],
      "relatedFieldIds": [
        "CR-291",
        "CR-301",
        "CR-214",
        "CR-215"
      ],
      "lessonRefs": [
        "L04"
      ],
      "materialRefs": [
        "MAT-11"
      ],
      "practiceRefs": [
        "PR-13",
        "PR-45",
        "PR-66",
        "PR-67"
      ],
      "workedExampleRefs": [
        "WE-16"
      ],
      "offerWhen": "stock_numeral_missing_or_supported_charge_mismatch_or_learner_request",
      "offerIsDiagnosis": false,
      "autoFillAnswers": false,
      "changesNativeScoring": false
    },
    {
      "scaffoldId": "Q13-SCF-05",
      "contentPath": "scaffolds/Q13-SCF-05_PREFIXES.md",
      "primaryAnchors": [
        {
          "setId": "q13-naming",
          "rowId": "q13-q-03",
          "fieldIds": [
            "CR-305"
          ]
        },
        {
          "setId": "q13-naming",
          "rowId": "q13-q-04",
          "fieldIds": [
            "CR-307"
          ]
        },
        {
          "setId": "q13-naming",
          "rowId": "q13-q-06",
          "fieldIds": [
            "CR-311"
          ]
        }
      ],
      "relatedFieldIds": [
        "CR-226",
        "CR-227",
        "CR-228",
        "CR-229",
        "CR-230",
        "CR-231",
        "CR-232",
        "CR-233",
        "CR-234",
        "CR-235",
        "CR-331",
        "CR-332",
        "CR-237"
      ],
      "lessonRefs": [
        "L06"
      ],
      "materialRefs": [
        "MAT-13"
      ],
      "practiceRefs": [],
      "workedExampleRefs": [],
      "offerWhen": "molecular_count_prefix_mismatch_after_identity_probe_or_learner_request",
      "offerIsDiagnosis": false,
      "autoFillAnswers": false,
      "changesNativeScoring": false
    },
    {
      "scaffoldId": "Q13-SCF-06",
      "contentPath": "scaffolds/Q13-SCF-06_BOUNDARIES.md",
      "primaryAnchors": [
        {
          "setId": "q13-naming",
          "rowId": "q13-q-19",
          "fieldIds": [
            "CR-338"
          ]
        },
        {
          "setId": "q13-naming",
          "rowId": "q13-q-21",
          "fieldIds": [
            "CR-341",
            "CR-342"
          ]
        }
      ],
      "relatedFieldIds": [
        "CR-310",
        "CR-325",
        "CR-326",
        "CR-210",
        "CR-288"
      ],
      "lessonRefs": [
        "L02",
        "L06"
      ],
      "materialRefs": [
        "MAT-08",
        "MAT-10",
        "MAT-12",
        "MAT-13"
      ],
      "practiceRefs": [
        "PR-38",
        "PR-62",
        "PR-64",
        "PR-65",
        "PR-71"
      ],
      "workedExampleRefs": [
        "WE-15"
      ],
      "offerWhen": "boundary_context_needed_or_recognized_name_variant_or_learner_request",
      "offerIsDiagnosis": false,
      "autoFillAnswers": false,
      "changesNativeScoring": false
    }
  ]
}
```

## Lifecycle of an attachment

1. Resolve the native row and field.
2. Observe the existing check’s result or an explicit help request.
3. Offer the shortest relevant scaffold; do not claim a cause that has not been probed.
4. Keep both the entered answer and its native state.
5. Allow the learner to close, switch mode, or return to the same field.
6. Let the learner submit any revised answer using the native control.
7. Record a help event only through the existing private progress pathway, if available.

Do not append historical worksheet attempts to the app, manufacture new statistics, or write another source of truth for CR answers.

## Missing/changed reference handling

For a missing ID, mark `unresolved_anchor` in an editorial report and omit that action from the reader. The scaffold itself may remain readable. Do not redirect silently to a different question.

For a renamed ID, map the documented alias and record the current target. Keep the snapshot ID for provenance. For a disputed answer convention, retain both source identities and ask for review.

## Prior story integration

These short scenes may be offered beside the relevant Loom reading or directly beside exercises. Do not duplicate the entire long story. Resolve current chapter IDs from the installed source rather than guessing chapter anchors from a display title. A useful presentation is “Short explanation / Story scene / Full related chapter,” with all three returning to the same activity.

Source: S-INDEX lines 284–312, 1105–1110; S-MATERIALS lines 227–231. [Source register](09_SOURCES_DECISIONS_AND_QA.md).
