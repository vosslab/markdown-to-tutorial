# Plan: Restore instructional voice across tutorial materials

Status: **COMPLETE** (2026-10-22). All five milestones are accepted in the
[final integration review](reports/voice_final_integration.md).

## Context

The direct comparisons in [the Babies report](reports/voice_babies_original_comparison.md),
[the Caffeine report](reports/voice_caffeine_original_comparison.md), and
[the Microbes and PETase report](reports/voice_microbes_petase_original_comparison.md) find that
migration changed original paragraphs, descriptive headings, humor, and compact numbered action
groups into repeated action-label bullets. These differences appear in the generated student
materials, so the existing quality-review completion claims do not establish fidelity to the
original teaching voice.

The generator already builds DOCX, XLSX, and PDF bundles, and recent repository evidence reports
successful builds and calculations. The unresolved failure is the content and authoring contract:
the action syntax has been allowed to dominate prose presentation, and reviewers compared many
tests or migration summaries without consistently closing the direct original-to-student-materials
comparison. The Caffeine source is incomplete and needs added lesson content, while its existing
good prose still needs protection. This plan restores source fidelity and makes semantic actions
coexist with authored prose and headings in the generated materials.

## Objectives

- Restore original wording, descriptive headings, humor, paragraph cadence, and compact numbered
  groups across all 12 lessons, except where technical references, formulas, data, or verified
  scientific errors require correction.
- Keep the semantic actions machine-readable without making action labels or hidden formula lists
  part of the students' visible lesson prose.
- Complete the Caffeine three-part set from its outline while preserving its accurate, useful prose
  and filling only missing instructional content.
- Verify every lesson against its original source and actual generated student pages and workbooks.

## Design philosophy

Apply **Fix the design, not the symptom** and **Ground requirements in actual needs** from
`docs/REPO_STYLE.md`: separate action meaning from paragraph presentation, preserve authored source
as the authority for voice, and verify the products students receive. Keep the semantic layer small
and closed. Do not solve this by heuristically rewriting prose or accumulating presentation flags.

## Scope

- Record the approved source and workbook semantics contract in the implementation and authoring
  documentation.
- Separate semantic action parsing and replay from visible paragraph composition in the compiler
  and renderers.
- Restore the twelve source lessons using the comparison reports as correction maps and original
  sources as wording authority.
- Rebuild all lesson bundles and review actual source, rendered pages, and spreadsheet regions.
- Record focused durable contract tests, independent specification and quality reviews, and final
  integration evidence.

## Non-goals

- Rewrite scientifically sound original prose for uniformity, brevity, or generic textbook tone.
- Move workbook data, answers, or calculations to new cells for visual style alone.
- Add heuristic prose rewriting, hidden duplicate formula inventories, a new theme-configuration
  system, or broad authoring features beyond the approved contract.
- Treat tests passing, migration completion, or prior approval of a rewritten version as proof of
  original-voice fidelity or student learning.
- Claim student outcomes, live Google Docs/Sheets fidelity, or Google calculation behavior without
  direct evidence from those environments.

## Current state summary

### Observations

- Three independent comparison reports document voice changes across Babies, Caffeine, Microbes,
  and PETase, with source anchors and specific technically required exceptions.
- Babies and Microbes are established lessons whose teaching experience should be retained.
- Caffeine's original outline is a draft foundation. Some prose is already good and accurate; missing
  lesson content must be developed without replacing that prose.
- PETase's fictional variant-performance narrative is a scenario premise to preserve. The supplied
  Bradford assay supports total-protein estimates, so inferring PETase amount or activity from it is
  a genuine scientific error. The copied Microbes exercise chunk is unrelated and remains excluded.
- Current repository artifacts and evidence cover all 12 lessons, but those checks did not prevent
  the original-voice regression.

### Progress ledger (2026-10-22)

- **M1-M2 complete: core contract accepted.** Ordered semantic actions remain separate from
  visible authored text. Closed workbook roles convey meaning without filling student answers.
  [Core quality](reports/voice_core_quality.md) accepts the design; the
  [final rendering SPEC](reports/voice_last_rendering_spec.md) accepts the local label, hardbreak,
  heading, and pagination repairs with 177 focused checks. Integration matched all seven reviewed
  code/source fingerprints to the final files.
- **M3 complete: all 12 sources restored and reviewed.** Original prose, headings, humor, and
  nested numbered groups are retained subject to narrow technical/scientific corrections. Caffeine
  retains good draft prose and completes missing instruction. PETase keeps its fictional strain
  premise while limiting Bradford conclusions to total protein. Independent source acceptance is
  recorded for [Babies](reports/voice_babies_source_recheck.md),
  [Caffeine](reports/voice_caffeine_source_spec.md), and
  [Microbes and PETase](reports/voice_microbes_petase_source_spec.md), with the last numeric alpha
  and blank spacer corrections confirmed by the final rendering SPEC. The
  [summary](reports/voice_restoration_summary.md) links the actual recovery maps, superseding
  initial restoration claims.
- **M4 complete: final outputs rebuilt and accepted.** The current build contains all 36
  DOCX/XLSX/PDF products and 12 validation reports, totaling 92 PDF pages. LibreOffice Calc passed
  13 scenarios / 254 comparisons with unchanged expectations. Integration independently verified
  all 60 source/artifact hashes and every page count against the
  [final build receipt](reports/voice_restoration_final_build.md).
  [Fresh material quality](reports/voice_final_material_recheck.md) accepts all 12 bundles after
  reviewing all 92 pages as contacts and 21 full-size pages. All prior concrete findings are closed;
  all workbook layouts match earlier actual renders except the intended Microbes 5 blank correction.
- **M5 complete: documentation and integration accepted.** Authoring docs, README example, evidence ledger, and final
  screenshots describe the implemented contract. Both managed screenshots are current; integration
  matched their receipt to all five source/product/image hashes. The
  [final integration report](reports/voice_final_integration.md) records 1,548 passing repository
  tests, the final fingerprints, and ACCEPT. All source/specification/material findings are closed.
- **Evidence boundary:** local Calc is not Google Sheets validation. Google Docs/Sheets import and
  live calculation remain unverified. No student study or learning outcome is claimed. Original PDF
  comparisons exist only for Babies; the other original comparisons use Markdown/outline/workbook.
- **Overall: COMPLETE.** Source, rendering specification, final material quality, fingerprint,
  and final repository checks are accepted. The completed plan stays at this referenced path.

### Decisions

- Original source wording and descriptive section structure are the default. Change prose only to
  correct technical references, formulas, data, or genuine scientific errors, or to add missing
  Caffeine instruction.
- Approved action syntax uses semantic links around the existing visible text: `label:A1`,
  `enter:A1`, `replace:A1`, `fill:A2:A26`, and `select:A1:B26`. Values or formulas appear once in
  the visible label/action text. Multiple actions in one paragraph retain their order.
- These links render their existing text and never expose semantic URIs. The action model and replay
  remain compatible with legacy actions. Existing backtick and bare-green-formula parsing stays.
- Existing worksheet-scope directives remain; an omitted scope defaults to the sole worksheet.
- Workbook roles use a closed set of meanings in a hidden Workbook section, with declarations such
  as `- **Region A1:B26:** source`. Roles describe meaning, not permission. Seeded tables default to
  `source`, calculation-entry regions to `calculation`, and result and interpretation regions are
  declared explicitly when needed without overlap.
- Preserve original heading text, case, emphasis, and canonical standalone Part/Step/Substep
  numbering. Correct incoherent source numbering when required. Heading-prefix metadata supports
  bold and case-insensitive matching without changing visible headings.
- The first proof slice is Caffeine Part 3 Step 9: four related actions (add column, label, enter
  formula, fill down) presented compactly, alongside preservation of good prose. Babies 2 is a
  previously broad comparison and supplies a second established-lesson check.

## Architecture boundaries and ownership

### Mapping (milestones -> components)

| Milestone | Component | Review boundary |
| --- | --- | --- |
| M1 | Semantic action parser, model, validation | Meaning and replay are independent from visible paragraph wording; contract review |
| M2 | DOCX and workbook renderers | Existing authored text stays visible; workbook regions carry semantic roles |
| M3 | Twelve canonical lesson sources | Source-to-current corrections, with technical exceptions noted |
| M4 | Generated DOCX/XLSX/PDF bundles | Current outputs represent current sources and student-facing layout |
| M5 | Authoring docs, review reports, integration record | Contract discoverable; direct comparisons and independent review complete |

### File scope

| File or directory | Intended change | Canonical source, for generated output |
| --- | --- | --- |
| `tutorial_lib/parser.py`, `compiler.py`, action/model modules | Parse semantic actions and compose visible source text independently | Markdown tutorial source |
| `tutorial_lib/docx_inline.py`, `docx_renderer.py`, `docx_styles.py` | Bind action semantics to existing text; preserve heading styling and numbering | Markdown tutorial source |
| Workbook renderer modules under `tutorial_lib/` | Render declared semantic regions and preserve workbook meaning | Markdown Workbook section and table |
| `tutorial_data/*.md` (12 lessons) | Restore prose and grouping; correct only approved technical/scientific issues; complete missing Caffeine content | Original 2025 lessons, Caffeine outline, current data and formulas |
| `tests/test_tutorial_semantics.py`, `tests/test_tutorial_docx.py`, focused workbook tests | Retain only durable parser, replay, visible-text, heading, and region-role contracts | Approved authoring contract |
| `docs/AUTHORING_GUIDE.md`, `docs/TUTORIAL_SPEC.md` | Explain semantic syntax and workbook region roles with concise examples | Implemented contract |
| `README.md`, previews, quality reports | Refresh only where current behavior or examples change; add comparison and integration receipts | Current sources and generated materials |
| `tutorial_output/` | Rebuild current DOCX/XLSX/PDF artifacts and review evidence | `tutorial_data/*.md` |
| `docs/HUMAN_GUIDANCE.md`, `docs/CHANGELOG.md` | Record user's correction and this plan's work entry | Direct user instruction and current work |

The comparison reports remain evidence and correction maps; original materials remain read-only
wording authorities. Specific original files are identified in those reports and the external
`Tutorial_Outline.md`; do not edit those sources as part of this plan.

## Milestone plan

| M | Title | Summary | Goal |
| --- | --- | --- | --- |
| M1 | Separate action meaning | Implement the shared semantic action contract and validation | Actions replay without prescribing paragraph presentation |
| M2 | Bind semantics to output | Render existing text and workbook regions using their roles | Student output shows original prose with useful spreadsheet meaning |
| M3 | Restore lesson sources | Prove the method, then restore the remaining original lessons | Twelve accurate sources retain their teaching voice |
| M4 | Rebuild and inspect | Build all bundles and review actual student-facing pages and workbook regions | No source/output drift or blocking content/layout issues |
| M5 | Close documentation and review | Update instructions, publish evidence, and complete fresh integration review | Current, independently reviewed result is ready for human review |

### Milestone M1: Separate action meaning

- Depends on: None; the comparison reports and approved contract are available.
- Deliverables: Shared action representation, parser, validation, and replay behavior for all five
  action forms; legacy action compatibility; multiple ordered actions per paragraph.
- Workstreams: Parser/model behavior; validation and focused contract coverage.
- Entry criteria: Record baseline failures separately from changed-surface behavior; use
  `source source_me.sh && python3` for Python commands.
- Exit criteria: Semantic action links do not become visible URIs or action-label prose; formulas
  and values occur once in visible lesson text; malformed regions/actions receive direct diagnostics;
  old replay behavior remains supported. Focused durable tests cover only stable behavior.
- Parallel-plan ready: no; parser and action-model ownership is a shared contract that must settle
  before renderer bindings.

### Milestone M2: Bind semantics to output

- Depends on: M1; renderers need the stable action contract.
- Deliverables: DOCX text binding and heading visual styles; workbook region-role rendering for
  source, calculation, result, and interpretation areas; optional formula/value hyperlinks where
  the destination is known, while fill guidance stays plain text.
- Workstreams: DOCX paragraph/action binding; workbook region role presentation.
- Entry criteria: M1 action/model examples parse and replay.
- Exit criteria: Existing visible source text is preserved exactly through semantic link rendering;
  heading text, case, emphasis, and canonical numbering remain authored; seeded and calculation
  regions receive expected meaning styles; explicitly declared result/interpretation regions render
  without conflicting declarations; worksheet defaulting works for a single-sheet source.
- Parallel-plan ready: yes; the DOCX and workbook renderer changes have separate output ownership
  after M1 fixes their shared contract.

### Milestone M3: Restore lesson sources

- Depends on: M2; the authoring syntax must be usable in actual lessons.
- Deliverables: First Caffeine Part 3 Step 9 proof; Babies 2 voice proof; restoration and technical
  exception notes for all twelve sources.
- Workstreams: Caffeine three-part source completion; established Babies/Microbes restoration;
  PETase narrative restoration with qualified synthetic data and assay limits.
- Entry criteria: M2 passes a representative source-to-DOCX and source-to-workbook example.
- Exit criteria: The first proof preserves four compact Step 9 actions and existing accurate prose;
  each comparison report's anchors are resolved; original headings and wording return wherever
  sound; cell references, formulas, data, and verified scientific corrections remain accurate;
  no action semantics require visible operational labels or duplicate formula listings. All twelve
  sources build successfully.
- Parallel-plan ready: yes; the three lesson groups are source-independent once the authoring and
  renderer contracts are fixed. Merge content changes without overwriting one another.

### Milestone M4: Rebuild and inspect

- Depends on: M3; current student materials must come from the restored sources.
- Deliverables: Rebuilt 12 DOCX/XLSX/PDF bundles; a file-backed review ledger distinguishing source
  observations, decisions, and completion evidence; a representative and then complete comparison
  of actual student materials.
- Workstreams: Builds/calculation evidence; document visual review; workbook semantic and learner
  task walkthrough; original-to-current voice comparison.
- Entry criteria: All twelve source edits are complete. LibreOffice-dependent builds, imports, and
  exports run outside the sandbox through repository scripts.
- Exit criteria: Every generated artifact is current; actual PDF pages show preserved headings,
  compact numbered groups, and readable formulas; actual workbooks show correct source/calculation/
  result/interpretation regions and blank answer cells; formulas calculate as expected in the local
  available spreadsheet engine; each of twelve original-to-generated comparisons is resolved.
  Tests support these claims but do not substitute for inspecting student materials.
- Parallel-plan ready: yes; PDF review, workbook review, and source fidelity comparisons can proceed
  against the same frozen build.

### Milestone M5: Close documentation and review

- Depends on: M4; documentation and independent review must describe final artifacts.
- Deliverables: Updated authoring specification/guide, current README examples/previews as needed,
  focused review reports, and an integration record with current source/output hashes and limits.
- Workstreams: Author documentation; fresh independent specification and quality review; final
  integration and changelog closeout.
- Entry criteria: M4's source and artifact set is stable.
- Exit criteria: A fresh reviewer accepts the semantic specification against implementation and
  source; a separate reviewer inspects original and generated student materials; integration
  confirms all sources, outputs, and screenshots/preview links are current. No claim implies live
  Google behavior or student outcomes without direct evidence.
- Parallel-plan ready: yes; documentation updates and independent review may proceed together from
  the stable M4 evidence.

## Test and verification strategy

Use focused tests for durable behavior: parsing each action form, preserving visible text, ordered
multi-action replay, legacy replay, validation of workbook regions, heading-prefix recognition, and
single-sheet scope defaulting. Avoid tests that encode particular lesson prose or duplicate renderer
internals. Run the relevant focused tests and repository suite using the repository's Python
bootstrap; report existing baseline failures distinctly.

Build all twelve current bundles from canonical Markdown. Review rendered DOCX/PDF pages and actual
XLSX regions directly. For each lesson, compare original source wording and structure with current
Markdown and generated student materials. Workbook review includes formulas, starting data, answer
cell blanks, and the learner's path through action groups. Use local calculation evidence where
available, stating the engine and its limits. Run all LibreOffice-dependent commands outside the
sandbox through repository scripts.

Independent review has two separate questions: does implementation match the semantic/action and
region-role specification, and do original versus generated materials preserve voice and learner
flow while keeping scientific corrections? Address blockers in their owning files, rebuild affected
bundles, and repeat only the relevant review plus final integration checks. The completion decision
comes from these product comparisons; test success alone is insufficient.

## Risk register

| Risk | Impact | Trigger | Owner | Mitigation |
| --- | --- | --- | --- | --- |
| Semantic actions become visible labels or duplicate formulas | Voice regression returns | Rendered text differs from authored visible text | Parser/renderer | Keep source text as the rendered payload; test visible text and inspect real pages |
| Voice restoration reintroduces factual errors | Student-facing science becomes false | Original statement conflicts with current data or evidence | Lesson source owner | Apply only the documented technical exceptions; retain source comparison notes |
| Caffeine completion replaces already-good prose | New content is less authentic and useful | Broad rewrite during gap filling | Caffeine source owner | Mark missing sections; add around sound text and compare each edit to outline |
| Workbook role declarations overlap or infer permission | Styles misstate data meaning | Ambiguous or conflicting region role | Workbook renderer/source owner | Use closed semantic roles, explicit declarations, and controlled conflict diagnostics |
| Evidence relies on tests or migration summaries alone | Student-facing defect survives | No page/workbook inspection receipt | Review owner | Require actual source and generated artifact comparison for each lesson |
| Parallel content edits collide | Source changes are lost | Two edits touch the same lesson or shared contract | Integration owner | Assign disjoint source ownership and merge against the shared contract; inspect final diff |

## Rollout and release checklist

- [x] Keep original sources and outline read-only; restore canonical tutorial Markdown.
- [x] Build current DOCX/XLSX/PDF outputs through repository scripts.
- [x] Review actual generated pages and workbook regions after the final source rebuild.
- [x] Update preview/example artifacts only from current canonical outputs.
- [x] Report local calculation engine, unavailable Google checks, and student-outcome limits accurately.
- [x] Leave final file changes and evidence ready for human review; do not imply release or commit.

## Documentation close-out requirements

- Plan / progress tracker: this file, updated as evidence arrives and retained at this referenced
  path when complete.
- `docs/CHANGELOG.md` entry: record this plan and later implementation/review results under their
  appropriate dated category.
- `docs/HUMAN_GUIDANCE.md`: preserve the user's latest explicit voice-restoration correction.
- Authoring docs: update `docs/AUTHORING_GUIDE.md` and `docs/TUTORIAL_SPEC.md` to the implemented
  contract and examples.
- Reports: record semantic SPEC, actual source-to-output quality review, and final integration
  evidence in `docs/active_plans/reports/`.
- Closure notes: mark this referenced plan complete only after all milestones and documentation
  are done; retain its location so the current review links remain stable.
- Temporary verification closeout: remove temporary evidence/checks that are not intentionally
  retained; keep only justified permanent contracts.

## Open questions and decisions needed

- Manager/subagent decision procedure:
  - Decision owner or dedicated class: implementation integrator for code contracts; source editors
    for lesson-level technical exceptions, grounded in comparison reports and current data.
  - Evidence and decision rule: preserve the original wording unless it is technically inaccurate,
    confusing after workbook changes, or absent from incomplete Caffeine material. Record each
    exception at the source comparison anchor and verify its generated rendering.
- Non-blocking follow-up: live Google Docs/Sheets import and calculation can be checked if credentials
  and access exist; otherwise report them as unverified without blocking local completion.

## Evidence and decision ledger

| Type | Record | Authority |
| --- | --- | --- |
| Observation | Repeated action labels fragment prose and numbered groups in all comparison sets | Three `voice_*_original_comparison.md` reports |
| Observation | Existing mechanical builds and tests did not establish original-voice fidelity | Current review reports and this regression |
| Decision | Preserve wording, headings, humor, and compact numbered groups; change only technical/data/scientific errors and missing Caffeine content | User's latest correction, recorded in `docs/HUMAN_GUIDANCE.md` |
| Decision | Semantic action links carry meaning while rendering only the existing visible text | Approved implementation contract |
| Decision | Workbook regions state closed semantic roles; roles do not grant permissions | Approved implementation contract |
| Completion evidence | Actual source, PDF, DOCX, and workbook comparison across twelve lessons, followed by fresh independent review | Milestones M4-M5 |
