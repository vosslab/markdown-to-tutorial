# Instructional voice restoration review ledger

Updated 2026-10-22. This ledger gathers the evidence for restoring the original teaching voice in
all 12 tutorial sources. Independent source, specification, and final material reviews accept the
current work. The final integration review records repository checks and fingerprint verification.

## What changed for students

The sources now restore original narrative, headings, humor, and numbered action groups while
keeping spreadsheet actions attached to authored words. For example, the original Caffeine 3
instruction, “To let our regression model curve, we need to square our predictor variable (x).”
This again leads into the squared-column task and its four compact actions. The visible lesson no longer
turns that sequence into repeated `Label` and `Enter` entries. The original-source maps and
corrections are in the [Babies](voice_babies_original_comparison.md),
[Caffeine](voice_caffeine_original_comparison.md), and
[Microbes and PETase](voice_microbes_petase_original_comparison.md) comparisons.

Babies restores its playful committee stories and nested numbered instructions; for instance,
Babies 2 again includes “^ this is our representative mean baby weight of the population.” The
technical correction remains: a small sample alone does not invalidate a z-test, and the t-test
right-tail calculation handles a negative statistic. Microbes restores the advisor conversations,
method-specific “Why Use ... Now?” explanations, and the 30-year transition. It retains the needed
limits: repeated sites do not establish independent samples, variance does not establish community
homogenization, and a test does not establish cause or trend. PETase restores its startup and
plastic-waste narrative while keeping the data synthetic and the Bradford measurement limited to
total protein; it cannot identify PETase abundance or activity by itself. Caffeine's prior useful
prose remains in place while missing lesson instruction was added. The lesson-level changes are
recorded in the [Babies recovery](voice_babies_recovery.md),
[Caffeine](voice_caffeine_restoration.md),
[Microbes 1-3 recovery](voice_microbes_early_recovery.md),
[Microbes 4-5 recovery](voice_microbes_late_recovery.md), and
[PETase recovery](voice_petase_recovery.md) reports. Initial restoration reports are historical;
their completion claims were superseded by these recovery maps and independent source reviews.

Semantic links now carry action meaning on existing words, such as
`In F2, enter [=AVERAGE(C2:C3)](enter:F2).` The workbook's hidden region declarations describe
source, calculation, result, and interpretation areas, so seeded data stay distinct from blank
student work. A bare formula such as `=SUM(A1:A3)` receives formula styling only; its color does not
assign a cell action or destination. Original PDFs were available for the Babies comparison. The
Caffeine and Microbes/PETase source checks use the original Markdown sources because original PDFs
were not available. The [core contract review](voice_core_quality.md) and
[final 177-check specification review](voice_last_rendering_spec.md) cover the renderer behavior.

## Evidence ledger

| Area | Current evidence | Status and boundary |
| --- | --- | --- |
| Source fidelity | All 12 source lessons were restored. The [Babies source-spec recheck](voice_babies_source_recheck.md) is accepted; the [Caffeine source review](voice_caffeine_source_spec.md) passes; the [Microbes and PETase source review](voice_microbes_petase_source_spec.md) passes after fixing the quoted `0.05` period in Microbes 1. | Source review is not final rendered-output acceptance. |
| Core authoring/rendering | [Core quality](voice_core_quality.md) and [final rendering SPEC](voice_last_rendering_spec.md) accept the implementation; the final focused run passed 177 checks. | These checks establish the contract only, not final lesson layout. |
| Build and calculation | The final post-fix build contains 12 DOCX/XLSX/PDF bundles and 92 PDF pages. Calc passed all 13 scenarios / 254 comparisons against unchanged expectations. The [final-build receipt](voice_restoration_final_build.md) preserves commands, diagnostics, and 60 source/artifact hashes; [validation](voice_final_validation.md) records the builder's 1,545-test suite. | Integration independently matched all 60 hashes and 92 pages. Calc is local LibreOffice evidence, not Google Sheets evidence. |
| Final material quality | [Fresh material review](voice_final_material_recheck.md) accepts all 12 bundles, with contact inspection of all 92 PDF pages and 21 full-size pages. | All prior concrete findings are closed. Original comparisons and source reviews remain separate evidence; the final pass did not repeat every original comparison. |
| Caffeine layout | Final pages name E2/E3/E4, preserve internal native breaks, and keep the compact four-action squared-column task and complete 36-hours aside together. | No terminal blank list lines or literal backslashes remain. |
| Babies layout | Final pages display alpha and italic decision labels correctly. Babies 2 p5 keeps D13, the E13 instruction, and its first formula together. | The prior literal entity/asterisk and detached-group findings are closed. |
| Microbes layout | Microbes 2 p9 holds the transition and closing link together; Microbes 1 visibly enters numeric 0.05; Microbes 5 G1:G25 is blank. | The short closing page is readable and contains its transition, rather than only a link. |
| Student workbook regions | All 12 final workbook cell values/types/styles and widths match previously rendered layouts, except the intended Microbes 5 G1 blank correction. Fresh Caffeine 3 and Microbes 5 renders confirm actual workbook regions; no student formulas are pre-entered. | Local inspection accepted. No Google import or live Google calculation was observed. |
| Managed previews | Both WebPs were refreshed from final Caffeine 3 PDF/XLSX and visually inspected. The [screenshot receipt](../../screenshots/README.md) records page 4 of 7, capture methods, and current hashes. | Integration matched all five source/product/screenshot receipt hashes. |
| Learning outcomes | Reviews are expert source, document, and workbook walkthroughs. | No student study was performed; no learner outcome is claimed. |

Prior build and quality reports are dated snapshots. The final-build receipt now describes the
post-fix 92-page build; the fresh review closes the earlier material reports' concrete findings.
Historical comparison image/log artifacts may live under ignored `tutorial_output/`; linked durable
proof is limited to files in the repository.

## Integration and limits

The [final integration review](voice_final_integration.md) accepts all five milestones and records
**1,548 repository tests passed**, 60 matching source/artifact hashes, and five matching screenshot
receipt hashes. The [five-milestone plan](../instructional_voice_restoration.md) remains at its stable
referenced location with its completion ledger. Historical comparison images and machine logs under
ignored output are local evidence; durable reports name those paths without promising committed files.

Google Docs/Sheets import and live calculation remain unverified. No student study was performed,
and no measured learning outcome is claimed. Original PDFs were available only for Babies; original
Markdown and the Caffeine outline/workbook provide the other source comparisons. Local Calc evidence
checks final-state formulas rather than every intermediate student workbook state.
