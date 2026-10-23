# Independent authoring-guide review

## Scope and verdict

**Subsequent repair:** the source-integrity defects below were fixed after this baseline review.
See [authoring_visual_reference_review.md](authoring_visual_reference_review.md#independent-assessment-follow-up)
for the manager's reproduction, repair verification, and documentation updates. Original findings
and scores are retained below.

**Reviewer:** independent walkthrough reviewer who did not author the guide.

**Review date:** 2026-10-23.

**Verdict:** The student-facing route supported an original, small tutorial through source,
lint, DOCX/XLSX output, a native PDF check, a data-range revision, and a deliberate-error
recovery. The normal authoring route is strong. One optional maintenance workflow made an
unexpected prose change in its preview; do not treat its current prose-preservation promise as
reliable without manual diff review.

These are original **pre-correction baseline** scores. The reviewer made no guide edits. The
manager corrected student documentation after reading this report; those corrections are not
rescored here.

| Dimension | Score / 4 | Evidence and reason |
| --- | --- | --- |
| Audience and purpose | 4 | README says that BIOL 318 authors create original material for classmates and future students, explains open pedagogy/SGC, and reserves scientific and teaching decisions for the author ([README.md](../../../README.md) lines 3-21). The hub repeats the author-owned scenario and approach ([AUTHORING_GUIDE.md](../../AUTHORING_GUIDE.md) lines 3-10). |
| Clarity and navigation | 4 | The README leads directly to the hub and a purpose-based table ([README.md](../../../README.md) lines 23-37). The hub points to Parts, visual reference, and specification ([AUTHORING_GUIDE.md](../../AUTHORING_GUIDE.md) lines 12-24). I navigated README -> hub -> Parts 1/2/3 -> `CHANGES.md` without a compiler-internal or test lookup. |
| Visual demonstrations | 4 | The sampled fill source in [authoring_features.md](../../examples/authoring_features.md) lines 86-89 matches the visible text in `docs/screenshots/authoring_fill.webp`: "In cell B2, enter =A2^2" and "Fill B2:B6 down." Part 2 pairs the same literal source with an output image and explains that work cells remain blank ([PART_2_STATISTICS.md](../../learn/PART_2_STATISTICS.md) lines 110-125). My native one-page PDF visually showed the authored table, headings, formula, and fill instruction without clipping. |
| Capability coverage | 4 | The visual index covers document structure, formatting, tables/images/links, workbook layout, blanks, results/responses, formulas, actions, repairs, and optional changes ([FORMATTING_GUIDE.md](../../FORMATTING_GUIDE.md) lines 7-21). The walkthrough used title, Part, Step, prose, table, worksheet labels/data, blank work/results/responses, formula entry, and fill. |
| Student independence | 4 | The hub says Roots is not a required scenario ([AUTHORING_GUIDE.md](../../AUTHORING_GUIDE.md) lines 22-24), and its placeholder outline is explicitly not runnable or prescriptive ([AUTHORING_GUIDE.md](../../AUTHORING_GUIDE.md) lines 44-67). I chose an invented algal-respiration question rather than Roots or an instructor lesson. |
| Technical accuracy and recovery | 3 | The documented lint/build commands worked for the new source; initial and revised DOCX/XLSX bundles were produced. The documented action-target error was detected and repaired. A mismatch inside a fill workflow also produced a second valid `fill-source` diagnostic, so recovery requires reading more than the single diagnostic illustrated in Part 3. The optional resize preview made an unexpected prose capitalization change and left visible fill text stale while changing its hidden target; it was preview-only and not written. |
| Quality and maintainability | 3 | Documentation consistently separates compiler checks from scientific/instructional judgment ([AUTHORING_GUIDE.md](../../AUTHORING_GUIDE.md) lines 75-90; [PART_3_IMPROVE.md](../../learn/PART_3_IMPROVE.md) lines 107-119), and its normal path is concise. The optional editor documentation overstates prose preservation: its preview changed ordinary prose and action binding, although its diff/review instruction prevented a write. |

No total is used; the optional-maintenance finding should not obscure the strong core path.

## Walkthrough record

### Declared authoring goal

I authored `tutorial_output/independent_guide_review/algal_respiration.md`, an original small
tutorial about whether warmer water is associated with a larger overnight dissolved-oxygen decline
in sealed algal cultures. Intended reader outcome before building:

- Read supplied temperature, initial oxygen, and final oxygen data.
- Calculate oxygen decline in a blank column with `=B2-C2` and fill it down.
- Enter the largest decline in a blank result cell and write an evidence-based response in a blank
  interpretation cell.

This source includes a title, Workbook and Tutorial sections, Sheet/Part/Step structure, ordinary
prose, numbered instructions, a document table, supplied labels/data, blank calculation/result/
response areas, an `enter:` formula action, and a `fill:` action.

### Navigation and documentation used

1. Started at [README.md](../../../README.md), then opened the named
   [AUTHORING_GUIDE.md](../../AUTHORING_GUIDE.md).
2. Read [PART_1_CREATE.md](../../learn/PART_1_CREATE.md) for title, Part/Step structure, and a
   document table.
3. Read [PART_2_STATISTICS.md](../../learn/PART_2_STATISTICS.md) for a Sheet, blank work cells,
   result/response tables, `enter:`, and `fill:`.
4. Read [PART_3_IMPROVE.md](../../learn/PART_3_IMPROVE.md) for lint, build, inspection, and the
   visible-address recovery example.
5. Used [CHANGES.md](../../reference/CHANGES.md) only when deliberately sampling its optional
   range-revision preview.

I used no compiler internals or tests to learn authoring syntax. I did use `make_tutorial.py
--help` only to learn the documented command's optional output-directory argument, and used ZIP/
XLSX/PDF inspection tools after builds. Those were technical inspection aids, not syntax help.

### Builds, output, and inspection

Commands used from the repository root:

```bash
source source_me.sh
python3 make_tutorial.py lint tutorial_output/independent_guide_review/algal_respiration.md
python3 make_tutorial.py build tutorial_output/independent_guide_review/algal_respiration.md \
  --format docx,xlsx --output-dir tutorial_output/independent_guide_review/initial_build
```

Lint passed. Both commands printed only the non-blocking `google-unmapped` note, which says a
Google Sheets URL is optional. The initial artifact evidence is local-only ignored output,
unavailable on GitHub: `tutorial_output/independent_guide_review/initial_artifact_evidence.json`.

- `A1:C4` held supplied labels/data; `D2:D4`, `G2`, and `G7` were blank as intended.
- Numeric and blank calculation cells displayed `0.000`.
- The DOCX contained the title, document-table header, and formula text; it did not expose the
  hidden `enter:D2` target.

For reader-visible document inspection, I ran the repository's all-format command outside the
macOS sandbox because it invokes LibreOffice:

```bash
source source_me.sh
python3 make_tutorial.py build tutorial_output/independent_guide_review/algal_respiration.md \
  --format all --output-dir tutorial_output/independent_guide_review/initial_native
```

The resulting one-page PDF had readable heading hierarchy, table, formula, and fill instruction;
no clipping or awkward page split was observed. The rendered page is local-only ignored output,
unavailable on GitHub: `tutorial_output/independent_guide_review/initial_native/algal_respiration_page1.webp`.
This supported-host success does not prove Google Docs/Sheets import or student learning.

### Range revision

I added a 35 C data row, extended source/calculation regions from row 4 to row 5, and changed the
fill action from `D2:D4` to `D2:D5`. Lint and the revised DOCX/XLSX build passed. XML inspection
of the revised XLSX confirmed supplied `A5=35`, `C5=6.4`, and an empty styled calculation cell
`D5`; see the local-only ignored bundle, unavailable on GitHub:
`tutorial_output/independent_guide_review/revised_build/`.

### Deliberate error and recovery

I changed the otherwise valid entry link from `(enter:D2)` to `(enter:D3)` while keeping the visible
text "In cell D2." Lint reported the Part 3-documented error:

```text
error [action-visible-target] Visible cell D2 disagrees with enter target D3
  Correction: Use cell D3 in the instruction or change the binding target
```

Because the next instruction filled from D2, lint also reported:

```text
error [fill-source] Fill requires a first-row formula in every possible branch
  Correction: Enter a formula in each source cell before Fill
```

I restored `(enter:D2)` and reran lint successfully. This was recoverable from the diagnostics,
but it is a small friction point: the guide's isolated mismatch example cannot show the dependent
fill error an author may see in a real mini-tutorial.

### Optional change-preview observation

After the successful manual range change, I ran the documented optional preview only:

```bash
source source_me.sh
python3 make_tutorial.py worksheet-edit tutorial_output/independent_guide_review/algal_respiration.md \
  --sheet Respiration resize-observations --data-range A1:D5 --rows 5
```

It printed `Preview only; rerun with --write to replace the source.` It correctly proposed another
blank observation row and extended the regions. It also changed the ordinary sentence `The blank
decline column is where...` to `The blank decline column IS where...`. More seriously, it changed
the hidden fill binding from `(fill:D2:D5)` to `(fill:D2:D6)` while leaving its visible label
`Fill D2:D5` unchanged. It emitted multiple notices to review coordinate-looking text and numerical
explanations. I did not use `--write`; the review source is preserved. The complete stdout, stderr
notices, and command are local-only ignored evidence, unavailable on GitHub:
`tutorial_output/independent_guide_review/resize_observations_preview.txt`.
This is the exact observed evidence, not a claim that every use of the editor rewrites prose.

## Findings and smallest useful corrections

1. **High priority: qualify the optional editor's prose-preservation promise and require an
   action-text review.**
   - Affected task: range revision through the optional preview.
   - Evidence: the exact preview above changed `is` to `IS`; yet [CHANGES.md](../../reference/CHANGES.md)
     lines 37-39 says the helper "preserves lesson prose and worked explanations."
   - Student impact: an author who trusts the claim could accept a non-obvious wording change or a
     visible/hidden fill-range mismatch when using `--write`.
   - Smallest correction: say that the helper may propose changes outside coordinates and that the
     author must inspect the complete diff, including visible action text and action targets, before
     `--write`; retain the existing preview-first workflow. Do not imply the preview is safe to
     apply without review.

2. **Medium priority: expand the mismatch-recovery example with a dependent-action note.**
   - Affected task: correcting an `enter:` target when a later `fill:` starts at the visible cell.
   - Evidence: the mismatch generated both the displayed `action-visible-target` diagnostic and
     `fill-source`.
   - Student impact: a novice may fix the headline diagnostic yet be surprised by another error.
   - Smallest correction: after Part 3's example, add one sentence: when another action depends on
     the destination, read and resolve every diagnostic before linting again.

3. **Low priority: offer the DOCX/XLSX subset beside the normal all-format build.**
   - Affected task: first build on a host where PDF/LibreOffice is unavailable.
   - Evidence: README's quick build intentionally uses `--format docx,xlsx` and clearly labels
     PDF/LibreOffice as additional ([README.md](../../../README.md) lines 77-90), while Part 3
     presents the all-format default.
   - Student impact: this is not a defect on a supported installed host; it is a recoverable
     fallback discovery burden.
   - Smallest correction: add a parenthetical next to the Part 3 build command that points to
     `--format docx,xlsx` when the author is completing the DOCX/XLSX review first.

## Limits

- This was an expert documentation walkthrough, not an observed BIOL 318 student session; it does
  not establish learning, time-on-task, or classroom readiness.
- Local DOCX/XLSX/PDF inspection does not establish Google Docs/Sheets import, link navigation, or
  spreadsheet formula execution.
- I inspected one native PDF page visually and worksheet/document structure programmatically; I
  did not claim a complete accessibility audit or a visual inspection of every reference image.
- The optional editor issue is based on one precise preview. It should be reproduced before any
  implementation change, but the documentation should not overpromise behavior that this preview
  contradicted.
