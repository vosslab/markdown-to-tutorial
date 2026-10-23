# Babies actual-material quality review

**Decision: CHANGES NEEDED** for the canonical bundles rebuilt on 2026-10-22 at
18:11. The original teaching voice, instructional sequence, figures, and restored
nested explanations survive into the generated materials. One visible markup
regression remains in all three lessons. Source acceptance alone does not close it.

## Review method and evidence

This is an independent expert cognitive walkthrough and visual review using
`hic-human-interact-expert` and `pdf-guide`, not a student study. The learner is a
BIOL 318/418 student reading the tutorial while completing the supplied blank
spreadsheet. Success means recognizing the next action, finding its worksheet and
cell, distinguishing alternative test branches, and reaching a decision and written
interpretation without needing hidden action metadata.

I directly compared all three read-only Fall 2025 Fried Foods Markdown originals,
original DOCX content and original PDFs with the actual current DOCX, PDF, and XLSX
bundles. The source-only
[voice_babies_source_recheck.md](voice_babies_source_recheck.md) establishes the
accepted source boundary; it was not used as proof of output quality. Current
materials were read directly, not inferred from validation JSON or the build report.

I inspected contact sheets covering every current PDF page (6 + 6 + 5 = 17) and
every original PDF page (6 + 5 + 4 = 15). Full-size original/current comparisons
covered the opening scenarios and artwork, z conceptual formula and sample summaries,
one-/two-tail p-value instructions and nested explanations, decisions, interpretation,
practice tasks, takeaways, and closing story. Additional full-size current pages
resolved the continuation of the one-sample t branch and the two-sample syntax group.
All named images are WebP quality 90.

Evidence directory: `tutorial_output/voice_restoration/quality_babies/`.

- `current{1,2,3}_contact.webp` and `original{1,2,3}_contact.webp`: complete page coverage.
- `currentN_pagePP.webp` and `originalN_pagePP.webp`: every page at 1.25 scale.
- `current1_page04.webp`, `current2_page05.webp`, `current3_page04.webp`: markup defect.
- `current2_page04.webp` / `current2_page05.webp`: right-tail branch pagination.
- `workbook1_print_sheet2.webp`, `workbook2_print_sheet2.webp`, `workbook3.webp`:
  actual working-sheet regions, including all designated answer cells.
- `workbook1.webp` and `workbook2.webp`: data-sheet renders.
- `workbook_structure.json`, `docx_semantics.json`, `artifact_hashes.json`, and
  `manifest.json`: cells, native document structure, reviewed artifact identities,
  and page counts.

For workbook rendering I created disposable copies changing only print settings:
A3 landscape, fit-to-page, print area, margins, printed gridlines and cell headings.
No values, formulas, widths, fills, or labels were inserted. The supplied
`screenshot-docs/scripts/render_artifact_libreoffice.sh` ran outside the sandbox
through the repository bootstrap. It exports all sheets to PDF but screenshots
only the first page; I therefore also rendered and inspected the second PDF page
for both national-comparison working sheets. Canonical XLSX and original artifacts
were not modified. All Python commands used `source source_me.sh && python3`.

## Required correction

**Render authored label markup as readable text and formatting.** The original
PDFs render the Greek alpha and italic decision labels. The current PDF and DOCX
instead expose source syntax in the very text students are told to type:

| Lesson / page | Destination | Actual visible defect |
| --- | --- | --- |
| Babies 1 / 4 | D14 | `Significance Level (&alpha;).` |
| Babies 1 / 4 | D16, D17 | `*Two-Tail Decision*.` and `*One-Tail Decision*.` |
| Babies 2 / 5 | D15 | `Significance Level (&alpha;).` |
| Babies 2 / 5 | D17, D18 | `*Two-Tail Decision*.` and `*One-Tail Decision*.` |
| Babies 3 / 4 | F6 | `Significance Level (&alpha;)` |

DOCX paragraph inspection independently confirms these exact literal strings.
This is a presentation regression from the originals, not an authorized scientific
correction. Preserve the authored paragraph and nested structure while correcting
the common inline/binding presentation path, then rebuild and inspect these actual
pages again. Check the corresponding replayed label values as well; this review
does not assume that a visible-text fix proves workbook scalar behavior.

The issue was reported to the manager immediately. No lesson source or renderer
changes were made in this lane.

## Direct original-to-generated comparison

| Lesson | Original experience retained in generated materials | Necessary technical differences |
| --- | --- | --- |
| Babies 1 z test | Hospital illustration, original definition cadence, population-versus-sample explanation, numbered cell instructions with child entries/explanations, conceptual statistic formula, p-value branch parents, normal-curve figure, nested IF explanation, both interpretation examples, practice and takeaways, butter-and-bacon celebration, committee letter and protest illustration/story. | Explicit stipulated national values and known-SD assumption, no automatic n=30 rule, explicit normal CDF arguments, right-tail direction, prespecified choice, noncausal interpretation, standalone workbook setup. The committee letter corrects the original false claim that fewer than 30 automatically invalidates z. |
| Babies 2 one-sample t | Butter Ball illustration, committee challenge and new scenario headings, both task bullets, Why Use a T-Test progression, numbered summary/statistic/df instructions, separate df explanation, nested p-value walkthrough, IF entries, interpretation/practice/takeaways, Joe's closing voice. | Correct unknown-SD rationale and assumptions, STDEV.S, signed right-tail calculation with E9/E10, explicit tail choice, corrected degrees-of-freedom explanation, and ending consistent with the actual nonsignificant result rather than awarding a statistically unsupported victory. |
| Babies 3 two-sample t | Previous/new hospital scenario paragraphs, Alex's challenge, rationale, separate sample-mean/SD/size steps, full function-syntax introduction, Range1/Range2/Tails/Type walkthrough, nested explanation groups, Important Notes, combined significance label/value instruction, decision and example interpretation. | Welch type 3, ranges through 101, signed Joe-greater IF guard with explicit explanation, prespecified alternative before summaries, independence caveat, consolidated repeated decision entry, and causal/equality limits. Joe now hopes to regain eligibility, consistent with the corrected previous ending. |

No unexplained replacement of the author's narrative or explanation sequence was
found in this artifact review. The removed historical Google-menu/template
screenshots describe the superseded combined-workbook workflow; the current setup
explicitly describes supplied standalone workbooks. The retained scenario artwork
and normal-curve illustration are visible and legible, with their original roles.

## Blank-workbook cognitive walkthrough

The action-question ledger asks at each stage: is the goal recognizable; is the
action and destination visible; is the relevant workspace findable; can completion
be recognized? These are expert inspection results, not measured student success.

| Stage | Concrete current evidence | Result |
| --- | --- | --- |
| Open and find data | The PDF names `Datas for Part 1 and 2` and `Part 1 National Z-Test` / `Part 2 National T-Test`; those exact tabs exist. The two-sample PDF names `Fried Foods vs Green Veggies`, the actual single tab. Original national data sheet and current national data both contain 24 weights; the working sheets already hold those observations, as the text explicitly states. | Pass locally; Google import and File > Make a Copy were not exercised. |
| Set benchmark | Babies 1 D2/E2 and D3/E3 map to blank teal cells; Babies 2 E2 is blank and E3 visibly says `not used`. The source explains that distinction. | Pass except leaked label text noted above. |
| Calculate summaries/statistic | Babies 1/2 D5:E9, plus D10:E10 for t, sit beside the blue data table. Babies 3 F2:H4 is a contiguous teal summary region with separately named hospital columns. Each formula instruction names its target cell; no destination must be inferred from semantic links. | Pass. |
| Select tail and calculate p | Z branches target E11/E12; t branches target E12/E13; two-sample alternatives explicitly share G5. Each has a visible test/direction description and a formula. Two-sample text says retain one chosen alternative and enter the decision once. | Pass with minor page-continuity observation below. |
| Decide | Amber regions include z E14/E16/E17, t E15/E17/E18, and two-sample G6/G7; references match the visible IF instructions. | Pass apart from markup labels. |
| Interpret | Purple response regions are E19, E20, and G8 respectively. They are blank and the PDF explicitly tells students to write there, with examples or reporting direction. | Pass. |
| Practice | Z range extends through 40; t/two-sample through 101. Existing 24-observation tables end at row 25 and blank rows can receive additions. Instructions state that blanks do not increase sample size. | Pass as an instruction/destination inspection; recalculation is the separate live replay lane. |

All canonical XLSX files contain zero formula cells. Statistical labels and answers
are blank apart from supplied headings and the intentional t-test `not used` marker.
The calculation/results/interpretation fills are visible in actual Calc exports,
not merely inferred from XML: teal `DCEFEA`, amber `FCE6CF`, purple `EAE2F5`.
The blank cells are addressed by coordinates, so the colors are helpful secondary
cues rather than the sole instruction. Original spelling `Datas` is consistently
findable. Two-sample B3 and B6 differ from the national dataset by design; the PDF
explicitly says hospital summaries come from their own columns.

## Typography and pagination

Native DOCX Heading 1/2/etc. styles are retained, with blue `203864`. Instructional
lists have native numbering properties (66, 76, and 68 numbered paragraphs).
Formula runs are green `188038`, visibly monospace and readable in the reviewed
pages. This supports the intended hierarchy while retaining editable semantics.
I found no clipped text, overlapping paragraphs, broken glyph boxes, missing
figures, or formula truncation in the reviewed page coverage. Deep nesting on the
t and two-sample p-value pages still leaves adequate line width and distinguishable
indentation. The long two-sample IF remains complete on a single line.

Minor continuity observation: Babies 2 page 4 ends with the right-tail branch
heading and D13 label; page 5 starts its E13 entry and explanation (source lines
242-252). Keeping this short label/entry opening together would reduce page turns
while entering the branch. This does not lose content or make the task impossible.
The original keeps that branch on one page. Babies 1 similarly continues a sample
explanation on page 3 and the committee letter on page 6; the continuation remains
readable. Babies 3 has a short final page containing the example interpretation and
references; no heading is isolated without its content. No prose should be deleted
or flattened merely to shorten these pages.

## Limits and closure

This review covers actual local PDF/DOCX appearance, original-to-current teaching
fidelity, blank-workbook region design, native document semantics, and expert task
mapping. It does not claim observed student comprehension, a usability study,
screen-reader accessibility, live Google Docs/Sheets fidelity, verified menu actions
in Google's current UI, or spreadsheet calculation correctness. The separate Calc
replay review owns numerical execution. The review does not substitute passing
lint or machine compilation for learner-visible quality.

Close the material-quality finding only after rebuilt DOCX/PDF pages render alpha
and decision emphasis cleanly and a fresh direct inspection confirms that the
original prose and nested teaching groups remain intact.
