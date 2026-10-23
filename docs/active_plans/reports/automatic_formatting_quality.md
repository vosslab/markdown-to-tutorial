# Automatic formatting quality review

Review date: 2026-10-22. Status: accepted for the planned DOCX/PDF formatting work.

## Review scope

Compared the approved [automatic tutorial formatting plan](../automatic_tutorial_formatting.md)
with the current implementation, rebuild evidence, and rendered output. Applied the repository,
Python, pytest, and Markdown style rules. This review covers formatting and copy-text preservation;
the lesson sources and scientific content were not changed in this work.

The rebuild manifest records all 12 tutorial bundles (36 artifacts) and 65 current PDF pages,
compared with 70 pages in the preserved baseline PDFs. Every current source hash matches its
validated source hash. The literal-action correction left the published bundle members unchanged,
as recorded in the rebuild report.

## Visual evidence

Rendered all 65 current and 70 baseline PDF pages with Poppler and reviewed contact sheets plus
full-size pages. The current pages show the planned compact list spacing without crowded or
overlapping text. Wrapped list continuations stay aligned with their text, formulas remain legible,
and no content is clipped. The reduced spacing removes a page from five tutorials without awkward
page starts or broken lesson flow.

Reviewed the requested pages and their surrounding pages:

- Babies 2, current page 3: the table and calculation steps remain readable; list spacing is compact.
- Microbes 3, current pages 3-5: the comparison table continues across pages with its header
  repeated; the chart and long T.TEST instructions remain intact.
- Microbes 5, current pages 3-5: dense ANOVA steps are easier to scan with compact lists, and the
  page break falls between steps.
- Caffeine 2, current page 6, and Caffeine 3, current page 4: formula text fits on one line.
- PETase, current pages 3-4: formulas and their instructions remain together and readable.

The contact sheets and rendered pages used for this review are preserved in the ignored
`tutorial_output/verification/automatic_formatting/quality/` directory.

## Formula and text checks

All 12 rebuilt DOCX files have green `188038` formula runs matching every parsed formula role:
8, 9, 10, 7, 11, 19, 9, 13, 19, 17, 27, and 14 runs respectively. The contact sheets show the
green cue throughout the PDF set. Long formulas in Caffeine and PETase remain copyable and do not
clip or collide with surrounding text.

Normalized PDF text, excluding standalone page numbers and whitespace, matches the baseline exactly
for 10 tutorials. Babies 1 differs only in extraction of the table's `Cell Contents` header, which
falls at a changed page boundary. Microbes 3 includes one repeated table header in the current
extraction because the table continues onto another page. Visual inspection confirms that rows and
lesson text remain present. The unchanged source hashes also confirm that the authors' prose and
voice were preserved.

The focused permanent tests cover automatic formulas in prose, actions, links, code spans, fences,
and tables; literal action payloads; formula styling; list paragraph spacing; token immutability;
and unchanged body spacing. The rebuild report records the completed full-suite run; this review did
not rerun it.

## Implementation and plan

Formula recognition remains in the parser and assigns a neutral formula role for DOCX rendering.
The bounded scanner distinguishes complete spreadsheet expressions from ordinary equations,
comparisons, and URLs, while existing validation remains the authority for formula validity.
Literal scalar action payloads bypass formula recognition and preserve their authored characters.
No new author configuration or formula grammar was introduced. These choices match the approved
plan and its specification recheck. The implementation has focused regression tests for the
changed behavior, with no material architectural drift found.

## Limits

The review supports the formatting and source-preservation claims above. It does not establish that
Google Docs or Sheets will render or import the files the same way, that students will find the
lessons enjoyable, or that the materials improve student outcomes. Those claims require direct
external testing or learner evidence.
