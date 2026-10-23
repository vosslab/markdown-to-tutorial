# README showcase refresh

## Task ledger

| Work | Owner | Status | Evidence |
| --- | --- | --- | --- |
| README journey and rubric | README owner | Complete | Three output screenshots lead; the verified low-dependency DOCX/XLSX quick start, actual Caffeine 3 excerpt, full example, and curated routes follow. |
| Output gallery refresh | Screenshot-docs owner | Complete | Three current Caffeine 3 views are captured and reviewed; the managed block remains intact. |
| SPEC recheck | Independent SPEC review | ACCEPT | All three actual views match their captions and the screenshot receipt; 48 source/product hashes are unchanged. The complete excerpt and runnable example are present, and the Google limitation appears before Quick start. |
| QUALITY review | Independent quality review | ACCEPT | No material issues. The README demonstrates the outputs, offers a verified first success, explains semantic actions, and routes readers to focused documentation. The subjective rubric scores 100/100. |
| INTEGRATION review | Integration manager | ACCEPT | Composition, managed image block, capture helper, screenshot receipt, and repository documentation agree. Focused documentation checks and the full suite pass. |

## Rubric

Score the page as a CLI/output-producing educational tool. Scores follow the readme-docs rubric and are editorial judgments supported by repository evidence.

| Category | Before | After | Evidence and remaining improvement |
| --- | ---: | ---: | --- |
| Purpose, audience, and value | 15 | 15 | Both versions explain the source-to-output value; keep the opening concise. |
| Distinctive project identity | 11 | 15 | The Caffeine 3 excerpt and runnable example show semantic cell actions, workbook regions, and preserved instructional voice. |
| Proof and demonstration | 10 | 20 | Three current output images show the illustrated opening, complete fill-down instruction, and full role-colored workbook; all captions match the inspected views. |
| Meaningful first success | 11 | 15 | The README lint/build path now has a successful isolated DOCX/XLSX run and names its output directory. |
| Usage and conceptual orientation | 10 | 10 | A real lesson excerpt explains semantic links, with the complete runnable example retained below it. |
| Documentation navigation | 8 | 10 | Six curated routes cover setup, use, authoring, catalog, contract, and Google evidence. |
| Adoption context | 3 | 5 | Synthetic PETase data and unverified Google behavior are stated before Quick start; PDF prerequisites precede the all-formats command. |
| Presentation, accessibility, and currency | 8 | 10 | Useful alt text, resolved links, three fresh captures, and clear student-workspace descriptions support the page. |
| **Total** | **76** | **100** | This is a subjective README rubric score, not a product-quality claim. |

## Verification

- `source source_me.sh && python3 make_tutorial.py lint tutorial_data/caffeine_3_quadratic_regression.md` passed offline lint with the source's existing Google-mapping note and formula-coverage warnings.
- `source source_me.sh && python3 make_tutorial.py build tutorial_data/caffeine_3_quadratic_regression.md --format docx,xlsx --output-dir /tmp/markdown-to-tutorial-readme-check` published DOCX/XLSX outputs outside the canonical output directory.
- Manager verified `source source_me.sh && python3 make_tutorial.py build tutorial_data/caffeine_3_quadratic_regression.md --format all --output-dir /tmp/markdown_to_tutorial_showcase_pdf_check` outside the sandbox; all three outputs were published.
- `devel/capture_readme_artifacts.py` produced three current WebP views; integration confirmed 48 source/product hashes remain unchanged. The isolated capture-tool hygiene checks passed 511 Bandit, pyflakes, shebang, typing, and dependency-import checks; see [the screenshot receipt](../../screenshots/README.md).
- `source source_me.sh && python3 -m pytest tests/test_readme_first_paragraph.py tests/test_markdown_links.py` passed (155 tests).
- The integration manager's final `source source_me.sh && python3 -m pytest tests/ -q` run passed (1,549 tests).
- Independent SPEC recheck: ACCEPT. It verifies three actual rendered views against their captions and receipt, the complete excerpt and full runnable example, the limitations before Quick start, and the unchanged 48 protected source/product hashes.
- Independent QUALITY review: ACCEPT with no material issues. Final subjective README rubric: 100/100 (15, 15, 20, 15, 10, 10, 5, 10); the earlier 88/100 preliminary score is superseded by the final evidence.
- INTEGRATION review: ACCEPT. README, managed screenshot block, capture helper, screenshot receipt, and verification record are consistent.
- Google Docs/Sheets import and execution remain unverified. No student study or learner outcome is claimed.
