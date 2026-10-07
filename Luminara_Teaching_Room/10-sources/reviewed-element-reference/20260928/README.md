# Temporary standalone element-reference inputs

These files are pinned build inputs for the standalone campus, not a second
canonical Lumi_OS element library. Do not edit their scientific values in place.
The native importer rejects changes to pinned input hashes.

[`ADOPTION.json`](ADOPTION.json) identifies the copied Lumi files, supplemental
publisher inputs, their current consumers and required integration disposition.
It is an explicit planning marker, not a runtime resolver, registered Lumi schema
or automatic deletion mechanism. Canonical adoption and retirement receipts are
currently absent; the compiler still needs these inputs.

The existing [Lumi handoff](../../../60-integration/LUMI_TEACHING_HANDOFF.md)
owns the acceptance and cleanup checklist. On integration, use the accepted
scientific owner's export, reconcile new facts/corrections once, verify a clean
build without these snapshots, then retire redundant payloads through their
existing custody owner. Keep compact lineage; do not preserve every full copy.

Generated browser bundles are deployment artifacts and must never be edited as
an independent scientific source. Original course archives and private learner
notebooks are outside this retirement scope.
