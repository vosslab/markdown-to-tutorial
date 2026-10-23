# Whole-pipeline quality follow-up

Status: complete, 2026-10-23. Fresh SPEC, QUALITY, and INTEGRATION reviews accept the follow-up.

Review the completed illustrated course as a whole and improve only consequential, evidence-backed gaps. Preserve authored prose, ASCII source, blank learner calculations, and settled author design choices. Keep changes small and within existing pipeline boundaries; do not add an app, framework, or human-dependent workflow.

## Work ledger

| Work | Status | Owner | Evidence or completion record |
| --- | --- | --- | --- |
| Native artifact audit | Complete | `pipeline_native_audit` | Response areas E26/I16 remain blank, wrapped, 10 pt, and 123 pt tall; earlier table pagination loss is resolved and recorded in the [native visual report](../active_plans/reports/pipeline_quality_followup_visual.md) |
| Workflow audit | Complete | `pipeline_workflow_audit` | Identified worksheet movement, blank-line parsing at `At`, duplicate legacy coordinate shift, and stale nested-sheet formulas |
| Student-facing audit | Complete | `pipeline_student_audit` | Identified novice setup gaps; course otherwise coherent |
| Select worthwhile fixes | Complete | Manager | D1-D7 below; broad pagination grouping and speculative capture transactions deferred |
| Repair worksheet editor | Complete | `pipeline_edit_repair` | Owning editor and compiled-table behavior repaired with focused tests |
| Correct response-area height | Complete | `pipeline_response_space` | Eight-line / 123-point interpretation minimum; taller regions preserved |
| Fence examples and compose practice workbook | Complete | `guide_codeblocks` | Literal Markdown examples retained; Parts 1/2 use Roots checkpoint 05 and Part 3 uses checkpoint 06 |
| Add novice setup guidance | Complete | `guide_codeblocks` | Bash sourcing, font installation, and setup path clarified |
| Assess Roots and humanizer edits | Complete | `roots_humanizer_assessment` | Retain Roots; five small jargon edits accepted without changing Roots science |
| Lightweight HCI task model and walkthrough | Complete | Manager | Expert walkthrough wording and task model recorded below; no student study claimed |
| Repair native table pagination | Complete | `tutorial_lib/docx_renderer.py` | Header-cell paragraph `keep_with_next` keeps the first body row with its header; final PDF proof in native visual report |
| Correct GFM baseline findings | Complete | Manager | Two source/output mismatches and novice setup gaps corrected across README, AUTHORING_GUIDE, INSTALL, USAGE, MARKDOWN, and WORKSHEETS; fresh render/review remains part of SPEC |
| Fresh SPEC review | Complete | Fresh reviewer | [ACCEPT](../active_plans/reports/pipeline_quality_followup_spec.md); actual current GFM and native/source reconciliation |
| Fresh QUALITY review | Complete | Fresh reviewer | [ACCEPT](../active_plans/reports/pipeline_quality_followup_quality.md); expert authoring/maintenance walkthrough and template builds |
| Fresh INTEGRATION review | Complete | Fresh reviewer | [ACCEPT](../active_plans/reports/pipeline_quality_followup_integration.md); current artifact and receipt reconciliation, final suite |
| Final record reconciliation | Complete | Integration reviewer | Ledger and changelog updated; baseline failures retained as history; completed follow-up archived |

## Decisions and evidence

- D1. Retain Roots, as explicitly requested. Prefer existing authored science in future work; do not add a story or rewrite lesson prose.
- D2. Fence student examples in the three guides. Compose the course practice workbook from existing checkpoint root 05 for Parts 1 and 2 and root 06 for Part 3, refreshing the existing seam. Do not introduce compiler syntax.
- D3. Repair worksheet editing at its owning module and protect behavior with focused tests.
- D4. Interpret response height by role and preserve blank learner space.
- D5. Explain Bash sourcing and font installation for novice users at first build.
- D6. Use rendered GFM and browser inspection to catch source/output and setup mismatches. The baseline exposed two reference mismatches and setup gaps; the corrections and current actual GitHub rendering are accepted in SPEC and QUALITY.
- D7. Set `keep_with_next` on DOCX table header-cell paragraphs at `docx_renderer` so a header remains with its first body row. The initial Part 1 PDF lost all five body rows; the final native PDF shows the header and all five rows together. See the [native visual report](../active_plans/reports/pipeline_quality_followup_visual.md).
- Defer broad pagination grouping because current findings do not justify expanding scope. Reject speculative capture transactions because evidence does not establish a need.

HCI task model: a BIOL 318 novice uses GitHub, a plain editor, a spreadsheet, and a terminal. Tasks are to copy literal Markdown into an authoring file, build the labeled blank starter, enter `COUNT`/`AVERAGE` and check cells/results, and insert a column while keeping headers, actions, and formulas consistent. Success means fences remain literal, the starter begins blank, learner data is retained, and coordinates remain correct. Use an expert cognitive walkthrough after fixes; this is not a student study.

## Handoff evidence and limits

- [Native visual report](../active_plans/reports/pipeline_quality_followup_visual.md): all 12 canonical PDFs, three course Parts, and the published capstone were rebuilt and visually inspected (94 canonical pages, 19 Part pages, and one capstone page). The five Part 1 table rows now render together; all 106 cells across six tables are present. All 12 canonical source hashes, 102 manifest hashes, and 131 screenshot/receipt comparisons match. Of 25 maintained screenshots, 24 are byte-identical to HEAD and the changed ANOVA image was inspected.
- [Student GFM baseline](../active_plans/reports/pipeline_student_gfm_review.md): actual GitHub GFM rendering and browser inspection of 30 files found two source/output mismatches and setup gaps. It is historical baseline evidence, not acceptance of the corrected state.
- The humanizer review made five small jargon edits and no Roots science changes. The updated Roots summary matches the retained course source.
- A historical full-suite checkpoint reported 2,050 passed and one failed in 4.78 seconds. The nonexistent `WORKSHEET_EDITING.md` link was corrected to `USAGE.md#maintain-a-worksheet-after-a-layout-decision`. Later passing checks supersede that failed snapshot; its failure remains documented.
- [Final integration](../active_plans/reports/pipeline_quality_followup_integration.md) accepts all D1-D7 requirements and reconciles 30 current GFM source/API hashes, 43 image references, 16 PDFs, 102 bundle comparisons, and 131 receipt comparisons. It records the final full-suite result after closeout edits. All 12 lesson sources and eight Roots checkpoints are unchanged from HEAD.
- SPEC, QUALITY, and INTEGRATION accept. Expert HCI inspection and temporary runtime-environment proof do not establish a student study or clean-machine installation. Google Sheets import, assistive technology, mobile behavior, and student outcomes remain unverified.
