# Final teaching typography SPEC review

Review date: 2026-10-22

## Snapshot and result

I visually reviewed all 70 pages in the 12 rebuilt PDF bundles and inspected the corresponding DOCX paragraph styles and run properties. This is the snapshot built after the six standard paragraph styles and role formatting were added, but before the subsequent ordinary-run font-inheritance correction. All 12 PDFs pass the visual review. The DOCX files in this snapshot have one specification defect: every ordinary prose and heading run writes PT Sans directly, overriding the standard paragraph style's font inheritance. The renderer source has since been corrected and the final bundle rebuild is in progress; that new artifact set still requires a fresh independent review.

Rendered pages with Poppler at 100 dpi, converted each page to WebP at quality 90, and inspected 12 per-lesson contact sheets plus the critical pages at full resolution. Fresh PDF text extracts, source/DOCX/PDF SHA-256 values, and the DOCX style audit are retained under `tutorial_output/verification/teaching_review/final_typography_spec_pre_editability_fix/`:

- Per-page images: `pages/` (70 WebP files).
- Contact sheets: `contact/` (12 WebP files).
- PDF text: `text/` (12 text files).
- Exact source, DOCX, and PDF hashes: `artifact_hashes.json`.
- Paragraph styles, direct font runs, table font roles, and hyperlink relationship counts: `docx_style_audit.json`.

## Per-lesson visual results

| Lesson | Pages | Result |
| --- | ---: | --- |
| `babies_1_z_test` | 7 | Accept. Figures and formulas fit. The final illustration, caption, and closing story read together on page 7. |
| `babies_2_t_test` | 7 | Accept. Tables, formulas, decision sequence, and closing interpretation are legible and coherent. |
| `babies_3_two_sample_t_test` | 4 | Accept. Page 4 keeps Step 8, Label F8, and Instruction G8 together; the closing interpretation and reference are coherent. Open space below is harmless. |
| `caffeine_1_descriptive_statistics` | 3 | Accept. Part 1 contains Steps 1-5. Step 1 continues from page 1 to page 2 with its setup context intact; formulas and the final task are legible. |
| `caffeine_2_linear_regression` | 8 | Accept. Part 1 contains Steps 1-7. Page 7 keeps Label G2 and Enter H2 together; formulas and both figures fit without clipping. |
| `caffeine_3_quadratic_regression` | 7 | Accept. Part 1 contains Steps 1-7. Page 5 keeps Label H5 and Enter I5 together; both actual-data plots and their labels are clear on page 6. |
| `microbes_1_z_test` | 5 | Accept. Tail graphic, formulas, decision, and interpretation are complete and legible. |
| `microbes_2_t_test` | 5 | Accept. The test-choice sequence, formulas, decisions, and interpretation remain coherent across page breaks. |
| `microbes_3_two_sample_t_test` | 7 | Accept. Page 4's six-column Welch table and adjacent distribution figure are fully visible; wrapped table headers remain legible. Long formulas on page 5 fit their text blocks. |
| `microbes_4_f_test` | 5 | Accept. Tail formulas and decision sections fit without clipping. |
| `microbes_5_anova` | 6 | Accept. The table-building instructions, calculations, decision, and interpretation are readable. |
| `petase_1_linear_regression` | 6 | Accept. Page 3 keeps Label F3 and Enter G3 together. Calibration and residual figures, table text, and formulas are legible. |

Across the complete set I found no clipped formula, image, figure label, or table text; no broken glyphs; and no page transition that lost its instructional context. Some pages have open lower space, including Babies 3 page 4 and several lesson openings or closings. Their content remains coherent, so I did not recommend layout changes for whitespace alone.

## DOCX contract checks

The 12 DOCX files in this snapshot use only the six permitted paragraph styles: `Normal`, `Title`, `Subtitle`, `Heading 1`, `Heading 2`, and `Heading 3`. The authored Part, Step, and Substep labels match the PDF numbering; Parts use Heading 1, Steps use Heading 2, and Substeps use Heading 3. All six standard styles carry PT Sans. The PDF output also shows the expected standalone Caffeine numbering: Part 1 with Steps 1-5, 1-7, and 1-7 respectively.

The role-specific formatting is serialized and visible: all 70 table text runs use PT Sans Narrow, all 677 code, cell-reference, and menu runs use Roboto Mono, and 13 hyperlink relationships remain in the DOCX set. Hyperlinks appear underlined and blue in the PDFs; cell and menu emphasis remains bold and monospaced.

However, each ordinary prose/title/heading run also has a direct `w:rFonts` value of PT Sans: 3,315 of 3,315 examined ordinary runs across the 12 files. The standard paragraph styles already specify PT Sans, so these direct run overrides are redundant and prevent a destination editor from applying its paragraph-style font to that text. For example, the Babies 1 title, Part 1, and Step 1 all serialize a direct PT Sans run font as well as their paragraph style font. This is an editability contract failure in these artifacts, not a visual PDF defect. The renderer source has been changed to inherit ordinary text fonts and to emit the chart menu separator as ASCII `>`; the post-change DOCX/PDF artifacts have not yet been reviewed here.

## Limits and handoff

This review covers PDF rendering and serialized DOCX structure for the pre-correction artifact snapshot. It does not establish Google Docs import or live behavior, student usability, or learning outcomes. No tests, LibreOffice commands, workbook walkthroughs, or product edits were performed for this review. The final style-inheritance rebuild needs fresh visual and DOCX metadata review before integration acceptance.
