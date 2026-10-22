# Usage

Run commands from the repository root after loading its shell environment:

```bash
source source_me.sh
```

Choose a lesson from [TUTORIAL_CATALOG.md](TUTORIAL_CATALOG.md), which indexes all 12 migrated
sources, including the explicitly synthetic PETase calibration example.

## Validate and build

Lint checks one source without writing output files:

```bash
python3 tutorial.py lint tutorials/babies_1_z_test.md
```

Build DOCX, XLSX, and PDF into `output/<source-stem>/`:

```bash
python3 tutorial.py build tutorials/babies_1_z_test.md
```

On this macOS host, an agent must invoke this build command with
`sandbox_permissions="require_escalated"` so the project's LibreOffice conversion wrapper runs
outside the sandbox. The command above runs normally in a human terminal. PDF output is reopened
with a PDF reader and must contain pages before the bundle is published.

Use `--format` to build a supported subset. `docx,xlsx` skips PDF conversion; `docx` and `xlsx`
build one file. `all` is the default. `--output-dir` selects a different bundle directory.

```bash
python3 tutorial.py build tutorials/babies_1_z_test.md --format docx,xlsx
python3 tutorial.py build tutorials/babies_1_z_test.md --format xlsx --output-dir /tmp/babies-workbook
```

The bundle contains the requested deliverables and `validation.json`. The report describes offline
checks and does not claim Google import, link navigation, or formula calculation. Warnings are
reported while a build may still complete; validation errors stop publication. Existing generated
files are protected by the bundle manifest, and edited outputs must be preserved before rebuilding.

## Import a workbook

Create a Markdown draft from a simple XLSX workbook:

```bash
python3 tutorial.py import-xlsx template.xlsx --output draft.md
```

The destination must not already exist. The draft contains workbook data and a Tutorial scaffold;
author the instructions before building. See [AUTHORING_GUIDE.md](AUTHORING_GUIDE.md) and the
[tutorial specification](TUTORIAL_SPEC.md) for supported content and limits.

## Check numerical expectations

Generate independent SciPy/NumPy expectations for all 12 lessons, then prepare the optional
Google Sheets execution cases without API requests:

```bash
python3 -m devel.check_tutorial_calculations
python3 -m devel.validate_google_sheets tutorials/*.md --dry-run \
  --expectations output/validation/tutorial_expectations.json --output output/validation/sheets
```

With authorized Application Default Credentials available, replace `--dry-run` with `--live`
and choose a separate output directory. The live runner creates fresh test workbooks and records
their IDs; it does not modify linked original spreadsheets. See
[GOOGLE_SHEETS_VALIDATION.md](GOOGLE_SHEETS_VALIDATION.md) for credentials, evidence, and limits.
An unavailable-credentials result is not a successful calculation check.
