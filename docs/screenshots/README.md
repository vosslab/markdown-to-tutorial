# Screenshot capture receipt

Captured 2026-10-22 at 23:36 UTC from the finished canonical Caffeine 3 PDF and XLSX.
The three managed README images show an illustrated lesson opening, a compact instructional
excerpt, and the complete student worksheet. These are actual rendered outputs, with no
compositing or substituted answers. The opening contains a narrative illustration, not a
computed regression chart.

| Asset | Actual view | Dimensions | Bytes |
| --- | --- | --- | --- |
| `caffeine_3_illustrated_opening.webp` | PDF page 1, title, research story, and embedded illustration; PDF clip (50, 49, 564, 664) | 1028 x 1230 | 269574 |
| `caffeine_3_fill_down_instructions.webp` | PDF page 4, complete Step 3 including all four actions, green formula, and 36-hours aside; PDF clip (50, 49, 564, 214) | 1028 x 330 | 45268 |
| `caffeine_3_blank_predictor_workspace.webp` | Actual XLSX, complete A1:N26 with blue source data, teal calculations, orange results, and purple written-response spaces | 1920 x 649 | 36348 |

PDF clips were rendered at 144 dpi with Poppler. The workbook was rendered through the
screenshot-docs skill's `render_artifact_libreoffice.sh`, with LibreOffice outside the sandbox.
A disposable copy changed only its print area, A3 landscape fit-to-page settings, margins,
printed grid, and row/column headings. Values, formulas, styles, and column widths were retained.
Blank workspaces are intentional: students enter their own calculations and interpretations.
The workbook asset retains its established filename even though its view now includes all columns.

All three WebPs were encoded with `cwebp -q 90` under `/tmp` and visually inspected after encoding.
They are under the 1920 px edge and 1 MB limits. The portrait opening preserves genuinely vertical
document content; the other two views are compact excerpts. All three README embeds resolve.
These are the complete managed image set: no stale unreferenced assets, removals, retained
reference images, or capture gaps.

## Reproduce the capture

Use [../../devel/capture_readme_artifacts.py](../../devel/capture_readme_artifacts.py) after
building the canonical outputs. This optional documentation workflow requires the existing
application environment, Poppler (`pdftoppm`), ImageMagick (`magick`), WebP (`cwebp`), LibreOffice,
and the screenshot-docs skill renderer. These capture tools are not application runtime dependencies.
Run the entire command outside the macOS sandbox because it invokes LibreOffice:

```bash
source source_me.sh && python3 devel/capture_readme_artifacts.py \
  --artifact-renderer /Users/vosslab/nsh/vosslab-skills/skills/documentation/screenshot-docs/scripts/render_artifact_libreoffice.sh
```

The script uses a fresh `/tmp/readme_capture_*/` workspace, refreshes the same three asset names,
and emits a JSON receipt with capture time and SHA-256 fingerprints. It fails if any of the
12 teaching sources or 36 canonical DOCX/PDF/XLSX files change during capture.
This run's JSON receipt is `/tmp/readme_capture_kzzvx56w/receipt.json`; all 48 protected files
were unchanged. Canonical PDF and XLSX hashes also match the final build manifest.

## Current fingerprints

| File | SHA-256 |
| --- | --- |
| `tutorial_data/caffeine_3_quadratic_regression.md` | `a8736df780e128fa08cb78b8590611b2256221ab67c043aad1ebcc93bf818983` |
| `tutorial_output/caffeine_3_quadratic_regression/caffeine_3_quadratic_regression.pdf` | `2e076c3743bec887f16278322a5079b38a6c1bfb1bc312ef5cb817abda6d3fab` |
| `tutorial_output/caffeine_3_quadratic_regression/caffeine_3_quadratic_regression.xlsx` | `80dfe167a82526de0278d8a70e15599bf5872dca4aafce550d60f7ab40f5d599` |
| `caffeine_3_illustrated_opening.webp` | `8ea9ca2555c8afca179981c94e0fbe46cf725dadcfc26cef1d49684ff9a0109e` |
| `caffeine_3_fill_down_instructions.webp` | `efc2267c45b638d15b28772ea93d2ae59d7d67aaaed5258bd4435104cd2c64d1` |
| `caffeine_3_blank_predictor_workspace.webp` | `a4021f6906339f475a8e0c476495628b595370ffafae23576dfc616126fee882` |
