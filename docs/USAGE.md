# Usage

For the student learning path, see the [student guide](STUDENT_GUIDE.md). This page is for building
and maintaining tutorial files.

Run commands from the repository root after loading its shell environment:

```bash
source source_me.sh
```

Choose a lesson from [TUTORIAL_CATALOG.md](TUTORIAL_CATALOG.md), which indexes all 12 migrated
sources, including the explicitly synthetic PETase calibration example.

## Validate and build

Lint checks one source without writing output files:

```bash
python3 make_tutorial.py lint tutorial_data/babies_1_z_test.md
```

Build DOCX, XLSX, and PDF into `tutorial_output/<source-stem>/`:

```bash
python3 make_tutorial.py build tutorial_data/babies_1_z_test.md
```

On this macOS host, an agent must invoke this build command with
`sandbox_permissions="require_escalated"` so the project's LibreOffice conversion wrapper runs
outside the sandbox. The command above runs normally in a human terminal. PDF output is reopened
with a PDF reader and must contain pages before the bundle is published.

Use `--format` to build a supported subset. `docx,xlsx` skips PDF conversion; `docx` and `xlsx`
build one file. `all` is the default. `--output-dir` selects a different bundle directory.

```bash
python3 make_tutorial.py build tutorial_data/babies_1_z_test.md --format docx,xlsx
python3 make_tutorial.py build tutorial_data/babies_1_z_test.md --format xlsx --output-dir /tmp/babies-workbook
```

The bundle contains the requested deliverables and `validation.json`. The report describes offline
checks and does not claim Google import, link navigation, or formula calculation. Warnings are
reported while a build may still complete; validation errors stop publication. Existing generated
files are protected by the bundle manifest, and edited outputs must be preserved before rebuilding.

For real local formula execution, generate independent expectations and run the final workbook
states through LibreOffice Calc:

```bash
python3 devel/check_tutorial_calculations.py -o tutorial_output/validation/local_calc
python3 devel/validate_libreoffice.py tutorial_data/*.md \
  -e tutorial_output/validation/local_calc/tutorial_expectations.json \
  -o tutorial_output/validation/local_calc/calc
```

This compares Calc's saved results with independent expectations after all authored assignments.
It does not verify intermediate steps or Google Sheets behavior. On macOS, invoke the validator
outside the sandbox because it launches LibreOffice. See
[local_calculation_readiness.md](active_plans/reports/local_calculation_readiness.md) for current
engine evidence.

## Import a workbook

Create a Markdown draft from a simple XLSX workbook:

```bash
python3 make_tutorial.py import-xlsx template.xlsx --output draft.md
```

The destination must not already exist. The draft contains workbook data and a Tutorial scaffold;
author the instructions before building. See [AUTHORING_GUIDE.md](AUTHORING_GUIDE.md) and the
[tutorial specification](TUTORIAL_SPEC.md) for supported content and limits.

## Maintain a worksheet after a layout decision

Students write ordinary Markdown and ordinary Excel formulas. They do not need this command for
normal tutorial authoring. Use it only when an author has deliberately changed an existing layout
and wants the compiler to update the associated workbook coordinates, formula operands, action
links, and explicit cell instructions together.

The command prints a preview and leaves the source unchanged by default:

```bash
python3 make_tutorial.py worksheet-edit tutorial_data/caffeine_3_quadratic_regression.md \
  --sheet "Sleep and scores" insert-columns --at A --count 1
```

Review the diff, then rerun the same command with `--write` to atomically replace an unchanged
source file. `--write` may appear before or after the edit operation. The command recompiles its
candidate before it can write. It supports familiar
worksheet maintenance operations:

```bash
python3 make_tutorial.py worksheet-edit lesson.md --sheet Data insert-rows --at 2 --count 1
python3 make_tutorial.py worksheet-edit lesson.md --sheet Data move-range \
  --range H1:M26 --destination J1
python3 make_tutorial.py worksheet-edit lesson.md --sheet Data resize-observations \
  --data-range A1:B26 --rows 50
```

The editor changes only declared worksheet geometry, semantic action targets, explicit cell/range
instructions, and formulas marked as spreadsheet formulas. It intentionally leaves scientific
prose, worked numerical conclusions, URLs, and unmarked mathematical notation alone. An ambiguous
bare coordinate in otherwise instructional prose is retained and reported for review instead of
being guessed at; use an explicit `cell`, `range`, action link, or code-formatted spreadsheet
formula when it must be maintained. A resize prints review notices for nearby numerical
explanations; authors remain responsible for checking whether those examples and interpretations
still make sense. If a reference only partly overlaps a moved range, or the resulting source does
not compile, the command stops without writing anything.

## Check numerical expectations

Generate independent SciPy/NumPy expectations for all 12 lessons, then prepare the optional
Google Sheets execution cases without API requests:

```bash
python3 -m devel.check_tutorial_calculations
python3 -m devel.validate_google_sheets tutorial_data/*.md --dry-run \
  --expectations tutorial_output/validation/tutorial_expectations.json --output tutorial_output/validation/sheets
```

With authorized Application Default Credentials available, replace `--dry-run` with `--live`
and choose a separate output directory. The live runner creates fresh test workbooks and records
their IDs; it does not modify linked original spreadsheets. See
[GOOGLE_SHEETS_VALIDATION.md](GOOGLE_SHEETS_VALIDATION.md) for credentials, evidence, and limits.
An unavailable-credentials result is not a successful calculation check.

## Refresh documentation screenshots

After changing renderer styles, rebuild the documentation screenshots so the examples show the
current output. From the repository root, run:

```bash
source source_me.sh && python3 devel/refresh_documentation.py
```

The refresh renders the documentation capture sets from native outputs and anchors crops to
semantic content, so a style change can be reviewed in the affected images. It also records a
machine-readable capture receipt. Review the refreshed images and receipt alongside the lesson
pages that use them.

This optional documentation workflow uses the existing application environment and Pillow,
Poppler (`pdftotext`, `pdftoppm`), WebP (`cwebp`), librsvg (`rsvg-convert`), LibreOffice, and the
required fonts. See [INSTALL.md](INSTALL.md) for `brew bundle` and font requirements. On this
macOS host, agents must run the command with `sandbox_permissions="require_escalated"` because
it invokes LibreOffice. Human terminal commands use the ordinary command above.
