# Caffeine destination references

The sleep mean, median, and sample standard deviation instructions now name their visible
workbook destinations in the existing formula sentences: E2, E3, and E4. Their formula
text, semantic `enter` bindings, explanations, and task grouping remain intact.

Validation: `source source_me.sh && python3 make_tutorial.py lint
tutorial_data/caffeine_1_descriptive_statistics.md` passed. Lint retains its existing
`google-unmapped` note. Compiling the source before and after this prose-only edit confirmed
all 12 semantic actions remain identical. No LibreOffice command was run. Fresh PDF review
remains with the parent integration workflow.
