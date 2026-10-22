# Teaching tutorial bundle rebuild

## Result

All 12 migrated sources were rebuilt into their default `tutorial_output/<tutorial>/` bundles
using `make_tutorial.py build`. Each bundle contains DOCX, XLSX, and PDF outputs. PDF export ran
outside the sandbox through the repository builder, as required for LibreOffice on this host.

The SHA-256 source hash in every bundle's `validation.json` matches the current Markdown source
and the source hash captured by the Calc validation run. All 12 generated XLSX workbooks passed
the repository's typed-seed readback check, including blank student destinations. DOCX package
verification passed for all 12 bundles. The artifact hashes and byte sizes are recorded in
[`manifest.json`](../../../tutorial_output/verification/teaching_review/rebuild/manifest.json).

| Tutorial | PDF pages |
| --- | ---: |
| `babies_1_z_test` | 7 |
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

`source source_me.sh && python3 devel/check_tutorial_calculations.py -o
tutorial_output/verification/teaching_review/calculation` generated independent SciPy/NumPy
expectations for 12 tutorials, 13 scenarios, and 254 formulas, plus eight synthetic direction
checks. The subsequent `devel/validate_libreoffice.py tutorial_data/*.md -e
tutorial_output/verification/teaching_review/calculation/tutorial_expectations.json -o
tutorial_output/verification/teaching_review/calculation/calc` run used LibreOffice Calc outside
the sandbox. All 13 scenarios and 254 comparisons passed; no formula errors or missing caches
were reported. This preserves the existing 254-formula, 13-scenario baseline.

The Calc execution report and per-scenario workbooks are under
`tutorial_output/verification/teaching_review/calculation/calc/`; independent expectation and
oracle reports are beside them. Build diagnostics still include authoring warnings about open
input ranges and formula coverage in some tutorials; those were not suppressed or treated as
calculation failures.

These checks establish source-to-artifact matching, package/seed integrity, and calculation
execution. They do not establish classroom quality or visual correctness; fresh PDF review is
still required.
