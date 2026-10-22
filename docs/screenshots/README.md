# Screenshot capture receipt

Captured and inspected both README images on 2026-10-22 at 22:26 UTC. No older managed images
were present. The two WebP files are the complete managed set; no reference images or capture gaps
remain.

| Asset | Current evidence |
| --- | --- |
| `caffeine_3_fill_down_instructions.webp` | Page 3 of the current Caffeine 3 PDF, rendered fresh with Poppler at 160 dpi and cropped to the Step 2 content. 1103 x 870 px, 86,400 bytes. |
| `caffeine_3_blank_predictor_workspace.webp` | Current generated Caffeine 3 XLSX, rendered through the LibreOffice artifact script from a temporary copy. The copy uses print area A1:F26, landscape fit-to-page, and printed row/column headings. No cell values were added; 75 cells in C, E, and F remain blank. 1327 x 878 px, 29,964 bytes. |

The PDF excerpt was rendered from page 3 with Poppler at 160 dpi, then cropped to the Step 2 content.
The workbook screenshot came from the current generated XLSX through the screenshot-docs workflow's
LibreOffice renderer, using a disposable copy with a landscape, fit-to-page print area. LibreOffice
was run outside the sandbox; the workbook data were not changed.

Current product hashes at capture time:

| File | SHA-256 |
| --- | --- |
| `tutorial_data/caffeine_3_quadratic_regression.md` | `120175139c17f57bf7831ad8258c1c5e77eed1a208529fd7500d693a9b601d07` |
| `tutorial_output/caffeine_3_quadratic_regression/caffeine_3_quadratic_regression.pdf` | `b56ffe8c5b75f674e71bd63271dfe495ce0f09b7e73f09fc266a2529c0c62518` |
| `tutorial_output/caffeine_3_quadratic_regression/caffeine_3_quadratic_regression.xlsx` | `f90a87a1ea124ecffa437765a92f085ec273d59dac3e899759b278c88797dde6` |
