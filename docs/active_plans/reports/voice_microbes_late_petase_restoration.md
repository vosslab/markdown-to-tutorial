# Microbes 4/5 and PETase voice restoration

## Scope

Restored the original Fall 2025 narrative and instructional cadence in Microbes 4, Microbes 5, and
PETase while retaining the current workbook data, formulas, and technically required corrections.
The original artifacts were read-only. This work changed only the three assigned tutorial sources
and this report; it did not change compiler, test, or generated workbook files.

## Restored source material

- **Microbes 4:** Restored the Busse Woods 2014/2024 comparison, the advisor's suggestion to move
  from comparing means to comparing variances, and the heading **Why Use an F-Test Now?** The
  original instructional sequence remains organized as numbered steps and numbered test substeps.
- **Microbes 5:** Restored the 30-year transition from the older theses and the heading
  **Why Use ANOVA Now?** The comparison across 1994, 2004, 2009, 2014, and 2024 remains a continuing
  Busse Woods investigation with numbered table-building and calculation steps.
- **PETase:** Restored the original startup and plastic-waste framing; the detailed fictional
  codon-optimized variant, three-strain, fermentation, and partial-purification narrative; and the
  headings **Background: PET and Plastic Waste**, **Engineering Yeast to Produce PETase**,
  **Your Task: Quantifying PETase Production**, **Concept: How the Bradford BSA Assay Works**, and
  **Why Use Linear Regression Now?** The original strain-performance claims remain scenario
  premises. Spreadsheet work uses the coherent synthetic Bradford calibration already in the
  current lesson.

## Scientific and instructional exceptions

- **Microbes 4:** Replaced the source claim that the preceding t-test confirmed a decrease because
  comparing means does not establish a causal ecological decline. Clarified that lower Shannon
  Index variance means less variation in the index values; it does not establish more uniform
  species composition or reduced ecological resilience. Kept the advisor's story and variance
  question. The 24 named locations repeat across years, so independence is explicitly hypothetical;
  the classical F-test is especially sensitive to nonnormality.
- **Microbes 5:** Replaced the source premise that the preceding F-test established both a decrease
  and homogenization. ANOVA has a right-tail omnibus test of equality across five population means;
  rejection indicates at least one mean differs, not that all years changed or that a decline
  continued. Retained the supplied warning that historical method differences are confounded with
  year and that the results establish neither time trend nor environmental cause.
- **PETase:** Corrected the source's claim that Bradford results identify which strain produces the
  most PETase per fermentation batch. Bradford estimates total protein. Retained the synthetic-data
  disclosure, partially purified sample description, BSA-equivalent concentration language, and
  limits on claims about PETase abundance or activity. The source's spreadsheet directions after
  **Why Use Linear Regression Now?** contain a copied Microbes t-test exercise and were not
  restored; the existing synthetic calibration is internally coherent with the PETase objective.

## Validation

Ran the repository tutorial compiler lint on all three sources with the required Python bootstrap:

```text
source source_me.sh && python3 make_tutorial.py lint tutorial_data/microbes_4_f_test.md
source source_me.sh && python3 make_tutorial.py lint tutorial_data/microbes_5_anova.md
source source_me.sh && python3 make_tutorial.py lint tutorial_data/petase_1_linear_regression.md
```

All three passed offline lint without errors. Microbes 4/5 report expected range-overshoot and
input-availability notices because formula ranges intentionally extend to row 101 while the
supplied observations occupy rows 2:25. The compiler also reports absent optional Google Sheets
cell-link mappings. PETase reports an input-availability notice for the student interpretation
entry. Lint does not establish live Google Sheets import or calculation behavior.
