# Authoring reference review

## Purpose and inspection method

For the subsequent independent assessment, use [AUTHORING_GUIDE_RUBRIC.md](AUTHORING_GUIDE_RUBRIC.md).
It adds explicit scoring and an original-content walkthrough to the implementation checks below.
Results are in [AUTHORING_GUIDE_INDEPENDENT_REVIEW.md](AUTHORING_GUIDE_INDEPENDENT_REVIEW.md).

Audience: BIOL 318 students who have completed several biostatistics tutorials and now author
original tutorials. The interface is GitHub Markdown, read on a desktop or narrow viewport.
The source and example files produce native DOCX, XLSX, and PDF materials.

Method: expert cognitive walkthrough and rendered-output inspection, using the humanizer and
hic-human-interact-expert skills. This is not a participant study and does not measure student
learning. The prior course's imposed Roots progression, introductory spreadsheet/statistics
explanations, and source/output mismatches supplied the baseline problems.

## Tasks and acceptance criteria

| Task | Information needed | Completion evidence |
| --- | --- | --- |
| Discover a feature | Task-named visual index and reference link | Reach an appropriate source/output pair without completing an example lesson |
| Copy document structure | Literal headings and list syntax | Pasted source keeps headings, punctuation, and nesting |
| Design the starter | Table placement, supplied content, blanks, action ownership | Workbook contains chosen labels/data and leaves intended work blank |
| Supply original content | Clearly labeled placeholders | Placeholders remain visible in docs and are replaced before compilation |
| Build and recover | Commands, diagnostics, output paths | Own-content variation builds; a mismatched target reports a useful correction |
| Review the files | Native document and workbook | Visible instructions, blank cells, and source agree |

## Accessibility and clarity checks

- Keep selectable source next to screenshots and describe each screenshot in alternative text.
  This supports [WCAG text alternatives](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html).
- Check body reflow at 320 CSS pixels; code and data tables may scroll within their own containers.
  See [WCAG reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).
- Inspect native screenshot readability, link navigation, placeholder fences, and source/output
  correspondence. No claim of full WCAG conformance is made from these limited checks.
- Humanizer review keeps explanations concrete and removes artificial significance from Roots.
  Existing instructor-authored excerpts remain unchanged.

## Implementation findings

- Replaced the mandatory checkpoint progression with document, workbook, and build/refine guides.
- Consolidated the authoring entry point and retained the useful topic-reference organization.
- Created one small feature source for accurate, reusable output crops.
- Moved the demonstration response table below the data because its row height distorted adjacent
  measurements in the first capture.
- Corrected source examples whose wording differed from their adjacent generated screenshots.
- Kept compiler requirements distinct from advisory scientific and instructional review.

## Final verification

- Full repository suite: 2,105 passed. The first run exposed a tracked-file inventory issue after
  retiring the student hub; registering that deletion resolved collection without changing tests.
- GitHub Markdown API rendered 31 student-facing pages, references, examples, and templates.
  Their source hashes match the final files. Browser inspection used GitHub styles at 1280 and
  320 CSS pixels: zero broken images, empty image alternatives, body overflows, or accidental
  mathematical renderers. Code and tables keep their own horizontal scrolling where needed.
- All 31 heading-target inventories resolve. The API omits GitHub host heading IDs, so the local
  navigation wrapper modeled those IDs and relative document routes. Keyboard activation reached
  the authoring guide and visual index; the feature link brought its formula section into view
  after scrolling settled. This is API/local-browser evidence, not a published-site claim.
- Placeholder text remains inside selectable code blocks. Body text on white measures 15.80:1
  contrast in the GitHub-style review. This limited check does not establish full accessibility
  conformance or screen-reader usability.
- Checked 26 displayed source fragments against the shared feature source and instructor excerpt.
  All match. Native screenshot receipts match the current source and asset hashes.
- Built and inspected all three guide PDFs (5, 5, and 3 pages), with no text outside page bounds.
  Inspected the native feature images and workbook regions. Removed a repeated Part 3 outline
  after it caused a large page gap; the final guide links the existing source examples instead.
- A separate content-transfer walkthrough changed the title, worksheet name, labels, and data,
  then produced DOCX/XLSX files with those changes and blank learner-work cells. A deliberate
  E2/E3 target mismatch produced the documented diagnostic; correcting it restored a valid source.
- Instructor sources, archived originals, compiler modules, and existing templates are unchanged.
  A fresh read-only documentation review found one duplicated alt-text phrase, which was corrected.
- One-time check scripts were removed from tests/_temp; no prose/count-specific permanent tests
  or new documentation framework were added.

Evidence artifacts are under the ignored tutorial_output/authoring_review directory: gfm contains
API responses, source/asset fingerprints, browser measurements, and navigation captures; native
contains page images and bounds evidence; walkthrough contains the independent example, outputs,
and error-recovery record. Maintained screenshot provenance remains in
[../../screenshots/syntax_capture_receipt.json](../../screenshots/syntax_capture_receipt.json).

Google import, actual student use, and learning outcomes were not tested. The checks establish
local technical behavior, accurate examples, and expert-inspected documentation.

## Independent assessment follow-up

The subsequent [independent review](AUTHORING_GUIDE_INDEPENDENT_REVIEW.md) scored audience,
navigation, visuals, coverage, and independence at 4/4; accuracy/recovery and maintainability at
3/4. These are the original reviewer scores, not a post-correction rescore. The reviewer authored
an original algal-respiration tutorial from the student-facing documentation, built native outputs,
extended its data range, and recovered from an intentional action-target error.

Corrections made after the findings:

- CHANGES.md and USAGE.md now describe the observed worksheet-editor limitation instead of
  promising prose preservation. They direct authors to leave an unintended preview unapplied and
  make manual source changes. The manager independently reproduced the original preview command.
- Part 3 explains that an incorrect entry destination can also cause a dependent `fill-source`
  diagnostic. Correct the destination, rerun lint, and then address remaining errors.
- Part 3 exposes the existing DOCX/XLSX-only option beside the default PDF-inclusive build.

Rebuilt Part 3 with the repository's native workflow outside the sandbox and visually inspected its
three PDF pages after these changes. The added guidance fits without clipping. The independent
review's manual range revision and repaired action target both passed lint and generated DOCX/XLSX
outputs; the optional editor remains preview-only in the evidence.

**Implementation follow-up resolved:** a subsequent narrow repair in
[worksheet_edit.py](../../../tutorial_lib/worksheet_edit.py) distinguishes uppercase column notation
from ordinary prose and synchronizes an exact displayed Fill range with its original action target.
The original independent report and scores remain unchanged as baseline evidence.

The manager replayed the original resize on a disposable copy, checked that preview left source
bytes untouched, applied `--write`, linted, and built DOCX/XLSX. The source and Word document retain
`The blank decline column is where...`; source and document now show D2:D6 consistently. Existing
data remain intact and D6 is a styled blank calculation cell. The newly added observation row has
blank inputs, so lint correctly warns about B6/C6 until the author supplies data.

Local evidence is under `tutorial_output/worksheet_editor_repair/`: before/after previews, the
write log, the repaired source, built files, and `artifact_evidence.json`. Two permanent regressions
protect prose preservation, exact fill synchronization, and legitimate uppercase column updates.
The temporary limitation text in CHANGES.md and USAGE.md was replaced with the supported syntax.

Repair verification: all 2,115 repository tests pass, including 18 worksheet-editor tests.
Pyflakes and `git diff --check` pass. The full suite initially encountered the retired student-guide
file in its Git inventory; registering the existing deletion restored collection without modifying
test behavior. The editor still validates its candidate and checks source freshness before writing.

Representative student sessions remain the next way to test whether real authors can independently
find features, create original content, build files, and recover from errors. Expert scores do not
substitute for that evidence.
