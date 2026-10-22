# markdown-to-tutorial

Markdown to Tutorial helps science instructors write spreadsheet lessons once, then create editable
DOCX instructions, a student workbook with starting data, and a PDF review copy.

## One lesson, three files

Instructions and starting data share one Markdown source. In the real
[Caffeine 3 lesson](tutorial_data/caffeine_3_quadratic_regression.md), a student enters one formula
and fills it down:

```markdown
- **Enter C2:** `=A2^2`
- **Fill C2:C26:** Down
```

The build produces an editable DOCX, a student XLSX with blank answer cells, and a PDF. For
Caffeine 3, the files are in `tutorial_output/caffeine_3_quadratic_regression/`.

<!-- screenshots:begin (managed by screenshot-docs) -->
![Caffeine 3 PDF excerpt showing Step 2 formula entry and fill-down directions](docs/screenshots/caffeine_3_fill_down_instructions.webp)
![Caffeine 3 blank student workbook with sleep data and empty predictor columns](docs/screenshots/caffeine_3_blank_predictor_workspace.webp)
<!-- screenshots:end -->

The project provides:

- One source for lesson prose, spreadsheet data, and cell instructions.
- Editable DOCX, student XLSX with blank answer cells, and review PDF outputs.
- Offline checks for source structure, workbook labels, and cell references.
- A draft importer for turning a simple XLSX workbook into a Markdown scaffold.

## Quick start

Install the Python requirements with `python3 -m pip install -r pip_requirements.txt`, plus
LibreOffice and the fonts listed in [docs/INSTALL.md](docs/INSTALL.md). Then run from the repository
root:

```bash
source source_me.sh
python3 make_tutorial.py lint tutorial_data/caffeine_3_quadratic_regression.md
python3 make_tutorial.py build tutorial_data/caffeine_3_quadratic_regression.md
```

The bundle appears in `tutorial_output/caffeine_3_quadratic_regression/` with `.docx`, `.xlsx`,
`.pdf`, and `validation.json` files. Use [docs/USAGE.md](docs/USAGE.md) for builds without PDF
conversion and other commands.

Lint checks structure and workbook references; it does not run spreadsheet formulas. LibreOffice Calc
has passed 254 independent expected values across 13 scenarios. Live Google Docs and Sheets import
and execution remain unverified without credentials.

## Documentation

- [docs/INSTALL.md](docs/INSTALL.md) - Set up Python, LibreOffice, and fonts.
- [docs/AUTHORING_GUIDE.md](docs/AUTHORING_GUIDE.md) - Write a lesson and workbook tables.
- [docs/TUTORIAL_CATALOG.md](docs/TUTORIAL_CATALOG.md) - Browse the 12 lessons and data notes.
- [docs/USAGE.md](docs/USAGE.md) - Run lint, builds, imports, and validation tools.
- [docs/TUTORIAL_SPEC.md](docs/TUTORIAL_SPEC.md) - Read the complete source and output contract.
- [docs/GOOGLE_SHEETS_VALIDATION.md](docs/GOOGLE_SHEETS_VALIDATION.md) - Review Google validation scope and evidence.

The PETase example uses synthetic teaching data, as described in the [catalog](docs/TUTORIAL_CATALOG.md). Source code is licensed under the [MIT License](LICENSE.MIT).
