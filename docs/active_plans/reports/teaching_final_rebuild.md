# Final teaching tutorial rebuild

All 12 current default bundles were rebuilt from `tutorial_data/*.md` with `make_tutorial.py build`. Each bundle contains PDF, DOCX, and XLSX artifacts. Builds used the repository bootstrap and ran outside the sandbox because PDF conversion invokes LibreOffice. Per-source logs are in `tutorial_output/verification/teaching_review/final_rebuild/build_logs/`.

Every generated bundle validation source hash matches both its current Markdown source and the refreshed Calc report. The build verified workbook serialized values and types (typed seed readback) and DOCX package integrity. Artifact hashes, byte sizes, and PDF page counts are recorded in `tutorial_output/verification/teaching_review/final_rebuild/manifest.json`.

| Tutorial | PDF pages |
| --- | ---: |
| `babies_1_z_test` | 6 |
| `babies_2_t_test` | 7 |
| `babies_3_two_sample_t_test` | 3 |
| `caffeine_1_descriptive_statistics` | 3 |
| `caffeine_2_linear_regression` | 8 |
| `caffeine_3_quadratic_regression` | 7 |
| `microbes_1_z_test` | 5 |
| `microbes_2_t_test` | 5 |
| `microbes_3_two_sample_t_test` | 7 |
| `microbes_4_f_test` | 5 |
| `microbes_5_anova` | 6 |
| `petase_1_linear_regression` | 6 |

## Calculation validation

`source source_me.sh && python3 devel/check_tutorial_calculations.py -o tutorial_output/verification/teaching_review/final_rebuild/calculation` generated expectations for 12 tutorials, 13 scenarios, and 254 formula comparisons, plus eight synthetic direction checks. `devel/validate_libreoffice.py tutorial_data/*.md -e tutorial_output/verification/teaching_review/final_rebuild/calculation/tutorial_expectations.json -o tutorial_output/verification/teaching_review/final_rebuild/calculation/calc` ran LibreOffice Calc outside the sandbox. Calc passed all 13 scenarios and 254 comparisons. The per-scenario results are preserved in the calculation report directory. This matches the previous 13-scenario, 254-comparison baseline.

This report records rebuild and calculation evidence. It does not claim classroom approval or fresh visual review.

## Repository checks

The full suite collected 1,336 tests: 1,334 passed and two failed in `tests/test_markdown_links.py`. One failure was the unresolved generated-manifest link in the earlier `teaching_rebuild.md` report; that target is absent. The failure in this report was corrected to use a plain output path, and its targeted link-check case then passed (1 passed, 92 deselected). No tutorial build, workbook, DOCX, semantic, oracle, or calculation tests failed.
