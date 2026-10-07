# Lumi University Chemistry

Chemistry content for Lumi University. This repository owns lessons, question banks,
course editions, source references, scientific reference snapshots and chemistry's
Atlas history. The shared university owns grading, page generation, study modes,
templates, windows, saving and the desktop launcher.

## Working layout

Keep these sibling checkouts on the same drive:

- `F:/Luminara_Campus` — the shared university and installed application.
- `F:/Lumi_University_Chemistry` — this content repository.

Git LFS is required for binary source assets. After cloning, run `git lfs pull`.
The original relative folders are preserved so source IDs, course manifests and
Atlas citations retain their meaning. This is content custody, not a second app.

| Collection | Location |
| --- | --- |
| Chemistry workbook and question bank | `Luminara_Teaching_Room/30-modules/chem-1117-f2026/source/` |
| Ion lessons, practice seeds and course editions | `Luminara_Teaching_Room/30-modules/chem-1117-f2026/ion-language/` |
| Ms. Luminara adventure and Q13 teaching companions | `Luminara_Teaching_Room/30-modules/chem-1117-f2026/adventure/` and `q13-scaffolds/` |
| Unit II lessons, questions and answer keys | `Luminara_Teaching_Room/30-modules/chem-1117-f2026/unit-ii/` |
| Element and ion reference sources | `Luminara_Teaching_Room/10-sources/reviewed-element-reference/` and `reviewed-ion-language/` |
| Periodic workbench handoff | `Chemistry/periodic_workbench_packet/` |
| Atlas ownership and continuity | [ATLAS/README.md](ATLAS/README.md) |

## Editing and delivery

Edit the content here. Native campus tools consume it through the campus's
`Luminara_Teaching_Room/CONTENT_REPOSITORIES.json` registration. Missing sources,
changed fingerprints and conflicting ownership fail explicitly; an old campus
copy is not a fallback. Content stays off the HTTP allowlist: only the campus's
generated lesson pages are served. Existing routes, study IDs and save keys remain.

`CONTENT_MANIFEST.json` records the migrated source bytes and original campus
commit. A content update must refresh the affected file fingerprints, pass the
existing campus content-admission and grading checks, and update the campus's
registered manifest fingerprint after review. Commit and push content first, then
the campus reference update. Do not maintain another grading implementation here.

The native chemistry compiler and ion compiler remain in the university. Unit II
build inputs resolve directly from this checkout. Generated `ion-data.json`, the
generated lesson reader, HTML pages and deployment snapshots remain campus-owned
outputs; they are not independent authoring sources.

Historical source packages may contain old demo scripts or HTML. They remain inert
provenance, not supported launchers or alternate grading engines. Mixed-subject
campus evidence remains in the [university repository](https://github.com/Natalie-Eiryk/Lumi_University);
its original Git history is not rewritten by this extraction.

After a fresh clone, build the campus tools and run the campus compiler's
`references prepare-checkout CAMPUS_ROOT` command once. This recreates only the
existing local Atlas transaction lock; it validates but does not alter history or
admit new sources. Runtime lock files remain outside Git. See the university's
`Luminara_Teaching_Room/CONTENT_REPOSITORIES.md` for the complete update procedure.
