# Design decisions

<!-- VENDORED HEADER: START -->
Record each durable decision about how this code and repository are shaped, once it is settled, with
the reasoning a later reader needs. Guidance Neil Voss states belongs in
[HUMAN_GUIDANCE.md](HUMAN_GUIDANCE.md), dated history in `docs/CHANGELOG.md`, open discussion in
`docs/active_plans/decisions/`. [PROPAGATED HEADER - ENTRIES BELOW ARE YOURS]
<!-- VENDORED HEADER: END -->

### Temporary Graphify Cargo reconciliation

**Decision.** Reconcile exact Cargo aliases with their AST package twins before
reclustering; verify the resulting IDs against Graphify's loaded graph before writing.

**Why.** Graphify 0.9.80 compares normalized candidate counts with raw JSON counts,
and its original-link export otherwise drops links still pointing to removed aliases.

**Consequence.** Preserve all link records and the active shrinkage guard. Keep the
correction in one removable function; already reconciled upstream output is a no-op.

**Owner.** `normalize_cargo_twins` in
[devel/graphify_prune_tests.py](../devel/graphify_prune_tests.py)
and [devel/graphify_map_repo.py](../devel/graphify_map_repo.py).

Write each decision as a level-three heading with these four fields. `Owner` names the
authoritative code or contract document, rather than a person.

```markdown
### <decision title>

**Decision.** <the durable direction>

**Why.** <the reason it was chosen>

**Consequence.** <the constraint a future change preserves>

**Owner.** <the authoritative code or contract doc>
```

### Single-source tutorial and workbook contract

**Decision.** Use one Markdown file with a Workbook section of GFM tables and a Tutorial
section of list-authored instructions. Generate native DOCX and XLSX, then PDF from DOCX.

**Why.** Writers prefer lists for instructions and can represent these simple spreadsheets
as tables without maintaining a separate formula registry or workbook manifest.

**Consequence.** Workbook tables define initial values; student instruction actions retain
expected assignments for validation without filling student answers in the XLSX. Generated
files do not synchronize edits back to Markdown.

**Owner.** [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md).

### Shared meaning and explicit validation limits

**Decision.** Parse source once into a source-located semantic model consumed by validators
and native output renderers. Track static references and assignment history without evaluating
spreadsheet formulas or claiming statistical correctness.

**Why.** The legacy templates contain blank answer cells, and formula/range consistency
cannot be established merely by checking existing workbook formulas.

**Consequence.** Unsupported formula analysis remains visible as a coverage warning. Use
adjacent projects as implementation references, without importing their application schemas
or depending on their local checkouts.

**Owner.** [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md) and
[tutorial_converter_plan.md](archive/tutorial_converter_plan.md).

### Readable PDF before bundle publication

**Decision.** Reopen LibreOffice output with `pypdf` in strict mode and require a nonempty page tree
before publication.

**Why.** A converter can report success while producing truncated output with a valid PDF header.
The Python reader checks document structure without adding a separate system executable.

**Consequence.** Invalid output fails the staged build and preserves the previous published bundle.
This check does not claim rendered layout or visual review.

**Owner.** [pdf_export.py](../tutorial_lib/pdf_export.py).

### Independent scientific expectations

**Decision.** Keep numerical curriculum checks in developer tooling using SciPy and NumPy,
separate from static source validation and the optional real Google Sheets runner.

**Why.** Formula syntax and reference consistency cannot establish the statistical model,
tail direction, or numerical answer. A locally computed expectation also cannot establish
Google Sheets compatibility.

**Consequence.** Compare live calculated values against independent expectations when credentials
exist. Report dry runs, unavailable credentials, and actual Google execution separately.

**Owner.** [tutorial_oracles.py](../devel/tutorial_oracles.py) and
[GOOGLE_SHEETS_VALIDATION.md](GOOGLE_SHEETS_VALIDATION.md).

### Repaired PETase teaching data

**Decision.** Present the PETase lesson as an illustrative Bradford calibration using explicitly
synthetic standards and unknowns, retaining recoverable narrative and original images.

**Why.** The linked legacy workbook contains unrelated microbial diversity data and supplies no
original Bradford measurements.

**Consequence.** Keep synthetic provenance visible. Interpret Bradford as total protein relative
to a standard, rather than PETase-specific abundance, activity, or fermentation productivity.

**Owner.** [petase_1_linear_regression.md](../tutorial_data/petase_1_linear_regression.md) and
[petase_migration.md](active_plans/reports/petase_migration.md).

### User-selected tutorial layout

**Decision.** Use `make_tutorial.py` for the executable, `tutorial_lib/` for the application
package, `tutorial_data/` for authored lessons and assets, and `tutorial_output/` for default
generated bundles and verification evidence.

**Why.** The latest explicit user instruction selects this coordinated layout and supersedes
the earlier distinct-prefix naming decision.

**Consequence.** Update imports, command examples, source discovery, and default paths together.
Retain existing generated evidence under the renamed ignored output directory; rebuild manifests
after the rename before claiming current artifact provenance. Provide no old-name aliases.

**Owner.** [AUTHORING_GUIDE.md](AUTHORING_GUIDE.md), [tutorial_lib](../tutorial_lib/),
[tutorial_data](../tutorial_data/), and [make_tutorial.py](../make_tutorial.py).

### Focused readiness contracts

**Decision.** Keep the authored schema unchanged while enforcing label ownership and rejecting
instruction items that contain only bold, colon-terminated labels and no substantive continuation,
valid action, nonempty fence, or substantive descendant.

**Why.** The 12-lesson readiness review exposed these gaps in existing source and AST handling; the
current `Label`, `Enter`, `Select`, and `Choose` actions already express the needed work.

**Consequence.** A seeded label is for inspection; a student `Label` assignment starts blank.
Identical repeated assignments continue to warn. An empty child does not make its parent
instruction substantive. Do not add directives or compatibility layers for these cases.

**Owner.** [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md) and the compiler in
[tutorial_lib/compiler.py](../tutorial_lib/compiler.py).

### Targeted workbook and document readability

**Decision.** Freeze worksheet panes at `A2`, keep columns at least 12 characters wide, and add a
native Word `PAGE` footer field. Teach number formats as explicit menu tasks when a lesson requires
them.

**Why.** These defaults make entry worksheets easier to follow while preserving simple authored
tables and an honest boundary around native spreadsheet formatting.

**Consequence.** Do not infer arbitrary formats from cell values or claim full Excel/Sheets
formatting fidelity. Replace misleading worked-example screenshots with native editable tables;
preserve original image assets.

**Owner.** [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md),
[tutorial_lib/workbook.py](../tutorial_lib/workbook.py), and
[tutorial_lib/docx_styles.py](../tutorial_lib/docx_styles.py).

### XLSX formula token serialization

**Decision.** Add the OOXML `_xlfn.` prefix only to recognized modern formula-name tokens when
writing XLSX, and remove it on readback only for recognized tokens.

**Why.** Modern spreadsheet functions otherwise fail to calculate in some engines even though
the authored formula is valid. Prefixing the full formula or rewriting its math would alter the
source semantics.

**Consequence.** Keep authored whitespace, function arguments, strings, references, and
mathematical operations unchanged. Leave unknown functions untouched and report their validation
coverage honestly. Formula normalization is a storage-boundary operation, not calculation.

**Owner.** [formula_io.py](../tutorial_lib/formula_io.py) and [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md).

### Repository and developer import paths

**Decision.** Source both the repository root and `devel/` from `source_me.sh` after it loads
the user's shell configuration.

**Why.** The CLI and tests import the root `tutorial_lib` package, while developer tools and tests
share flat support modules from `devel/`.

**Consequence.** Keep the paths after `.bashrc` because it clears `PYTHONPATH`; run repository
Python commands through `source source_me.sh` so package and support imports resolve consistently.

**Owner.** [source_me.sh](../source_me.sh).

### Preserve archival source characters

**Decision.** Scope the ASCII-compliance check to exclude imported `2025_Artifacts/**` through
the existing layered test registry. Keep new tutorials, application code, and documentation checked.

**Why.** Historical exports contain Unicode characters that must remain unchanged as source
evidence. Editing them solely to satisfy a new implementation's hygiene run would damage provenance.

**Consequence.** This is an explicit archival scope rule, not an ASCII exception for new work.
Source fingerprints verify the original artifacts remain intact.

**Owner.** [conftest.py](../tests/conftest.py).

### Fill-down action and label sizing

**Decision.** Author a spreadsheet fill as one `Fill` action such as `Fill C2:C26: Down`; the range
includes its seeded first row, supports downward filling only, and expands through blank student cells.
Translate with the spreadsheet reference translator and report malformed source formulas through
controlled diagnostics. Estimate workbook widths and wrapping from authored labels and quoted
formula text, including IF decisions, while leaving answer cells blank.

**Why.** Students should enter a formula once and fill the intended range efficiently, while authored
labels and decision text provide evidence for estimating readable dimensions before answers exist.

**Consequence.** Keep this action distinct from repeated `Enter` instructions. Keep student answers
blank and treat dimensions as estimates, not font measurements or calculated formula results.

**Owner.** [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md), [compiler.py](../tutorial_lib/compiler.py), and
[workbook.py](../tutorial_lib/workbook.py).

### Standalone lesson numbering

**Decision.** Number each independently usable Caffeine lesson from Part 1. Caffeine 1 uses Steps 1-5;
Caffeine 2 uses Steps 1-7 with substeps 3.1-3.2 and 6.1-6.4; Caffeine 3 uses Steps 1-7.

**Why.** The three lessons are separate classroom materials, not sequential parts of one document.

**Consequence.** Preserve semantic Part, Step, and Substep markers in each source and render numbering
from that source structure; do not number the lessons as Parts 1, 2, and 3.

**Owner.** [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md) and
[docx_numbering.py](../tutorial_lib/docx_numbering.py).

### DOCX Google Docs style mapping

**Decision.** In generated DOCX, use Google Docs' Normal text, Title, Subtitle, and Heading 1-3
paragraph styles. Map Title to document titles, Subtitle to optional metadata, and Heading 1-3 to
parts, steps, and substeps. Use Normal text for body, lists, formulas, quotes, tables, and the page
footer. Directly format emphasis, code, cell references, menus, and links. Set PT Sans for body text,
PT Sans Narrow for compact table text, and Roboto Mono for formulas, cells, and menus.

**Why.** LibreOffice exported byte-identical DOCX packages with different pagination when Carlito
font files with mismatched versions resolved on the host. The user confirmed these fonts and six
paragraph styles are available in Google Docs, matching the intended import workflow.

**Consequence.** Restrict emitted DOCX paragraph references to the six Google Docs styles and set font
names explicitly so PDF pagination does not depend on inherited theme fonts. Unused stock definitions
may remain in the template. Do not rely on custom tutorial paragraph or character styles; preserve
instructional emphasis through direct formatting. Keep XLSX font styling unchanged. Keep existing
point sizes, spacing, and margins unless rendered evidence requires a focused change.

**Owner.** [docx_styles.py](../tutorial_lib/docx_styles.py) and the PDF conversion contract in
[TUTORIAL_SPEC.md](TUTORIAL_SPEC.md).

### ASCII menu separators

**Decision.** Continue accepting `>` and the Unicode right arrow as `Choose` path delimiters. Render
bold Roboto Mono segments with ASCII ` > ` separators.

**Why.** The selected three-font palette does not include a separate arrow font, and the ASCII menu
separator is already used in authored lessons.

**Consequence.** Normalize either accepted source delimiter to ASCII ` > ` in DOCX; do not require a
fourth font or arrow-glyph fallback.

**Owner.** [TUTORIAL_SPEC.md](TUTORIAL_SPEC.md) and
[docx_inline.py](../tutorial_lib/docx_inline.py).
