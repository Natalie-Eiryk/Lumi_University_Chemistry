---
document_id: Q13-SCF-03
package_id: LU-CHEM-Q13-SCAFFOLDS
version: 0.1.0
status: editorial_draft
created: 2026-09-28
visibility: content_candidate
integration_mode: additive_scaffold_overlay
assessment_owner: existing_native_exercises
---

# More passengers, not different passengers

**Scaffold ID:** Q13-SCF-03  
**Primary anchors:** CR-309, CR-313, CR-333  
**Related:** CR-158–CR-160, CR-294, CR-296, CR-298; L01, L03; MAT-06, MAT-10  
**Time:** about 8 minutes, or split into three short returns  
**Model change:** “Write one of each named ion” → “Keep each ion intact and choose enough complete copies to balance.”

## 1. Teaching scene — the baggage scale counts charge

The station’s baggage scale read **NET CHARGE**, not kilograms.

Ms. Luminara placed one ammonium card and one nitrate card on it:

**NH₄⁺ | NO₃⁻**

The display read **+1 − 1 = 0**.

**Natalie:** “Ammonium nitrate. NH₄NO₃. One of each.”

**Ms. Luminara:** “Now change just the negative ion.”

She removed nitrate and placed sulfide on the scale:

**NH₄⁺ | S²⁻**

The display read **+1 − 2 = −1**.

Natalie reached toward the tiny four inside NH₄.

**Henry:** “That number belongs inside the ammonium identity. Were you trying to change the ion, or change how many ions we have?”

**Natalie:** “How many. I carried ‘one of each’ over from nitrate without checking whether the charges still matched.”

Ms. Luminara slid over a second, identical ammonium card.

**NH₄⁺ | NH₄⁺ | S²⁻**

**Jackson:** “Two positive ones and one negative two. Zero.”

**Ms. Luminara:** “Now translate that arrangement into a formula.”

Natalie drew a boundary around one NH₄ group and placed a two outside:

**(NH₄)₂S**

**Natalie:** “The four stays inside the ion. The outside two counts complete ammoniums.”

**Ástríðr:** “We repaired the relationship without changing the passengers.”

Carlos leaned onto the scale. It objected to his presence with a small bell.

**Carlos:** “I am emotionally positive.”

**Jeff:** “Wrong quantity. Off.”

### Slow Turn

The display expanded into two ledgers. One counted charge; the other counted atoms.

**Natalie:** “I see why these need different columns. Two ammoniums mean two nitrogens and eight hydrogens, but a total charge of only plus two.”

**Ms. Luminara:** “Yes. Atom inventory and charge inventory describe the same collection in different ways. Neither number substitutes for the other.”

## 2. Three deliberate passes

### Pass A — identify the constituents

Use the established reference identities, not charges guessed from a subscript:

| Name | Complete ion | Charge number |
|---|---|---:|
| ammonium | NH₄⁺ | +1 |
| sulfide | S²⁻ | −2 |
| potassium | K⁺ | +1 |
| sulfate | SO₄²⁻ | −2 |
| magnesium | Mg²⁺ | +2 |
| chlorate | ClO₃⁻ | −1 |

If the charge is the missing knowledge, show its reference card. Do not respond “use the correct charge” without supplying the information needed to learn it.

### Pass B — choose a whole-ion ratio

For a neutral salt represented by these known ions:

**number of positive ions × charge each + number of negative ions × charge each = 0**

The total in this display is in elementary-charge units. This is a neutrality constraint, not a reaction mechanism or proof that every invented neutral combination exists.

| Target | First attempt | What is missing? | Balanced counts |
|---|---|---|---|
| ammonium sulfide | 1(+1) + 1(−2) = −1 | one NH₄⁺ | 2:1 |
| potassium sulfate | 1(+1) + 1(−2) = −1 | one K⁺ | 2:1 |
| magnesium chlorate | 1(+2) + 1(−1) = +1 | one ClO₃⁻ | 1:2 |

### Pass C — serialize the groups

- Two NH₄ groups and one S → **(NH₄)₂S**.
- Two K and one SO₄ group → **K₂SO₄**.
- One Mg and two ClO₃ groups → **Mg(ClO₃)₂**.

Use parentheses when a polyatomic group is repeated. The multiplier belongs outside the entire group. Do not alter the internal subscript to repair the overall charge.

## 3. Bridges from successful patterns

**NH₄NO₃ → (NH₄)₂S:** same +1 ammonium, different negative charge. One of each no longer suffices.

**Na₂SO₄ → K₂SO₄:** Na⁺ and K⁺ are both +1 in this activity. The sulfate and the 2:1 ratio remain unchanged.

**K₂CO₃ → K₂SO₄:** carbonate and sulfate are both −2. Their internal formulas differ, but the potassium count needed for neutrality is the same.

These are comparisons, not chemical reaction equations. They do not instruct the learner to transform one material into another.

## 4. Under the Floorboards — composition as a constrained count vector

Let `a` be the number of cations and `b` the number of anions. With charge numbers `z₊ > 0` and `z₋ < 0`, solve:

```text
a z₊ + b z₋ = 0
```

Choose the smallest positive integer solution. Reducing the **ion-count pair** is legitimate. Reducing all **atomic subscripts** can destroy a polyatomic identity. For sodium peroxide the whole-ion ratio is two Na⁺ to one O₂²⁻, so Na₂O₂ is retained, not NaO.

The familiar cross-over shortcut encodes this integer balancing for many simple cases. The charge ledger explains and checks it.

## 5. Hands-on and accessible interaction

Provide whole-ion tiles, +/− one-copy buttons, a charge subtotal, and a separate atom-count panel. Dragging is optional, never the only control. Each tile states its formula and charge in text; color is supplementary.

The ion interior is locked in this activity, because editing the ion is a different task. A label explains why. This is not a claim that ions can never react or change in real chemistry.

Write-out prompt: “I need ___ copies of ___ because ___.” Learner prose remains ungraded self-review.

## 6. Codex hook

**Offer when:** recognizable target ions are present but their copy ratio is nonneutral, or grouping is missing.  
**Separate checks:** ion identity, charge references, copy ratio, atom inventory, conventional grouping.  
**Feedback:** “You kept sulfate intact. One K⁺ and one SO₄²⁻ leave −1. Which whole ion supplies the missing +1?”  
**Do not:** replace KSO₄ with the final formula automatically, infer the learner never knew sulfate, or count a tile animation as an independent graded response.

A typed MgCl₂O₆ can have the target atom inventory while omitting conventional chlorate grouping. State both facts. MgClO₆ has a different chlorine count and is a composition error; do not collapse the two cases.

Sources: S-Q13 rows 5, 7, 11, 12, 13, 17; S-INDEX PR-85, PR-96, PR-98, PR-104, PR-107, PR-108; S-MATERIALS MAT-06, MAT-10. [Full source register](../09_SOURCES_DECISIONS_AND_QA.md).
