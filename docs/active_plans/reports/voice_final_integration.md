# Final instructional voice integration

Date: 2026-10-22. Decision: **ACCEPT**. All five milestones are complete: the current source,
specification, material-quality, fingerprint, and repository checks pass. No integration blocker
remains in this local completion scope.

## Scope and decision basis

This fresh integration audit follows the approved five-milestone
[restoration plan](../instructional_voice_restoration.md). It reviews the final contract, source
recovery evidence, current generated products, screenshots, and documentation. It does not treat
earlier failed restoration claims or a passing suite as evidence of original-voice fidelity.

The current source evidence is the [Babies independent recheck](voice_babies_source_recheck.md),
[Caffeine source review](voice_caffeine_source_spec.md), and
[Microbes and PETase source review](voice_microbes_petase_source_spec.md), with the last numeric alpha
and blank spacer corrections accepted in the [final rendering SPEC](voice_last_rendering_spec.md).
Recovery maps are [Babies](voice_babies_recovery.md),
[Microbes 1-3](voice_microbes_early_recovery.md),
[Microbes 4-5](voice_microbes_late_recovery.md), and [PETase](voice_petase_recovery.md).
The [Caffeine restoration map](voice_caffeine_restoration.md) documents retained draft prose and
added missing instruction. Initial failed restoration reports remain historical.

The [fresh final material review](voice_final_material_recheck.md) accepts the exact final bundles:
all 92 PDF pages inspected as contacts, 21 full-size pages, all 12 native workbook layouts checked
against previously rendered cells/types/styles/widths, plus fresh Caffeine 3 and Microbes 5 workbook
renders. It closes every previous concrete material finding. It builds on the original comparisons
and earlier full lesson walkthroughs rather than claiming every original comparison was repeated.

## Architecture and visible instruction

Read the actual binding/compiler and DOCX/workbook paths. Bindings create ordered action records
from existing inline text; DOCX renders the authored child tokens and suppresses semantic URI
navigation. Formula checks derive from actions rather than a second formula inventory. Closed
workbook roles style existing cells and student-entry regions without pre-entering answers. Local
same-row/adjacent-entry pagination and final-paragraph keeping address the observed page splits;
terminal list breaks are removed from copied tokens while internal breaks remain.

This respects KISS and Fix the design, not the symptom: meaning is independent of presentation,
and there is no heuristic prose rewrite, lesson-specific pagination table, new theme system, or
hidden duplicate formula source. Core quality and the final 177-check SPEC review independently
accept those boundaries. All seven final SPEC code/source fingerprints still match current files.

The final Caffeine preview visibly retains the exact sentence "To let our regression model curve,
we need to square our predictor variable (x)." and its four numbered actions, green formula, and
complete 36-hours joke. Integration visually inspected both refreshed managed WebPs. Workbook
source observations are blue and blank predictor regions are teal; no answers are supplied.

The documentation now names D5/E5 visibly in its semantic-label/formula example and explains that
hidden destinations do not guide the learner. It distinguishes Markdown-decoded label links from
legacy Label payloads and JSON Enter/Replace scalars. The README example itself remains unchanged;
only its stale "remaining artifact review" phrase now says "final artifact review".

## Exact final files

Using `source source_me.sh && python3` for independent read-only Python checks:

- Recomputed SHA-256 for all **12 canonical sources, 36 DOCX/XLSX/PDF products, and 12 validation
  JSON files**: all **60 match** the final build manifest. Parsed all PDFs independently with
  `pypdf`: all per-lesson counts match, totaling **92 pages**.
- Matched all **seven** source/code hashes in the final rendering SPEC and all **five**
  source/product/screenshot hashes in the current screenshot receipt. No mismatch was found.
- Inspected native DOCX XML for all 12 lessons: paragraph references remain within the approved
  six-style contract. The files use Title/Heading 1-3 explicitly and Normal implicitly; Subtitle
  remains available for optional metadata. Normal plus direct fonts are PT Sans, PT Sans Narrow,
  and Roboto Mono. No semantic action URI was found in visible DOCX/PDF content, and no hidden
  Workbook region declaration leaked into PDF prose.

The machine manifest is ignored generated output at
`tutorial_output/voice_restoration/final_build/manifest.json`, SHA-256
`4162f55fe5e19843fd5222686024da1df4bec675c07a3827938aafa2823ff9cb`.
The durable [build receipt](voice_restoration_final_build.md) records all 60 fingerprints and
page counts. The [screenshot receipt](../../screenshots/README.md) records final Caffeine page 4
of 7 and both image hashes. Original artifacts were not edited.

## Verification

The independent builder's [validation](voice_final_validation.md) records LibreOffice Calc
26.2.6.3 passing **13 scenarios / 254 comparisons** against unchanged expectations, and an earlier
full suite of **1,545 passed**. Build and Calc commands ran outside the sandbox using repository
scripts. Integration did not repeat LibreOffice exports or modify generated products.

Final integration runs the complete repository suite after documentation closeout:

```sh
source source_me.sh && python3 -m pytest tests/ -q
```

Result: **1,548 passed in 3.38 seconds**, exit status 0. The first integration run found two
path-like link-label violations introduced in the closing documents (1,546 passed / 2 failed).
Replacing the ambiguous slash labels with ordinary descriptive words resolved both; the complete
rerun passed. `git diff --check` also passed. No suite failure was waived as baseline.

The misplaced untracked pagination report was moved byte-for-byte to
[voice_semantic_pagination_fix.md](voice_semantic_pagination_fix.md); the empty root `reports/`
directory was removed. The completed plan stays at its established referenced path to preserve
current report links.

## Limits

This accepts local authored content, implementation, generated rendering, workbook layout, and
expert task coherence. Google Docs/Sheets import and live calculation remain unverified. No
student study or measured learning outcome is claimed. Original PDFs were available only for
Babies; other original comparisons use Markdown and the Caffeine outline/workbook. Calc checks
final-state formulas rather than every intermediate learner state. Existing compiler diagnostics
are documented in the build receipt; source fidelity does not imply byte-identical documents.
