<!-- @version 2026-09-22 @lifecycle REVIEWED_LOCAL_PILOT -->
# Q3 checked-feedback ledger

Rules `q3-2026-09-22.1` are implemented by the native `chemistry_practice.cpp`
boundary. This ledger sits beside the existing question definitions. It covers
source-04 only: 20 prompts and 26 fields. Source-19 keeps its independent answers
and self-review until task-by-task equivalence is separately verified.

Basis: the single printed Q3 page preserved in `Chem_1117_F2026.zip`; exact source
identity is in `questions.json`. The full page was rendered and visually checked
for decimal points, exponents and arithmetic. No handwritten answer is a key.
These are authored mathematical checks, not an official instructor solution.

| Question | Value / calculator field | Rounded field or precision | Representation and remaining limits |
| --- | --- | --- | --- |
| I.a | 43.75 | 4 significant figures | Normalized scientific notation: 4.375e1 |
| I.b | 0.000030 | 2 significant figures | 3.0e-5; trailing decimal zero counts |
| I.c | 60230000 | Needs review | 6.023e7 is value-equivalent; trailing integer zeros ambiguous |
| I.d | 220 | Needs review | 2.2e2 is value-equivalent; final integer zero ambiguous |
| I.e | 4000100 | Needs review | 4.0001e6 is value-equivalent; two final integer zeros ambiguous |
| I.f | 3300. | 4 significant figures | 3.300e3; printed decimal point explicit |
| I.g | 0.000020 | 2 significant figures | 2.0e-5 |
| I.h | 0.08205 | 4 significant figures | 8.205e-2; interior zero counts |
| II.a | 359 | 3 significant figures | Decimal notation |
| II.b | 0.0600 | 3 significant figures | Decimal notation with trailing zeros |
| II.c | 437600000 | Needs review | Given coefficient has 4 figures; integer decimal form cannot state that unambiguously |
| II.d | 0.0432 | 3 significant figures | Decimal notation |
| II.e | 400 | Needs review | Given coefficient has 2 figures; integer decimal form ambiguous |
| II.f | 0.000073750 | 5 significant figures | Decimal notation, final zero retained |
| III.a | 5000000 | 5e6, 1 significant figure | Calculator field precision not assessed |
| III.b | 1.728 | 1.7, 2 significant figures | Calculator field precision not assessed |
| III.c | 40000 | 4e4, 1 significant figure | Calculator field precision not assessed |
| III.d | 0.115756363636… | 0.12, 2 significant figures | Repeating calculator result: relative tolerance 5e-10; rounding field exact |
| III.e | 12.7075 | 12.71, hundredths | Subtraction uses decimal place, not a fixed figure count |
| III.f | 151.2465 | 151, units | Addition uses decimal place |

All other value checks compare exact decimal digits. The shared decimal reader
bounds inputs to 40 digits and exponents -100 through 100. Scientific notation
accepts e/E or a coefficient followed by x, × or * and `10^exponent`. Commas,
units, arithmetic expressions and prose are not numeric input: they remain saved
drafts with “input not understood,” never a wrong-answer score. Precision
assumptions and explanation belong in the reasoning field.

Normalized form, value and precision are reported separately. A plain integer
ending in zero can match a value while still needing precision review. Open
reasoning is ungraded. Self-review is independent of every numeric check.

Each deliberate check retains answers, reasoning, rule version, a local timestamp
and hint/reveal exposure. Revisions do not rewrite earlier checks. Forty checks
per question is an explicit bound; history is never silently trimmed. Checks use
the existing chemistry key, common Save and reviewed recovery. Worksheet format 1
stays readable; the first hint/reveal/check uses format 2 and requires release
1.4.0 or later. Earlier releases refuse that format; keep an earlier backup for
rollback. Unknown future rules fail closed rather than silently rescoring history.

Verification: `evidence/u08-feedback/` contains native boundary tests, independent
50-digit Decimal calculations, browser race/failure checks and the measured
synthetic browser journey. Normal-browser and physical file-dialog coverage are
part of the still-open U07/U12 verification register.
