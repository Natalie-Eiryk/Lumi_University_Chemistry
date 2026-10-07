# Ms Luminara Periodic Table Workbench Interaction Design

## Purpose and implementation boundary

This is an integration design for a reusable chemistry tabletop in the Campus learning experience. It specifies what learners see, do, recover, and understand. It does not implement an application, create an alternative gradebook, or assume that a working prototype already exists. Codex should bind the proposed events and state below to the actual Campus stores, activity shell, and native grader after inspecting those interfaces. Names in interaction_contract.json are a proposed adapter contract, not claims about existing APIs.

The learner is an adult nursing student with substantial physics experience. Keep the reasoning rigorous, make unfamiliar chemistry notation explicit, and avoid childish rewards, countdowns, or a presumption that needing a hint means failure. Useful nursing-adjacent examples can motivate chemistry, but must not become patient-care advice or medication calculations.

A single coherent workbench supports exploration, element identification, formula construction, ionic charge bookkeeping, and electron configurations. Lewis structures are a later extension with explicit boundaries. The periodic table remains a reference and an input surface; it is not a replacement for explanations, nor a collection of hidden click puzzles.

## Nonnegotiable interaction principles

1. Inspecting an element, selecting an answer, and adding an atom are different actions with explicit labels and mode-specific behavior.
2. Subscripts count atoms or repeated groups. Superscripts express charge. Coefficients count whole formula units. Never store or edit these as the same number.
3. The learner may ask for conceptual help before any attempt. Help is not unlocked by failing.
4. Draft work survives reference browsing, hints, modal cancellation, tab changes, and a return to the same activity.
5. Click sequence is provenance, not chemical formula order. Render using the activity's declared representation policy and explain any reordering.
6. Ambiguous clues produce a valid candidate set or a request for an additional clue. They do not secretly require one arbitrary answer.
7. The formula type matters. Molecular and empirical formulas must not be silently collapsed into one answer.
8. Native Campus records remain authoritative for draft persistence, submission, feedback, and completion. No parallel local gradebook or private progress system.

## Tabletop regions and information hierarchy

### A Activity rail

Show the activity title, mode, short learning goal, task type, and a compact persistence status: Saving, Saved, or Not saved. Include Back to course, Resume later when supported, and a consistent Help button. Show progress only where the course provides a meaningful denominator. A free exploration session has no fake completion meter.

The task type is visible next to the prompt: Element identification, Molecular formula, Empirical formula, Formula unit, Ion, or Electron configuration. This prevents a correct representation from being judged against an unstated convention.

### B Clue card

Show the current clue verbatim, relevant conditions such as neutral atom or ion, and a list of previously revealed clues. Label supplied information separately from the learner's deductions. A clue based on an electron configuration must explicitly identify full or shorthand notation and whether it describes a neutral atom, ion, or an otherwise constrained species.

Actions: Read aloud if the host supports it, Explain notation, Show a hint, Ask for another clue when authored, and View task requirements. An additional clue is an authored progression event, not an invented fact. Optional confidence controls read Not sure yet, Tentative, and Confident; they never gate submission or influence correctness.

### C Periodic table surface

Maintain conventional period and group positions with blank spaces preserved. Each cell includes symbol and atomic number. Element name is visible in a spacious layout and always available on focus or inspection; avoid relying on hover. When a separately validated category map is available, a category label and visual pattern or border supplement category colors. The supplied layout regions are not a chemical-family classification; without that map, use neutral styling and explicit period/group labels. Selection and keyboard focus use distinct shapes or outlines.

A persistent interaction label says Inspect elements, Choose an answer, or Add atoms to assembly. In Add mode, each activation of Fe adds one Fe atom; two activations make a composition containing two Fe atoms. The resulting Fe₂ means two iron atoms in this construction, not iron(II), Fe²⁺, or a claim that the free Fe₂ species is stable. The charge editor is elsewhere and does not change when an element tile is activated.

Inspect mode is always reachable without changing the answer or assembly. A visible switch and keyboard-accessible Inspect action on the focused tile provide this path. On touch, do not use long-press as the only way to inspect. Never make a double-click mean inspect while a single-click means add: that would accidentally add atoms.

### D Reference drawer

Opening the drawer shows the element's name, symbol, atomic number, course-relevant group and period, neutral-atom electron configuration when included in the validated reference set, and a clearly qualified valence explanation. The supplied data covers all 118 identities and layout positions, but only a defined subset of configurations and ions. Missing fields say Not included in this reference set; they are never guessed. Distinguish atomic number from relative atomic mass and do not derive an isotope's neutron count by rounding atomic weight. Display advanced transition-metal qualifications through an expandable explanation rather than an oversimplified universal valence rule.

An element reference card may include Add one atom and Use as candidate buttons with mode-appropriate labels; ordinary inspection never invokes them. Where a reference would reveal a practice answer, label it Answer-revealing reference and let the learner choose. Do not forbid access in ordinary learning mode. Assessment restrictions, if required by Campus, are explicitly authored and disclosed at activity entry.

Closing the drawer restores focus to its opener and preserves edits. Pinned reference cards remain visible while the learner edits the workbench; close only the specified card.

### E Assembly tray

Show a structured list of parts and a large formula preview. An element row has symbol, name, count, increase, decrease, remove, and inspect controls. An intact polyatomic ion or group has a label, interior formula, charge if applicable, and a group multiplier. Internal atoms are read-only until an explicit Decompose group action, if that task permits it. Decomposition is a reversible edit that changes representation; never do it automatically to simplify display.

The tray provides both a formula view and a counts view. Counts view expands totals without discarding grouping. For Ca(NO₃)₂, show one calcium, two nitrogen, six oxygen, and two nitrate groups. The two views share one structured draft; they are not separately editable competing sources of truth.

An activity-defined maximum keeps an accidental repeated press bounded. Announce the bound and offer typed count entry for legitimate large counts when permitted. Count zero removes a part through a reversible edit. Decrease at zero is disabled. Negative and noninteger counts are not valid atom counts.

### F Electron and charge ledger

A separate panel names the species to which its charge applies. In a monatomic ion exercise it shows atomic number, protons, electrons, net charge, and a transparent relation: charge in elementary-charge units equals protons minus electrons. In a formula-building exercise it shows charge of each selected ion, multiplicity, charge contribution, and total charge. These are different ledger views.

Charge controls explicitly say Set charge, Remove electron, or Add electron. They do not use an unlabeled plus sign beside the atom-count control. Positive charge means fewer electrons than protons. Oxidation state, formal charge, and net ionic charge are distinct quantities and must not be substituted for each other.

For iron(II), choosing Fe and setting species charge +2 produces Fe²⁺ with one atom. Choosing Fe twice produces two atoms and does not assign any ionic charge. A formula activity with Fe³⁺ and O²⁻ can show the charge balance for Fe₂O₃ while preserving the distinction between constituent ion charges and the neutral formula unit.

### G Reasoning and hint panel

A persistent button opens a progressive ladder: orient to the task; recall a relevant principle; apply it to the current representation; show a partial worked step; reveal and explain the answer. Labels indicate how much will be revealed. The first hints should teach the process without merely naming the target. Navigation Back and Close retain the current level and do not request or reveal the next level.

Show a short Why this feedback explanation alongside result feedback. Offer an optional reasoning note. Never require private autobiographical reflection, speed, or confidence as evidence of chemistry mastery. A useful prompt is What property ruled out your other candidate? An unhelpful prompt is Why did you make that mistake?

### H Session journal

A collapsible journal records meaningful chemistry actions in plain language, submissions, viewed hints, and learner notes. It is a review aid, not a public score feed. It distinguishes Your action, Workbench formatting, and Feedback. Example: Added oxygen; formula display reordered to the task's convention. The journal must not expose hidden answer data before reveal or leak other learners' state.

Undo history and the journal serve different purposes. Undo reverses draft edits; the journal may retain the fact that an attempt or hint occurred. A learner can undo an edit without falsifying a submitted attempt record.

## Mode contracts

### Explore

Goal: inspect patterns, compare elements, and test freely. No answer is presumed. Search matches atomic number, symbol, and name; filters are labeled views, not correctness checks. Learners may pin several elements and select Find all matching elements for a property. A many-result query displays the complete matching set plus the predicate used. Clearing a filter restores the table without clearing pinned cards or any assembly draft.

Optional scratch assembly is labeled exploratory. A parseable formula does not imply a known stable compound. A composition and charge balance alone are insufficient proof of molecular structure or existence. Exploration may hand off an explicit Copy to practice draft action where the host supports it; it never submits a graded answer.

### Identify an element

The table starts in Choose an answer mode. Selecting a tile highlights one candidate and updates the draft answer; it does not grade immediately. Select another tile to replace the candidate. Select the chosen tile again to keep it selected, with an explicit Clear choice action to remove it. Check answer is enabled once the required response shape is present.

For select-all tasks, each tile toggles set membership and the prompt explicitly says Select all that apply. The action label states Check selected set. In an ambiguous-clue activity, a learner may submit a candidate set, explain insufficient information, or request the next authored clue. Native grading accepts the authored valid response form rather than inventing uniqueness.

After a check, correct feedback explains which clues agree. Incorrect feedback identifies an actionable discrepancy without erasing the choice. If the learner changes the candidate after feedback, retain the old attempt in history and label current work Changed since last check.

### Build a formula

The table starts in Add atoms mode with a visible Inspect toggle. Every intentional activation adds exactly one atom. Parts can also be chosen from an authored group or ion palette. The palette shows group identity and charge before insertion. A selected group remains intact, e.g. hydroxide is not silently replaced by a generic oxygen and hydrogen list.

The preview is a representation of the structured composition, with a clear task-specific formula-order policy. For simple ionic exercises, display cation then anion according to the authored species roles; for molecular exercises, use the authored target's chemically appropriate ordering. Do not universally sort alphabetical, by atomic number, or by tap sequence. Organic conventions, hydrates, coordination compounds, and multiple equivalent notations require explicit curriculum support; unsupported notations receive a scoped message rather than a fabricated normalization.

If formula order itself is being assessed, expose order controls and grade order separately; do not auto-correct the assessed skill before submission. If formula order is not assessed, reorder only on a clear rule and show a brief explanation. A compositionally correct answer in a noncanonical order receives representation guidance according to the activity rubric, not an unexplained wrong mark.

Check answer validates required structure, parses locally for legibility, then submits through the native grader. Local chemistry hints are provisional. They must not mark the course item complete or override authoritative grading. Count mismatches, grouping mismatches, charge mismatches, representation mismatches, and unavailable validation are distinct outcomes.

### Ion and charge ledger

Start with a specified neutral atom or ion and explicit target. Let the learner manipulate electrons or set a charge, depending on the task. Protons are fixed by element identity unless a separate nuclear-chemistry activity is authored. Altering proton count is never presented as ordinary ion formation.

For compound neutrality, the learner chooses quantities of explicit ion species. The ledger updates their summed charge without automatically choosing the balancing ratio. A Show balance step hint can explain the arithmetic without concealing the learner's existing work. A net-zero total is a necessary check for the requested neutral ionic formula unit, not proof that every arbitrary species combination is a real compound.

### Electron configuration and orbital work

Show whether the task asks for full notation, noble-gas shorthand, orbital boxes, or identifying an element from a configuration. Keep an electron-count ledger tied to the current species and its charge. Orbital labels and subshell capacity are visible or accessible as help. Box interactions cycle through explicit occupancy states with equivalent keyboard controls; arrow orientation has a text alternative.

A notation editor can accept normalized spacing and Unicode or ASCII exponents, but only after a successful structured parse. Distinguish ordering conventions from occupancy errors. Occupancy, total electron count, permitted reference configuration, and ion-specific removal order belong to the chemistry/grader contract, not guesses made by the view. A later task may assess excited states; therefore an unusual but valid occupancy must not automatically be called impossible merely because it differs from the ground state.

### Later Lewis structure mode

Reserve a mode boundary and extension fields rather than enabling a decorative drawing tool that pretends to grade chemistry. The future model must support connectivity, bond order, lone pairs, unpaired electrons where relevant, whole-species charge, per-atom formal charge, valence electron totals, and allowed equivalent resonance contributors. Atom arrangement and screen coordinates are presentation data, not molecular identity.

Do not imply that formula entry determines a unique Lewis structure. Do not grade equivalent rotations, translations, or symmetry-equivalent drawings as different chemistry. Expand only after the curriculum declares scope for resonance, radicals, electron-deficient species, expanded-valence representations, and formal-charge reasoning. The initial workbench may link to a lesson and explain this boundary without losing the current formula draft.

## State model and transitions

The session has orthogonal state dimensions instead of a single overloaded status:

- Mode: explore, identify_element, build_formula, ion_ledger, electron_configuration, or future lewis_structure
- Interaction intent: inspect, choose_candidate, toggle_candidate, add_atom, or edit_orbital
- Draft lifecycle: pristine, edited, restored, or changed_since_check
- Validation: unchecked, checking, correct, needs_revision, ambiguous, or unavailable
- Persistence: clean, saving, saved, failed, or conflicted
- Overlay: none, reference, hints, notation_help, or discard_confirmation

Opening an overlay changes no draft state. Checking changes no atom counts. Saving changes no correctness state. Editing after a correct attempt changes the current draft's validation to unchecked or changed_since_check, but must not retroactively revoke a completed course item unless the native course rules explicitly support revisions.

### Initial and restored entry

1. Load the activity contract and current user's matching draft through Campus.
2. Keep the workbench read-only while the necessary contract is loading; do not briefly display another activity's draft.
3. If no draft exists, display a concise mode-specific first action and a direct help route.
4. If a compatible draft exists, restore it and label Resumed where you left off.
5. If the activity changed incompatibly, preserve the old draft for host-supported recovery, explain the mismatch, and offer Start the updated activity. Never silently reinterpret an old draft against a changed question.
6. If loading fails, show Retry and Back to course. Preserve an in-memory draft already present. Do not substitute invented default chemistry data.

### Typical edit and check

An edit produces one semantic transaction, updates the view immediately, marks the draft edited, and requests a host draft save. Submit snapshots a specific draft revision. While checking, the learner can inspect or read hints. Prefer temporarily disabling chemistry edits for that short check; if editing is permitted, a response for an older revision must be labeled as such and never overwrite the current draft's feedback. Repeated Check actions reuse the same in-flight submission identity rather than create duplicate attempts.

If the grader is unreachable, keep the draft and show Could not check this answer yet. Retry check. Never report incorrect or complete because of a network error. Persisted retries must follow the host's idempotency semantics.

### Undo and redo

Undo and redo apply to atom additions, count changes, group insertions, removals, charge edits, candidate changes, and configuration edits. Each committed typed count is one transaction rather than one transaction per keystroke. Undo a group insertion as one group insertion. A new edit after undo clears redo. Reference browsing, hint reading, focus movement, and validation requests are not undoable chemistry edits. An already submitted attempt is immutable; undo affects the draft, then a new check creates a new attempt.

Expose buttons with descriptive accessible names such as Undo add oxygen. Keyboard shortcuts operate only when they do not hijack text-field native undo. Announce the resulting formula or candidate concisely. Undo and redo states are included in the host draft only if the actual host contract supports them; chemistry state persistence is mandatory, deep edit history restoration is optional and must be disclosed accurately.

### Reset, leaving, and cancellation

Reset draft is reversible when the host can preserve the prior state as one undo transaction. In that case it requires no interrupting confirmation and offers Undo reset. If reset would irretrievably remove unsaved work or unsupported history, ask Reset this draft? with Keep working as the safe default. Do not show a discard warning when the draft is pristine or already safely recoverable.

Back to course saves through the shared store. On save failure, offer Stay and retry or Leave without saving this draft, with explicit potential loss. Closing the warning, Escape, browser Back returning from the warning, and repeated cancellation all leave the exact draft untouched. The default focused button is Keep working. Discard occurs only on the explicit destructive action.

Changing modes within one activity should preserve a separate compatible draft per mode through the host-owned session model. A prompt is necessary only if the transition would actually lose work. Switching to an incompatible task is a navigation event, not an automatic reset. Any deep link back restores the matching activity and user, never a global last-used chemistry object.

### Conflict and recovery

A save conflict means another revision exists, not that the answer was wrong. Explain Another version of this activity was saved. Offer Review versions using host-supported mechanisms, reload the remote version, or keep the current version only with supported revision protection. Never silently last-write-win across devices. A request that times out may have succeeded; read current native state before repeating a consequential submission.

## Accessibility and responsive behavior

Design targets are at least 44 by 44 CSS pixels where practical, including count controls and touch targets; this is a product target rather than a claim that every viewport can show 18 table columns simultaneously. Use a horizontally pannable periodic-table region at narrow widths with a visible scroll cue, persistent search, and an accessible list alternative. Do not shrink all element tiles into unreadable text. Reflow surrounding panels vertically and keep Check answer and Help reachable without covering active controls.

Provide skip links to prompt, periodic table, draft, feedback, and help. The table uses a managed focus pattern with one tab stop and spatial arrow movement through actual populated cells. Horizontal movement skips physical gaps; vertical movement seeks the next populated cell in the same group, with documented f-block access. Home and End move to the first and last element in the current rendered row. Explicit jump links move between the main table and detached f-block, retaining the last focus position. A simple searchable list provides an equivalent route for screen-reader users and anyone who prefers it.

Detached f-block rows must map to explicit element IDs, atomic numbers, display rows, and display columns supplied by the validated layout dataset. Connector markers are labeled navigation controls, never fake elements. Category conventions and group-3 placement must follow the chosen curriculum source consistently and disclose its convention. Do not derive chemical family membership solely from screen position. Search selection scrolls the element into view without changing its state until activated.

A cell's accessible name communicates symbol, name, atomic number, and relevant selection or assembly count; full reference prose belongs in the drawer. For example: Fe, iron, atomic number 26, add one atom. When two are present: Added iron. Two iron atoms in assembly. Charge unchanged. Do not announce every changing ledger cell independently; use one polite summary and keep detailed values readable on demand.

Formula displays need a text equivalent: Fe₂ means iron, atom count two; Fe²⁺ means iron ion, charge plus two. Superscript and subscript must survive zoom and high-contrast rendering. Provide meaningful text labels in addition to color, icons, border patterns, and orbital arrows. Respect reduced motion; none of the content requires animation. No drag-only action, hover-only explanation, timed hint, sound-only feedback, or accuracy dependence on pointer precision.

At browser zoom up to 400 percent, the surrounding interface reflows; the inherently two-dimensional periodic table may scroll within a named region. Focus must stay visible above sticky bars. Test actual assistive technologies rather than treating ARIA labels as proof of accessibility.

## Performance and graceful degradation

The periodic table is a bounded dataset; rendering its cells should not require a network call per hover, activation, or element. Load validated activity and element data once per version and cache only through approved host facilities. Keep chemical calculations and event transitions deterministic. Inspecting many tiles or rapidly incrementing an atom must not duplicate network grade submissions.

Suggested acceptance budgets, to be measured on agreed reference devices rather than asserted as achieved: visible response to a tile activation within 100 milliseconds for typical interaction; no lost counts during ten deliberate rapid activations; hint navigation independent of grader latency; and usable keyboard navigation before optional imagery loads. Screen-reader and zoom performance are part of the test matrix. Avoid virtualization that makes portions of the table unreachable to assistive technology.

If advanced graphics fail, preserve textual configuration editing, formula counts, reference text, and the ledger. If a chemistry data module is missing or fails validation, disable the affected exercise with a clear reason; do not calculate using partial data and present it as reliable. The host's offline policy governs whether an unsent draft can survive reload. Display that limitation honestly instead of claiming Saved based on an in-memory update.

## Acceptance scenarios for integration

UX-01: In Inspect mode, activate Fe twice. The drawer shows iron; assembly and attempt count are unchanged.

UX-02: In Add atoms mode, activate Fe twice. The tray contains two Fe atoms and a Fe₂ preview, the charge control is unchanged, and no grade is submitted. Undo once leaves one Fe; redo restores two.

UX-03: In a monatomic ion exercise, add one Fe and set charge +2. Display Fe²⁺, one atom, 26 protons, and 24 electrons. Changing count elsewhere must not rewrite that species charge.

UX-04: Build the Ca(NO₃)₂ composition using one calcium part and two intact nitrate groups. Show group multipliers and expanded totals. Undo removes the last group increment, not one oxygen atom. Parentheses appear according to grouping, not as cosmetic string replacement.

UX-05: Add O before H in a water molecular-formula exercise, then make counts O one and H two. Render the task's H₂O convention; explain ordering without changing click history or atom counts. If ordering is assessed, instead retain learner order until checked.

UX-06: Enter H₂O₂ for a molecular-formula target H₂O₂. Normalization must not reduce it to HO. Enter HO for an empirical target where that is intended and evaluate using that separate rubric.

UX-07: A clue admits multiple elements. The activity accepts the authored candidate set or insufficient-information response and exposes the next authored clue. It never chooses a hidden unique answer solely because one cell was visited first.

UX-08: Open Help before selecting any atom, progress one level, close, inspect an element, reopen, and press Back. The current draft is unchanged; no later hint has been exposed; focus returns predictably.

UX-09: After a correct check, edit the draft. The current draft is marked changed since check, the prior attempt remains recorded, and course completion follows native Campus rules rather than a local boolean.

UX-10: While checking revision seven, either prevent draft edits visibly or permit revision eight without applying revision-seven feedback to it. Repeated Check presses produce one authoritative attempt for that submission identity.

UX-11: Reset an undoable draft and choose Undo reset. All groups, counts, species charges, text, and candidate state return. When reset is not recoverable, cancel its warning three times; the state and save revision remain unchanged each time.

UX-12: Cause a draft-save failure, select Back to course, cancel the loss warning twice, retry save, and then leave. No intermediate cancel clears the draft; navigation proceeds only after save confirmation or explicit discard.

UX-13: Reload a saved activity and resume the matching draft. Change the authored task version incompatibly and verify an explicit recovery choice instead of silently grading the old draft against the new task.

UX-14: Use only keyboard controls to find an element, inspect it, add it, alter its count, set charge, open help, check, and leave. No focus trap, lost focus, hover dependency, or unannounced validation error occurs.

UX-15: At narrow viewport and 400 percent zoom, locate any element via table navigation or the equivalent list. Touch targets remain usable, the prompt and Help remain reachable, and the two-dimensional table scrolls without forcing the entire page to a tiny scale.

UX-16: Traverse detached f-block connectors. Each target resolves to the correct element ID and atomic number; no connector is submitted as an element. Focus returns to its originating region when the return action is used.

UX-17: Enter malformed charge notation or an unsupported formula form. The parser points to the problem, preserves the exact original input for editing, and does not coerce it into a different chemical answer.

UX-18: A conflict arrives from another device. Show the conflict separately from chemistry feedback and preserve both recoverable versions through host-supported flows. Canceling resolution does not overwrite either version.

UX-19: A grader timeout leaves the learner's draft and confidence intact and reports checking unavailable. Retrying observes native submission identity rules and does not award completion locally.

UX-20: Count controls, ionic charge, oxidation-state explanation, and future Lewis formal-charge labels are independently discoverable and separately named. A learner cannot accidentally change two concepts with one unlabeled control.

UX-21: Search and filters return multiple results without erasing the draft. Clear filter restores all cells. Selecting an inspection result does not answer an identification question until the explicit answer action occurs.

UX-22: A configuration clue lacks charge context. The authored task either supplies the needed neutral/ion condition or accepts the defined ambiguity response; electron count alone is not silently treated as an element's atomic number for every ion.

UX-23: Assistive technology reads formula and charge correctly, announces one concise update per transaction, and can access all ledger details without a flood of live-region announcements.

UX-24: Execute ten deliberate add activations, five undo actions, and five redo actions. Counts equal ten, five, and ten respectively, with no duplicate submissions or dropped additions. A new edit after undo correctly invalidates the redo branch.

UX-25: An unavailable element datum or unsupported Lewis rule yields scoped explanatory feedback. It does not fabricate a chemistry value, show a wrong mark, or unlock a later course item.

## Release gate

The interaction design is ready to implement when Campus integration owners confirm actual draft, grading, identity, revision, and navigation contracts; chemistry owners validate authored clues, formula ordering and accepted variants; and accessibility reviewers approve keyboard, screen-reader, zoom, and touch paths. This packet proposes those behaviors and tests. It does not assert that integration, chemistry validation, or runtime accessibility testing has already occurred.

## Composite answers and naming workspace

An activity may require several related answers, not just the currently visible tray. The submitted response is an envelope of typed, stable-ID parts: element selection or selection set; numerical counts; full and shorthand configurations; core choice; formula; chemical name; classification; explanation; and, when enabled later, Lewis graph and domain summary. The prompt and rubric determine which parts are required. Canonical answer-key examples and accepted aliases must not accidentally become extra mandatory fields.

A required explanation is a visible response field, distinct from the optional reflection journal. If a learner identifies the element correctly but omits the requested electron count, feedback says the element is correct and asks for the missing count. It does not erase the scientifically correct part or report the entire attempt as wrong. Likewise, a correct formula with an incomplete naming explanation remains visibly correct in its own component. Each response field links to its feedback and relevant hint.

Activities 038 and 039 require two independent formulas. Use a labeled subquestion tab or stacked card for each requested compound, with its own assembly state, raw input, undo transactions, and component feedback. Switching subquestions preserves both drafts. Check activity submits their shared revision as a composite response; it does not accidentally submit only the active tray. Activities 044 and 045 similarly need independent naming fields for each supplied formula. Activity 049 needs an item-by-item classification and naming response rather than one global category toggle.

Naming uses an editable text field plus optional scaffolded tokens. The scaffold can offer constituent names, an oxidation-state Roman numeral when appropriate, and prefixes under the declared naming system. It must not insert a Roman numeral based on atom count or universalize a fixed-charge convention to all metals. A token removal is undoable; free text is preserved when changing scaffold views. An activity may ask why a naming system applies, in which case an explanation is a separate required part. Accepted spelling and nomenclature variants come from the chemistry rubric; capitalization, punctuation, and spacing tolerance must not change the substance of the name.

Classification tasks provide named items and explicit category choices with keyboard and touch controls. Dragging can be an optional convenience, never the only route. Comparing configurations can use side-by-side or stacked fields with explicit equivalence choices and a reasoning field. Configuration building must allow a shorthand core, remaining subshells, full expansion, and derived or requested counts to coexist rather than overwrite each other in a single string.

Raw notation remains available when parsing fails. Under this packet's text-entry policy, Fe2 is a formula atom-count entry. Fe2+ requires clarification because plain-text conventions can make its intended count and charge unclear. Explicit Fe^2+ and Fe²⁺ identify the charge unambiguously. Formula case is meaningful: Co and CO are different inputs. Normalizing appearance must preserve chemical identity.

For later Lewis activities, an electron budget can be answered numerically with reasoning before a canvas exists, but the activity remains gated consistently with the planned extension release. Domain questions require separately labeled bonding-domain count, lone-pair-domain count, total domains, electron geometry, and molecular shape when requested. Do not present electron geometry and molecular shape as interchangeable labels. Equivalent graph layouts and permitted resonance contributors require chemistry-aware comparison, not pixel matching.
