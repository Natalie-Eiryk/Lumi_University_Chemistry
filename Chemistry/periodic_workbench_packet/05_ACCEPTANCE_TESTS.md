# Workbench Acceptance Tests

## How to use this test plan

These are required future implementation tests, not a claim of executed campus tests. For each record capture the inspected baseline, input/setup, steps, expected result, actual result, evidence, and pass/fail/blocked status. A blocked test remains blocked. Do not convert a packet content review into a runtime pass.

Use synthetic learner entries in the authorized environment. The native chemistry and C++20 validator remain authoritative. Pair deterministic checks with keyboard, screen-reader, touch, and actual Save/journal tests; schema conformance alone cannot prove these behaviors.

## Table and evidence surface

| ID | Setup and action | Expected result |
|---|---|---|
| PT01 | Enumerate the reference and rendered tiles | Exactly 118 unique atomic numbers 1–118; each has its correct symbol/name; no duplicate or missing element; authored activities counted separately |
| PT02 | Search by `26`, `Fe`, and `iron` | Same element selection; exact chemical symbol is retained; search convenience does not become formula-parser case folding |
| PT03 | Navigate the entire table by keyboard | Every element, including detached rows, is reachable; focus remains visible; movement rules are documented; no keyboard trap; empty layout cells do not strand focus |
| PT04 | Open a drawer, compare, switch mode, close it | Selected elements/context remain intelligible; focus enters predictably and returns to the invoking control; no unseen selection reset |
| PT05 | Touch at narrow width and increased text size | Tiles or equivalent accessible list targets remain usable; no essential hover-only interaction; labels, charges and subscripts remain readable; no clipped primary controls |
| PT06 | Inspect a tile with a missing property | Show unavailable/not supplied, with model/source context; never substitute zero or invent a trend value |
| PT07 | Switch a quantitative overlay | Definition, units, scale, legend and source are visible; missing data distinct from low values; color has a non-color equivalent |
| PT08 | Inspect lanthanoid/actinoid layout | All detached elements reachable and labeled; layout convention does not falsely resolve disputed group/block assignments |
| PT09 | Screen-reader select and compare | Element identity, position, selection, property values and comparison context announced usefully; no endless duplicate tile narration |
| PT10 | Use reduced motion and high contrast | Learning actions still work; no information relies on animation/color alone; no flashing or time-dependent task requirement |

## Chemistry identity and notation

| ID | Input or action | Expected result |
|---|---|---|
| CH01 | Contrast `Fe2`, ambiguous `Fe2+`, and explicitly charged `Fe^2+` / Fe²⁺ | The packet grammar reads `Fe2` as Fe:2 without explicit charge, rejects `Fe2+` as ambiguous, and accepts `Fe^2+` / Fe²⁺ as a single iron(II) ion. A separate charge control is the preferred beginner path; no guessed interpretation |
| CH02 | Contrast `Co` and `CO` | Co is cobalt; CO is carbon monoxide with C and O; capitalization is chemically meaningful |
| CH03 | Classify N₂ | Elemental nitrogen is an element and a diatomic molecule, not a compound merely because it has two atoms |
| CH04 | Build NaCl from Na⁺ and Cl⁻ | Charge balances 1:1; describe a formula unit of an ionic compound, not a discrete NaCl molecule in ordinary solid context |
| CH05 | Compare SO₄ and SO₄²⁻ | Sulfate is the charged intact polyatomic ion SO₄²⁻; missing charge is not silently supplied where ion identity is the target |
| CH06 | Build (NH₄)₂SO₄ | Two intact ammonium ions and one sulfate; outside subscript multiplies the entire parenthesized ion; total charge zero |
| CH07 | Neutral iron then Fe²⁺ | Both have 26 protons; electrons change from 26 to 24; losing electrons makes charge more positive |
| CH08 | Change an atom's proton count | Element identity changes; the system does not label it as an ionization step |
| CH09 | Ask for neutron count from element tile only | Do not round average atomic weight and present that as a unique isotope neutron count; request a mass number/isotope or state a chosen model |
| CH10 | Supply impossible counts | Negative electrons/protons, inconsistent atomic number and symbol, and impossible declared isotope counts are rejected at the appropriate authoring/input boundary |
| CH11 | Submit `Al2(SO4)3` and valid rendered equivalent | Preserve ion identity, atom counts, grouping and charge; accept only the documented equivalent notation set |
| CH12 | Balance ionic versus molecular formulas | Reduce ionic stoichiometric ratio when appropriate; do not reduce a molecular formula merely to its empirical ratio |
| CH13 | Select a common ion suggestion | Show it as a context-dependent teaching example, not the only possible oxidation state or proof every atom forms that ion |
| CH14 | Inspect first-20 electron configurations | Occupancies match the stated neutral ground-state model and sum to Z; noble-gas shorthand matches full notation where supported |
| CH15 | Use Fe ion configuration | If supported, remove 4s electrons before 3d for Fe²⁺/Fe³⁺ in the stated model; never apply naive last-written-term deletion; if not supported, state the boundary |
| CH16 | Use Cr or Cu configuration | Explicit exception record or transparent unsupported state; no incorrect universal Aufbau shortcut |
| CH17 | Submit a clue compatible with several elements | Preserve the candidate set and explain which extra evidence would disambiguate; no arbitrary single-answer rejection |
| CH18 | Compare periodic trends | General trends are labeled as patterns with qualifications; missing data and exceptions do not become false exact orderings |
| CH19 | Request detailed data outside authored reference scope | Clearly state unavailable coverage. An all-118 name/layout reference does not imply all-118 orbital/property/ion content |
| CH20 | Enter malformed notation or unrelated prose | Specific recoverable input guidance, no crash, no chemical guess masquerading as an accepted parse |

## Activity and teaching behavior

| ID | Setup and action | Expected result |
|---|---|---|
| AC01 | Count authored cases and inspect all records | Exactly 60 stable unique authored activity IDs; coverage families and selected element scope explicitly reported |
| AC02 | Start a case from a tile or learning route | Prompt context selects/uses the workbench; response surface supports a meaningful action or explanation rather than only answer reveal |
| AC03 | Open first hint, revise, then reveal | Hints are staged; answers not pre-exposed in the learner default view; assistance is represented honestly if the native schema supports it |
| AC04 | Trigger a misconception | Feedback names the next useful check without shame, vague “wrong,” or dumping the full solution prematurely |
| AC05 | Give an equivalent valid explanation/notation | Accept documented alternatives; concept/self-check routes are transparent when arbitrary free text cannot be evaluated reliably |
| AC06 | Try transfer after a worked correction | New case tests the same reasoning in a changed context; earlier work remains inspectable; no claim of mastery from one success |
| AC07 | Leave and return mid-activity | Existing draft/context preservation contract is honored; temporary mode switching does not erase an attempt |
| AC08 | Explore without starting a case | Table, lookup, comparison and supported manipulations remain useful; exploration is not blocked by quiz completion |
| AC09 | Inspect teacher/checker materials | Answer-bearing files are separated from default learner rendering; package source files are acknowledged as readable authoring material |
| AC10 | Inspect companion language | Adult, precise, warm teaching; no invented native Lumi memory, autonomous learning, medical dosing, streak penalties, or speed scoring |

## Integration and persistence

| ID | Setup and action | Expected result |
|---|---|---|
| IN01 | Inspect baseline before edits | Current module, version, schemas and named native contracts recorded; unverified supplied names are not treated as inspected facts |
| IN02 | Map all packet fields and IDs | Explicit native destination/derivation/unsupported disposition; existing source IDs/routes preserved; no collision or silent field loss |
| IN03 | Run actual C++20 validation against transformed content | Documented native validator passes; malformed/version-mismatched records rejected; no invented command/API or alternate grader |
| IN04 | Admit through the native pathway | Admission succeeds only after required validation; no direct edits to sealed/generated release files |
| IN05 | Compare prior Q13 and chemistry workflows | Existing scaffolds, companions, questions and feedback continue to function; no replacement system introduced |
| IN06 | Save a synthetic entry, read back, reopen | Existing notebook `luminara-chem1117-workbook-pilot-v1` receives exactly the intended entry; activity identity and work survive; no parallel store or duplicate write |
| IN07 | Cause supported stale-edit conflict and choose Cancel | No silent local/remote overwrite; local draft recoverable; no false saved indication |
| IN08 | Cause save failure and retry under supported contract | Error visible; recoverable draft remains; no duplicate successful entry from blind retry |
| IN09 | Return to journal and re-enter study | Correct journal/work context and stable IDs restored; shared Save behavior unchanged |
| IN10 | Inspect release proposal | Active 0.2.0 baseline verified or corrected; 0.3.0 remains proposal until separately authorized; no silent migration |
| IN11 | If release authorized, activate and exercise rollback | Native release manager/root dispatcher used; starting version recorded; documented rollback verified; no broader action than authorized |
| IN12 | Audit work process and report | One job at a time, no more than two build workers, bounded logs as confirmed by owner; report separates authored content, validation, admission, runtime and release |

## Release gate and exclusions

No critical chemistry-identity, inaccessible essential control, data-loss, unauthorized migration, or conflicting-grader failure can be waived as a cosmetic issue. Instructor-dependent conventions must be resolved or excluded from automatic correctness judgments. A smaller honestly supported feature slice is preferable to invented scientific data or guessed APIs.

This packet does not contain completed native test logs. Completion requires evidence from the inspected application environment. Packet structural/content QA is reported separately in QA_STATUS.md.
