# Plan: Single-source spreadsheet tutorials

Status: complete, 2026-10-22. This plan covers the converter implementation and migration of the
requested tutorial collection. The normative behavior is in [TUTORIAL_SPEC.md](../TUTORIAL_SPEC.md).

## Context

The user wants one editable Markdown file containing list-authored tutorial instructions and GFM
tables defining a simple workbook. It generates DOCX for Google Docs, XLSX for Google Sheets, and
a PDF through LibreOffice for visual review. Cell references and formulas need meaningful validation
alongside consistent part/step/substep, menu, and list formatting.

Existing artifacts supply realistic migration and acceptance inputs. Adjacent repositories provide
working source-aware parsing and native DOCX patterns, but neither has this tutorial/workbook model.

## Objectives

- Let tutorial writers maintain instructions and starting spreadsheet data in one readable file.
- Generate the three outputs without duplicating authored formulas or pre-filling student answers.
- Diagnose structural and reference mistakes at their source locations, with explicit coverage limits.
- Produce editable DOCX/XLSX and readable PDF output; assess Google import if access is available.
- Preserve original artifacts and previous successful outputs when validation or conversion fails.

## Design philosophy

Apply **Ground requirements in actual needs** and **Design for adaptability** from
[REPO_STYLE.md](../REPO_STYLE.md): ordinary Markdown lists describe actions, GFM tables describe
workbook values, and a small semantic model joins them. Avoid a separate formula registry, a custom
document language, or an Excel calculation engine. Parse once and let exporters consume resolved
meaning, rather than having each exporter rediscover references from prose.

Apply **Use the scientific method** to Google import fidelity and parser behavior. A short spike
must test the difficult cases before a renderer or parser API becomes a dependency of every module.
If a method loses information needed downstream, change the boundary rather than patching outputs.

## Scope

- Implement the syntax, actions, state tracking, diagnostics, and output contracts in the spec.
- Generate native DOCX and simple XLSX, with LibreOffice Writer PDF conversion.
- Import simple XLSX workbooks into a draft single-source Markdown file.
- Migrate all three Fried Foods/babies tutorials, all five Microbes tutorials, and the three-part
  Dr Caffeine tutorial set.
- Repair PETase as a clearly labeled illustrative example using the approved synthetic Bradford
  dataset because its current source is contaminated by unrelated Microbes content.
- Resolve scientific questions during migration using authoritative sources, and document any
  corrections and their sources.
- Document authoring, operation, limitations, and verification; add focused behavior checks without
  speculative acceptance gates.

## Non-goals

- Build HTML previews, a web editor, a Google add-on, or an automated publishing service.
- Synchronize edits bidirectionally between Markdown and Google Docs/Sheets.
- Reproduce arbitrary Excel formatting, macros, charts, pivots, or formula calculation engines.
- Generate filled answer keys or infer statistical correctness from syntactic formula validity.
- Convert all archived course materials or introduce runtime dependencies on adjacent checkouts.

## Current state summary

Observations from this session:

- The target repository contains starter engineering/documentation infrastructure, with no tutorial
  application. Its README has only a title/license and its changelog was empty before this plan.
- `2025_Artifacts/` contains nine Markdown tutorials and four XLSX files, plus syllabus/schedule,
  tutorial-list TSV, and alternate DOCX/PDF exports. The four XLSX files include a tutorial-list
  workbook; only three are teaching dataset/template workbooks.
- The Fried Foods and Microbes template workbooks have no stored formulas. Blank student outputs
  are expected, so matching only against stored formulas cannot validate the tutorial.
- The Fried Foods two-sample sheet has populated birth-weight data at B2:C25; its guide refers to
  both row 100 and row 101 endpoints. It also mixes `6.1` and `Step 6.3` and duplicates a decision
  instruction. Resolve scientific issues using authoritative sources, then document evidence and
  corrections in the migrated tutorial records.
- The slide builder retains physical source locations in semantic objects and has explicit link
  nodes. Its layout/slot/reveal syntax is specific to slides and is not adopted here.
- The exam project uses python-docx, named styles, limited HTML rich text, and a Writer PDF script.
  Its inline parser does not implement generic Markdown links; its exam schema is not reused.
- The SLIDES path resolves to the external-volume checkout. Its operative rules require LibreOffice
  outside the sandbox on this macOS host. No conversions were run as part of drafting this plan.
- Google URLs could not be read through the available browser tool. Local files supplied the data
  evidence; optional live Google calculation was later attempted, but credentials were unavailable.

Decisions: one source file, list actions, workbook tables, native DOCX/XLSX, and DOCX-derived PDF.
Hypotheses to test: ordinary editable Word runs can retain the desired formula/menu/cell appearance
after Google import, and the selected Markdown parser can retain enough raw table/source detail.

## Architecture boundaries and ownership

Use one root CLI and a small `sheetlesson/` package. The component names below are ownership
boundaries, not a requirement for one class per concept or one file per table row.

| Component | Owns | Does not own |
| --- | --- | --- |
| Markdown parser | Markdown syntax, source spans, raw table geometry | Spreadsheet evaluation or DOCX |
| Semantic compiler | Reserved headings/actions, types, numbering, scope | Output XML or network access |
| Workbook validator | Sparse cells, assignment history, static references, diagnostics | Statistical conclusions |
| DOCX renderer | Native styles, paragraphs, hyperlinks, images, pagination intent | Re-parsing authored formulas |
| XLSX I/O | Typed workbook serialization, simple import, logical round-trip | Student instruction execution |
| PDF exporter | LibreOffice Writer execution and fresh-output verification | Independent tutorial layout |
| Build coordinator | Staging, publication, reports, command outcomes | Domain parsing rules |

The parsed model carries `SourceSpan(path, start_line, end_line)`, ordered content blocks, sheet
declarations, typed cell seeds, and typed instruction actions. The resolved model adds worksheet
identity, displayed numbering, cell/range objects, instruction availability states, and links.
Diagnostics carry category/severity/location/message/correction and an optional related location.
Use sparse coordinates for cells, retaining rectangle extents separately for overlap checks.

Freeze shared model fields and semantics after the first vertical example. Exporters consume that
resolved model and must not mutate it. Formula literals and literal string values retain their
semantic text; matching tokens are separate from displayed text. Alternative branches preserve
possible assignment states without executing calculations or implementing a general workflow engine.

Initial dependency candidates are `markdown-it-py`, `python-docx`, and `openpyxl`, declared in the
runtime requirements. Confirm parser table/source-position behavior in M1 before committing to its
adapter. Use an existing Markdown parser; extend only semantic recognition and source mapping.
Do not copy the exam project's limited HTML regex parser as the tutorial parser. Use stdlib JSON
for the explicit quoted scalar convention; add other dependencies only for demonstrated needs.

### Mapping (milestones -> components)

| Milestone | Component | Review boundary |
| --- | --- | --- |
| M1 | Syntax sample, parser adapter, renderer probes | Authoring and Google import feasibility |
| M2 | Semantic compiler and validator | One source meaning and actionable diagnostics |
| M3 | XLSX I/O and importer | Cell/value/type preservation and blank answers |
| M4 | DOCX renderer | Editable prose, lists, formulas, links, and assets |
| M5 | Build coordinator and PDF exporter | Complete, fresh, safely published bundles |
| M6 | Full tutorial collection, documentation, verification | Real authoring and delivery workflow |

### File scope

| File or directory | Intended change | Canonical source, for generated output |
| --- | --- | --- |
| `tutorial.py` | Thin application CLI | Authored code |
| `sheetlesson/` | Parser, model, validation, DOCX/XLSX I/O, build and PDF modules | Authored code |
| `pip_requirements.txt` | Runtime dependencies | Verified imports |
| `Brewfile`, `source_me.sh` | Only required runtime tooling/environment updates | Existing environment contract |
| `tutorials/` | The migrated babies, Microbes, Dr Caffeine, and PETase tutorials and needed local images | Reviewed legacy artifacts |
| `output/` | Ignored output bundles and validation manifests | Example/user Markdown and assets |
| `tests/` | Few retained contract tests, inline inputs and tmp_path workbooks | Spec acceptance contracts |
| `tests/_temp/` | Temporary probes and import/PDF evidence | Real source/output samples |
| `README.md`, `docs/USAGE.md`, `docs/INSTALL.md` | Purpose, first build, dependencies and workflow | Implemented CLI |
| `docs/AUTHORING_GUIDE.md`, `docs/TUTORIAL_SPEC.md` | Short writer guide and normative behavior | User decisions and accepted contracts |
| `docs/active_plans/reports/` | Pilot migration and import/visual acceptance records | Observed results |
| `docs/HUMAN_GUIDANCE.md`, `docs/DESIGN_DECISIONS.md`, `docs/CHANGELOG.md` | Correctly attributed guidance, decisions and history | Session/implementation evidence |

Keep `2025_Artifacts/` and both adjacent projects unchanged. Runtime outputs never become input
authority. Refine module filenames as cohesive responsibilities emerge; no deep package tree.

## Milestone plan

| M | Title | Summary | Goal |
| --- | --- | --- | --- |
| M1 | Prove the authoring path | Small parser and DOCX import experiments | Resolve foundational uncertainty |
| M2 | Compile and validate | Implement semantic model, numbering and cell checks | Reliable source meaning |
| M3 | Build workbook round trips | XLSX generation and import-to-Markdown | Preserve data and blank tasks |
| M4 | Render editable documents | Styles, links, formulas, tables and images | Useful Google Docs source |
| M5 | Publish complete bundles | CLI, PDF conversion, staging and reports | One-command three-output build |
| M6 | Migrate and assess the collection | All tutorial migrations, local checks, PDF review and docs | Evidence-backed release candidate |

### Milestone: Prove the authoring path

M1 depends on this spec; entry is a reviewed reading of its syntax and representative local sources.
Deliver a small single-source sample and temporary probes for escaped pipes, backticks, nested
lists, reference-style images, empty cells, and physical line reporting. Generate a minimal DOCX
containing headings, formula text, cell hyperlinks, and menus; inspect its LibreOffice PDF. If
Google access is available, import is useful optional evidence, not a milestone dependency. This is
not a production parser or final styling pass.

Decision rule: accept the parser if it retains needed source information or permits a small isolated
table-source adapter. If it silently discards geometry, compare one alternative before committing.
Accept DOCX style/run choices when local structure and rendered output retain editable/copyable
text and useful links. If Google import is available, use its observed result to guide adjustments.
Do not use formula screenshots or make unavailable Google access an acceptance dependency.

Exit: chosen parser adapter and native DOCX strategy, concrete syntax sample, bounded limitations,
and a settled shared model. Parallel-plan ready: no; later work depends on these contracts.

### Milestone: Compile and validate

M2 depends on M1's source/model contract. Deliver heading numbering, sheet/table/scalar parsing,
list actions, worksheet resolution, explicit alternatives/replacements, formula tokenization for
static references, and diagnostics. Preserve ordinary Markdown content around semantic actions.
Implement `lint` so this milestone is directly usable without LibreOffice.

Exit: minimal example resolves correctly; deliberate wrong-sheet/overlap/assignment conflicts fail
with exact source locations; range overshoot and unsupported formulas warn without false certainty.
Permanent tests protect selected contracts, not token/class layouts. Parallel-plan ready: yes;
parser and validator responsibilities can separate once model and diagnostic contracts are fixed.

### Milestone: Build workbook round trips

M3 depends on M2's typed workbook and instruction-destination model. Deliver sparse XLSX writing,
entry-cell styling, logical read-back verification, and `import-xlsx` with unsupported-feature
inventory and draft scaffolding. Preserve row/column positions, blanks, text/number distinctions,
and formulas. Verify that student actions are not serialized as answers.

Exit: the existing Fried Foods workbook's populated cells round-trip through draft Markdown and
generated XLSX without changed addresses/types/values, allowing documented loss of presentation.
Unrepresentable workbook content blocks import before a misleading draft is published.
Parallel-plan ready: yes; XLSX work is independent of DOCX after M2.

### Milestone: Render editable documents

M4 depends on M2 and the M1 style evidence. Deliver native DOCX content and styles, worksheet/cell
hyperlinks, internal bookmarks, images, nested lists, menus, and formula blocks. Use the existing
exam project as a reference for python-docx techniques, not a runtime import or copied exam schema.

Exit: document XML and a rendered sample preserve text and action order; formulas copy exactly as
semantic source text; Google mapping is applied only when supplied; workbook-only content is absent
from student prose. Parallel-plan ready: yes; this can proceed alongside M3 with fixed model inputs.

### Milestone: Publish complete bundles

M5 depends on M3 and M4. Deliver the complete CLI, format subset selection, LibreOffice Writer
wrapper, staging/publication, artifact ownership checks, and validation JSON. Document the macOS
unsandboxed conversion lane. Verify outputs belong to this run, not stale files.

Exit: default build produces all three outputs; DOCX/XLSX-only iteration works without LibreOffice;
an induced PDF failure leaves the previous bundle intact and returns nonzero; modified outputs
cause an actionable conflict. Parallel-plan ready: no for integration/publication; focused export
and failure-path checks may run independently after the coordinator is working.

### Milestone: Migrate and validate the tutorial collection

M6 depends on M5. Migrate all three Fried Foods/babies tutorials, all five Microbes tutorials, and
the three-part Dr Caffeine set into single-source Markdown tutorials. Repair PETase as an
illustrative regression tutorial using the approved synthetic Bradford dataset, clearly labeled
synthetic in its source and migration report. Record migration choices, scientific concerns, and
source relationships. The migrated collection should exercise embedded images, multiple workbook
layouts, and the supported statistical procedures.

Exercise author edits: insert a Step, move a table block and update its references, change a formula,
and rename a worksheet. Check both success and useful diagnostics with behavior tests. Verify local
DOCX/XLSX structure and content, then use agent visual assessment of rendered PDFs. Agents resolve
scientific migration issues against authoritative sources and record the evidence and corrections.
Attempt live Google Docs/Sheets import only if access is available; it is optional and must not be
reported as tested without observed evidence.

Exit: every tutorial has a reviewed single-source Markdown file and local acceptance evidence,
including the synthetic-data label for PETase. Automated DOCX/XLSX behavior checks pass and agents
assess rendered PDFs. Scientific corrections and supporting authoritative sources are documented.
Google acceptance is optional and is claimed only when observed. Human milestone signoff is not
required. Writer guide, usage, installation, and change records match actual behavior. Review
remaining temporary checks for removal/promotion.
Parallel-plan ready: yes; migration, visual review, and documentation can separate after M5.

## Test and verification strategy

Follow [PYTEST_STYLE.md](../PYTEST_STYLE.md) and the existing repository checks. Run Python with
`source source_me.sh && python3`; use `source source_me.sh && python3 -m pytest tests/` for the
required implementation suite. Do not add permanent tests merely to mirror every module or example.

Retain a small set of deterministic offline behavior tests for these plausible regressions:

- Semantic formula/string preservation, including pipes, quotes, and absolute references.
- Worksheet/address resolution and source-located errors, without matching entire error prose.
- Automatic numbering and independent alternative branches using compact inline examples.
- XLSX type/address round trips and the exclusion of student answers from seeded values.
- DOCX native formula/link content and failed-build preservation of an existing owned bundle.

Use inline data and temporary paths rather than a growing fixture collection. LibreOffice and PDF
page inspection provide one-time integration evidence across the migrated collection. Google
imports are optional, and neither imports nor visual review become dependencies of fast behavior
tests. Existing repository checks still apply to changed code.

| Acceptance evidence | Blocks | Failure response |
| --- | --- | --- |
| Spec/source structural contracts | Publication of the affected tutorial | Correct the source or compiler defect |
| Logical XLSX round trip | Workbook publication | Fix type/address serialization before release |
| DOCX text/link integrity | Document publication | Fix renderer; preserve editable text |
| Current-run PDF creation | Complete default build | Report conversion failure; preserve prior bundle |
| PDF visual review | Local visual acceptance | Agent assessment; adjust styles/flow and inspect changed pages |
| Google Docs/Sheets import | Google-verified claim only | Optional when access is available; claim only observed results |
| Scientific issue review | Accuracy of migrated content | Resolve against authoritative sources and document corrections |

The known B2:B100/B2:B101 versus B2:B25 mismatch is useful diagnostic evidence, not a golden output
whose exact warning wording must become permanent. Do not benchmark arbitrary runtime or require
byte/pixel identity where content/layout may intentionally improve.

## Migration and compatibility policy

Use the original files as read-only evidence. Normalize structural headings and action lists in new
migrated sources. Include full original datasets, not the small illustrative spec sample. Record
changed ranges and scientific issues with authoritative sources and corrections. The converter
cannot make statistical claims correct merely by matching formulas to cell addresses. Use explicit
alternatives for competing formulas.

The new unified format is the v1 authority. Unannotated legacy prose is not automatically considered
validated; manually normalize it or report the unbound references. Keep old files until the user
chooses otherwise. Do not migrate the unrelated tutorial-list workbook or syllabus as teaching data.

## Risk register

| Risk | Impact | Trigger | Owner | Mitigation |
| --- | --- | --- | --- | --- |
| Syntax becomes cumbersome | Writers avoid maintained sources | Repeated annotations or duplicated formulas | Parser/spec | Preserve list/table conventions; revise during M1 |
| Parser loses raw geometry | Wrong cell addresses or locations | Ragged tables silently normalized | Parser | Inspect raw spans before semantic table construction |
| Spreadsheet references overclaimed | Incorrect confidence in teaching content | Dynamic functions or missing inputs | Validator | Report coverage and uncertainty separately |
| Student answers leak | Exercise is pre-solved | Actions treated as seed writes | XLSX I/O | Separate seed cells from instruction state and test it |
| Google changes formatting/links | Poor delivered tutorial | Available import differs from local PDF | DOCX renderer | When import access exists, assess observed results and simplify native styling |
| Snapshot/link drift | Links open wrong workbook/tab | New upload or student copy | Author/validator | Explicit mapping and visible worksheet labels |
| XLSX import loses semantics | Changed starting data | Merges, dates, rich types, unsupported features | Importer | Inventory and stop on semantic loss |
| PDF crash or stale output | Broken or misleading bundle | Sandbox invocation/conversion failure | Build coordinator | External conversion lane, staging, fresh verification |
| Spec and implementation diverge | Inconsistent authoring guide | Unrecorded expedient syntax changes | Implementer | Update normative spec and decisions with each change |

## Rollout and release checklist

- [x] Complete M1-M5 local implementation with focused behavior and repository checks.
- [x] Migrate all three Fried Foods/babies tutorials, all five Microbes tutorials, the three-part Dr Caffeine set, and the clearly labeled synthetic-data PETase example.
- [x] Verify editable DOCX, logical XLSX contents, and PDF visual quality.
- [x] Attempt optional Google calculation: unavailable without ADC; no live result is claimed.
- [x] Demonstrate source editing, table relocation, worksheet rename, and failed-build preservation workflows.
- [x] Confirm no original artifacts, sibling repositories, or Google documents were overwritten.
- [x] Publish documentation and runtime dependency instructions matching the actual CLI.
- [x] Review temporary checks, promote only justified coverage, and remove obsolete PDF review copies.

## Documentation close-out requirements

This plan is the implementation tracker: mark workstream status and link evidence as work progresses.
Keep [TUTORIAL_SPEC.md](../TUTORIAL_SPEC.md) normative and make the authoring guide shorter and
example-led. Record human preferences in [HUMAN_GUIDANCE.md](../HUMAN_GUIDANCE.md), implementation
decisions in [DESIGN_DECISIONS.md](../DESIGN_DECISIONS.md), and dated work in
[CHANGELOG.md](../CHANGELOG.md). Existing starter guidance is preserved rather than reattributed.
Execution is complete. This plan and its execution ledger are archived under `docs/archive/`.
Implementation evidence is summarized in
[implementation_validation.md](../active_plans/reports/implementation_validation.md).

## Open questions and decisions needed

There are no unanswered user choices blocking implementation. Defaults are established in the spec.
M1 owns parser/style experiments with explicit decision rules; M6 owns external acceptance evidence.
Future named-range authoring, filled instructor workbooks, Google automation, mathematical typesetting,
and broad legacy import are separate proposals, not hidden prerequisites for this release.
