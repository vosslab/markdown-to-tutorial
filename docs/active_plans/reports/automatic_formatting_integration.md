# Automatic formatting integration review

Review date: 2026-10-22. Status: accepted for the planned formatting and authoring work.

## Review scope

Compared the approved [automatic formatting plan](../automatic_tutorial_formatting.md) with the
current implementation, authoring contract, tests, and rebuild and quality reports. Applied the
repository, Python, pytest, and Markdown style rules. The plan's original 12 tutorial source files
remain unchanged.

## Implementation and plan

Formula recognition runs in the shared Markdown parser and assigns semantic formula roles. The
existing compiler and formula validator retain their semantic and validation roles; DOCX rendering
applies Roboto Mono and dark green (`188038`). The literal-action safeguard preserves authored
operator characters and leaves JSON scalar literals and labels unstyled. Formula text remains
copyable. The renderer gives list paragraphs 0 pt before, 2 pt after, and single line spacing while
body paragraphs retain their existing 6 pt after and 1.08 line spacing. Student workbook targets
remain blank. These boundaries match the approved plan and the rechecked specification; no
architectural drift or unaddressed review finding remains.

The changed behavior has permanent semantic and DOCX tests for bare formulas and their validation,
prose boundaries, formula roles across inline and block contexts, literal action payloads, unchanged
compiled tokens, compact list paragraphs, and unchanged body spacing. The literal-action issue found
in the first specification review is resolved in the recheck.

## Verification

- `source source_me.sh && python3 -m pytest tests/test_guidance_doc_format.py tests/test_markdown_links.py -q`:
  111 passed. `git diff --check` passed.
- Checked ASCII characters in the 13 changed or current formatting Markdown files: no violations.
- Built a complete temporary tutorial containing the README's bare `=A2^2` action and fill-down
  example with `source source_me.sh && python3 make_tutorial.py build
  /private/tmp/automatic-formatting-readme-example.md --format docx
  --output-dir /private/tmp/automatic-formatting-readme-example-output`. The CLI published DOCX
  successfully; it reported only the expected unmapped-Google-sheet note. PDF conversion and
  LibreOffice were not invoked.
- Rechecked the ignored rebuild manifest against all 12 current source hashes and all 36 canonical
  artifact hashes. Every hash matched. The recorded rebuilt PDFs total 65 pages against 70 baseline
  pages; the independent visual report accepted all 65 current pages.
- Rechecked the source, PDF, XLSX, and two WebP hashes in the screenshot receipt; all match current
  files. The canonical Caffeine 3 workbook has all 75 designated student answer cells blank.
- The rebuild report records 254 passing Calc comparisons across 13 scenarios and a full suite run
  with 1,493 passing tests. This integration review did not rerun the full suite or all 12 builds.

## Limits

The evidence supports local DOCX, XLSX, PDF, copy-text, and source-preservation claims in the plan.
Google Docs and Sheets import behavior, learner enjoyment, and student outcomes remain unverified.

