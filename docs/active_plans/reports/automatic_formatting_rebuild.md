# Automatic formatting rebuild

All 12 current tutorial sources built successfully with the repository CLI on 2026-10-22. Builds
ran outside the sandbox because PDF export invokes LibreOffice. Per-source logs, output hashes,
byte sizes, source hashes, and baseline/new PDF page counts are recorded under
`tutorial_output/verification/automatic_formatting/rebuild/`. Every bundle's source hash matches
its current Markdown source.

| Tutorial | Baseline PDF pages | Rebuilt PDF pages |
| --- | ---: | ---: |
| babies_1_z_test | 7 | 6 |
| babies_2_t_test | 7 | 6 |
| babies_3_two_sample_t_test | 4 | 4 |
| caffeine_1_descriptive_statistics | 3 | 3 |
| caffeine_2_linear_regression | 8 | 8 |
| caffeine_3_quadratic_regression | 7 | 6 |
| microbes_1_z_test | 5 | 5 |
| microbes_2_t_test | 5 | 5 |
| microbes_3_two_sample_t_test | 7 | 7 |
| microbes_4_f_test | 5 | 5 |
| microbes_5_anova | 6 | 5 |
| petase_1_linear_regression | 6 | 5 |
| **Total** | **70** | **65** |

The rebuilt DOCX files contain formula runs in color `188038` across all 12 lessons. All 634
numbered or bulleted paragraphs have 0 pt before, 2 pt after, and single line spacing. Every
backtick-delimited formula literal found in each Markdown source remains an exact substring in its
DOCX text. These are package-content checks; this report does not make a visual approval claim.
After the literal-action preservation code change, I rebuilt DOCX-only copies for all 12 sources.
Every member in each DOCX package matched its published counterpart, so the fix did not change any
lesson output and no bundle rebuild was needed.

Independent expectations generated for 12 tutorials, 13 scenarios, 254 formula comparisons, and
eight synthetic direction checks. LibreOffice Calc passed all 13 scenarios and all 254 formula
comparisons. The expectation generator uses SciPy/NumPy models independently of authored formula
strings. After the literal-action preservation correction, the full suite collected 1,493 tests:
1,492 passed on the first run. The remaining guidance-format check was fixed by shortening the new
`docs/HUMAN_GUIDANCE.md` bullet to three physical lines. A fresh full run then passed all 1,493 tests.

Google Sheets import, live Google Sheets behavior, link navigation, and student outcomes remain
unchecked by this rebuild.
