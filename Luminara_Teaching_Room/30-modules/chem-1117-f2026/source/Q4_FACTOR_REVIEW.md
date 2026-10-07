<!-- @version 2026-09-22 @lifecycle REVIEWED_LOCAL_PILOT -->
# Q4 factor-practice ledger

Rules `q4-2026-09-22.1` cover the nine existing `source-09-q1` through
`source-09-q9` identities. The source is the two-page Q4 worksheet in
`10-sources/originals/Chem_1117_F2026.zip`, identified by `questions.json` and
SHA-256 `dab9d6a93b4e604c9bafbd5409be708ef8a7c366307bff021747f540ebef0c3d`.
Both pages were rendered and visually reviewed (printed pages 259–260).
The archive and existing authored question bank, wording, answer IDs and earlier
responses remain unchanged. No PDF is admitted to the lesson.

The worksheet supplies answers and asks for dimensional working. This workshop
checks the declared mathematical model; it does not claim to grade the instructor's
required method, medically validate the source's narrative, or certify a learner's
explanation. Existing neutral campus paraphrases remain in use.

| ID suffix | PDF page / printed page | Starting quantity → target | Model result as reported | Precision and variation range |
| --- | --- | --- | --- | --- |
| q1 | 1 / 259 | 120. day → hs | 1.04e5 hs | 3 figures; 1–10000 day |
| q2 | 1 / 259 | 3000. unit/day → unit/min | 2.083 unit/min | 4 figures; 1–1e9 unit/day; generic counts preserve the existing paraphrase |
| q3 | 1 / 259 | 1.2 m → in | 47 in | 2 figures; 0.001–10000 m |
| q4 | 1 / 259 | 4.2 in/year → mm/ms | 3.4e-9 mm/ms | 2 figures; 0.001–10000 in/year; 365-day model year |
| q5 | 2 / 260 | 6813 L/day → USgal/min | 1.250 USgal/min | 4 figures; 0.001–1e9 L/day; US liquid units |
| q6 | 2 / 260 | 1800 USqt/day → lb/day | 3800 lb/day is consistent with two-figure rounding | Precision needs review; 0.001–1e9 USqt/day; assume exactly 1 g/mL in this model |
| q7 | 2 / 260 | 1500. mg/day → lb/year | 1.207 lb/year | 4 figures; 0.001–1e9 mg/day; 365-day model year |
| q8 | 2 / 260 | 11.4 L/day → mL/min | 7.92 mL/min | 3 figures; 0.001–1e9 L/day |
| q9 | 2 / 260 | 4.80e4 ft² → m² | 4.46e3 m² | 3 figures; 0.01–1e12 ft²; square the entire length factor |

Every row is mapped, built and checked against independent arithmetic, native
tests, and an original/variation browser journey. Local release evidence is in
`MILESTONE_9_REPORT.md` and `evidence/u09-factors/`. The released calculation scope
does not establish full course coverage or resolve the convention limits below.

## Source distinctions and assumptions

- Q7's printed target is **lb/yr**. The prior campus wording describes annual
  consumption in pounds over 365 days. Its text and old answers are preserved;
  the new checked panel explains that it follows the printed rate units. A factor
  of 365 day/year keeps the yearly denominator. A total-mass answer is not silently
  accepted as the rate.
- Use the existing campus conversion reference: 1 in = 2.54 cm, 1 ft = 12 in,
  1 US qt = 0.946352946 L, 1 US gal = 4 US qt, 1 lb = 453.59237 g, and the usual
  exact metric/time definitions. No external factors were fetched. The source
  handwriting uses rounded 0.9463 L/qt and 454 g/lb. In Q7 that produces a
  different rounded answer from the printed 1.207. Handwriting is learner evidence,
  not an authoritative key. Approximate alternatives are visibly outside this
  declared model; instructor acceptance of them remains unverified.
- Q6's 1800 has ambiguous trailing integer zeros. Accepting the printed 3800 as
  consistent rounding does not establish its precision. Density is an explicit
  model assumption, not a measured physical claim. Variations use the entered
  starting precision within this assumption; actual measurement uncertainty is
  not assessed.
- Variations preserve the same units and assumptions. They are authored practice
  in a separate draft, never a rewrite of the assigned source. Ranges bound the
  arithmetic, not biological or engineering plausibility.

## Evaluation and preservation

The existing C++ decimal reader handles numeric input. Native checks separately
report factor equivalence, literal unit cancellation, final value, final unit and
precision. Powers 1–3 apply to both numbers and units. At most eight factors are
admitted. Empty input stays pending; malformed, negative, zero-denominator and
out-of-range inputs stay recoverable and are not clamped. Relative tolerances are
1e-12 for factor equivalence and 1e-10 for the answer. Rounding halfway within the
declared tolerance remains needs-review. Unknown or more than ten significant
figures do not receive a precision certificate. Displayed model values use up to
twelve digits and are not asserted to be exact decimal expansions.

Eighteen independent drafts preserve each original/variation pair. Up to sixty
intentional checks retain problem inputs, chain, answer, reasoning, rule version,
time and assistance. No automatic trimming occurs. Editing current reasoning,
resetting, or visiting the shared journal cannot rewrite past check explanations.
Native saving revalidates retained feedback under its recorded model. Unknown
future models are refused rather than silently rescored. Workbench format 1 remains
readable; factor practice adds format 2 and needs campus 1.5.0 or later. A pre-upgrade
backup is required for returning to a release that cannot read these new fields.

Independent evidence includes 50-digit Decimal calculations for nine originals
and eighteen variation bounds, nine independently selected shorter factor chains,
invalid direction/dimension/power/denominator cases, cancellation and changed-input
races, original worksheet preservation, and native save/backup/recovery checks.
