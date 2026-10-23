# Voice restoration full test suite

## Command and result

After all 12 restored tutorial sources and the core renderer fixes were released,
the complete repository pytest suite ran once outside the sandbox, as required by
`AGENTS.md`:

```sh
mkdir -p tutorial_output/voice_restoration/test_logs && source source_me.sh && python3 -m pytest tests/ -q 2>&1 | tee tutorial_output/voice_restoration/test_logs/full_suite.log
```

Pytest collected and ran the normal `tests/` suite without exclusions. It reported
**1,528 passed and 1 failed in 4.26 seconds**. The test implementation is in the repository's
[tests/](../../../tests/) directory. The console log was captured under ignored generated output
and is not a durable Markdown-link target.
The command pipes output through `tee` without `pipefail`, so the shell pipeline
status reflects `tee`; the pytest summary above is the test result.

## Failure

The sole failure is a local-link check for
`docs/active_plans/reports/voice_microbes_petase_original_comparison.md:50`. Its
image link targets
`tutorial_output/verification/voice_microbes_petase_original_comparison/current_pdf_opening_pages_side_by_side.png`,
which is absent. This is a documentation artifact link, not a pytest failure in
the restored sources or renderer. The full suite therefore did not pass; rerun
after the missing link is repaired if a clean full-suite result is required.

This is a historical checkpoint. The broken comparison-image link has since been removed from its
report, but the suite has not been rerun against the current documentation and renderer fixes. The
result measures automated repository checks; it does not establish classroom quality or student
outcomes.
