# Student GFM rendering review

Status: historical baseline, reviewed 2026-10-23. The findings below describe the initial
snapshot and are retained as evidence. Corrections and current-source GFM acceptance are
recorded in the [accepted SPEC review](pipeline_quality_followup_spec.md),
[accepted QUALITY review](pipeline_quality_followup_quality.md), and
[final integration review](pipeline_quality_followup_integration.md). The original snapshot
rendered successfully but had an incomplete novice installation handoff and two reference
examples that did not match their adjacent output pictures.

## Findings

1. **High: the first installation command assumes prerequisites the student has not acquired.**
   [INSTALL.md](../../INSTALL.md), lines 16-23, begins with `brew` and then
   `pip install -r pip_requirements.txt`. Neither that page nor the preceding
   [README.md](../../../README.md), lines 190-192, tells a new reader how to obtain the
   repository, extract it, open its directory in Terminal, or obtain Homebrew. The README
   tells readers to open a terminal in the project folder only after following installation.
   A reader arriving from GitHub can therefore encounter `brew: command not found` or a missing
   requirements file before reaching the build exercise. Supply a short download/extract/open
   folder sequence and a Homebrew installation link before those commands. Keep subsequent
   Bash/source/build commands in that same folder. Do not require a new installer interface.
   Evidence: `contact_opening_3.webp` and `contact_remaining_2.webp` in the artifact directory.
   This is an expert walkthrough finding, not an observed participant failure.

2. **Medium: the worksheet source and its output picture disagree on supplied labels.**
   [WORKSHEETS.md](../../reference/WORKSHEETS.md), lines 46-62, shows `Summary`, `n`, and
   `Sample SD (mm)` in its literal source example. The immediately following Roots screenshot
   shows `Statistic`, `Sample size`, and `Sample standard deviation (mm)`. Cell positions agree,
   but a novice checking whether their source produced the expected labels cannot reproduce
   that picture from the displayed example. Align the small source example with the canonical
   Roots labels, or explicitly identify the picture as a differently labeled example.
   Evidence: `docs__reference__WORKSHEETS__950.webp` and `contact_reference_4.webp`.

3. **Medium: an unannounced dataset switch breaks the heading source/output comparison.**
   [MARKDOWN.md](../../reference/MARKDOWN.md), lines 29-52, teaches `Describe root lengths`,
   worksheet `Roots`, and `Inspect the measurements`, then displays a picture headed
   `Explore a curved relationship`, worksheet `Sleep and scores`, and `Inspect the observations`.
   The next sentence asks the reader to notice the generated hierarchy, without explaining
   that the words come from another example. Label this as the older sleep illustration,
   as the emphasis section already does at lines 70-72, or use matching source/output.
   Evidence: `docs__reference__MARKDOWN__950.webp` and `contact_reference_3.webp`.

4. **Low: agent execution terminology interrupts student setup.**
   [INSTALL.md](../../INSTALL.md), lines 29-32 and its final paragraph, exposes
   `sandbox_permissions="require_escalated"` and agent sandbox instructions in the same route
   where students are learning Terminal and Bash. These are not actions a student can perform
   in Terminal. Keep human commands and immediate prerequisites in the student route; the
   repository already has the operational agent rule in `AGENTS.md`.

Two additional low-severity observations do not require a layout rewrite: the Part 1 opening
places a roughly 530-pixel Workbook source sample before its first Step at a 1280-pixel viewport;
the Student Guide places three large output illustrations before the first course link. Both
surfaces eventually provide clear labels and navigation, but the reader must scroll before the
next action. These are inspection observations, not measured student comprehension results.

## Method and evidence boundaries

Used the HCI expert skill's cognitive walkthrough method: a novice biology student on a desktop
browser attempts to identify a starting file, preserve Markdown punctuation while copying,
connect source cells with workbook pictures, distinguish blank starters from completed answers,
and reach a first local build. One expert reviewer; no students were recruited, no completion
times were measured, and this does not claim a usability study or WCAG certification.

All 30 scoped current-source files were submitted to the actual public GitHub REST renderer:
`POST https://api.github.com/markdown`, JSON fields `text`, `mode: gfm`, and
`context: vosslab/markdown-to-tutorial`; API version `2026-03-10`. Every request returned 200.
The accepted public-source request did not publish or modify GitHub content.

The returned HTML was displayed in Chromium at 1280 x 1100 using the stylesheet URLs extracted
from the live GitHub repository page and GitHub's light-theme document attributes. A local
article wrapper supplied a 980-pixel content width and padding. Current local image bytes were
embedded as data URLs, so the screenshot review did not accidentally inspect older remote images.
This is actual GitHub-parsed GFM with GitHub CSS in a local wrapper; it is not a claim that the
uncommitted source was published to or displayed inside GitHub's complete application shell.

Full-page captures exist for all 30 files. All opening contact sheets, every course/reference/
formatting viewport contact sheet, and the remaining lower-page contact sheets were visually
inspected. Selected course opening and actual live GitHub screenshots were inspected at larger
size. DOM checks inspected images, preformatted samples, tables, headings, and page overflow.

The live public Part 3 was additionally opened in GitHub itself to answer the specific concern
about `$E$3` / `$F$3` becoming mathematical markup. Its comparison table visibly retained both
dollar signs; `math-renderer` count was zero. The public opening predates the current local
Workbook fences, so that live visit verifies only the dollar-sign behavior, not current-source
acceptance. `live_part3_mean_reference.webp` and `live_part3.json` retain that evidence.

## Results and task ledger

| Student task | Visible cue and observed result | Error recovery / limit |
| --- | --- | --- |
| Find the course | README Start here links to the student guide and Part 1; each Part has guide and previous/next links | Guide's large opening images require scrolling; local link targets exist |
| Copy actual lesson source | Part 1 explicitly says choose GitHub Raw, copy into plain text, and retain one working `.md` file | Copying a rendered checkpoint would lose punctuation; the Raw instruction explains this |
| Recognize examples as source | All three Part opening Workbook examples and guide action examples render inside literal fenced code | No accidental normal tables or heading interpretation inside those fences |
| Map observations to results | Part 2 annotation separates A2:A6 inputs from E3 destination; displayed mean is 18.000 | Count/mean/SD examples retain exact equals signs, punctuation, and target syntax |
| Distinguish starting and finished work | Starter pictures show blank E2:E4; completed pictures and nearby prose explicitly identify demonstrations | Readers are told to calculate on a copy and reopen the blank starter |
| Fill six observations | Part 3 source and completed picture distinguish B2:B7 and fixed mean E3 | Last-row checks explicitly identify the unfilled-B7 error |
| Move a layout | Part 3 comparison table and worked pictures move A/B/E references to B/C/F | Literal dollar signs remain visible in local API and live GitHub output |
| Match a reference's source to its picture | Worksheet labels and Markdown heading words differ from adjacent output | Requires the two targeted corrections above |
| Reach a first build | Build command, output paths, Bash shell, and source loading are visible | Installation lacks acquisition/folder/Homebrew prerequisites; targeted correction required |

Measured desktop checks: 43 image elements loaded successfully; zero body horizontal overflows;
zero missing local targets among links produced by the API. Nested lists and simple pipe tables
remain structurally distinct. Long shell commands in Part 3 and USAGE use horizontally scrollable
code blocks rather than overflowing the page. README's collapsed details content produces an
empty-text overflow measurement while hidden; this was not treated as a rendering failure.
This review did not perform a keyboard/assistive-technology audit or narrow-screen acceptance.

Templates, checkpoints, and the two complete lesson examples intentionally remain complete raw
lesson sources. Their Workbook tables render as ordinary GitHub tables, and GitHub strips the
unsupported custom action link destinations while retaining readable formula/instruction text.
They must be copied through Raw; they are not malformed guide examples and should not be fenced
wholesale. In contrast, guide snippets preserve `enter:`, `fill:`, backticks, pipes, and headings
inside code samples. No observed guide formula was accidentally struck through or interpreted
as mathematics.

## Artifacts and focused re-review

All ignored browser evidence is under `tutorial_output/gfm_review/`:

- `render_manifest.json`: exact 30-file inventory, HTTP statuses, source SHA-256, API body SHA-256,
  and stylesheet URLs. Coverage includes README, STUDENT_GUIDE, all three learn Parts, all six
  topic references, FORMATTING_GUIDE, AUTHORING_GUIDE, INSTALL, USAGE, TUTORIAL_CATALOG,
  TUTORIAL_SPEC, all three templates, formatting_demo, adding_rows_and_columns, and eight Roots
  checkpoints.
- `browser_evidence.json`: file-by-file DOM measurements and viewport capture filenames.
- `navigation_evidence.json`: local link-target check (empty missing list).
- `NAME.api.html`: unmodified API response, and `NAME.html`: the local visual-review wrapper.
  `NAME` is the source path with `/` replaced by `__` and `.md` removed.
- `NAME.webp`: full-page screenshot; `NAME__Y.webp`: course/reference/formatting viewport at
  scroll position Y. `contact_opening_*`, `contact_course_*`, `contact_reference_*`,
  `contact_formatting_*`, and `contact_remaining_*` are the inspected contact sheets.

The snapshot hashes must be compared before reuse: USAGE changed while this audit was running,
so its current source needs a fresh response/capture if accepted as part of the final state.
The findings refer to the explicit line ranges/source state above, not an assertion that concurrent
fixes have already been reviewed.

The next fresh reviewer can render only changed files through the same endpoint, then open them
with the same recorded GitHub CSS and current local images. Re-check INSTALL's acquisition to
build sequence and the two source/output comparisons; also refresh any concurrently changed
USAGE/source hashes. Unchanged source hashes and unchanged local screenshot assets permit reuse
of this 30-file baseline. The temporary audit helpers under `tests/_temp/` are removed at handoff;
the API responses, measurements, and screenshots remain available for independent inspection.
