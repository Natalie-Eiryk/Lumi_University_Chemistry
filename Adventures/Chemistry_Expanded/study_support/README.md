# Optional study support and source navigation

This folder adds 60 new vocabulary retrieval cards to the five expanded chemistry adventures: 12 per chapter, balanced between definition, contrast, and application. The cards were authored for this edition. No pre-existing flashcard deck was recovered or reconstructed.

## Choose a route

- Read the stories without doing any practice.
- Pick one card after a scene and explain it in your own words.
- Read the answer first, then revisit the story or support.
- Use a card as a short bridge to a longer practice question.
- Stop or change modes whenever useful. References, calculators, labeled sketches, and spoken explanations are welcome.

These are original AI-assisted materials for private conceptual reinforcement, not an instructor answer key, graded assignment, or certification of course coverage.

## Files

- [Readable cards](VOCABULARY_CARDS.md): prompts, answers, reasoning notes, verified scenes/support/sources, and related practice.
- [cards.json](cards.json): the canonical 60-card array.
- [cards.tsv](cards.tsv): the same fields as UTF-8 tab-separated text; list fields contain JSON arrays.
- [card_navigation.json](card_navigation.json): verified scene/support/practice/source bindings, separate from card content.
- [unit_ii_crosswalk.json](unit_ii_crosswalk.json): selected source-task references and explicit limits, not a complete coverage claim.
- [Sources and boundaries](SOURCES.md).

## Five chapter routes

### 01 · The Address With No Row

- [Story](../chapters/01_periodic/STORY.md) · [Support](../chapters/01_periodic/SUPPORT.md) · [Practice](../chapters/01_periodic/PRACTICE.md) · [Worked key](../chapters/01_periodic/TEACHER_KEY.md) · [Chapter sources](../chapters/01_periodic/SOURCES.md)
- Story ID: luminara.adventure.001
- New cards: luminara.adventure.001.card01 through card12
- Original practice IDs: [luminara.adventure.001.q01](../chapters/01_periodic/PRACTICE.md#q01), [luminara.adventure.001.q02](../chapters/01_periodic/PRACTICE.md#q02), [luminara.adventure.001.q03](../chapters/01_periodic/PRACTICE.md#q03), [luminara.adventure.001.q04](../chapters/01_periodic/PRACTICE.md#q04)

### 02 · The Bracket Luggage Office

- [Story](../chapters/02_brackets/STORY.md) · [Support](../chapters/02_brackets/SUPPORT.md) · [Practice](../chapters/02_brackets/PRACTICE.md) · [Worked key](../chapters/02_brackets/TEACHER_KEY.md) · [Chapter sources](../chapters/02_brackets/SOURCES.md)
- Story ID: luminara.adventure.002
- New cards: luminara.adventure.002.card01 through card12
- Original practice IDs: [luminara.adventure.002.q01](../chapters/02_brackets/PRACTICE.md#luminaraadventure002q01), [luminara.adventure.002.q02](../chapters/02_brackets/PRACTICE.md#luminaraadventure002q02), [luminara.adventure.002.q03](../chapters/02_brackets/PRACTICE.md#luminaraadventure002q03), [luminara.adventure.002.q04](../chapters/02_brackets/PRACTICE.md#luminaraadventure002q04)

### 03 · The City Without Couples

- [Story](../chapters/03_city/STORY.md) · [Support](../chapters/03_city/SUPPORT.md) · [Practice](../chapters/03_city/PRACTICE.md) · [Worked key](../chapters/03_city/TEACHER_KEY.md) · [Chapter sources](../chapters/03_city/SOURCES.md)
- Story ID: luminara.adventure.003
- New cards: luminara.adventure.003.card01 through card12
- Original practice IDs: [luminara.adventure.003.q01](../chapters/03_city/PRACTICE.md#luminaraadventure003q01), [luminara.adventure.003.q02](../chapters/03_city/PRACTICE.md#luminaraadventure003q02), [luminara.adventure.003.q03](../chapters/03_city/PRACTICE.md#luminaraadventure003q03), [luminara.adventure.003.q04](../chapters/03_city/PRACTICE.md#luminaraadventure003q04)

### 04 · Ms Luminara and the Compound Naming Station

- [Story](../chapters/04_naming/STORY.md) · [Support](../chapters/04_naming/SUPPORT.md) · [Practice](../chapters/04_naming/PRACTICE.md) · [Worked key](../chapters/04_naming/TEACHER_KEY.md) · [Chapter sources](../chapters/04_naming/SOURCES.md)
- Story ID: luminara.adventure.004
- New cards: luminara.adventure.004.card01 through card12
- Original practice IDs: [luminara.adventure.004.q01](../chapters/04_naming/PRACTICE.md#question-1-copper-at-two-platforms), [luminara.adventure.004.q02](../chapters/04_naming/PRACTICE.md#question-2-a-salt-without-a-metal), [luminara.adventure.004.q03](../chapters/04_naming/PRACTICE.md#question-3-choosing-a-naming-language), [luminara.adventure.004.q04](../chapters/04_naming/PRACTICE.md#question-4-a-formula-that-must-keep-its-passengers)

### 05 · Ms Luminara and the Mole Counting Station

- [Story](../chapters/05_moles/STORY.md) · [Support](../chapters/05_moles/SUPPORT.md) · [Practice](../chapters/05_moles/PRACTICE.md) · [Worked key](../chapters/05_moles/TEACHER_KEY.md) · [Chapter sources](../chapters/05_moles/SOURCES.md)
- Story ID: luminara.adventure.005
- New cards: luminara.adventure.005.card01 through card12
- Original practice IDs: [luminara.adventure.005.q01](../chapters/05_moles/PRACTICE.md#question-1-a-new-molecule-on-the-receipt), [luminara.adventure.005.q02](../chapters/05_moles/PRACTICE.md#question-2-equal-amounts-and-unequal-masses), [luminara.adventure.005.q03](../chapters/05_moles/PRACTICE.md#question-3-a-different-artificial-isotope-mixture), [luminara.adventure.005.q04](../chapters/05_moles/PRACTICE.md#question-4-reconstructing-a-mixture)

## Distinct ID families

The twenty original questions retain q01–q04 under their original story IDs. New chapter questions use additional IDs assigned in each PRACTICE.md; cards use card01–card12 and never replace a question. Unit II IDs such as LUMI-U2-Q07-L are source-packet authoring references, not verified links to a live campus activity. Supplemental LUMI-U2-NEW IDs are a separate category, not worksheet-source questions.

A card’s practice_ids means “this question gives related longer practice,” not “the card fully answers every part.” A selected crosswalk entry similarly indicates conceptual relevance, not mastery, complete preparation, or instructor endorsement.

## Reading the data

kind is definition, contrast, or application. source_refs contains direct source URLs plus explicit anchors in this folder’s source register. scene_ids contains verified explicit chapter scene anchors. card_navigation.json supplies scene, support, practice, and source deep links and labels method-transfer cases. accepted_reasoning is human-readable guidance; no semantic grader or spaced-repetition application has been implemented.

All 60 cards are now bound to checked expanded scenes, support topics, relevant practice, and source entries. The chapter set currently has 72 practice questions: twenty preserved originals and 52 new expansion questions. A card may use a newer question when it is the closer match. Link integrity should be rechecked after later chapter revisions. This folder provides portable content only; no standalone reader, flashcard app, spaced-repetition service, or automatic checker has been implemented.


## Central deck and chapter-copy source contract

The central deck in this folder is the content source of truth. Each chapter’s vocabulary_cards.json contains its twelve cards with exactly the same id, story_id, kind, prompt, answer, accepted_reasoning, scene_ids, and practice_ids. The readable versions are derived from those same records.

source_refs deliberately uses the file’s own location:

- In study_support/cards.json, SOURCES.md#ref-… resolves to this folder’s scientific source register.
- In a chapter’s vocabulary_cards.json, SOURCES.md#… resolves to that chapter’s own source section, using its explicit or Markdown-heading anchor. This keeps a chapter’s source links usable without the central study folder.
- Direct HTTPS scientific-source URLs are retained unchanged in each copy. Chapter source sections can group several references, so the number and wording of local source anchors may differ.

These local source routes are intentionally context-specific; they are not differences in the card’s chemistry or learning target. Compare all other fields exactly, and resolve each relative source reference from the directory containing that JSON file. Do not copy central relative source_refs unchanged into a chapter or compare the local source strings as if both files shared one directory. A copy or relocation requires rebasing and a fresh link check.
