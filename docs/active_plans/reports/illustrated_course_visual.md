# Illustrated course native visual refresh

## Refresh and provenance

- Ran `source source_me.sh && python3 devel/refresh_documentation.py` outside the sandbox on
  2026-10-23 after the source and renderer owners froze their changes. It exited successfully.
  The first inspection exposed the final-Step spill described below; after the source owner
  consolidated the summary-location instruction, reran the same complete command successfully.
- The existing capture owner now adds `course_overview_excerpt.webp` using the native PDF title
  `Exploring root lengths` through the end-exclusive `Part 2: Summarize root lengths` anchor. The
  complete first inspection Step, including its summary-location cue, is visible; no arbitrary
  crop coordinates or replacement lesson template are used. All fifteen prior course views remain.
- All 25 final images were opened and visually inspected: sixteen course, five syntax, and four
  landing-page views. All asset SHA-256 values agree with the three current capture receipts.
  Course images use the existing quality-90 WebP encoder and remain below the 1920-pixel edge cap.
  After the final refresh, reopened its five changed images; the other twenty are byte-identical
  to the directly inspected versions. The final excerpt is 1018 by 535 pixels.
- The eight checkpoint source hashes match the course receipt. Published Markdown, DOCX, PDF,
  and XLSX hashes agree with the source/build copies and the publication receipt.
- Protected source/artifact hashes in all three receipts still agree with the current files.
  A separate before/after SHA-256 check confirms all twelve canonical `tutorial_data/*.md`
  sources are unchanged.

## Visual inspection

Rastered every PDF page with `pdftoppm -r 96 -png` and opened every raster: Part 1 has six pages,
Part 2 five, Part 3 six, and the final published capstone one. Following the final source correction,
rerastered every PDF; reopened all five changed pages and verified that the remaining thirteen
pages are byte-identical to their inspected rasters. Temporary final review rasters are under
`/private/tmp/illustrated_course_visual/final/`.

| Check | Current evidence |
| --- | --- |
| Previous Part 1 page 2 image clipping | Fixed. The worksheet image shows every row and all summary columns. The opening excerpt fits on page 1 with its explanatory paragraph. |
| Previous Part 2 page 5 image clipping | Fixed. Page 5 now contains the reader calculation practice and result table without clipped images. |
| Build-step interruption | Fixed. Part 2 page 4 uses the compact completed-statistics view between the build command and the explanation; there is no full-document picture interrupting this Step. |
| Code-line widows | None found across all seventeen Part pages. Source examples and the two-line build command remain whole. |
| Worksheet views | Native starters visibly preserve blank results, completed demonstrations show values, labels are readable, and final rows remain visible. The formula map is explicitly labeled as an annotated teaching view. |
| Published final Step | Fixed after the source owner merged the redundant summary-location Step into the preceding inspection Step. The entire capstone now fits coherently on one page. Its final spread Step includes Read, Calculate, Check, and Explain without clipping or a page spill. The final variation image and Part 2 page 3 have no page seam. |

## Calculation evidence

The capture harness verified LibreOffice-recalculated disposable workbooks against independent
Python statistics. The five-root summary is `5`, `18`, `4.94974746830583`; the six-root and moved
summaries are `6`, `20`, `6.60302960768767`. These agree with independent sample standard deviations
`4.949747468305833` and `6.603029607687671`. Every checked numeric observation, result, and deviation
cell has display format `0.000`. Student-starter result and deviation cells remain blank.

## Limits

This is native artifact, capture-provenance, calculation, and visual-layout verification. It does
not establish Google Docs/Sheets import fidelity, student usability, or learning outcomes.
The final native artifacts are ready for fresh independent review; no unresolved material visual
defect was found in this inspection.
