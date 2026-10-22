# Final teaching tutorial rebuild

All 12 current default bundles have been built from their Markdown sources with `make_tutorial.py build`. After the final teaching and DOCX style edits, all bundles were rebuilt: 36 artifacts across 70 PDF pages. Builds used the repository bootstrap and ran outside the sandbox because PDF conversion invokes LibreOffice. Per-source logs are in `tutorial_output/verification/teaching_review/final_rebuild/build_logs/`.

Every generated bundle validation source hash matches both its current Markdown source and the refreshed Calc report. The build verified workbook serialized values and types (typed seed readback) and DOCX package integrity. Artifact hashes, byte sizes, and PDF page counts are recorded in `tutorial_output/verification/teaching_review/final_rebuild/manifest.json`.

| Tutorial | PDF pages |
| --- | ---: |
| `babies_1_z_test` | 7 |
| `babies_2_t_test` | 7 |
| `babies_3_two_sample_t_test` | 4 |
| `caffeine_1_descriptive_statistics` | 3 |
| `caffeine_2_linear_regression` | 8 |
| `caffeine_3_quadratic_regression` | 7 |
| `microbes_1_z_test` | 5 |
| `microbes_2_t_test` | 5 |
| `microbes_3_two_sample_t_test` | 7 |
| `microbes_4_f_test` | 5 |
| `microbes_5_anova` | 6 |
| `petase_1_linear_regression` | 6 |

The final style-integrated manifest SHA-256 is `87fc4e7723df76a2a2f42637318ddde3d61624150483b84d018dc26d5e4daaff`.

## Calculation validation

`source source_me.sh && python3 devel/check_tutorial_calculations.py -o tutorial_output/verification/teaching_review/final_rebuild/calculation` generated expectations for 12 tutorials, 13 scenarios, and 254 formula comparisons, plus eight synthetic direction checks. `devel/validate_libreoffice.py tutorial_data/*.md -e tutorial_output/verification/teaching_review/final_rebuild/calculation/tutorial_expectations.json -o tutorial_output/verification/teaching_review/final_rebuild/calculation/calc` ran LibreOffice Calc outside the sandbox. Calc passed all 13 scenarios and 254 comparisons. The final run is `tutorial_output/verification/teaching_review/final_rebuild/calculation/calc/run-wgdwbqqd/report.json`; all 12 source hashes match the current Markdown sources. The refreshed artifact manifest records current source hashes, artifact hashes, byte sizes, and page counts.

Repeated exports of the Babies 3 DOCX produced the same text layout, normalized font set, and all four page pixel hashes. This confirms the earlier pagination variation from resolving different Carlito font files is no longer present in repeated exports.

## Repository checks

The full repository suite passed: 1,464 tests. Pyflakes passed for the four changed DOCX implementation and test files, and `git diff --check` passed. The accepted final typography recheck covers all 12 current DOCX files and all 70 PDF pages; see [teaching_typography_spec_recheck.md](teaching_typography_spec_recheck.md). The final integration review subsequently confirmed all 12 source hashes and 36 product hashes against the manifest and passed the full 1,474-test suite; see [teaching_integration_review.md](teaching_integration_review.md). This report does not claim classroom approval or student success. Offline checks do not validate Google Docs/Sheets import, live Google Sheets calculation, link navigation, or student learning.
