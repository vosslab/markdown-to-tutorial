# Automatic tutorial formatting

Status: complete. Improve the shared GFM-to-DOCX/XLSX/PDF workflow so authors get useful
formatting from ordinary Markdown, without adding author markup or configuration.

## Work ledger

| Work | Status | Evidence or remaining work |
| --- | --- | --- |
| Locate parser ownership and formula-token recognition | Complete | Accepted the shared parser semantic boundary; pass a formula role to output renderers without putting presentation choices in parsing. |
| Recognize spreadsheet formulas and apply a common dark-green style | Complete | Bare action formulas, inline and fenced formulas, and formula table cells preserve text and receive the `188038` role. JSON-quoted literal semantics apply to Workbook and Enter/Replace scalars; narrative tables and prose retain formula roles. The literal-action correction passed the SPEC recheck. |
| Reduce spacing between list paragraphs | Complete | All 634 list paragraphs use 2 pt after, 0 pt before, and single spacing; body paragraphs retain 6 pt after and 1.08 line spacing. |
| Check focused behavior and documentation links/characters | Complete | Literal-action SPEC recheck accepted; focused semantic, DOCX, and workbook checks passed. Final integration checks passed 111 scoped guidance-format and Markdown-link tests; all 13 formatting Markdown files passed ASCII checks and `git diff --check`. |
| Rebuild and compare all 12 tutorials | Complete | All 12 bundles match current sources. The rebuilt PDFs total 65 pages versus 70 baseline pages; Calc passed 254 comparisons across 13 scenarios, and the full suite passed 1,493 tests. Package-level comparison confirms the literal-action correction leaves published DOCX content equivalent. Independent visual quality review accepted all 65 pages. |
| Improve author guidance and examples | Complete | Authoring guide and specification show bare formula entry and distinguish scalar JSON literals from quoted narrative examples. The decision record and human guidance capture the accepted style and user goal. |
| Quality review and integration | Complete | The specification recheck, quality review, and final integration review are accepted. All 12 source hashes, 36 canonical artifact hashes, current screenshot hashes, and the 75 blank answer cells were verified. |

## Scope

- Preserve the six paragraph styles: Normal text, Title, Subtitle, and Heading 1-3. Keep the three
  font families PT Sans, PT Sans Narrow, and Roboto Mono, each with regular, bold, and italic variants.
- Keep student workbook answer cells blank.
- Preserve lesson wording and teaching voice; this work concerns formatting and author convenience.
- Compare with the preserved original PDFs in `tutorial_output/verification/automatic_formatting/baseline/before_pdfs/`.
  Original list spacing varies, so the accepted 2 pt value is a deliberate output choice, not a claim
  that the earlier PDFs all used wider spacing.
- Treat Google Docs/Sheets behavior as unverified unless directly observed. Do not build screenshot
  automation for this work.
