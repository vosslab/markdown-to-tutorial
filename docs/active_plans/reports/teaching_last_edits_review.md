# Final teaching content edits: SPEC review

## Result

The three content edits meet their stated wording and worksheet contracts. Babies 1 and PETase
render cleanly. The current Babies 3 PDF has a concrete pagination regression: Step 8 begins at the
bottom of page 3, while its instruction, example, conclusion, and references are pushed onto a new,
sparsely used page 4. An earlier three-page render kept all of Step 8 together on page 3. This is a
current-artifact defect to resolve before accepting the final bundle; the text itself is accurate.

## Contract checks

- **Babies 1:** Page 6 states that Joe mistakes the higher sample mean for proof despite a
  nonsignificant Z-test. The Baby Butter Ball Award and butter-and-bacon celebration remain. The
  only source diff is the closing sentence replacement. The rendered paragraph is complete and has
  no clipping or new page break.
- **Babies 3:** Step 6 renders its automatic headings as `6.1: Calculate the p-value` and
  `6.2: Plan the decision`, under `Step 6`. The Step 0 rationale remains. The stated two-tailed and
  right-tailed alternatives, formulas, and decision steps appear intact. Page 3 ends with the Step 8
  heading and `Label F8`; the remainder starts on page 4, which uses only about one quarter of the
  page. The archived earlier page-3 render contains the complete Step 8 and references on the same
  page. This is a pagination regression in the current artifact, with no clipped text.
- **PETase:** Page 3 identifies `A2:A8` as the calibration X-axis and `C2:C8` under the separate
  Series control as the only absorbance series. Page 4 identifies `A2:A8` as the residual X-axis and
  `J2:J8` under the separate Series control as the residual series. The chart ranges are distinct,
  and the source diff changes only those instructions. No formula or source data changes were made.
- **Student workbooks:** The current Babies 1, Babies 3, and PETase workbooks have all authored
  student-entry targets blank. Checked targets include Babies 1 `E2:E19` entries, Babies 3 `G2:H4`
  and `G5:G8`, and PETase calibration/regression targets `C2:C8`, `G2:G4`, `I2:J8`, and
  `E13:G15`. The bundle rebuild report records successful typed-seed readback for all 12 bundles;
  this prose-only source diff does not change workbook directives or data.

## Artifact identity

The refreshed build manifest reports successful bundle validation and Calc validation (13 scenarios,
254 comparisons). Current source, DOCX, PDF, and XLSX SHA-256 values for the reviewed tutorials are:

| Tutorial | Source | DOCX | PDF | XLSX | PDF pages |
| --- | --- | --- | --- | --- | ---: |
| Babies 1 | `8248755d18246bf77702b143523b67bc3398b996eb89802f2f6cdffe95be9266` | `4802feb56e7b31507e50eb2ee71ac3cc5a6102b50f4ea3397ea48981bc9351af` | `73c66ab0f766c31e0b62a472b699353e9f9f6780c23c46a0d17cb4d8f353c91e` | `06f0cd3e2c7e53ea5400844712a21fda6a986cb23f5645eef880c27408990f78` | 6 |
| Babies 3 | `f52939c01a343afdaecdedd568761a150030b5e7ddd08d375eb96d3f7425044e` | `ade5c159bba2e9a2d134ad7b543ece4a91f1e4e2e9591b222b035bebd84dd468` | `d0b54516da2a52a95218006b70170efdc651ced5461d961352df980e37859f9e` | `10869a659cc88afa5616b7cb1374d432f895dbab77ce108ed186765dd5ce09c0` | 4 |
| PETase | `47e90689983287168230fd486f57179065240e69720f506d33e6acfedd23d907` | `62c99d68f9243f9c1060c71e95b7146d10bbe1f94d0bdda40a72ae6ce5bc9bee` | `d444887ed81740d295eacc1dd375a61e50cd16c9e8e2928a6bf5892c732d6da3` | `86901fd9869e3b49a34323707729bdc2e88ba2b76ce089ce4176d45ad46006` | 5 |

## Evidence

- Current PDFs were inspected with Poppler text extraction and page renders. Rendered pages are in
  `tutorial_output/verification/teaching_review/last_edits_spec/`:
  `babies_1_page_6.webp`, `babies_3_page-3.webp`, `babies_3_page-4.webp`, and `petase_page-2.webp`
  through `petase_page-5.webp`.
- Earlier Babies 3 page-3 comparisons are in
  `tutorial_output/verification/teaching_review/established_quality/babies_3_two_sample_t_test_page_3.png`
  and `tutorial_output/verification/teaching_review/established_spec/fullsize/babies_3_two_sample_t_test-page-3.png`.
- Bundle identities and build checks are recorded in
  `tutorial_output/verification/teaching_review/final_rebuild/manifest.json`.
- No LibreOffice command or test suite was run for this review.
