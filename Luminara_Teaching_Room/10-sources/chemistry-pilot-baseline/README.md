# Luminara Teaching Room — chemistry pilot added

Read **CHEMISTRY_START_HERE.md** for this release. The first chemistry workspace uses only the one recovered seven-page Unit I workbook. The requested Windows course directory remains uninspected; do not read this pilot as a full course import.

Open `Launch-Teaching-Room.cmd` for the shared entrance, `Launch-Chemistry.cmd` for the pilot, or `Launch-Lab.cmd` for the unchanged Bioethics app. Keep the same browser profile and fixed address. Export each subject’s private backup independently.

Build chemistry with `python scripts/build_chemistry.py`; build the portal with `python scripts/build_room.py`. Both use Python’s standard library. The chemistry app has no remote runtime dependencies. JavaScript source is in `30-modules/chem-1117-f2026/source/`.

The original assembly README is retained at `10-sources/assembly-1-baseline/README.md`. The original consolidation report remains `CONSOLIDATION_REPORT.md`. Current chemistry evidence is `CHEMISTRY_PASS_REPORT.md` and `evidence/chemistry/`. Older app test receipts are history, not newly rerun learning-outcome evidence.
