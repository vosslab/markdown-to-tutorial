# README capabilities refresh

Reviewed 2026-10-22. Capture timestamps use UTC.

## Delivered

- A student-author introduction, template-first quick start, ordinary Excel examples, and
  preview-first worksheet maintenance instructions in the root README.
- Three current README images: the F-statistic formula display, Caffeine's complete squared-column
  instructions, and a clearly identified completed ANOVA demonstration.
- Four managed captures in total, including the illustrated opening in the screenshot gallery.
  Native PDF and Calc captures preserve the canonical teaching files. The completed ANOVA view
  applies authored actions only to a disposable copy of the styled workbook.
- Removal of the unlabeled Caffeine grid from the README, gallery, and capture harness. It did
  not communicate the worksheet's purpose. Authors establish headings and structure before
  formatting; tutorial users do not generally construct those headings.

The screenshot gallery and reproducible capture command are in
[../../screenshots/README.md](../../screenshots/README.md). The machine-readable receipt is
[../../screenshots/capture_receipt.json](../../screenshots/capture_receipt.json).

## Verification

- The README's template lint and DOCX/XLSX build commands succeeded. The optional all-format build
  also produced a PDF using LibreOffice outside the sandbox.
- The complete runnable Markdown example compiled and built DOCX/XLSX in a temporary directory.
- The worksheet-edit command printed a preview without writing the source. It updated the formula,
  data location, and action targets, and flagged unchanged visible fill-range wording for review.
  The README describes that actual behavior.
- The template workbook contains three supplied observations and blank C1:C4 learner cells.
- The opening paragraph is 225 characters. The focused documentation, typing, lint, dependency,
  indentation, executable-script, and security checks passed: 1,073 tests in 1.88 seconds.
- Captures use quality-90 WebP, at most 1920 pixels on the longer edge and under 1 MB each.
  Document crops end at complete paragraphs; the ANOVA view focuses on H1:M16 for readability.
- All 48 canonical source/product hashes match the capture receipt. Three README embeds are
  idempotent; all four remaining images have live embeds. No reference images or capture gaps remain.

The capture agent used `py_compile`, which explicitly writes cache files even when
`PYTHONDONTWRITEBYTECODE=1`. Local inspection confirmed that the environment setting and
`sys.dont_write_bytecode` were correct. No `__pycache__` folders remained at verification.
Further syntax checks use in-memory compilation rather than `py_compile`; no ignore rule was added.
The manager also reused the capture agent for corrections rather than following the fresh-agent
rule. That was a workflow error, not a change to repository policy.

## Editorial score

This is an editorial README assessment, not a score for the compiler or teaching materials.

| Category | Before | After | Evidence |
| --- | ---: | ---: | --- |
| Purpose, audience, and value | 11/15 | 15/15 | BIOL 318 authors and the author/learner distinction are explicit |
| Distinctive project identity | 8/15 | 15/15 | Preserved scientific prose, Excel design, and student templates lead the page |
| Proof and demonstration | 10/20 | 15/20 | Current native captures; a labeled starting-workbook example remains a product gap |
| Meaningful first success | 15/15 | 15/15 | Verified template builds produce editable files and an optional PDF |
| Usage and conceptual orientation | 5/10 | 10/10 | ASCII examples, templates, and an accurate maintenance preview |
| Documentation navigation | 8/10 | 10/10 | Template links, authoring guide, usage, catalog, specification, and capture gallery |
| Adoption context | 5/5 | 5/5 | Prerequisites, license, and Google verification limits remain visible |
| Presentation, accessibility, and currency | 5/10 | 10/10 | Fresh, cleanly cropped images with descriptive alt text and readable equivalents |
| Total | 67/100 | 95/100 | Strongest gain: project-specific authoring workflow and current output evidence |

Five applicable quality gates pass; the animation gate does not apply to static captures.

## Remaining product limitation

Some current lessons encode headings as learner label actions, producing incomplete starting
worksheets. The completed ANOVA demonstration proves formatting, not that this instructional
boundary is correct. The README says so explicitly.

Follow-up owner: worksheet compiler and lesson authoring. Target: the supplied-label versus
learner-action contract and representative Caffeine/ANOVA starter workbooks. Evidence: the human's
clarification that authors establish labels first and tutorial users generally receive them.
Success means readable labeled starting worksheets with only the intended learner calculations
and responses blank, while preserving explicit spreadsheet-construction activities. Verify the
actual starter XLSX, its source intent, and the corresponding tutorial before capturing new proof.

Google import and student outcomes remain unverified. No lesson prose or application behavior was
changed by this documentation refresh.
