# Final material quality recheck

Date: 2026-10-22. Decision: **ACCEPT** the final 12 canonical student bundles and the refreshed
README screenshots for this document/workbook inspection scope. Every previously reported material
finding is closed in the actual final outputs. No new material regression was found.

## Method and provenance

This was an expert cognitive walkthrough and visual review using `hic-human-interact-expert`,
`pdf-guide`, and `screenshot-docs`. The learner task is to read each lesson, recognize its next
action, find the named worksheet/cell, distinguish test branches, calculate, and write an
interpretation. The checks assessed whether visible instructions and grouping support that task.
No students participated and no learning or measured usability outcome is claimed.

I waited for the release-candidate builder to publish all 12 final bundles, then rendered the current
canonical PDFs independently with PyMuPDF. Contact sheets cover **all 92 final pages**; I inspected
21 full-size pages around former findings, action/formula groups, and changed endings. All named
review images are WebP quality 90. The evidence directory is ignored generated output:
`tutorial_output/voice_restoration/final_material_recheck/`.

The separate [voice_restoration_final_build.md](voice_restoration_final_build.md) contains the full
60-entry source/artifact hash receipt and build/calculation evidence. I independently matched all
12 source hashes and 48 DOCX/PDF/XLSX/validation hashes to the actual files and its machine manifest
at `tutorial_output/voice_restoration/final_build/manifest.json` (SHA-256
`4162f55fe5e19843fd5222686024da1df4bec675c07a3827938aafa2823ff9cb`). Page counts match exactly.
The reviewer snapshot is `reviewed_manifest.json` inside the evidence directory. Canonical hashes
were rechecked after screenshot capture; disposable spreadsheet renders did not alter the bundles.

This pass closes findings from the prior direct original-to-material comparisons. Those completed
reviews remain the source-fidelity evidence: [voice_babies_material_quality.md](voice_babies_material_quality.md),
[voice_caffeine_material_quality.md](voice_caffeine_material_quality.md),
[voice_microbes_early_material_quality.md](voice_microbes_early_material_quality.md), and
[voice_microbes_late_petase_material_quality.md](voice_microbes_late_petase_material_quality.md).
Their earlier CHANGES NEEDED verdicts describe older artifacts. I did not repeat every original
comparison here. Original PDF comparison exists for Babies; the Microbes/PETase comparisons used
original Markdown, and Caffeine used its original outline/workbook. No original Microbes/PETase PDF
comparison is claimed.

## Findings closed in final student materials

| Finding | Actual final evidence and disposition |
| --- | --- |
| Babies label entity/emphasis leak | Babies 1 p4, Babies 2 p5, and Babies 3 p4 display Greek alpha. Babies 1/2 decision labels are italic and retain their authored quotes/punctuation. No `&alpha;` or literal emphasis markers remain in these label instructions. The native DOCX text checks also pass for all three. Closed. |
| Babies 2 detached D13/E13 right-tail group | Its p5 starts with the one-tailed branch, D13 label, E13 instruction, and first nested green formula together. The two-tail branch remains readable on p4. No label or first formula is stranded across that boundary. Closed. |
| Caffeine literal hard-break backslashes | No backslash appears in any final Caffeine PDF's extracted text. Full-size chart actions (lesson 2 p4), hypotheses/statistics (p8), p-value/decision/reflection (p9), and the squared task (lesson 3 p4) show clean native breaks. Closed. |
| Caffeine 1 missing sleep-statistic cells | Full-size pp2-3 explicitly name E2 with AVERAGE, E3 with MEDIAN, and E4 with STDEV.S. Paired exam destinations F2:F4 remain visible. Closed. |
| Extra empty lines in Caffeine 3's squared-column group | Final p4 is a compact, consecutive four-item task. The heading, introduction, label, green `=A2^2`, fill action, and complete 36-hours joke remain together. No action-label log, empty list lines, or literal slashes interrupt it. The original outline's blue-square instruction and humorous aside remain recognizable. Closed. |
| Microbes 2 isolated closing link | Final p9 now holds the transition heading, complete two-sample introduction, and next-tutorial link together. It is a short final page, but no longer a page containing only the link. Closed. |
| Microbes 1 numeric alpha | Full-size p6 visibly instructs `In cell D14, enter 0.05.`. The decimal and punctuation are distinct; the source's numeric binding is accepted by the final specification/build checks. Closed. |
| Microbes 5 G1 period in blank separator | The actual final XLSX has `None` throughout G1:G25. A fresh LibreOffice render shows the blank G separator beside observations and the ANOVA work area, without the former period. Closed. |

The final materials preserve the restored narrative experience: Babies' hospital/award stories and
closing scenes, Caffeine's questions, asides, and four-action teaching group, Microbes' Busse Woods
scenario and successive method transitions, and PETase's fictional startup/yeast context and Bradford
explanation remain visibly present. Formula destinations and scientific qualifications accompany
these passages. PETase continues to distinguish illustrative total-protein estimation from PETase
abundance/activity; the synthetic-data qualification is visible before the practical workflow.

## Coverage and page counts

| Final canonical tutorial | PDF pages | Reviewed PDF SHA-256 |
| --- | ---: | --- |
| `babies_1_z_test` | 6 | `3e4f472da08a2312f1524e9bbb1d66a3a539d0041a498962538d24fa5210acc4` |
| `babies_2_t_test` | 6 | `161f234197910d866530b55d1ab77bf41665bc5584c825ffaa5324f9f4404b53` |
| `babies_3_two_sample_t_test` | 5 | `bec039792173033bda66c9395b280b21ed38b265b047220c7f9293d43907c20f` |
| `caffeine_1_descriptive_statistics` | 3 | `b5284f2a26f3ff3cc8c18816931be6824c89555b30787ea1541317f62c4f3096` |
| `caffeine_2_linear_regression` | 10 | `f19af82f62f4ee9f2b1c4cae5515ba8ebc6b597d0acad9085121bacec2d21c4c` |
| `caffeine_3_quadratic_regression` | 7 | `2e076c3743bec887f16278322a5079b38a6c1bfb1bc312ef5cb817abda6d3fab` |
| `microbes_1_z_test` | 9 | `6e301211fcf5c8d07c9846e47340ccc7b3ec7ec1cac88d0a3fd9df6d546e250f` |
| `microbes_2_t_test` | 9 | `c207bcb850871022d9960e7bd8031ca79743cb2ce053d28e33ea6f17b675ed5e` |
| `microbes_3_two_sample_t_test` | 12 | `3499531ea4154667b605743d02bc8d2c1afb72e45c4c34514288a2125dceeeb5` |
| `microbes_4_f_test` | 10 | `2e9447634ece3ecba80536adf2b2de1a1336b91e7f665a124f3ba9b53f3eccd0` |
| `microbes_5_anova` | 9 | `158752c5ce6bf1a870bb932a84a30ae897c90dfa906267b1f1c84a143a001597` |
| `petase_1_linear_regression` | 6 | `5002470fd54cda0e2d0ec68f8548aff8ca4bb76dfa5816c8e593b6d3f84fb177` |

All-page contact inspection checked each opening, figure/table placement, heading progression,
continuation, and ending. Full-size inspection covered Babies 1 pp4/6; Babies 2 pp4/5/6;
Babies 3 p4; Caffeine 1 pp2/3; Caffeine 2 pp4/8/9; Caffeine 3 pp4/7; Microbes 1 p6;
Microbes 2 p9; Microbes 3 p7; Microbes 4 pp7/8; Microbes 5 p3; and PETase pp5/6.
The restored formula explanations and nested list groupings are readable. The final contact pass
found no clipping, overlapping content, broken figures, or newly isolated first-action groups.
Some long explanations continue between pages, and some final pages remain short; these are readable
continuations rather than lost content or the reported detached-action defects.

## Workbook and screenshot evidence

I opened all 12 final XLSX files and compared every cell's value, type, and style plus column widths
against the disposable workbooks used for the earlier material reviews. Eleven match exactly. The
only difference in Microbes 5 is G1 changing from `.` to blank, with its style unchanged. Thus prior
actual workbook renders remain applicable to the unchanged layouts. The comparison receipt is
`workbook_semantic_comparison.json` in the evidence directory. All canonical workbooks retain the
seeded observations and contain no pre-entered student formulas.

Fresh Caffeine 3 and Microbes 5 workbook views were exported using the provided screenshot skill
`render_artifact_libreoffice.sh`, outside the sandbox through the repository bootstrap. Copies
changed only print settings: selected area, A3 landscape fit-to-page, margins, gridlines, and row/
column headings. No answers, labels, formulas, styles, widths, or observations were inserted.
The actual full Caffeine sheet shows blue source data, teal calculation/predictor workspaces, orange
result areas, and purple written responses. The 75 cells in C2:C26 and E2:F26 remain blank.

The two managed README assets were refreshed from these final files at quality 90 and inspected:
[the compact four-item instruction excerpt](../../screenshots/caffeine_3_fill_down_instructions.webp)
(1028 x 330) and the blank predictor workspace (1237 x 910, subsequently removed from the showcase
because its unlabeled areas did not demonstrate a useful starting worksheet).
The complete four-item excerpt is uncropped. Capture parameters, byte sizes, current
source/PDF/XLSX hashes, and final WebP hashes are recorded in
[docs/screenshots/README.md](../../screenshots/README.md). Caffeine 3 is **7 pages** in this final
build; the older eight-page capture receipt has been replaced.

## Limits

This accepts actual local document rendering, workbook layout, and expert task coherence. The
independent final build/calculation lane supplies test and LibreOffice formula-execution evidence;
those tests alone were not used as a visual-quality oracle. This pass does not establish Google
Docs/Sheets import fidelity, live Google calculation, intermediate workbook-state behavior, student
comprehension, or classroom learning. Existing compiler diagnostics and their limits remain explicit
in the final build receipt; no new broad test or infrastructure was added in this lane.
