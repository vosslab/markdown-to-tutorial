# Teaching quality review summary

## Current state

All 12 lesson sources have been compared with their originals and generated materials. First-pass
corrections and the later Babies 1, Babies 3, and PETase edits are in the completed content build.
The pre-style content build recorded 36 artifacts across 68 PDF pages, 254 Calc comparisons across
13 scenarios, and 1,458 passing tests. The final style-integrated rebuild contains 36 artifacts across
70 PDF pages; all 12 source hashes match the bundle and Calc reports. Calc again passed all 254
comparisons across 13 scenarios, and the full suite passed 1,464 tests. Repeated Babies 3 exports
have matching text layout, normalized fonts, and all four page pixel hashes. The fresh typography SPEC
review accepted the current DOCX/PDF outputs. A further independent style-quality review found no
blocker after checking 48 source/artifact hashes, four native workbook/DOCX pairs, and 11 critical
pages. The final integration audit matched all 12 source hashes and 36 artifact hashes against the
manifest; the complete suite passed 1,474 tests. The README embeds two current Caffeine 3 images; their
capture settings and product hashes are recorded in [the screenshot receipt](../../screenshots/README.md).
These expert inspections do not establish student success or comparative teaching efficacy.

The font-resolution fix maps generated DOCX to Google Docs' Normal text, Title, Subtitle, and Heading
1-3 styles with PT Sans, PT Sans Narrow, and Roboto Mono. It clears inherited theme font selectors;
direct formatting preserves emphasis and monospaced roles. Menu paths render in bold Roboto Mono with
ASCII ` > ` separators. The Label/instruction pairing fix is included. Fresh review found all 70 PDF
pages visually clean. Repeated Babies 3 exports now have matching layout and pixel hashes, and the
full suite passes after the style changes. The [fresh typography SPEC recheck](teaching_typography_spec_recheck.md)
accepted the current 12 DOCX/PDF bundles, including the six paragraph styles, 4,911 ordinary runs
with style inheritance, 70 narrow table runs, and 677 monospaced runs. The earlier
[typography review](teaching_final_typography_spec.md) documents the superseded pre-fix snapshot.
PT Sans lacks
some Greek alpha/beta glyphs, so LibreOffice embeds Helvetica in PDFs for those glyphs only; no DOCX
style uses Helvetica. PDF builds require the selected fonts installed locally; setup does not install
fonts or download fallbacks. XLSX font styling is unchanged.

## Changes with teaching impact

- Babies keeps each lesson's story while moving hypothesis choices before result inspection. Babies 1
  now makes clear that its higher sample mean does not overcome the nonsignificant test result.
- Microbes restores student/advisor transitions, concise recaps, and missing images while clarifying
  known versus estimated SD, Welch assumptions, F-test scope, and ANOVA interpretation. The 24
  locations in Microbes 3 recur across years, but the source does not establish paired measurements;
  its Welch exercise remains hypothetical, and paired analysis may be appropriate if linked.
- Caffeine is now three standalone lessons, each starting at Part 1. Focused additions support
  formula entry, recovery, result checks, interpretation, chart reopening, and submission. Four
  misleading legacy visuals (caffeine04, caffeine06, caffeine09, caffeine13) were removed or replaced
  with plots from the actual observations; the regression recheck accepted the figures.
- PETase restores the new-hire task and Bradford assay explanation, labels its calibration data as
  synthetic, and tells students to use **Series > Add series**. It makes no claim about actual
  PETase abundance, activity, or fermentation productivity.
- Fill Down translates formulas with source-located diagnostics. Workbook widths and wrapping use
  authored labels and quoted formula text, including IF decisions, while leaving answers blank.
  Width and height remain estimates, not font measurements or calculated formula results.

## Evidence and limits

The [review ledger](../teaching_quality_review.md) links group audits and fix reports. Final
integration acceptance and suite evidence are recorded in
[teaching_integration_review.md](teaching_integration_review.md). The
[final rebuild report](teaching_final_rebuild.md) supersedes the initial artifact inventory. The
[Caffeine figure report](teaching_caffeine_figures_fix.md), [regression recheck](teaching_regression_spec_recheck.md),
[established HCI review](teaching_established_hci_quality.md), [regression HCI review](teaching_regression_hci_quality.md),
the [typography recheck](teaching_typography_spec_recheck.md), and the
[final style-quality review](teaching_final_style_quality.md) record the latest visual and walkthrough evidence.

These were expert inspections and cognitive walkthroughs without student participants. They are not
an accessibility conformance claim or evidence of classroom learning. Google Sheets import and live
behavior remain unverified. PETase data remain synthetic.
