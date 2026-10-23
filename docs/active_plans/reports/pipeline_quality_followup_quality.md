# Pipeline follow-up QUALITY review

Result: ACCEPT. Fresh expert review on 2026-10-23 found no material correction needed after
the [accepted SPEC review](pipeline_quality_followup_spec.md). The existing follow-up plan is
sufficient. INTEGRATION remains a separate gate. This reviewer changed only this report and
ignored disposable evidence; no production source, lesson prose, or permanent tests were edited.

## Scope and method

Applied the requested HCI cognitive walkthrough and humanizer skills. The question was whether
a novice BIOL 318 author can follow the desktop GitHub-to-editor-to-build route, preserve literal
Markdown, construct a labeled blank starter, explain the input/output connection, and maintain
the optional expanded layout. The user works in a browser, plain-text editor, Bash, and a
spreadsheet application. A wrong destination or omitted final input can yield a plausible but
incorrect result, so correctness and recovery matter more than appearance alone.

The [follow-up plan](../../archive/pipeline_quality_followup.md) supplied the task model before this
walkthrough. Measures were successful source lint/build, blank starting answers, preserved
observations and labels, correct action/formula destinations, recognizable rendered source,
and an explicit recovery path for likely mistakes. The stopping rule was a concrete blocking
mismatch or completion of the specified tasks. No participant timings or student outcomes were
collected. This is one expert inspection, not a participant usability study.

## Walkthrough ledger

| Task and start state | Action, cue, and observed completion evidence | Error and recovery |
| --- | --- | --- |
| Find a starting file from the reading route | README and the student guide link to Part 1; Part 1 names `root_01_meet.md`, GitHub Raw, a plain editor, `.md`, and one continuing personal file | The Raw instruction explains why copying a rendered checkpoint loses punctuation; README/AUTHORING_GUIDE also name Raw or Copy raw file |
| Copy source rather than formatted output | Inspected actual GFM course images: Workbook, headings, pipes, backticks, action URLs, and formulas appear literally in fenced guide samples | Part 2 explicitly says copy the fence contents without the three-backtick lines; complete checkpoint files remain complete Raw sources |
| Design a blank first workbook | Started from root 01, used the guide's Workbook sample and count/mean/SD samples, and saved a disposable personal file. Lint and DOCX/XLSX build both passed | The guide distinguishes blank from zero and warns that placing a computed answer in the Workbook supplies it to readers |
| Connect observations to results | The rendered annotation identifies A2:A6 as inputs and E3 as the mean destination. Disposable output retains five measurements, all four summary labels, blank E2:E4, and `0.000` display | E2/count, E3/mean, and E4/sample SD are repeated in the source, diagrams, and result checks; result checks distinguish count, center, and spread |
| Calculate and interpret | Current native completed-workbook caches contain 5, 18, and 4.94974746830583; independent Python statistics agree. The source retains explanations and author-written interpretation tasks | Missing equals, wrong endpoints, and inappropriate scientific inputs are explained as meaning checks beyond a successful build |
| Grow to six observations and fill deviations | Replaced the Workbook sample, updated ranges to A2:A7, and appended the guide's deviation Part. Lint/build passed; the grown starter has six observations and no supplied formulas | Part 3 explains computing the mean first, `$E$3`, and the last-row check B7; a short fill must be corrected through B7 |
| Move the chosen layout | Ran the documented insert-columns preview and then `--write` on the disposable grown source. Preview preserved source bytes. Write, lint, and rebuild passed | Source and DOCX now use B2:B7 inputs, F2:F4 summary destinations, `=B2-$F$3` at C2, and fill C2:C7; the author is told to check ordinary explanation sentences |
| Reach a local first build | Latest INSTALL screenshots show Homebrew, clone, explicit `cd`, Python version check, named fonts, Bash, and sourcing in order. USAGE and the Part build commands name the output files | Wrong Python or protected pip leads to explicit Python 3.12 local-environment steps, with activation after sourcing in each new Bash shell |
| Choose a simple template | All three existing templates linted and built DOCX/XLSX successfully in disposable output | Templates ask the author to supply the scientific question and interpretation; they do not select a statistical analysis for the author |

The disposable personal file used the requested title and synthetic-data exercise with copied
guide examples. It is a concrete authoring walkthrough, not a claim that an unassisted student
performed those edits. No PDF export was needed: the equivalent current native artifacts already
have direct PDF proof, and this walkthrough changed only disposable wording and coordinates.

## Recovery and guideline ledger

| User need and principle | Acceptance criterion | Observed evidence and limit |
| --- | --- | --- |
| Recognition of the next action | Name the working file, source view, command, and expected artifact | Part 1 names Raw and the file; Part 2 names lint/build and output bundle; each Part supplies navigation |
| Externalize a multi-step connection | Show inputs, destination, and expected result together | Mean annotation and result table match the actual starter and native completed values |
| Make errors diagnosable | Give the concrete location and an actionable correction where syntax permits | Wrong `enter:E3` for visible E2 exits lint with `action-visible-target`, line 51, and a correction. Restoring the original target passes |
| Preserve author intent | Avoid inventing scientific meaning from valid syntax | Removing `=` passes lint as text, exactly as MISTAKES explains. The guide tells readers to inspect the formula bar and restore the equals sign; no stronger automatic protection is claimed |
| Support recovery from incomplete work | Check the final input and fill destination | Part 3 and MISTAKES identify B7 and the final deviation 10.000; native expanded/moved demonstrations include that value |
| Maintain graph-related references | Treat selection ranges as coordinates while retaining the author's chart choice | TUTORIAL_SPEC's chart example separates `Select B1:C3` from `Choose Insert > Chart`; the editor's recognized Select/range handling covers the coordinate boundary. This review does not claim chart creation or chart-object movement |
| Keep desktop material readable | Images load; content stays within the page; long code is reachable | Current saved browser measurements and inspected GFM images show loaded images and no body horizontal overflow; long commands scroll within code blocks |

These are task-specific recognition, consistency, feedback, and error-recovery checks. Browser
image-load and overflow measurements are limited layout evidence. They do not establish complete
WCAG conformance, keyboard operation, screen-reader behavior, or mobile usability.

## Render and provenance checks

Independently recomputed all 30 current source hashes, all 30 saved GitHub API response hashes,
and all 43 referenced image hashes against the exact evidence directory selected by the accepted
coverage reconciliation. All match. Actual GFM rendering evidence therefore remains applicable
to the current bytes; no new network render was necessary for this read-only review.

Opened all four course viewport contact sheets, the current INSTALL acquisition and recovery
crops, and the corrected WORKSHEETS and MARKDOWN reference crops. Literal source is visible;
summary labels match the worksheet image; the older Sleep-and-scores illustration is explicitly
identified. The Part 3 `$E$3`/`$F$3` comparison retains both dollar signs. Starter and completed
examples are labeled in their immediate context. The course's substantial introductory examples
require scrolling, as recorded in the baseline; navigation and the next action remain visible
and recognizable when reached. This does not justify a new layout layer.

Opened the actual current Part 1 PDF page 6. The `Spreadsheet location` table displays its header
and all five rows together, including the complete summary labels and blank-result explanation.
The [native visual report](pipeline_quality_followup_visual.md) supplies the broader 114-page
inspection and 106-cell reconciliation. This review did not repeat that whole audit.

Reopened the existing native completed Roots workbooks with cached values: five-root summary
is 5 / 18 / 4.94974746830583; expanded and moved summaries are 6 / 20 / 6.60302960768767.
Independent statistics agree. The retained native images show the corresponding three-decimal
displays and the final deviation. No new Calc evaluation or Google Sheets import is claimed.

## Maintenance quality

The fixes follow existing owners. Guide composition stays in the refresh script, takes an
explicit existing checkpoint, rebases rendered links, and leaves fenced source literal. The
compiler receives ordinary composed source; no guide-specific compiler language was added.

The worksheet editor now consumes compiler-owned table spans and geometry, patches tables in
reverse source order, and performs reference transformations once. Blank lines before `At:`
are handled at that boundary. Ordinary code samples stay literal; recognized executable nested
formula fences are maintained with their owning actions. Candidate compilation and the existing
unchanged-source write guard keep preview/write behavior concrete. The behavioral tests cover
the demonstrated defects without adding a new editing framework.

The interpretation-height minimum uses existing role regions and preserves greater authored
heights. The DOCX pagination repair sets keep-with-next only on header-cell paragraphs, leaving
body rows free to paginate. Its XML regression checks the owning property; the actual PDF page
supplies causal output evidence beyond serialization. A broad pagination regrouping would add
maintenance cost without a demonstrated remaining failure.

The prose review found no reason to rewrite settled lesson wording. The five restrained prior
jargon corrections preserve the Roots science. The author continues to choose the data, table
layout, statistics, and explanations; presentation and coordinate bookkeeping remain deterministic.

## Commands and evidence

```bash
source source_me.sh && PYTHONDONTWRITEBYTECODE=1 python3 tutorial_output/followup_quality/walkthrough.py
source source_me.sh && PYTHONDONTWRITEBYTECODE=1 python3 tutorial_output/followup_quality/reconcile.py
source source_me.sh && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_worksheet_edit.py tests/test_documentation_refresh.py tests/test_tutorial_workbook.py tests/test_tutorial_docx.py -q -p no:cacheprovider
```

The walkthrough's eight commands passed; three personal DOCX/XLSX bundles were verified. All
three templates also passed lint/build into separate disposable bundles. The focused regression
slice passed 47 tests. The wrong-destination probe intentionally failed lint; the missing-equals
probe intentionally remained valid text. This review does not substitute that focused slice for
the separate final full-suite integration check.

Ignored evidence is under `tutorial_output/followup_quality/`: `walkthrough.py`, `walkthrough.json`,
`reconcile.py`, `reconciliation.json`, copied personal/error-probe Markdown, three personal bundles,
and three template bundles. Existing GFM evidence was reused only after the hash checks above.
No LibreOffice invocation, package installation, permanent evaluation framework, or participant
study was introduced. Full GitHub application behavior, imported Google files, assistive
technology, student comprehension, and learning outcomes remain outside this acceptance.
