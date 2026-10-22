# markdown-to-tutorial

A tool for writing spreadsheet lessons once in Markdown, with instructions and workbook tables, then generating editable DOCX and XLSX files plus a review PDF.

## Quick start

```bash
source source_me.sh
python3 make_tutorial.py lint tutorial_data/babies_1_z_test.md
python3 make_tutorial.py build tutorial_data/babies_1_z_test.md
```

See [`docs/INSTALL.md`](docs/INSTALL.md) for setup, [`docs/USAGE.md`](docs/USAGE.md) for CLI
commands, and [`docs/AUTHORING_GUIDE.md`](docs/AUTHORING_GUIDE.md) for writing a lesson. The
complete authoring contract is in [`docs/TUTORIAL_SPEC.md`](docs/TUTORIAL_SPEC.md).

The build validates source structure and workbook references; it does not evaluate formulas.
Live Google execution requires credentials. Document cell navigation separately requires worksheet
mappings. See
[`docs/GOOGLE_SHEETS_VALIDATION.md`](docs/GOOGLE_SHEETS_VALIDATION.md) for that boundary and
the separate local LibreOffice Calc evidence.

Source code is licensed under [`LICENSE.MIT`](LICENSE.MIT).
