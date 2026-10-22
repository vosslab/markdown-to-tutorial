# Test validation

Updated 2026-10-22. The final repository suite passed after the README opening was shortened to
plain prose and after the final documentation updates. Direct checks cover the new formula I/O
module, which tracked-only vendored-test discovery does not yet include.

## Earlier snapshots

- The pre-rename suite passed 1272 tests. Its log remains in
  `tutorial_output/verification/final_verification/pytest_final.log` and covers that earlier
  snapshot only.
- The coordinated layout update then passed 1305 repository tests through the sourced environment.
  That run preceded the current formula-boundary documentation and final readiness edits.

## Final verification

The post-archive full suite passed **1309 tests in 3.04 seconds** using Python 3.12.15 through the
required sourced environment. The retained output is
`tutorial_output/verification/readiness/pytest_final_closeout.log`.

```bash
source source_me.sh && python3 -m pytest tests/
```

Before the suite, single-file lint, security, typing, import, ASCII, and shebang checks passed for
the current new Python source. CLI help and the XLSX import smoke check also passed. These direct
checks supplement the suite because no supported include hook exists for untracked Python files.

Build and real-engine calculation evidence is separate: see
[readiness_execution.md](readiness_execution.md) and
[local_calculation_readiness.md](local_calculation_readiness.md). Google Sheets remains unverified.
