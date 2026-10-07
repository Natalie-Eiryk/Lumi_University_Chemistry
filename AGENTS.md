# Chemistry content ownership

This is the chemistry content repository, separate from Lumi University and Lumi_OS.
The user explicitly requested content extraction on October 6, 2026. Grading,
page generation, templates, study modes and application/runtime code stay in
`F:/Luminara_Campus`. Do not create another launcher, server, grader or notebook store.

- Preserve scientific/source provenance, question IDs, source archives and original bytes.
- Use the existing course contracts and native campus validators. Do not fork schemas.
- The existing Atlas reference history is the authoritative history. ATLAS/INDEX.json
  points to it; do not create a competing graph or revision ledger.
- Git LFS owns binary source assets. Verify their upload when pushing.
- Keep shared repository references explicit and update the content manifest and campus
  registration together after content review. No silent fallback or automatic download.
- Keep student save state and per-installation identity in the campus's existing save system.
- Historical imported scripts are inert references. No new production backend belongs here.
- Campus build/test resource limits and process safety still apply when using its tools.
- No change here constitutes governed Lumi_OS integration or public website deployment.
