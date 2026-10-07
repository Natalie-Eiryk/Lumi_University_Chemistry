---
document_id: LU-IONS-DESIGN-12
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Campus interface, accessibility, and private/public separation

## Entry screen

Public/topic title: **Ion Language: Name ↔ Formula**. Keep the course code in private provenance, not in the page title, navigation, or ordinary prompts. Proposed route `/teaching/chemistry/ion-language/` must be checked for collisions and current campus conventions before use.

The opening choices are Walk beside me, Quick reference, Practice translations, and My notebook. Show an unobtrusive session resume link if a local session exists. No forced diagnostic before a reference page, no demand for a login to read local content, and no new launcher solely for this module.

## Lesson shell

Wide layout: main prompt/model plus optional right-hand scaffold. Narrow layout: prompt, controls, then collapsible scaffold. Keep source references and exceptions accessible without interrupting every sentence. Show the scope of the current task: isolated-ion recall, neutral-salt formula, or naming.

The required controls are Check, Hint, Reveal, Clear workspace, and Next/Back. Clear workspace is not Delete progress. Leaving a screen preserves drafts and makes storage status visible. Don't clear other subjects' progress or all site caches.

## Formula display and entry

Use semantic `<sub>` for atom/group counts and `<sup>` for charge. Accept keyboard ASCII through the parser. Provide a live display preview but keep the original input available for correction. Do not turn every digit into a subscript with a global regex: atomic/charge/stoichiometric numbers have different roles.

Example render target:

```html
<span class="chemical-formula">
  <span aria-hidden="true">SO<sub>4</sub><sup>2−</sup></span>
  <span class="sr-only">sulfate ion: one sulfur, four oxygens, net charge two minus</span>
</span>
```

Use one tested accessible reading strategy to avoid reading the formula twice. A raw `aria-label` on any arbitrary span is not proof of accessibility. Test the resulting accessibility tree and actual screen-reader behavior.

## Accessibility acceptance

All tile actions need a keyboard path and a tap/click-without-drag path. Keyboard access alone does not satisfy a touch-only alternative. Keep focus visible, avoid focus traps, and preserve meaningful order when panels expand. Use semantic buttons, headings, inputs, and tables. [SRC-W3C](15_SOURCES_AND_DECISIONS.md#src-w3c)

Aim for comfortable 44×44 CSS-pixel controls as a product choice; the WCAG 2.2 minimum target-size rule is 24×24 with specified exceptions/spacing alternatives. Do not claim the standard requires 44 for all controls. Verify at 200% zoom and narrow width; allow page zoom. [SRC-TARGETS](15_SOURCES_AND_DECISIONS.md#src-targets)

Do not rely only on color to convey charge, correctness, or speaker identity. Motion is optional and honors reduced-motion preferences. Audio is user-initiated with full transcript and repeat controls. No time penalties. For pointer-based writing, retain a typed alternative; do not grade penmanship.

## Public and private boundaries

**Publishable candidate:** reviewed lesson text, generic examples, curated ion data, source references, and blank notebook template.

**Private by default:** Natalie’s handwritten notes, confidence, response history, due-review queue, personal interpretations, instructor correspondence, course documents, and local file paths. A collapsed panel is not privacy; data shipped to the browser is available to the viewer.

Do not bundle raw course PDFs, these entire design docs, or private learner exports into public assets. Generate a public projection from an explicit allowlist, not by hiding fields in CSS. Do not expose account tokens, temporary download URLs, local usernames, or device paths.

## Offline and persistence

Core content, reference lookup, parser, and reviewed feedback should work without a model service. Optional narration may be absent on an offline device; present transcript gracefully. Do not rely on a CDN to perform formula rendering.

Use the existing campus storage interface if present. Otherwise propose a namespaced local adapter with versioned exports; do not introduce a competing global store. Storage failure leaves the current session usable and visibly marked unsaved, with an export path. Never promise perfect browser persistence.

Import validates module/version, size, and structure before merge. Preserve existing data, detect duplicate event IDs, and offer previewed merge/replace for this module only. Keep a backup before destructive replacement. No learner-data sync by default; optional sync uses the existing authorized interface and an explicit review of what is sent.

## Deployment boundaries

This packet creates no deployed page. The inspected registry points Luminara’s public site to the existing Quiz Engine source and a static GitHub Pages deployment; the `890.10-luminara` directory is DNS bookkeeping, not the teaching source. [SRC-REPO](15_SOURCES_AND_DECISIONS.md#src-repo)

Codex must reuse the active local teaching-campus launcher and conflict-confirmation flow. Do not build a second server, choose a fresh port just to bypass existing coordination, stop unknown processes, alter CNAME/DNS, clear shared study data, or change authentication for this lesson. Public deployment and canon promotion remain separate explicit decisions.
