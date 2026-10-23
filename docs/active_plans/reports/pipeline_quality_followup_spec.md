# Pipeline follow-up SPEC review

Final result: ACCEPT. Fresh review on 2026-10-23 closes the initial INSTALL blocker below.
All D1-D7 follow-up requirements pass the reviewed source and artifact checks. QUALITY and
INTEGRATION remain separate subsequent gates. This reviewer changed only this report and
ignored review evidence; no product files were edited.

## Final closure review

The current [INSTALL.md](../../INSTALL.md) installs Homebrew first, supplies the public
`git clone` command and explicit `cd markdown-to-tutorial`, and then installs Python 3.12 and
LibreOffice. That creates the real checkout required by `source_me.sh`. The Python version
check precedes package installation. A wrong minor version or Homebrew's protected-environment
error leads to the explicitly selected `python3.12` local environment, after repository sourcing.
Both INSTALL and [USAGE.md](../../USAGE.md) explain that activation follows repository sourcing
in each new Bash shell. The named font installation steps remain visible before PDF work.

Submitted those exact two current files to GitHub's actual REST `POST /markdown` endpoint with
`mode=gfm`, repository context, and API version `2026-03-10`. Both returned HTTP 200. Chromium
outside the sandbox displayed the returned HTML with actual GitHub CSS. Full-page and targeted
screenshots were inspected: the acquisition, version check, conditional environment, activation,
and first-build sequence are legible; neither document has body horizontal overflow or failed
browser requests. Long USAGE commands remain scrollable inside code blocks.

Reconciled the complete 30-document GFM scope against current bytes: 24 baseline documents,
four unchanged documents from the earlier six-file refresh, and these two new renders. All 30
source hashes, all 30 saved API-body hashes, and all 43 referenced local image hashes match.
All 30 reviewed Markdown sources are ASCII. The baseline's two source/output corrections remain
covered by the matching four-file refresh; baseline observations are preserved below.

Fresh code/diff review confirms the editor follows compiler-owned table regions, applies legacy
targets once, maintains executable nested formulas, and preserves literal code examples. The
composition seam keeps the fenced examples literal, compiles real ignored on-disk sources with
the specified root 05/root 06 workbooks, and rebases rendered assets. The response minimum is
shared across authored rows, and the header keep-with-next change remains at its DOCX owner.
No new compiler syntax or permanent evaluation framework was introduced.

Independently rechecked all 12 canonical lesson sources and all eight Roots checkpoints against
HEAD: all 20 are unchanged. All 16 current PDF hashes match the final native review. Direct
inspection of Part 1 page 6 confirms the header and all five body rows together; fresh PDF text
extraction contains both columns' required addresses and labels. Microbes 4 E26 and Microbes 5
I16 remain blank, wrapped, 10 pt, and 123 pt tall. The broader native report supplies the retained
114-page visual inspection and all-106-cell comparison; this closure does not claim to repeat
that entire page audit.

Commands and results:

```bash
source source_me.sh && python3 tutorial_output/gfm_review/accepted/rerender.py
node tutorial_output/gfm_review/accepted/capture.mjs
source source_me.sh && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_worksheet_edit.py tests/test_documentation_refresh.py tests/test_tutorial_workbook.py tests/test_tutorial_docx.py tests/test_markdown_links.py -q -p no:cacheprovider
git diff --check
```

The API render and browser commands passed; Chromium ran outside the sandbox. The focused test
command passed **234 tests**. The diff whitespace check passed. Disposable Python checks also
passed the source/render/image/PDF reconciliation and blank-response properties described above.
No LibreOffice run or system package installation was needed by this reviewer.

Final ignored evidence is under `tutorial_output/gfm_review/accepted/`:

- `render_manifest.json`, `*.api.html`, `*.html`: exact two-file current sources/render hashes
  and unmodified API responses with their review wrappers.
- `browser_evidence.json`, `css/`, `*.webp`: browser measurements, actual GitHub stylesheet
  captures, full-page screenshots, and focused setup/build screenshots.
- `coverage_reconciliation.json`: current 30-document source/API and 43-image comparisons,
  including the exact earlier evidence directory reused for each document.
- `native_spot_checks.json`: fresh 16-PDF, 20-source, blank-response, and Part 1 text checks.

This is desktop expert/specification review. Google Sheets import fidelity, participant usability,
assistive-technology behavior, mobile acceptance, and learning outcomes remain unverified.

## Initial review history

Initial result: NEEDS CORRECTION. The worksheet, response-space, guide-composition, native-table,
and source-preservation requirements pass this independent review. One beginner setup blocker
remains in the reviewed INSTALL snapshot: its Download ZIP route cannot satisfy the existing
Git-based shell bootstrap. No product changes were made by this reviewer.

## Blocking finding

The reviewed [INSTALL.md](../../INSTALL.md) tells a novice to download and extract a ZIP, then
source the repository environment. [source_me.sh](../../../source_me.sh) unconditionally obtains
`REPO_ROOT` with `git rev-parse --show-toplevel`, then uses that root for required Python import
paths. An extracted ZIP has no `.git` directory. In an ordinary folder outside another checkout,
the command fails; `git -C /private/tmp rev-parse --show-toplevel` independently returned exit 128
and `fatal: not a git repository`. The student therefore cannot establish the documented
environment through the recommended acquisition path.

Correct the acquisition instructions to create a real checkout after the prerequisites are
installed. A copyable public `git clone` command and explicit folder change fit the existing
bootstrap contract without introducing a new fallback. Then obtain a fresh GitHub API render
of INSTALL and inspect its acquisition-to-build order. The five other refreshed documents and
the 24 unchanged baseline documents can be reused when their recorded source/asset hashes match.

This finding applies to the exact INSTALL source SHA-256 in the review manifest below. A
concurrent correction is assigned separately and has not been accepted by this reviewer.

## Fresh verification

Read AGENTS.md, the three canonical style documents, the follow-up plan, current implementation
diffs, focused tests, and the native/GFM review reports. Independently checked these contracts:

- Worksheet insertion follows every compiler-owned table region, preserves blank lines after
  `At:`, shifts a legacy target once, updates executable nested `sheets` formulas, and leaves
  ordinary code examples literal. The owning code and regression cases cover those behaviors.
- Guide Workbook examples remain literal Markdown fences. The existing refresh seam composes
  checkpoint `root_05_variation` into Parts 1 and 2 and `root_06_grow` into Part 3, keeps composed
  sources under ignored output, and rebases rendered links while preserving fenced examples.
- The interpretation-role height uses eight lines shared across authored rows; a one-row panel
  receives 123 pt. Fresh workbook inspection found Microbes 4 E26 and Microbes 5 I16 blank,
  wrapped, 10 pt, and 123 pt tall. The unchanged Caffeine source retains its ten-row panel.
- All 12 canonical source files are byte-identical to HEAD. Roots remains the course example.
  The five restrained wording edits simplify instructions without changing scientific prose.
- Header paragraph `keep_with_next` addresses the actual table continuation failure. Direct
  inspection of current Part 1 PDF page 6 shows both columns and all five body rows together.
  Fresh PDF text extraction confirms A1, A2:A6, D1:E1, D2:D4, E2:E4, sample size, standard
  deviation, and the blank-result explanation. All 16 current PDF hashes match the native
  review's audited versions, including the published capstone. The native reviewer separately
  inspected all 114 pages and reconciled all 106 nonempty table cells.
- README and AUTHORING_GUIDE visibly give the Raw / Copy raw file route. Bash and the named
  font installation steps are explicit. INSTALL and USAGE no longer expose agent execution
  instructions to students. The reference Markdown crop is labeled as the older sleep example;
  the WORKSHEETS literal summary exactly matches its screenshot labels and blank E2:E4 cells.

Commands run through `source source_me.sh && python3`:

| Check | Result |
| --- | --- |
| `-m pytest tests/test_worksheet_edit.py tests/test_documentation_refresh.py tests/test_tutorial_workbook.py -q` | 31 passed |
| `-m pytest tests/test_tutorial_docx.py -q` | 16 passed |
| `-m pytest tests/test_markdown_links.py -q` | 187 passed, including this report |
| Disposable source/PDF/workbook spot checks | All source/PDF hashes and checked properties match |
| `git diff --check` | Passed |

The earlier records-only broken link in DESIGN_DECISIONS is corrected to the existing USAGE
anchor; the fresh local-link check above passed. No LibreOffice command was needed for this
review, and no permanent evaluation machinery was added.

## Actual GFM refresh evidence

Sent all six changed public source documents to the actual GitHub REST `POST /markdown`
endpoint with `mode=gfm`, context `vosslab/markdown-to-tutorial`, `Accept: text/html`, and API
version `2026-03-10`, without authentication. Every request returned HTTP 200. Saved exact
source/render SHA-256 values and unmodified API HTML, then rendered them in Chromium outside
the sandbox using the actual GitHub stylesheet set. All 30 unique stylesheet requests succeeded.

Reviewed browser screenshots of README, AUTHORING_GUIDE, INSTALL, USAGE, MARKDOWN, and
WORKSHEETS, including their changed regions. Eight current images loaded; no body horizontal
overflow or failed browser request occurred. Literal syntax remains visible in fenced examples,
and the summary source/picture comparison is now exact. The INSTALL picture itself preserves
the failing ZIP instructions as historical evidence rather than claiming their acceptance.

The baseline reconciliation independently confirms all other 24 document source hashes and
all 43 baseline image references still match. Together with the refreshed six, this maintains
the baseline 30-file GFM coverage. This is desktop expert review, not a student study,
assistive-technology audit, mobile acceptance, or Google Sheets fidelity test.

Ignored evidence is under `tutorial_output/gfm_review/final/`:

- `render_manifest.json`: six source/render hashes, HTTP statuses, and current image hashes.
- `baseline_reconciliation.json`: 24 unchanged source and 43 image-reference comparisons.
- `browser_evidence.json`, `css/`, `*.api.html`, `*.html`, and `*.webp`: actual API bodies,
  stylesheet capture, measured DOM, full-page screenshots, and changed-region screenshots.
- `native_spot_checks.json`: 12 unchanged sources, 16 current PDF hash comparisons, two blank
  response-panel checks, and actual Part 1 PDF page 6 text checks.

The retained temporary helpers exist only inside ignored review output. A fresh reviewer must
verify the corrected INSTALL acquisition path and its final render before SPEC acceptance;
QUALITY and INTEGRATION remain subsequent gates.
