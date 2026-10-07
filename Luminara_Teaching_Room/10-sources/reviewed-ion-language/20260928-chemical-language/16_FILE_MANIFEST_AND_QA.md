---
document_id: LU-CHEM-LANGUAGE-DESIGN-16
package_id: LU-CHEMICAL-LANGUAGE
package_version: 1.1.0
status: design_candidate
created: 2026-09-28
---

# File manifest and QA — v1.1

This integrated package contains **39 Markdown files**. It preserves the v1.0 ion-language scaffold and adds ionic-vs-covalent/naming-route design files and lessons.

## Checks performed in this build

- PASS — UTF-8 read/write for every Markdown file.
- PASS — all fenced code blocks are paired.
- PASS — all detected relative Markdown links resolve inside the packet.
- PASS — new authored practice IDs are unique.
- PASS — Na₂O₂ is explicitly protected from reduction to NaO and from molecular-prefix naming.
- PASS — N₂O₄ is explicitly protected from empirical reduction during molecular naming.
- PASS — NH₄Cl is represented as an ionic counterexample to a metal-only heuristic.
- PASS — LiH is represented as a reviewed ionic-hydride anchor.
- PASS — NaNO₃ is represented with nested internal-covalent / external-ionic boundary language.
- PASS — acid/hydrate/network/material cases are routed rather than guessed.

## Checks not performed here

No Lumi repository files were modified by this packet build. Runtime schema validation, browser rendering, current-course-source reconciliation, accessibility testing, storage migration, deployment, and the CLT-01–50 application tests remain implementation/human-review work.

## New v1.1 files

| File | Purpose |
|---|---|
| [17_IONIC_VS_COVALENT_CONCEPT_MODEL](17_IONIC_VS_COVALENT_CONCEPT_MODEL.md) | conceptual boundary model |
| [18_NAMING_ROUTER_AND_DECISION_TREES](18_NAMING_ROUTER_AND_DECISION_TREES.md) | deterministic naming router |
| [19_SPECIAL_CASES_AND_BOUNDARY_OBJECTS](19_SPECIAL_CASES_AND_BOUNDARY_OBJECTS.md) | peroxide, hydride, ammonium, nested cases |
| [20_IONIC_COVALENT_MODALITIES](20_IONIC_COVALENT_MODALITIES.md) | interaction designs |
| [21_IONIC_COVALENT_PRACTICE_BANK](21_IONIC_COVALENT_PRACTICE_BANK.md) | authored practice seeds |
| [22_IONIC_COVALENT_ANSWER_KEY](22_IONIC_COVALENT_ANSWER_KEY.md) | answers + diagnostic codes |
| [23_CHEMICAL_LANGUAGE_DATA_CONTRACTS](23_CHEMICAL_LANGUAGE_DATA_CONTRACTS.md) | data/engine extension |
| [24_CHEMICAL_LANGUAGE_TESTS](24_CHEMICAL_LANGUAGE_TESTS.md) | 50 acceptance/regression tests |
| [25_CODEX_DELTA_IMPLEMENTATION_PLAN](25_CODEX_DELTA_IMPLEMENTATION_PLAN.md) | staged Codex delta plan |
| [26_EXAM_CARD_EXTENSION](26_EXAM_CARD_EXTENSION.md) | cheat-sheet candidate |
| [27_SOURCES_BOUNDARIES_AND_OPEN_GATES](27_SOURCES_BOUNDARIES_AND_OPEN_GATES.md) | source layers + unresolved gates |
| [28_CODEX_HANDOFF_PROMPT](28_CODEX_HANDOFF_PROMPT.md) | copy/paste Codex handoff |
| [L07_CLASSIFY_THE_BOUNDARY](lessons/L07_CLASSIFY_THE_BOUNDARY.md) | route classification |
| [L08_IONIC_NAMING_ROUTE](lessons/L08_IONIC_NAMING_ROUTE.md) | ionic naming + special ions |
| [L09_MOLECULAR_NAMING_ROUTE](lessons/L09_MOLECULAR_NAMING_ROUTE.md) | molecular prefix naming |
| [L10_NESTED_BONDING_AND_TRANSFER](lessons/L10_NESTED_BONDING_AND_TRANSFER.md) | mixed boundaries and transfer |

## SHA-256 integrity hashes

Hashes below cover all Markdown files except this manifest. They are file-integrity values, not canon signatures.

| File | SHA-256 |
|---|---|
| `00_START_HERE.md` | `26bd1537e9b0c203a9122b4afabd1df340e2605e2b43ea585e8f857a1c439777` |
| `01_CODEX_IMPLEMENTATION_BRIEF.md` | `48120f0e8e8d9ce67ab9327fd39073fb755e68cfcb0c7bfb6f7fdcfa95499d56` |
| `02_LEARNER_AND_TEACHING_CONTRACT.md` | `7cdbd8cfa9d776920306a7839a68abce429f3692b7c8a9cbc9712eb4d0e2ec2f` |
| `03_CHEMISTRY_RULES_AND_BOUNDARIES.md` | `f6a419bcc5a9764a9f16fb713513cc933843c54e0f8750357390f2750cfa66f6` |
| `04_ION_BANK_AND_FAMILIES.md` | `91c472606121fba620e27de590b06acfc20f692f9950d41aed45a5fa2498c1e6` |
| `05_SESSION_AND_SKILL_GRAPH.md` | `eb5702f06e432f7fe1d8b0ae5dbeff1aeb95d9f747d2b20b8d5d25dd87a19e96` |
| `06_MODALITIES_AND_INTERACTIONS.md` | `2a21d5910ef852e452fdabe3305ade9b1551fbcf67ce93af6d421606d6434f7c` |
| `07_WORKED_EXAMPLES.md` | `a9d93624c4b97935e5fed7107ee7b011e41ae0c240d1a5d2fc79e49108d318ea` |
| `08_PRACTICE_BANK.md` | `2a81a9e007cce8c10e78627c03737934650f354382ba8cd51e611c885eae95fc` |
| `09_ANSWER_KEY.md` | `fb90294b4954c02198b91ab8d2dceb4fa2e1e82f04ec65254e440c183a4d8543` |
| `10_FEEDBACK_AND_SPACED_REVIEW.md` | `d2bcb205e5d13c72852d49fa3b1d7ba33d8c4d9a5f796332d3318ff928e5fbb8` |
| `11_DATA_AND_ENGINE_CONTRACTS.md` | `54598a8ecbb0ac72f86d08423928f7ecd8791c58a2a9baeffbcc13df18b67471` |
| `12_INTERFACE_ACCESSIBILITY_AND_PRIVACY.md` | `646eaba0f4a20f2e7e02d6a69fad782a74c42548882311ebab39ccf265bba243` |
| `13_TESTS_AND_ACCEPTANCE.md` | `e62d93a9f08bfae71716261e1eaa627fda252163d56d6347ae866a6a9a595b36` |
| `14_EXAM_CARD_AND_REVIEW.md` | `1b7eacc082a1676211e2c8aa0a701dffc4c74a1f8fb48dfc97b8649ae52160bb` |
| `15_SOURCES_AND_DECISIONS.md` | `00815d3a6f6315b2acc2740113e19467e8e38ba688d3a89496d1ac4b8aec7b2e` |
| `17_IONIC_VS_COVALENT_CONCEPT_MODEL.md` | `5732f3c713b70e288997e6f3ad0082de9d13c309bf124a1e9ec38f63223d7a00` |
| `18_NAMING_ROUTER_AND_DECISION_TREES.md` | `a24c5d933ff7e9d7058a9457678f308b8ec9fb7d7dbd4e5b460b9b0449dc823d` |
| `19_SPECIAL_CASES_AND_BOUNDARY_OBJECTS.md` | `60169efdb926ea714a5b0be032d4f1673ce690726478e2f11c4fbd8ab064ed1c` |
| `20_IONIC_COVALENT_MODALITIES.md` | `a9af5e89fc172b875898d73ba3ec4cf19c164628177cea335625160ae43ae9ef` |
| `21_IONIC_COVALENT_PRACTICE_BANK.md` | `f706cc6128c49c32ef0290ecd338db8cf4193451754bbc3ef6eb54886298e761` |
| `22_IONIC_COVALENT_ANSWER_KEY.md` | `9333d9fd53198408196dfb5a8649f00d515f72f3a9c3eab178b904f632130dac` |
| `23_CHEMICAL_LANGUAGE_DATA_CONTRACTS.md` | `f23ca9c4a9f5b80592bc82f2a393fca7b2b7e99267a047f08629bee68c84d2aa` |
| `24_CHEMICAL_LANGUAGE_TESTS.md` | `b9d309ff25410545ba9617ebbdde48786c4dd0fca068e7dd7c2b962e65629253` |
| `25_CODEX_DELTA_IMPLEMENTATION_PLAN.md` | `dc312388115f99e9c7af1b104572904b4774edb7f2cf9b91839daab754720cc4` |
| `26_EXAM_CARD_EXTENSION.md` | `d2463ada2d0cbff6459db2b070fbb5d1407b12203c22d4607a19e728fb7a9bb8` |
| `27_SOURCES_BOUNDARIES_AND_OPEN_GATES.md` | `f213f87cc93319b2856c649ecbe1027867876758b0172459a61c40923ce50708` |
| `28_CODEX_HANDOFF_PROMPT.md` | `ed7a86376ec4d3ac3806dcadfbdd002fbc4743e089e62fb4793793bf6440f88b` |
| `lessons/L01_CHARGE_AND_REPRESENTATION.md` | `fe50820bfb70a963525a5bf77f23c781be95dc971a60f23d6baadde698cca0b5` |
| `lessons/L02_NAMES_ROOTS_AND_CHARGES.md` | `8eb456d2bddf0411a966d41bb630cc5f01949dbf20e55735c01fb89011c2ba6e` |
| `lessons/L03_BUILD_FORMULAS.md` | `a5a4269397a1115fb2fc9aed1477469b0c3554f57fb17a1a768a4ed164c59b02` |
| `lessons/L04_READ_FORMULAS_AND_ROMAN_NUMERALS.md` | `0af64fb8c46d88cf0a5839da32732dd572a3124be71a7c5ec3c8d0a906c8d644` |
| `lessons/L05_OXYANION_FAMILIES.md` | `d92af58818ea5e9fff8f2568b7d612dc5dbd586cb4dcfd0667c428bb3c3724a4` |
| `lessons/L06_TRANSFER_AND_REFLECTION.md` | `880f62038dce2c4d489f4c61a8ace170f0b2a7cdf23a968d56e818d730051056` |
| `lessons/L07_CLASSIFY_THE_BOUNDARY.md` | `7f5e7bba214efeee8dbae941f047db6cb422417ababbbd1efd8235c0ea988467` |
| `lessons/L08_IONIC_NAMING_ROUTE.md` | `52a1c388cafae7555b02f451838488f883b7fd8a12ab20e7bd789d984fa2c08c` |
| `lessons/L09_MOLECULAR_NAMING_ROUTE.md` | `4d3fe25b73acbf4a3ca7f8b785450284b01bf7659ea52b2b47fa29199f6862ab` |
| `lessons/L10_NESTED_BONDING_AND_TRANSFER.md` | `b04428830c6e8169574ead9c94ace9bfcbb636132c8f56a894ac1c3f0aa1c3ee` |
