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

**Owner.** [pdf_export.py](../sheetlesson/pdf_export.py).

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

**Owner.** [petase_1_linear_regression.md](../tutorials/petase_1_linear_regression.md) and
[petase_migration.md](active_plans/reports/petase_migration.md).

### Distinct executable and library names

**Decision.** Keep the command-line executable named `tutorial.py` and name the application
package directory `sheetlesson/`.

**Why.** Distinct prefixes let shell autocomplete distinguish the executable from the library.

**Consequence.** Active imports and documentation use `sheetlesson`; do not add a
`tutorial_lib` compatibility alias that restores the autocomplete collision.

**Owner.** [tutorial.py](../tutorial.py) and the [sheetlesson package](../sheetlesson/).

### Repository and developer import paths

**Decision.** Source both the repository root and `devel/` from `source_me.sh` after it loads
the user's shell configuration.

**Why.** The CLI and tests import the root `sheetlesson` package, while developer tools and tests
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
