# Fill-down implementation

## Implemented contract

- `**Fill C2:C26:** Down` and `**Fill E2:F26:** Down` remain single authored actions.
- Only `Down` and ordered ranges containing at least two rows are supported.
- Each first-row source must contain a formula in every incoming branch, identical per column.
- The validator uses the existing openpyxl Translator dependency for ordinary relative, mixed,
  absolute, quoted-sheet, and string-literal behavior.
- Generated Enter children stay on the Fill action. They reuse ordinary assignment conflicts,
  redundancy warnings, reference checks, source locations, branch state, and entry styling.
- Shared `prepare_cases` replays the children for Sheets and LibreOffice execution cases.
- DOCX preserves the authored concise Fill item. Student XLSX inserts no generated answers.

No tutorial source files, shared changelog, human guidance, or decision ledger were edited here;
the manager owns source migration and those coordinated updates.

## Validation evidence

Command:

```bash
source source_me.sh && python3 -m pytest tests/test_tutorial_fill.py \
  tests/test_tutorial_semantics.py tests/test_sheets_validation.py \
  tests/test_tutorial_docx.py tests/test_tutorial_workbook.py -q
```

Result: 26 passed in 0.38 seconds. Three new behavior tests verify translated E:F formulas with
mixed anchors, quoted sheets and literal A1 text; complete downstream reference availability;
blank XLSX and concise native DOCX; invalid source/direction/range/overwrite errors; and both
joined and branch-local Fill execution choices. All checks are offline and invoke no LibreOffice.

Command:

```bash
source source_me.sh && python3 -m pytest tests/test_pyflakes_code_lint.py \
  tests/test_function_typing.py tests/test_import_requirements.py \
  tests/test_ascii_compliance.py tests/test_indentation.py tests/test_whitespace.py \
  tests/test_markdown_links.py tests/test_source_file_line_limit.py \
  tests/test_pytest_hygiene.py -q
```

Result: 769 passed; 2 unrelated report-link failures in concurrently authored
`teaching_babies_review.md` and `teaching_microbes_early_review.md`. Their `../../../tutorial_output`
targets resolve beneath `docs` and are missing. The manager was notified to route corrections.
All listed code/style checks and the edited authoring/spec links passed.

## Handoff

The manager should migrate the lesson sources, update the shared ledgers, and obtain fresh spec
and quality reviews. Build and inspect lesson PDFs only after source migration, running repository
LibreOffice scripts outside the sandbox. No live spreadsheet calculation or PDF evidence is claimed
by these offline tests.
