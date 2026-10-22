# Teaching typography SPEC recheck

Review date: 2026-10-22

## Result

Accepted the rebuilt typography artifacts against the DOCX style and role-formatting contract. I
rendered and inspected all 70 pages in the 12 current PDFs at 100 dpi, including all 12 lesson contact
sheets and the critical pages at full size. No clipping, overlap, broken glyph, or disruptive page
break appeared. The PDF outputs retain the established lesson pagination and visual layout.

The fresh build manifest reports 12 bundles and 36 artifacts. All 12 Markdown source hashes and the
DOCX/PDF hashes match the manifest. The PDF page counts total 70, and every page was rendered. The
build's Calc evidence remains 13 scenarios and 254 comparisons; this recheck did not rerun Calc.
The builder also confirmed that two repeated Babies 3 exports have identical text layout, font-name
and type inventory, and four page raster hashes.

## DOCX contract

All 12 DOCX files use only the six permitted paragraph styles: `Normal`, `Title`, `Subtitle`, and
`Heading 1` through `Heading 3`. Each style is configured with PT Sans. The page footer uses
`Normal`. No custom character-style references were found. Across 4,911 ordinary text runs, zero
write a direct PT Sans run font, so body copy and headings inherit from their editable paragraph
styles.

All 70 Word table-text runs use PT Sans Narrow. The 677 directly formatted code, cell-reference,
and menu runs use Roboto Mono. Menu paths serialize and render with bold monospaced ASCII ` > `
separators. The current PDFs preserve the visible menu paths. The Caffeine lessons each begin at
Part 1; Caffeine 1 has Steps 1-5, Caffeine 2 has Steps 1-7 with substeps 3.1-3.2 and 6.1-6.4, and
Caffeine 3 has Steps 1-7.

The PDF export uses Helvetica for nine Greek alpha/beta glyphs in five PDFs. The glyphs are legible,
and the DOCX files do not directly assign Helvetica; the other active PDF text uses the selected
font roles. This export-engine glyph fallback is recorded as a limitation, not an acceptance blocker.

## Page checks

| Lesson | Pages | Full-size checks |
| --- | ---: | --- |
| `babies_1_z_test` | 7 | Closing interpretation and story on page 6 |
| `babies_2_t_test` | 7 | Tables, formulas, and decision sequence |
| `babies_3_two_sample_t_test` | 4 | Label F8 and Instruction G8 together on page 4 |
| `caffeine_1_descriptive_statistics` | 3 | Steps 1-5 and chart/table instructions |
| `caffeine_2_linear_regression` | 8 | Label G2 and Enter H2 together on page 7 |
| `caffeine_3_quadratic_regression` | 7 | Label H5 and Enter I5 together on page 5; 25-point model comparison on page 6 |
| `microbes_1_z_test` | 5 | Tail figure and formulas |
| `microbes_2_t_test` | 5 | Test-choice and p-value instructions |
| `microbes_3_two_sample_t_test` | 7 | Six-column Welch table and distribution figure on page 4 |
| `microbes_4_f_test` | 5 | Tail formulas and decision |
| `microbes_5_anova` | 6 | ANOVA table instructions and calculations |
| `petase_1_linear_regression` | 6 | Label F3 and Enter G3 together on page 3 |

The Caffeine 3 comparison shows both fitted models against the same 25 observations. Formula and
chart labels remain readable, including the quadratic model comparison and its menu path.

## Evidence and limits

Fresh page renders, 12 contact sheets, PDF text extracts, style/hash audit, and the old-to-new raster
comparison are in `tutorial_output/verification/teaching_review/final_typography_spec_recheck/`.
The audit records source and artifact hashes per lesson. All 70 fresh pages have matching baseline
dimensions; no page has more than 0.5% of pixels differ by over 32 RGB levels from the prior
quality-90 WebP render. Extracted page text matches the prior snapshot after normalizing the menu
separator.

The final build manifest and detailed font evidence are in
`tutorial_output/verification/teaching_review/final_rebuild/`. The prior review and its inspected
baseline renders are documented in [teaching_final_typography_spec.md](teaching_final_typography_spec.md).

This evidence establishes serialized DOCX style assignments and the current LibreOffice PDF
rendering. It does not establish how Google Docs imports the DOCX or how students use these lessons.
The next external checkpoint should import representative DOCX files into Google Docs and inspect
the six style mappings, role fonts, links, table text, and Greek symbols; no Google Docs import or
classroom study was performed here.
