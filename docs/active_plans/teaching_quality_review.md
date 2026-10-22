# Teaching quality review

Status: in progress. The prior readiness closeout does not settle this review. Babies and Microbes
are established lessons: preserve their teaching experience and author voice while correcting
verified errors, typos, and format faults. The Dr Caffeine set is a draft foundation, not a quality
benchmark; complete all three parts as polished, independently usable classroom lessons. Minimize
wording edits. Change the converter only for recurring design issues demonstrated across lessons.

## Review work

1. For all 12 lessons, compare the original source and materials with the generated DOCX, XLSX,
   and PDF. Record what was preserved, changed, omitted, or newly introduced.
2. Walk through each generated XLSX as a student: open the personal workbook, understand the
   question and hypothesis, locate the target cell, enter a formula and fill it down, check the
   range and result, interpret the result, and recover by reopening the original copy. Record
   concise evidence of success and friction; do not build new review infrastructure.
3. Independently challenge the science, statistical choices, evidence, and teaching sequence.
   Invite reviewers to question one another's findings and distinguish sourced facts from judgment.
4. Make substantive lesson corrections that address supported findings while preserving author
   voice. Keep original materials unchanged.
5. Change converter behavior only for recurring design issues demonstrated across lessons. Do not
   add validation infrastructure for this review.
6. After corrections, request a fresh independent review of the changed lessons and generated
   outputs. Record remaining limitations and evidence before closing this plan.

For the expert walkthrough, use a cognitive walkthrough without student participants. The task
sequence draws on the W3C [clear steps pattern](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o1p04-clear-steps/)
and [task expectations pattern](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o5p04-task-expectations/)
as task-design references; this is not an accessibility conformance claim.

## Review groups

| Group | Lessons | Focus |
| --- | --- | --- |
| Babies | `babies_1_z_test`, `babies_2_t_test`, `babies_3_two_sample_t_test` | Original-to-generated comparison, workbook walkthrough, independent challenge |
| Microbes A | `microbes_1_z_test`, `microbes_2_t_test`, `microbes_3_two_sample_t_test` | Original-to-generated comparison, workbook walkthrough, independent challenge |
| Microbes B | `microbes_4_f_test`, `microbes_5_anova` | Original-to-generated comparison, workbook walkthrough, independent challenge |
| Caffeine | `caffeine_1_descriptive_statistics`, `caffeine_2_linear_regression`, `caffeine_3_quadratic_regression` | Complete three polished, standalone lessons from the draft foundation |
| PETase | `petase_1_linear_regression` | Original-to-generated comparison, workbook walkthrough, independent challenge |

## Ledger

| Work | Status | Evidence or remaining work |
| --- | --- | --- |
| Direct comparison of all 12 originals and generated lessons/artifacts | Complete | Four review groups are audited; see the teaching review reports below. |
| Student walkthrough of all 12 generated XLSX files | In progress | Workbook layout evidence covers representative populated workbooks; finish and record the full lesson-by-lesson cognitive walkthrough. Google Sheets import remains unverified. |
| Independent challenge | Complete | Review reports record challenges to scientific accuracy, statistics, evidence, and sequence. |
| Substantive authored lesson corrections | Complete | The first-pass edits and the fresh Caffeine figure corrections are recorded; review the corrected renders after rebuild. |
| Converter changes for recurring design issues | Complete | Fill Down, label-driven workbook sizing, and Label-to-Enter pagination grouping are implemented and reviewed; rebuilt PDF pagination review remains pending. |
| Fresh independent review after corrections | In progress | Rebuild and review corrected Caffeine figures and pagination, finish two group-level source/artifact reviews, and complete final quality/HCI review. |

## Review record

Add concise findings and links to evidence as review work proceeds. Keep one-time observations here;
record durable human guidance and settled design decisions in their designated documents.

- Babies: [teaching_babies_review.md](reports/teaching_babies_review.md) and
  [teaching_babies_fixes.md](reports/teaching_babies_fixes.md).
- Microbes: [teaching_microbes_early_review.md](reports/teaching_microbes_early_review.md) and
  [teaching_microbes_late_review.md](reports/teaching_microbes_late_review.md).
- Regression lessons: [teaching_regression_review.md](reports/teaching_regression_review.md).
- Workbook Fill implementation: [teaching_fill_implementation.md](reports/teaching_fill_implementation.md).
- Workbook layout review: [teaching_workbook_spec_review.md](reports/teaching_workbook_spec_review.md)
  and [teaching_workbook_layout.md](reports/teaching_workbook_layout.md).
- Consolidated progress and remaining review limits:
  [teaching_quality_summary.md](reports/teaching_quality_summary.md).
- Each caffeine lesson is standalone and starts at Part 1. Their step ranges are 1-5, 1-7, and
  1-7; caffeine 2 has substeps 3.1-3.2 and 6.1-6.4. This is settled, not an open numbering question.
