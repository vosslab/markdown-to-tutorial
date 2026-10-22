# Tutorial model contract

Exporters consume `sheetlesson.model.Document` from
`sheetlesson.compiler.compile_document(path)` or `compile_source(source, path)`.
Compilation is read-only. Exporters must preserve the compiled model.

- `Document.worksheets` retains declaration order. Each `Worksheet` has sparse `cells`
  keyed by `(row, column)`, rectangle `regions`, `entry_cells`, and optional `google` mapping.
- A `CellSeed.scalar` has `kind` equal to `blank`, `text`, `number`, `boolean`, or `formula`;
  its `value` is a native scalar. Formula strings include `=`. Blank is `None`.
- `Document.tokens` contains markdown-it block tokens and their inline children.
  `content_token_indices` selects introduction/tutorial block tokens for rendering.
  Inline children retain normal Markdown formatting. Their `meta` may contain a resolved
  `reference` or image `asset`. Block `meta` may contain a `heading` or `action` object.
- `headings` carry explicit `display` text, `slug`, `kind`, and optional generated `number`.
- `actions` carry `kind`, literal `payload`, resolved `target`, typed `scalar`, menu segments,
  and optional alternative group/branch identifiers. They never populate seed cells.
- `CellReference` coordinates are inclusive and one-based; `sheet` preserves declaration spelling.
  `address` preserves authored anchors and omits worksheet qualification.
- Diagnostics carry stable `category`, `severity`, source `span`, `message`, `correction`, and
  optional `worksheet`, `address`, `related` span. `Document.has_errors` blocks publication.
- `formula_checks` report `verified`, `partial`, or `unchecked` static reference coverage.
  No formula evaluation or external Google verification is implied.

Source lines are physical, one-based, inclusive. All renderer style values belong to its own
style definitions. This contract is the shared M2 boundary; changes require coordination.
