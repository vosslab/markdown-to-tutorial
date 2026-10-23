# Microbes 4/5 and PETase material quality

## Verdict

The restored lessons are coherent and usable as student-facing tutorials, with one small but direct
workbook mismatch to correct before acceptance: Microbes 5 says to leave column G blank, while the
generated workbook contains a period in `G1`. Remove that character from the seed worksheet or label
it explicitly as a spacer. Regenerate the bundle after the correction.

This is a document and workbook inspection, not a student study or live Google Sheets test. I read
the read-only Markdown originals in `2025_Artifacts/`; no original PDF was available or used. I
reviewed every page of the current generated PDFs and the actual generated XLSX files. The source
hashes and artifact hashes in each bundle's `validation.json` match the current Markdown source and
generated PDF, DOCX, and XLSX.

## Teaching sequence and source comparison

- **Microbes 4:** The opening page keeps the original T-test-to-F-test Busse Woods story, the
  advisor's suggestion, the T-test versus F-test figure, and the "Why Use an F-Test Now?" bridge.
  The procedure then moves from the observation table through sample statistics, F, both-tail and
  directional p-values, decisions, interpretation, practice, and takeaways. The PDF continues the
  original thesis-to-ANOVA transition on pages 9-10. The added independence and normality caveats
  are adjacent to the variance question and do not displace the original narrative or calculation
  sequence.
- **Microbes 5:** The opening ANOVA figure and Busse Woods transition lead into the original
  "Why Use ANOVA Now?" rationale. The tutorial proceeds through table setup, group statistics,
  grand mean, degrees of freedom, sums of squares, mean squares, F, right-tail p-value, decision,
  interpretation, and practice. The older-thesis context remains in the closing transition. The
  current wording correctly limits the omnibus result to whether at least one population mean
  differs and preserves the method-confounding caveat.
- **PETase:** The original packaging and polymer illustrations, startup scenario, engineered-yeast
  story, Bradford explanation, and "Why Use Linear Regression Now?" bridge are present. The new
  workbook sequence coherently shifts to synthetic calibration data: blank correction, scatterplot,
  regression, residuals, interpolation check, dilution correction, recovered protein, and limits
  on biological claims. The old copied Microbes t-test exercise is absent. The page 3 explanation
  and page 4 synthetic-data notice distinguish assay concepts from actual laboratory measurements.

The restored explanations and examples retain the original step/explanation grouping. The
scientific qualifications are placed beside the claims they narrow. The illustrative figures are
sharp, legible, and appear with the related scenario or method. No clipped text, overlap, missing
glyphs, or broken table borders appeared in the inspected pages.

## Student task and workbook check

Each workbook has one worksheet, preserves the supplied observations, and leaves student-answer
cells empty. The visible blue source areas, teal calculation areas, orange result areas, and purple
interpretation areas separate the work. The lesson headings and exact cell references identify the
purpose of each field; color is not the only instruction.

| Lesson | Seeded data and blank work areas | Task-path check |
| --- | --- | --- |
| Microbes 4 | `Two Sample F-Test`; locations and the two year columns occupy `A2:C25`. The labels and answer cells, including `D5:E11`, `D16:G18`, `D20:E20`, `D22:E24`, and `D26:E26`, are blank for students to enter. | Written formula destinations match the sheet: `STDEV` and `COUNT` use `B2:B101`/`C2:C101`, F is entered in `E11`, p-values in `E16:G18`, and decision/interpretation cells are identified. The 24 observed rows and blank extension rows are consistent with the range instructions. |
| Microbes 5 | `30 Year ANOVA Test`; data are in `A2:F25`, with unequal group counts and blank cells rather than zeroes where older-year observations are absent. The ANOVA table `H1:M4`, summary cells `H6:M9`, grand mean `H11:I11`, decision `H13:I14`, and interpretation `H16:I16` are empty. | The table and group-statistic instructions point to the right cells. The stated formulas for means, sample variances, counts, grand mean, sums of squares, F, and right-tail p-value match the sheet layout. `G1` contains `.` despite the instruction that column G remain blank; this is the required correction above. |
| PETase | `Bradford illustrative`; seven standards are in `A2:B8`, the three sample records in `A13:D15`, and calculated/interpretation regions remain blank, including `C2:C8`, `F2:G4`, `I2:J8`, `E13:G15`, and `I12:J13`. | Blank subtraction, fitted values/residuals, and sample formulas reference the supplied blank, standards, dilution factors, and volumes. The reported expected calibration and concentrations in the lesson agree with the synthetic dataset's intended calculations. The task compares original-preparation concentration separately from recovered total protein and warns against treating total protein as PETase-specific yield. |

The rendered XLSX views are inspection copies with only print setup changed. They were exported using
`/Users/vosslab/nsh/vosslab-skills/skills/documentation/screenshot-docs/scripts/render_artifact_libreoffice.sh`
outside the sandbox. These Calc renders confirm visible formatting and blank answer fields; they do
not establish Google Sheets import or behavior.

The colors have no visible legend, but they act as secondary grouping cues: each working area also
has a text heading and explicit cell instructions, so students do not need to infer what to enter
from color alone. I independently evaluated representative calculations from the seeded values:
Microbes 4 gives sample variances of about 1.9202 (2014) and 0.8116 (2024), and `F = 0.42265`
for 2024/2014; Microbes 5 has group sizes 10, 15, 20, 24, and 24, with `F = 0.87893`; PETase gives
slope `0.798286`, intercept `0.000214`, `R^2 = 0.999941`, and dilution-corrected concentrations
about 1.50, 5.03, and 2.00 mg/mL. These checks use the displayed values and formulas directly; they
are not spreadsheet-engine or Google Sheets validation.

## Page evidence and final rebuild targets

The PDF contact sheets cover all pages: Microbes 4 has 10 pages, Microbes 5 has 9, and PETase has 6.
Full-page views include the opening stories, Microbes 4's tail procedures and decision table,
Microbes 5's ANOVA table and inference, and PETase's calibration and sample workflow. Inspected
WebP evidence is stored under
`tutorial_output/voice_restoration/quality_microbes_late_petase/`.

The current PDFs were built from source hashes matching the present Markdown. The shared pagination
and quoted-label changes are still being finalized, so the final rebuild should recheck Microbes 4
pages 1-2 and 6-8, Microbes 5 pages 3-4, and PETase pages 4-6. In the inspected build, Microbes 4's
main-alternative sentence continues across pages 1-2 and its final decision entries continue across
pages 7-8. Those are recheck targets for the active pagination work, not separate findings in this
review.

The page contact sheets, inspected full-page PDF views, and workbook screenshots are stored in the
ignored directory `tutorial_output/voice_restoration/quality_microbes_late_petase/`. The PETase
workbook screenshot includes column J so the residual and interpretation regions remain in view.
