# Ms. Luminara’s periodic workbench: learning paths

Content/design specification, not a built application. These are newly authored companion lessons, not recovered quotations from earlier conversations. The voice is a warm, precise adult tutor: curious about the learner’s reasoning, candid about model limits, and willing to pause. No timers, streak penalties, speed scores, forced animations, or compulsory hint use.

## How the bank fits together

There are exactly 60 new activities in `activities.json`; all answer keys are in `answer_keys.json`. Neither file replaces an existing quiz bank. Every ID uses the new `pwb` namespace. Activity IDs are permanent: future edits change content/version metadata rather than repurposing an ID for a different problem.

| Journey | Activities | Central question | Core interaction |
|---|---|---|---|
| pwb.journey.01 | pwb.act.001–010 | What evidence identifies an element? | Table selection and comparison |
| pwb.journey.02 | pwb.act.011–020 | What does the noble-gas bracket replace? | Configuration editor and core expansion |
| pwb.journey.03 | pwb.act.021–030 | What changed: identity, count, or charge? | Electron ledger and species classification |
| pwb.journey.04 | pwb.act.031–040 | Can these whole ions make a neutral ratio? | Intact-ion formula assembly |
| pwb.journey.05 | pwb.act.041–050 | Does this numeral describe charge or count? | Formula/name response paired with table |
| pwb.journey.06 | pwb.act.051–060 | How do table clues become electron regions? | Gated Lewis/domain extension |

The reference table may contain all 118 elements, but that does not make every element an assessed configuration target. Assessed neutral configurations stay within H–Ca. Fe, Cu, Zn, and Ag occur in explicitly scoped ion/formula/name tasks. No Cr/Cu configuration puzzle is needed here; reference exception notes must not become silently graded content. Polyatomic ions are supplied or selectable by their verified names and charges. The naming mixed task also uses the verified sulfate ion. The final BF₃ example uses first-20 elements and explicitly states its monomeric introductory Lewis-model context.

### Interaction contract shared by all journeys

1. Invite a prediction and an optional reason. The learner can inspect the table, type, select, or use a keyboard-accessible equivalent of a construction gesture
2. A check reports the specific mismatch, not just a red X. Correct components remain visible; an error never erases the draft
3. Hints open individually: orientation, useful constraint, then a near-solution scaffold. Hints have no grade penalty. Never show the answer key or all three hints by default
4. Invite revision. The learner can also reveal and study the worked answer, then try an isomorphic activity
5. Ask one metacognitive question. Explanation quality is separate from selecting the right tile
6. Offer the next task without automatically navigating. Untimed exploration and “leave this here” are valid exits

Reference-aided practice is the default. Explicit recall mode hides the fields that would directly give away the current answer, such as configuration or charge overlays, while preserving identity and accessible navigation. A correct reference-assisted answer is not a failed recall attempt. Do not claim automated free-text grading exists: the integration owner may use deterministic component checks, or display the rubric for transparent learner self-check. Semantic rubrics describe the desired judgment, not an implemented model judge.

Plain text `Fe2` is an atom-count expression, not Fe²⁺. `Fe2+` is ambiguous and should trigger a clarifying notation choice; use `Fe^2+` for explicit ASCII charge. Preserve symbol case. A clickable rendering can show “two atoms,” “charge plus two,” or “coefficient two” in spoken text rather than relying on position alone.

## Journey 1 — The clue that earns its answer

ID: `pwb.journey.01` • activities 001–010 • initial mode: `identify_element`

**Learning outcome.** Distinguish a complete neutral ground-state configuration from a valence-family pattern. Combine independent row, column, and electron-count evidence. Say “not enough information” when a unique answer is not licensed.

**Opening scene.** The table is available; no answer tile is preselected. Ms. Luminara: “Let’s make the table work for you. I’ll give you a clue, and you decide whether it points to one address or a whole neighborhood.” Display `ns² np⁵` with scope “neutral main-group atoms among H–Ca.”

**Predict.** Ask, “Which tiles fit? You may choose more than one.” The answer is not forced into a single-select control. If the learner selects only Cl, retain it and ask, “What value of n did the clue give us?”

**Worked table interaction.** Open a valence comparison for F and Cl. Show F: 2s² 2p⁵; Cl: 3s² 3p⁵. Ms. Luminara: “The seven outer electrons tell us the family. The letter n leaves the row open. In this table scope, both of these belong.” The learner toggles both candidates; the check accepts the unordered set {F, Cl}.

**Narrow the clue.** Now add “period 3.” The learner deselects F. “That new evidence earns us a single answer: chlorine.” Show the full configuration 1s² 2s² 2p⁶ 3s² 3p⁵ and let the learner annotate 2 + 2 + 6 + 2 + 5 = 17. For a neutral atom, 17 electrons imply 17 protons and Z = 17.

**Common repair.** If the learner picks S, highlight the count in their own comparison rather than moving the selection: S ends 3p⁴. “You found the right row. One electron separates your tile from this clue. Which part of the written configuration holds that electron?” If the learner says a bare `3p⁵` proves there are five electrons total, isolate that subshell label: it counts only that subshell.

**Independent transfer.** Activity 010 asks for the outer configurations of O and S; activity 003 combines period 2 and four valence electrons. These test a different family rather than repeating the chlorine answer.

**Close.** “What clue tells you the family? What clue fixes the row? If one is missing, can you honestly keep more than one candidate?” Success means the learner can explain the distinction, not merely select the highlighted group.

## Journey 2 — When He hands the bracket to Ne

ID: `pwb.journey.02` • activities 011–020 • initial mode: `electron_configuration`

**Learning outcome.** Treat a bracket as an exact replacement for occupied subshells. Use the nearest earlier noble gas when requested; preserve all electrons when expanding or compacting.

**Opening scene.** Ms. Luminara: “A noble-gas bracket is a shortcut with a receipt. We should be able to open it and account for every electron.” Select Li. Build full 1s² 2s¹, count three electrons, then collapse only 1s² into [He]. Display [He] 2s¹ alongside its expansion.

**Predict the boundary.** Move to Ne. Ask, “If this task requires the immediately preceding noble gas, what may go inside the bracket?” The expected form is [He] 2s² 2p⁶. Do not automatically offer [Ne] as a trivial self-description when the objective is the preceding-core convention. “We’re describing neon; we haven’t moved past it yet.”

**Worked boundary crossing.** The learner inspects the next atomic number, Na, and predicts the new electron’s location. Expand neutral Na as 1s² 2s² 2p⁶ 3s¹. Group the first ten electrons. “Now the full neon pattern sits behind one additional electron. This is where [Ne] becomes the nearest-core shortcut.” Collapse to [Ne] 3s¹. Keep Z = 11 and total electrons = 11 visible during the transformation.

**Repair the missing-core attempt.** If the learner writes [He] 3s¹, show its expanded count as three, not eleven. “The bracket didn’t carry the middle eight electrons with it. Where should 2s² 2p⁶ go?” Invite the learner either to restore those terms or use [Ne]. If they submit [He] 2s² 2p⁶ 3s¹, award chemically correct occupancy and separately explain that the requested nearest-core form can be shorter. A formatting objective must not turn a valid configuration into a chemistry error.

**Second boundary.** Select K. Repeat the count using 19 total electrons. Ar supplies 18; [Ar] 4s¹ supplies the last one. Ca then becomes [Ar] 4s². Do not insert 3d² simply because the principal number is lower; the neutral first-20 filling sequence is 1s, 2s, 2p, 3s, 3p, 4s.

**Independent transfer.** Activity 018 asks for full P, compact P, and five valence electrons. Activity 020 supplies a count-correct but occupancy-wrong Ca configuration. These distinguish an electron-total check from a filling-order check.

**Close.** “A bracket is valid if expanding it restores every occupied electron. The nearest earlier noble gas makes that valid description compact.” The learner states when the He→Ne switch happens: at Na, not at an arbitrary point halfway across a row.

## Journey 3 — One iron, two irons, or two charges?

ID: `pwb.journey.03` • activities 021–030 • initial mode: `ion_ledger`

**Learning outcome.** Keep nuclear identity, number of atoms, number of electrons, and overall charge in separate ledgers. Classify species without conflating covalent bonding and compound identity.

**Opening scene.** Ms. Luminara: “Before we name anything, let’s ask what the symbols actually promise.” Show Na with 11 protons and 11 electrons. The learner removes one electron in the ledger. Proton controls remain unchanged during ordinary ion formation. Count: 11 − 10 = +1. Render Na⁺ and read it aloud as “one sodium ion, charge plus one.”

**Comparison that prevents a shortcut.** Place Ne alongside Na⁺. Both have ten electrons, but their proton counts are ten and eleven. “The electron arrangements can match without the identities matching. The nucleus keeps the element’s address.” Correctly call them isoelectronic, with a plain-language explanation before requiring terminology.

**Worked notation contrast.** Introduce Fe₂, Fe²⁺, and 2 Fe as separate cards. The learner assigns the role of each 2: subscript count; signed superscript charge; multiplying coefficient. State explicitly that Fe₂ is used here as a notation illustration, not a claim that ordinary iron is a bottle of diatomic molecules. Fe²⁺ has one Fe nucleus and charge +2. For a monatomic iron ion with Z = 26, this corresponds to 24 electrons; this may be explained without asking for a transition-metal electron configuration.

**Repair.** If the learner reads “iron(II)” from Fe₂, Ms. Luminara asks, “Where is the charge sign?” Move no atoms or electrons automatically. Offer accessible inputs labeled “number of Fe atoms” and “net charge” and preserve the distinction in the rendered formula. If typed Fe2+ appears, ask which meaning was intended instead of guessing.

**Worked category contrast.** Open N₂, NH₄⁺, and (NH₄)₂CO₃. N₂ has one distinct element, so it is elemental, though its atoms share electrons covalently. NH₄⁺ is a charged multi-atom unit: a polyatomic ion. The neutral salt combines ammonium cations and carbonate anions; it is ionic even though the bonds inside each ion are covalent. “Bond type and species category answer different questions.”

**Independent transfer.** Activity 027 asks the learner to create O²⁻ from neutral O. Activity 026 returns to ammonium versus its salt. Activity 030 introduces Fe’s variable charges and accepts “insufficient information” for an unspecified iron compound.

**Close.** The learner explains one chosen item by saying: element identity, atom count, electron change, and net charge. No speed target; precision matters more than fluency at first.

## Journey 4 — A neutral formula is a balanced collection

ID: `pwb.journey.04` • activities 031–040 • initial mode: `build_formula`

**Learning outcome.** Build the smallest whole-number ratio of intact ions with net charge zero. Use parentheses only when the notation requires repeated polyatomic units, and preserve those units’ internal composition.

**Opening scene.** Ms. Luminara: “Today the ion tiles are building blocks. We can change how many we use; we can’t quietly change what each block is.” Load Na⁺ and Cl⁻. One of each yields +1 + (−1) = 0, giving NaCl.

**Correct the bond story immediately.** Ask, “What holds the ions together?” If the learner says “they share the transferred electron,” respond, “Electron transfer can explain forming these ions. Once formed, their opposite charges attract. That attraction is the ionic bond.” Explain the solid as an extended ionic lattice; NaCl is a formula-unit ratio, not a standalone molecular pair. Do not animate one electron eternally shared between the ions.

**Increase charge mismatch.** Load Mg²⁺ and Cl⁻. One of each gives +1 net charge, so the learner adds a second chloride. The charge ledger reaches zero and the formula reads MgCl₂. Show why Mg₂Cl is not balanced. Then load Ca²⁺ and O²⁻: a 1:1 ratio already works, so CaO needs neither visible 2. This counters mechanical crisscrossing without reduction.

**Worked polyatomic build.** Replace tiles with NH₄⁺ and CO₃²⁻. One of each yields −1. Ask which intact unit should be repeated. Add a second NH₄⁺; total charge is 2(+1) + (−2) = 0. Render (NH₄)₂CO₃. Expand counts in a separate annotation: N₂H₈CO₃, meaning N = 2, H = 8, C = 1, O = 3. Do not replace the conventional ionic formula with this flattened count string.

**Repair.** For NH₄CO₃, show the −1 total and invite another ammonium. For N₂H₄CO₃, ask whether the second ammonium brought four more H atoms. For Ca₂(CO₃)₂, reduce the ratio of whole ion tiles from 2:2 to 1:1; keep the carbonate’s 3 unchanged. “We reduce how many tiles, not what’s printed inside one.”

**Independent transfer.** Activity 035 builds Ca(NO₃)₂; activity 034 builds Al₂O₃. The learner must both group a repeated polyatomic ion and solve a 3-versus-2 charge balance without changing an ion’s identity.

**Close.** The learner points to three checks: intact ions, zero net charge, and smallest whole-number ionic ratio. Never apply the ratio-reduction rule blindly to molecular formulas such as N₂O₄.

## Journey 5 — Choose the language before using its numbers

ID: `pwb.journey.05` • activities 041–050 • initial mode: `build_formula` with naming-response capability

**Learning outcome.** Route known examples to ionic or binary molecular naming. Interpret Roman numerals as charge per metal ion, and molecular prefixes as atom counts.

**Opening scene.** Ms. Luminara: “The number can mean different things depending on which naming language we’re using. Let’s choose the language first.” Place FeCl₂ and CO₂ in comparison slots, but do not imply their subscripts play identical naming roles.

**Worked ionic case.** Chloride contributes −1 each, so the two chlorides contribute −2. One iron must supply +2 for neutrality. Name FeCl₂ iron(II) chloride. The II states iron’s charge, not two iron atoms. Then work Fe₂O₃: three oxides contribute −6; two Fe must contribute +6 total; each Fe is +3. Name iron(III) oxide.

**Repair the tempting answer.** If the learner proposes iron(II) oxide for Fe₂O₃, preserve the selected formula and ask, “Is the 2 counting the iron atoms, or telling us the charge on each one?” Write 2q + 3(−2) = 0 as an optional equation, with a spoken alternative: “Split positive six equally between two irons.” Do not make algebra manipulation a prerequisite to understanding the charge.

**Worked molecular case.** CO₂ is carbon dioxide: the prefix di- describes two oxygen atoms in each molecule. N₂O₄ is dinitrogen tetroxide. The conventional vowel contraction is a naming detail; a learner who writes “tetraoxide” has not necessarily misunderstood the atom count. Offer spelling feedback separately from composition feedback.

**Fixed-charge and polyatomic comparison.** ZnCl₂ is zinc chloride and Ag₂O is silver oxide in the stated common introductory convention. Explicit zinc(II)/silver(I) names express correct charges; distinguish course-style expectations from scientific nonsense. For (NH₄)₂SO₄, recognizing the ammonium and sulfate ions takes precedence over “no metal means molecular.” Name ammonium sulfate without a di- prefix.

**Independent transfer.** Activity 044 contrasts CuCl with CuCl₂. Activity 049 mixes MgCl₂, PCl₃, and (NH₄)₂SO₄. Do not hide the initial route decision inside a single all-or-nothing spelling check.

**Close.** “Tell me what your number means before you use it.” The learner identifies whether a number expresses atom count, charge per ion, or total charge contributed by several ions.

## Journey 6 — From table electrons to three-dimensional regions

ID: `pwb.journey.06` • activities 051–060 • release: explicitly gated extension

**Learning outcome.** Use main-group valence counts to budget electrons, adjust for ionic charge, and distinguish electron-pair regions from molecular shape. This bridge does not promise a full Lewis editor or exhaustive VSEPR engine in the initial release.

**Opening scene.** Ms. Luminara: “The table helped us count an atom’s outer electrons. Now we’ll decide how that shared budget can be arranged.” Inspect H and O with the valence-count overlay. Budget H₂O as 2(1) + 6 = 8. Use two O–H single bonds, consuming four electrons; place the remaining four as two lone pairs on O. Check the eight-electron total, O’s octet, and each H’s duet separately.

**Worked geometry transition.** The learner marks four electron regions at O: two bonds and two lone pairs. Electron geometry is tetrahedral. Hide only the lone-pair markers from the atom-position sketch, without deleting them from the model: the molecular shape is bent. “The invisible pairs still affect the arrangement. They simply aren’t atoms we name in the molecular shape.” No forced 3-D animation is necessary; labeled static diagrams and text alternatives must be complete.

**Compare NH₃.** Budget eight electrons, make three N–H bonds and one lone pair. Four regions again produce tetrahedral electron geometry, but three attached atoms plus one lone pair produce trigonal-pyramidal shape. Compare with CH₄, which has four bonds and no central lone pair; both its electron geometry and molecular shape are tetrahedral.

**Repair double-bond counting.** For O=C=O, ask the learner to count directions away from C rather than shared pairs. Two double bonds are two regions, so CO₂ is linear. If four domains were entered, show the distinction explicitly: four shared pairs but two bonding regions. Never silently relabel the learner’s count.

**Ion budget and resonance.** NH₄⁺ has 5 + 4 − 1 = 8 valence electrons; CO₃²⁻ has 4 + 18 + 2 = 24. The charge changes the electron budget. For carbonate, any one of the three equivalent resonance contributors has three C–O directions and trigonal-planar geometry. Do not depict the double bond as jumping in time between three fixed structures; the contributors are representations, not sequential physical states.

**Boundary check.** Activity 060 uses H₂ and neutral monomeric BF₃ to show that forcing octets is not a universal construction rule. H follows a duet; the conventional BF₃ Lewis structure gives B six surrounding electrons. No invented extra electron may be added to satisfy a mnemonic.

**Independent transfer.** Activity 056 asks for NH₃ domains and shape, 057 for CO₂ domains, and 059 for carbonate. A learner may complete these through an accessible structured response if no graph editor exists; the extension should not pretend such a response validates every possible Lewis drawing.

**Close.** “First budget electrons. Then check the drawing. Then count regions. Only then name the shape.” The learner identifies which step caught a mistake and can revisit that step directly.

## Placement, recovery, and stopping rules

- Start with a learner-chosen question: identify, electrons, ions, formulas, names, or the later Lewis bridge
- For a brief diagnostic, offer 002, 013, 024, 036, 043, and optionally 057. These are ordinary bank activities, not separate or renumbered assessment items
- A correct answer with uncertain reasoning invites one transfer activity; it does not trigger an endless adaptive loop
- After an error, preserve the first answer and allow hints, reference viewing, revision, or reveal. Never require three failures before help
- Completion is learner-controlled. A suggested milestone is a worked example plus one independently explained transfer in that journey
- A learner can return to exploration at any point; assessment drafts are preserved according to the UX state specification
- Confidence prompts are optional and non-diagnostic: “What are you sure of?” or “What would you check next?” Do not infer a disability or label a learner from an error pattern

## Evidence and content QA

Chemistry was cross-checked against the publisher’s open introductory reference sections, with exact tasks and explanations newly authored for this packet:

- [Electron configurations](https://openstax.org/books/chemistry-2e/pages/6-4-electronic-structure-of-atoms-electron-configurations)
- [Molecular and ionic compounds](https://openstax.org/books/chemistry-2e/pages/2-6-molecular-and-ionic-compounds)
- [Chemical nomenclature](https://openstax.org/books/chemistry-2e/pages/2-7-chemical-nomenclature)
- [Lewis symbols and structures](https://openstax.org/books/chemistry-2e/pages/7-3-lewis-symbols-and-structures)
- [Molecular structure and polarity](https://openstax.org/books/chemistry-2e/pages/7-6-molecular-structure-and-polarity)

Scope qualifiers matter: first-20 neutral configurations; common introductory ion charges rather than all oxidation states; nearest earlier noble-gas notation when requested; ionic formula-unit ratios rather than universal molecular reduction; introductory monomeric BF₃; and carbonate resonance rather than one fixed localized double bond. A future integration must retain these qualifiers instead of trimming them out of card text.
