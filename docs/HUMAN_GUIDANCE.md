# Human guidance

<!-- VENDORED HEADER: START -->
Record the durable guidance Neil Voss states, or approves for preservation here, in his own words:
first person or close paraphrase, one to three lines per bullet. Material he supplies as a source
may inform [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md) once it is settled, and an entry of uncertain
origin belongs there too. Rules: [REPO_STYLE.md](REPO_STYLE.md).
[PROPAGATED HEADER - ENTRIES BELOW ARE YOURS]
<!-- VENDORED HEADER: END -->

- Make durable changes in starter-repo-template; consumer copies are vendored.
- A temporary, easily removable wrapper is acceptable for the Graphify crash.
  Make the edited node count match the expected normalized count.

## Tutorial converter

- Prioritize DOCX and XLSX for importing into Google Docs and Google Sheets.
- Use LibreOffice to convert DOCX to PDF for useful output review; HTML preview is not needed.
- On this macOS host, run every command that can invoke LibreOffice outside the sandbox through
  the repository scripts; ODP imports may launch it indirectly for metafile conversion.
- Keep authoring easy for humans: use lists for tutorial instructions and GFM tables for the
  simple spreadsheet data.
- Keep the list-authored instructions and table-authored workbook in one Markdown file that
  produces all three outputs.
- Format spreadsheet formulas, cell IDs, menu choices, and bold list openings consistently.
  Enforce part, step, and substep numbering, and connect or check spreadsheet references.
- Examine djot-slide-builder and exam-formatting-tools for relevant patterns; the slide
  project's syntax guide does not directly apply to tutorial authoring.
- Migrate all three Fried Foods/babies tutorials, all five Microbes tutorials, and the three-part
  Dr Caffeine set. Include PETase in the inventory and identify its incomplete source material.
- Keep the workflow KISS and avoid speculative gates. Agents should resolve scientific migration
  issues with authoritative sources and document corrections.
- Use local DOCX/XLSX behavior checks and agent PDF visual assessment to determine completion.
  Google import is optional when access exists; claim it only with observed evidence.
- Complete milestones without waiting for human milestone signoff.
- Repair PETase with a clearly labeled synthetic Bradford dataset when original measurements
  cannot be recovered.
- Run the optional Google Sheets calculation check when access is available.
- Use the final layout `make_tutorial.py`, `tutorial_lib/`, `tutorial_data/`, and
  `tutorial_output/`; this supersedes the earlier distinct-prefix naming request.
- Apply the selected names consistently without old-name aliases or legacy compatibility stubs.
- Treat this as preproduction: fix the design, keep it KISS, and finish the work without legacy
  compatibility layers or stubs. Check the real student walkthrough and current artifacts before
  declaring completion.
- Compare every original lesson directly with its generated materials, walk through the actual
  generated XLSX as a student, and invite independent challenges. Preserve author voice; change the
  converter only for recurring design issues, and do not add validation infrastructure for this review.
- Babies and Microbes are established lessons; preserve their teaching experience and voice while
  correcting verified errors, typos, and format faults. Make as few wording changes as practical.
- Treat the Dr Caffeine materials as a draft foundation, not a quality benchmark. Complete all three
  parts as polished, independently usable classroom lessons, with efficient Enter once / Fill down work.
- For the teaching-quality pass, use HCI cognitive-walkthrough methods and targeted humanizer edits;
  expert inspection does not count as student testing. Keep wording changes focused on actual learner
  needs and preserve the source voice.
- Each Caffeine lesson is standalone and starts with Part 1. Caffeine 1 has Steps 1-5; Caffeine 2 has
  Steps 1-7 with substeps 3.1-3.2 and 6.1-6.4; Caffeine 3 has Steps 1-7.
