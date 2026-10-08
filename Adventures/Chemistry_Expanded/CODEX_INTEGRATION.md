# Codex integration handoff

## Purpose

Integrate this reviewed chemistry expansion into the existing adventure library when Natalie requests implementation. This packet itself performs no repository, runtime, schema, permission or publication changes.

Use this edition as a content replacement for the matching original adventure version, not as five unrelated new adventures. Preserve existing IDs:

- luminara.adventure.001: The Address With No Row
- luminara.adventure.002: The Bracket Luggage Office
- luminara.adventure.003: The City Without Couples
- luminara.adventure.004: Ms Luminara and the Compound Naming Station
- luminara.adventure.005: Ms Luminara and the Mole Counting Station

The twenty original question IDs q01–q04 retain their original task meaning. The sixty new vocabulary-card IDs use a separate card01–card12 family under each story ID. Chapter card files are generated views of the central study_support/cards.json deck, not separate authoring authorities. New question IDs must not overwrite older learner responses. Preserve earlier revisions in history and ask the existing migration layer to reconcile changed resource paths rather than silently discarding saved progress.

## Inspect before implementing

1. Read catalogue.json, chapter SOURCES.md, scene maps and the source coverage notes.
2. Inspect the current adventure/Atlas schemas and installed Primer and Adventure Doctrine. This delivery's portable JSON is an authoring map; do not assert production-schema conformance from valid JSON alone.
3. Inspect the existing Chemistry module and University library integration points. Do not create a competing module, launcher, persistence store, vocabulary bank or assessment engine.
4. Validate source-specific conventions and pending instructor choices against actual source documents. A legacy worksheet filename does not establish the current course sequence or AI policy.
5. Plan a versioned content update. Preserve original identities, reference bindings, learner work and source provenance. Canonical promotion requires Natalie's approval.

## Experience to preserve

- Topic-first story titles; exact course identifiers stay in provenance, not fiction.
- Read-through story mode with optional support, not forced questions between scenes.
- Support and full explanations available before mistakes; no hidden timed or recall-only gate.
- Clear speaker labels, true chemical subscripts and superscripts, accessible reading order.
- Distinguish plain-text chemical equivalents from genuinely different species; never normalize S²⁻ to S₂.
- Open reasoning uses a visible rubric or self-check. Do not invent a semantic auto-grader.
- Existing shared Save and notebook flows are reused, with explicit migration tests.
- Original and new question IDs remain distinct; question-to-scene links supplement, not replace, question records.
- Source, fiction, model limit and course-specific convention remain distinguishable.

## Acceptance tests for an implementation

Check all story and question IDs, old-to-new resource links, existing saved-response retention, all explicit scene anchors, keyboard navigation, narrow-screen layout, zoom, text-only access and chemistry notation. Confirm teacher explanations can be reached voluntarily and are not presented as an instructor's official key. Confirm no course number appears in public-facing fiction. Test reading without a connection if local use is intended. Do not report these runtime tests as passed merely because the content ZIP's static checks passed.

The five narratives do not cover every Unit II worksheet task or establish a complete semester scope. Extend coverage deliberately and retain that distinction in the UI.
