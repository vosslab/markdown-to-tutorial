# Automatic formatting summary

Authors can write a spreadsheet formula directly in an instruction, for example
`- **Enter C2:** =A2^2`. The DOCX/PDF output preserves the formula text and gives it Roboto Mono with
dark green `188038`. JSON-quoted values stay literal in Workbook and Enter/Replace scalar contexts;
quoted formula examples in prose and ordinary Tutorial tables keep their formula styling. Lists use
0 pt before, 2 pt after, and single spacing. Body paragraphs retain 6 pt after and 1.08 line spacing.

This work changes the authoring and output format contract, not lesson prose. All 12 tutorial sources
match their validated source hashes, and the independent quality review confirms the source wording
was preserved. The compact lists reduce the rebuilt PDFs from 70 baseline pages to 65 across the 12
tutorials. Review of all current pages found readable formulas, aligned list continuations, and no
clipping or awkward page starts. PDF text extraction differences are limited to table-header
extraction at changed page boundaries and a repeated header for a table continuing across pages.

The 12 current bundles contain 36 artifacts. LibreOffice Calc passed 254 independent formula
comparisons across 13 scenarios; the repository suite passed 1,493 tests. These checks support the
formatting, copy-text, and local calculation contracts. They do not establish Google Docs or Sheets
import behavior, student enjoyment, or learning outcomes. The user goal is to make the source-to-output
workflow support engaging, scientifically accurate, classroom-ready lessons while preserving author
voice; the formatting review makes no learner-outcome claim.

The fresh quality review accepted the 65-page PDF set, and final integration accepted the complete
change. The integration review matched all 12 source hashes, all 36 canonical artifact hashes, and
the two current screenshot hashes; it also verified that all 75 designated Caffeine 3 answer cells
remain blank. The scoped guidance-format and Markdown-link checks passed 111 tests, and all 13
formatting Markdown files passed ASCII checks. Current README screenshot hashes and capture details
are recorded in [the screenshot receipt](../../screenshots/README.md).

Related evidence: [the active plan](../automatic_tutorial_formatting.md),
[the rebuild report](automatic_formatting_rebuild.md),
[the literal-action specification recheck](automatic_formatting_spec_recheck.md), and
[the quality review](automatic_formatting_quality.md), and
[the integration review](automatic_formatting_integration.md).
