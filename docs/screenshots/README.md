# Screenshot capture receipt

These four views demonstrate the publishing pipeline's illustrated document opening, spreadsheet
actions, formula treatment, and a completed calculation example. The rendered instruction excerpts
preserve the source writing while the renderer supplies the hierarchy, indentation, justification,
and formula styling. Workbook captures use the current three-decimal number format.

## Gallery

![Caffeine 3 illustrated lesson opening with sleep-and-exam-score story](caffeine_3_illustrated_opening.webp)

![Caffeine 3 complete squared-column step with formula and justified teaching aside](caffeine_3_fill_down_instructions.webp)

![Microbes 4 F-statistic action with a standalone formula and explanation](microbes_4_formula_instruction.webp)

![Completed Microbes 5 ANOVA demonstration with calculated values in a styled worksheet](microbes_5_completed_anova.webp)

| Asset | View |
| --- | --- |
| `caffeine_3_illustrated_opening.webp` | Title, research story, and embedded illustration |
| `caffeine_3_fill_down_instructions.webp` | Complete squared-column Step, formula, and teaching aside |
| `microbes_4_formula_instruction.webp` | F-statistic action, standalone formula, and explanation |
| `microbes_5_completed_anova.webp` | Disposable completed demonstration of the styled ANOVA worksheet |

The completed ANOVA image is a demonstration, not the student starter workbook. It starts with
the canonical styled starter, applies only the authored baseline label and formula actions in a
disposable copy, and has LibreOffice Calc calculate it before rendering. The canonical starter
remains unchanged. This completed view does not establish that the starter has an appropriate
instructional structure. Authors should establish labels before the compiler applies styling;
tutorial users should normally receive those labels already present.

The [capture receipt](capture_receipt.json) records the current source and artifact fingerprints,
image dimensions and hashes, protected-file checks, and completed-demo provenance. Capture counts
and measurements belong in that receipt rather than this gallery. Images are encoded as WebP at
quality 90; review the refreshed images alongside the receipt.

The separate syntax examples appear in [../FORMATTING_GUIDE.md](../FORMATTING_GUIDE.md), with
their source, capture command, and limitations documented there. Their provenance is recorded in
[syntax_capture_receipt.json](syntax_capture_receipt.json).

## Roots authoring course

The three-part [student course](../STUDENT_GUIDE.md) has its own screenshots for the Roots lesson
and starter workbook. Its assets are separate from the landing-page gallery and the syntax examples.
The course pages link to the capture set; [course_capture_receipt.json](course_capture_receipt.json)
records its provenance. Capture dimensions and other measurements belong in that receipt.

The course set distinguishes the generated lesson, blank student starter, and completed calculation
demonstration. The completed view is a disposable copy for comparison; it is not the published
starter workbook.

## Reproduce the capture

From the repository root, rebuild the documentation artifacts and all capture sets with one command:

```bash
source source_me.sh && python3 devel/refresh_documentation.py
```

The repository-owned helpers build native artifacts in temporary workspaces and locate crop content
automatically. No external skill renderer path is needed. They refresh the landing-page, syntax,
and course captures and their receipts; the refresh also rebuilds the illustrated course Parts.

This optional author workflow requires the existing Python environment with Pillow, Poppler
(`pdftotext`, `pdftoppm`), WebP (`cwebp`), librsvg (`rsvg-convert`), LibreOffice, and the required
fonts. See [../INSTALL.md](../INSTALL.md) for setup. On this macOS host, agents must run the command
with `sandbox_permissions="require_escalated"` because it invokes LibreOffice. Human terminal
commands use the ordinary command above.
