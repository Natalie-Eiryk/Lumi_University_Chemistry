---
document_id: Q13-SCF-04
package_id: LU-CHEM-Q13-SCAFFOLDS
version: 0.1.0
status: editorial_draft
created: 2026-09-28
visibility: content_candidate
integration_mode: additive_scaffold_overlay
assessment_owner: existing_native_exercises
---

# The Roman numeral belongs to one ion

**Scaffold ID:** Q13-SCF-04  
**Primary anchor:** CR-303  
**Related:** CR-291, CR-301; L04; WE-16; PR-45; MAT-11  
**Time:** about 6 minutes  
**Model change:** “One metal atom means no extra number is needed” → “A Roman numeral specifies the per-metal oxidation state/ion charge used by this naming model.”

## 1. Teaching scene — a name with a missing declaration

A small crate arrived labeled **NiS**. Natalie wrote **nickel sulfide** on the shipping record.

The clerk did not reject the whole crate. It highlighted one space after *nickel*.

**Natalie:** “I named the two elements. What did I leave out?”

**Ms. Luminara:** “For this Stock-naming exercise, which nickel charge is the formula asking us to use?”

**Natalie:** “There is only one nickel. That does not tell me its charge.”

**Henry:** “But the sulfide reference tells us something.”

He placed **S²⁻** beside the crate. Ms. Luminara left the nickel charge blank:

**q + (−2) = 0**

Natalie filled in **+2**.

**Natalie:** “Then nickel(II) sulfide. II is not how many nickels there are. It is the charge I inferred for the one nickel.”

Jackson rolled over a much larger crate labeled **Fe₂O₃**.

**Jackson:** “What happens when there are two metals sharing the positive contribution?”

Three oxide cards displayed a combined −6. Two iron cards together needed +6.

**Kàra:** “Plus six for the pair. Plus three for each.”

**Ms. Luminara:** “So the name is iron(III) oxide, not iron(II) oxide and not iron(VI) oxide.”

Carlos inspected the ledger.

**Carlos:** “The numeral is per passenger, not per bus.”

Jeff nodded once.

**Jeff:** “That one can stay.”

### Slow Turn

**Natalie:** “I do not need to memorize NiS as a whole new word. I need the sulfide charge, the neutral-compound condition, and the rule that the numeral names the charge of each metal.”

**Ms. Luminara:** “Exactly. Your first name found the constituents. The Roman numeral adds the missing specificity.”

## 2. Reverse-charge ledger

For the simple single-metal-charge salts in this activity:

```text
metal count × metal charge + anion count × known anion charge = 0
```

NiS:

```text
1q + 1(−2) = 0
q = +2
name = nickel(II) sulfide
```

Fe₂O₃:

```text
2q + 3(−2) = 0
2q = +6
q = +3
name = iron(III) oxide
```

The Roman numeral is a naming representation of the inferred state, not an atom-count prefix. It does not by itself establish a pure ionic description of every bond in the material; that broader question is outside the elementary ledger.

## 3. Contrast and fade

First show NiS with S²⁻ already provided. Then hide only the algebra result. Then let the learner retrieve the anion charge from the reference. Finally return to CR-303 and use the existing FeCl₂/FeCl₃ pair for transfer.

Do not teach “nickel is always +2” from this example. NiS constrains the answer in the chosen model; a new compound may require a new calculation and supporting reference.

Use “nickel sulfide” as **missing required specificity in this exercise**, not as an assertion that the words have no chemical use.

## 4. Self-explanation prompt

“Point to the symbol or subscript that gave you each part of the charge equation.”

Good target explanation: “There is one S, its listed charge is −2, and there is one Ni. Neutrality requires Ni to be +2, so I write II after nickel.”

This wording is an example, not a keyword template for grading learner prose.

## 5. Codex hook

**Offer when:** a name has the correct cation and anion but omits the configured Stock numeral, or a proposed numeral disagrees with the supported ledger.  
**Feedback:** preserve the valid constituent names; request the missing charge calculation or naming token.  
**Stop condition:** noninteger results, multiple plausible metal states, or out-of-bank identities must route to context review rather than rounded numerals. The existing PR-67 Fe₃O₄ boundary check must remain intact.

Sources: S-Q13 rows 1–2; S-INDEX PR-101, PR-45, CR-291; S-MATERIALS MAT-11. [Full source register](../09_SOURCES_DECISIONS_AND_QA.md).
