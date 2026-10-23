# Authoring guide

Start with the [student guide](STUDENT_GUIDE.md) and its three-part Roots lesson. It walks through
one source file from first draft to a complete statistics tutorial, with an optional extension.

When you are ready to author another lesson, copy a suitable file from `templates/`. Keep the
student-facing writing, workbook tables, and tutorial instructions in one Markdown source. The
compiler formats that source as an editable DOCX, XLSX, and PDF.
On GitHub, open the template and choose **Raw** or **Copy raw file** to copy the full Markdown source.

Use the topic references when needed:

- [Markdown](reference/MARKDOWN.md) covers headings, lists, tables, and semantic links.
- [Worksheets](reference/WORKSHEETS.md) covers sheet tables, regions, and cell coordinates.
- [Formulas](reference/FORMULAS.md) covers formula text and calculation conventions.
- [Actions](reference/ACTIONS.md) covers links for entering, labeling, selecting, and filling.
- [Changes](reference/CHANGES.md) covers worksheet edits and reference updates.
- [Mistakes](reference/MISTAKES.md) covers common authoring problems.

The [formatting guide](FORMATTING_GUIDE.md) pairs syntax with rendered examples. The
[tutorial specification](TUTORIAL_SPEC.md) is the complete syntax contract; [usage](USAGE.md)
covers linting and building files.
