---
document_id: LU-IONS-DESIGN-15
module_id: LU-CHEM-IONS-001
package_version: 1.0.0
status: design_candidate
created: 2026-09-22
audience: design-and-implementation
implementation_status: not_implemented_by_this_packet
---

# Source ledger, corrections, and open decisions

## Provenance categories

**Conversation-derived:** requested scope, prior ion-list transcription, preferences and course conventions reported by Natalie.  
**Repository-observed:** live connector reads of named files on 2026-09-22.  
**Externally checked:** educational/terminological/accessibility references below.  
**Original design:** lesson scripts, example selection, UI behavior, review intervals, thresholds, candidate IDs, and implementation hooks.

This packet does not claim to have modified, compiled, deployed, or tested Lumi itself. References support specific concepts; original examples and integer charge calculations are authored here. No instructor documents are redistributed.

<a id="src-chat"></a>
## SRC-CHAT — requested design and learning context

Source: this conversation, especially the ion-naming explanation, the proposed Lumi University study session, and Natalie’s request for modular Markdown implementation scaffolds. Exact course conventions are user-reported unless confirmed from an original document. Handwriting is Natalie’s reasoning layer, never silently the instructor’s statements.

Preserved preferences: first-principles bridges; conventional answer and personal reasoning shown separately; clear dialogue attribution; semantic chemical notation; topic-first public identity; private local notes; teacher/student/peer tone; correct thinking not invalidated solely by alternate notation.

<a id="src-course-ions"></a>
## SRC-COURSE-IONS — 1117 Ion List.pdf

Files metadata located the original attachment under `file_000000007b1c820ca59ce41f6e6386cb`. This build tried a page read with images; no readable content was returned. The raw-file materialization attempt reported no downloadable backing file. The bank in 04 therefore uses the earlier conversation’s explicit transcription, not a fresh document inspection.

The 62 charge-specific records are preserved for design completeness. Codex must locate the actual local course source and reconcile name/formula/charge rows before claiming complete course alignment. In particular, check phosphite PO₃³⁻, silicate SiO₄⁴⁻, carbide C⁴⁻, and whether additional ions or alternative names are required.

If the source remains absent, implementation may proceed with the clearly labeled candidate bank and checked ordinary examples. Do not silently declare source reconciliation passed, invent a local source path, or erase the provisional status.

The element-list attachment was likewise located but unreadable in this build. The design does not assert a freshly verified 58-element coverage requirement.

<a id="src-doctrine"></a>
## SRC-DOCTRINE — central Adventure Doctrine

Repository: `Natalie-Eiryk/Lumi_OS`.

Path:
`Library/800-Applications/820-Teaching/820.20-Pedagogy/820.21-Ms_Luminara_Persona/010-adventure-doctrine/010.0-luminara-adventure-doctrine-and-atlas-chronicle-protocol.md`

Observed metadata: doctrine `LUMI-ATLAS-DOCTRINE-ADVENTURE-001`, version `1.1.0`, status `CANONICAL`. Returned Git blob SHA: `c713ce5d2437ff4b8c237bb1d162e9becdd83da2`. The header/integration note was read; this packet does not claim to have re-audited the entire Primer or every doctrine section.

[Canonical repository file](https://github.com/Natalie-Eiryk/Lumi_OS/blob/main/Library/800-Applications/820-Teaching/820.20-Pedagogy/820.21-Ms_Luminara_Persona/010-adventure-doctrine/010.0-luminara-adventure-doctrine-and-atlas-chronicle-protocol.md)

The document explicitly separates doctrinal integration from implemented runtime behavior. This design preserves that distinction. A Git blob SHA is not the same thing as a repository commit or a SHA-256 file hash.

<a id="src-repo"></a>
## SRC-REPO — inspected integration surfaces

All read on 2026-09-22 using the connected GitHub tool, default branch. Resolve current equivalents again before modifying anything.

| File | Returned Git blob SHA | Observation |
|---|---|---|
| `Library/800-Applications/890-Websites/site-registry.json` | `2af4ca0d475d9da37bc6057478607921021668d1` | Luminara’s source is the Quiz Engine; deploy repo is `Natalie-Eiryk/luminara`; the website stub is DNS bookkeeping |
| `…/820.31-Quiz_Engine/820.31-v2/schemas/learning-item.schema.json` | `fa6393c8d70b8a9b104047261352c1191d1826bb` | existing kinds include station, scaffold, retrieval, vocabulary; `teaching` is an object extension point |
| `…/820.31-Quiz_Engine/820.31-v2/schemas/teaching-module-manifest.schema.json` | `a362464fc12b48887a8b0c8f6602f58a8d95a349` | existing module manifest carries route, sourceRefs, itemCollections, diagnostics, lumiSync |
| `…/820.31-Quiz_Engine/820.31-v2/schemas/learner-progress-record.schema.json` | `dfd0ea84b9533a58dafec7e0e7093b2af6977b07` | confidence is required numeric; notesLocalOnly and nextReviewAt exist |

The ellipsis above expands to:
`Library/800-Applications/820-Teaching/820.30-Tools`

[Site registry](https://github.com/Natalie-Eiryk/Lumi_OS/blob/main/Library/800-Applications/890-Websites/site-registry.json)

[Learning-item schema](https://github.com/Natalie-Eiryk/Lumi_OS/blob/main/Library/800-Applications/820-Teaching/820.30-Tools/820.31-Quiz_Engine/820.31-v2/schemas/learning-item.schema.json)

Runtime rendering, the latest local university-campus layout, launch behavior, native integration, and migrations were not inspected/executed in this build. Existing schema fields do not prove that every proposed interactive component is supported.

<a id="src-ionic"></a>
## SRC-IONIC — introductory ions and formulas

OpenStax, *Chemistry 2e*, §2.6, “Ionic and Molecular Compounds.”

[Publisher source](https://openstax.org/books/chemistry-2e/pages/2-6-ionic-and-molecular-compounds)

Supports the scoped monatomic-ion patterns, polyatomic groups, neutrality, and ordinary formula construction. It also states limits of simple periodic-table classification. The new worked examples are original applications, not quotations or claims about laboratory preparation.

<a id="src-naming"></a>
## SRC-NAMING — naming grammar

OpenStax, *Chemistry 2e*, §2.7, “Chemical Nomenclature.”

[Publisher source](https://openstax.org/books/chemistry-2e/pages/2-7-chemical-nomenclature)

Supports cation/anion naming, recognized polyatomic names, variable-metal numerals, and the need to route molecular/acid cases differently. The suffix mnemonics are teaching aids; their scope restrictions are part of this design.

<a id="src-energy"></a>
## SRC-ENERGY — the noble-gas heuristic is not a free-energy proof

OpenStax, *Chemistry 2e*, §7.5, “Strengths of Ionic and Covalent Bonds.”

[Publisher source](https://openstax.org/books/chemistry-2e/pages/7-5-strengths-of-ionic-and-covalent-bonds)

Supports the distinction between ionization-energy costs and lattice contributions. Used only for the short optional energetic caveat; the core module requires no thermodynamic derivation.

<a id="src-oxidation"></a>
## SRC-OXIDATION — oxidation state versus actual ion charge

IUPAC Gold Book, “oxidation state,” DOI `10.1351/goldbook.O04365`.

[Official terminology](https://goldbook.iupac.org/terms/view/O04365/1000)

Supports treating oxidation state as an ionic-approximation bookkeeping concept. For a monatomic ion it equals its charge; that does not turn the central atom of sulfate into an isolated S⁶⁺ species.

<a id="src-ies"></a>
## SRC-IES — learning design basis

Pashler, Bain, Bottge, Graesser, Koedinger, McDaniel, and Metcalfe (2007), *Organizing Instruction and Study to Improve Student Learning*, IES Practice Guide, NCER 2007-2004. ERIC ED498555.

[Official ERIC record and abstract](https://eric.ed.gov/?id=ED498555)

The official abstract was reviewed. It supports spacing, interleaving worked examples with problem solving, connecting graphical/verbal and concrete/abstract representations, retrieval practice, and reflective judgments of learning. It does not establish this packet’s exact minute plan, 1/3/7/14-day intervals, eight-item queue, or success thresholds. Those remain adjustable design proposals.

<a id="src-w3c"></a>
## SRC-W3C — accessible manipulation

W3C WAI, Understanding WCAG 2.2 SC 2.5.7, Dragging Movements.

[Official guidance](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements)

Supports a single-pointer alternative to dragging; keyboard support is a separate requirement. This is why the tiles need tap/click controls as well as a keyboard route.

<a id="src-targets"></a>
## SRC-TARGETS — touch target size

W3C WAI, Understanding WCAG 2.2 SC 2.5.8, Target Size (Minimum).

[Official guidance](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum)

The 24×24 CSS-pixel minimum has exceptions and spacing alternatives. The packet’s 44×44 goal is a larger comfort target, not a misquotation of this minimum.

## Explicit refinements to the earlier proposal

| Earlier simplification | Refinement now required |
|---|---|
| “All atoms want the nearest noble gas” | restricted main-group heuristic; full energetic context and transition-metal limits remain visible |
| “-ide means one atom” | useful rule for monatomic anions, not a reversible definition |
| “-ite = one fewer O” without a boundary | only within explicitly known families; no inferred universal charge |
| “Neutrality generates any valid compound” | necessary stoichiometric constraint, not proof of existence or formation |
| “Reduce subscripts” | reduce whole-ion ratio; preserve peroxide and other internal groups |
| “CaN₂O₆ is wrong” without qualification | acknowledge atom-count equivalence and teach conventional grouping |
| “One success means mastered” | assistance-aware, direction-specific evidence with delayed review |
| full bank treated as freshly verified | explicitly conversation-derived pending original-source reconciliation |

## Open decisions for Codex handback

1. Confirm current canonical content root, campus route, registry adapter, and storage interface.
2. Reconcile the actual instructor ion list and special scope entries.
3. Resolve optional confidence versus required legacy numeric confidence without inventing data.
4. Decide which conventional-form differences count as “needs revision” in practice; preserve component evidence either way.
5. Confirm privacy projection and authorized release target. Local preview is not public approval.
6. Confirm browser/device capability for optional speech; use text fallback when absent.

No open decision authorizes rewriting the central doctrine or changing launch/security behavior without explicit scope.
