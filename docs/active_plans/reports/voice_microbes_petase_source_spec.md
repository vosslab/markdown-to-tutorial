# Microbes 1-5 and PETase independent source SPEC review

Verdict: **source fidelity passes; one narrow numeric-entry correction remains in Microbes 1**.
No remaining blocking prose omission, instruction-group fragmentation, invisible formula destination,
or workbook role declaration issue was found. This accepts source fidelity and the narrowly necessary
technical exceptions, subject to the numeric-entry correction below. It does not accept generated
DOCX/PDF appearance or workbook calculation behavior.

## Narrow technical finding

At `tutorial_data/microbes_1_z_test.md:188`, the visible instruction is `enter "0.05."`. The semantic
payload is correctly numeric 0.05, but the quoted period can tell a student to type text rather than
the numeric alpha. This typo also exists in the original and is eligible for a technical correction.
Use `enter **[0.05](enter:D14)**.` while preserving the original numbered group and paragraph order.
The punctuation in quoted text labels has no corresponding numeric calculation risk. Rebuild the
affected Microbes 1 artifacts after correction and refresh this report's hash.

## Authority and method

Reviewed the actual six `2025_Artifacts/*Fall_2025.md` originals against the actual six canonical
`tutorial_data/` sources. Recovery reports supplied a map, but their completion claims were not
used as acceptance evidence. Original files were read-only throughout this review. The active
instructional voice restoration plan and repository rules supplied the review contract.

Used bootstrap Python to normalize semantic-link wrappers, Markdown emphasis/code markers,
HTML entities, harmless legacy backslash escapes, and whitespace, then compare narrative blocks
and scan original sentence candidates for missing wording. Read the changed paragraphs and their
surrounding instruction groups directly; low similarity was a prompt to inspect, not a failure
threshold. Compared heading inventories and nested lists separately because stripping Markdown
cannot establish preservation of instructional grouping. Inspected the original formulas beside
their current visible destinations and the hidden Workbook region declarations.

The sentence scan found these exact retained candidates before manual reconciliation:

| Lesson | Original sentence candidates | Exact candidates in current visible wording |
| --- | --- | --- |
| Microbes 1 | 131 | 81 |
| Microbes 2 | 124 | 83 |
| Microbes 3 | 164 | 110 |
| Microbes 4 | 153 | 94 |
| Microbes 5 | 152 | 92 |
| PETase introduction | 45 | 41 |

These are diagnostic counts, not a claim of perfect sentence segmentation: decimal punctuation,
list numbering, and headings sometimes join candidates. Each nonexact passage was reconciled by
direct reading. Differences cluster around the obsolete external-spreadsheet setup, corrected
functions/references, null-model interpretation, unknown population SD, sampling assumptions,
and limits on causal or species-composition inference. No unexplained missing instructional
paragraph was found. Original images now use extracted assets rather than base64 definitions.

Canonical standalone Part/Step numbering is approved. The early Microbes future-lesson Setup
sections retain their descriptive words as informational headings, an approved structural choice.
Those numeric/semantic changes are not findings. Accidental original heading markers around full
prose sentences become ordinary paragraphs; the sentences themselves remain. Repeated original
Step-by-Step Tutorial headings are present in the frozen Microbes 2 and 3 sources.

## Direct original-to-current evidence

### Microbes 1: Z-test

Compared `Microbes_1_Z-Test_Tutorial_Fall_2025.md` with `microbes_1_z_test.md`.

- Original lines 99-111: the multi-paragraph absolute-value, cumulative-probability, subtraction,
  symmetry, image, and doubling explanation is retained at current lines 143-155. It is not
  replaced by a short formula summary. The negative-Z image explanation is corrected locally.
- Original lines 155-161: the IF concept and both separate directional examples remain at current
  lines 199-205. The alpha references in the explanatory formulas now agree with D14.
- Original Practice Task and Key Takeaways remain at current lines 226 and 234, with the original
  change/add/observe tasks retained. The extra practice-copy instruction protects original data.
- Original lines 194-214: the confident student, email, quoted critique, and transition to the
  t-test remain at current lines 240-260. The criticism now correctly turns on whether population
  SD is known rather than a rigid N <= 30 rule.
- Example word difference: original "units of standard deviation" becomes "units of standard
  error" at current line 99. The surrounding explanatory paragraph is retained. Original
  `IF(D11 <= D13, ...)` becomes `IF(D11 <= D14, ...)` at current line 205; its directional teaching
  explanation remains intact.

### Microbes 2: one-sample t-test

Compared `Microbes_2_T-Test_Tutorial_Fall_2025.md` with `microbes_2_t_test.md`.

- Original t-statistic and degrees-of-freedom explanations remain at current lines 103-118,
  including the multi-sentence account of standard error and the t reference distribution.
- Original two-tail input descriptions, two formulas, and three explanatory paragraphs remain at
  current lines 137-159. The original Step-by-Step Tutorial headings also remain before the
  lower/higher-tail actions, IF actions, and interpretation actions.
- Original IF explanation and scientific interpretation remain at current lines 215-238. The
  inferential corrections preserve their paragraph purposes rather than deleting the explanations.
- Practice Task, four Key Takeaways, and the uncertainty/advisor/2014-data transition remain at
  current lines 240-273. The months of work and desire to discard the report are retained.
- Example word difference: original "cumulative is set to FALSE" becomes "cumulative is set to
  TRUE" in the two-tail T.DIST input description. Original incorrect lower-tail T.DIST.RT/T.TEST
  instruction becomes the signed T.DIST explanation plus the explicit one-sample T.TEST limitation
  at line 176. These are function corrections, not stylistic substitutions.

### Microbes 3: Welch two-sample t-test

Compared `Microbes_3_Two-Sample_T-Test_Tutorial_Fall_2025.md` with
`microbes_3_two_sample_t_test.md`.

- The sample-statistic action groups, t-statistic explanation, Welch equation explanation,
  six-row adjustment table, and degrees-of-freedom discussion remain at current lines 81-144.
- Both T.DIST and T.TEST input explanations remain at lines 167-188, as do the two-tail and both
  directional manual/quick-calculation groups at lines 190-248. All five original Step-by-Step
  Tutorial headings are present.
- Original IF explanations, interpretation group, three practice tasks, four takeaways, the
  student's sense of accomplishment, and the advisor's enthusiastic quoted reply remain at
  lines 250-329. The correction separates equal index values from species homogenization.
- Example word difference: original `T.TEST(C2:C101, B2:B101, 2, 2)` becomes
  `T.TEST(C2:C101, B2:B101, 2, 3)` at line 206. The surrounding direct-comparison explanation
  remains. The original two-tail T.DIST.2T method is replaced with BETADIST to preserve fractional
  Welch df; the explanatory paragraph at line 211 describes that actual formula. Directional
  T.TEST formulas now use the sign of E11 rather than treating the smaller tail as a chosen tail.

### Microbes 4: F-test

Compared `Microbes_4_F-Test_Tutorial_Fall_2025.md` with `microbes_4_f_test.md`.

- The original sample-statistics numbered groups and nested bullets remain at lines 94-109.
  F-statistic, degrees-of-freedom, F.DIST/F.TEST input, and three-tail explanations remain.
- The complete IF teaching explanation remains at lines 242-267. The original decision formulas
  still sit in their compact nested instruction groups with visible E22, E23, and E24 destinations.
- Original Practice Task and four Key Takeaways remain at lines 292-305.
- Original lines 241-263: the old lab data, graduate theses, labor-intensive plates/stains,
  selective media, CFUs, colony appearance, incubation, meticulous documentation, 1994/2004/2009,
  and 30-year investigation remain at current lines 307-329. The added method-confounding caveat
  does not replace that story. The Moving to ANOVA descriptive heading and closing request remain.
- Example word difference: original "Staining methods like Gram staining helped differentiate
  species, allowing for accurate identification and counts within the microbial community" becomes
  "Staining methods like Gram staining helped differentiate broad microbial groups, but these
  traits alone did not uniquely identify every species" at line 313. The rest of that original
  methods paragraph remains. The F-distribution's supposed convergence to normal is also
  corrected locally rather than dropping its surrounding df explanation.

### Microbes 5: ANOVA

Compared `Microbes_5_ANOVA_Tutorial_Fall_2025.md` with `microbes_5_anova.md`.

- All thirteen descriptive step titles remain. The original ANOVA table setup and nested groups
  remain, with corrections to the data-column description and malformed original list numbering.
- The separate explanations of group statistics, grand mean, df relationship, SSR, SUMPRODUCT,
  SSE, SST, SS relationship, mean squares, F, right-tail probability, IF, and interpretation remain
  at current lines 115-307. This includes the original extended SST teaching paragraphs.
- The original Step 10 paragraph prematurely claimed F had already been calculated and taught
  p-values before F. The current line 248 paragraph teaches calculating F from the completed mean
  squares, and the next step retains the original p-value instruction in its proper location.
- Original Practice Task and four Key Takeaways remain at lines 309-323. Additional model and
  method caveats constrain inference without removing the story or calculation explanations.
- Example word difference: original `I7:M7 - I10` becomes `I7:M7 - I11` in the SSR explanation at
  line 200. Original "p-value (in M3)" becomes "p-value (in M2)" at line 289. Its surrounding IF
  explanation remains, with nonrejection correctly described as insufficient evidence.

### PETase

Compared `PETase_1_Linear_Regression_Tutorial_Fall_2025.md` with
`petase_1_linear_regression.md` through the original Why Use Linear Regression Now? section.

- The original fictional startup, synthetic mutant's severalfold activity and thermal performance,
  engineering substitutions, fermentation premise, all three detailed yeast strain designs, and
  complete lysis/precipitation/Ni chromatography/size-exclusion purification paragraph remain at
  current lines 14-67. Treating the fictional performance statements as scenario premises is
  appropriate; requiring a new activity experiment before allowing them would rewrite the story.
- The full assignment, Bradford dye explanation, protein standards explanation, unknown-sample
  paragraph, and regression explanation remain at lines 71-118. The three original strain bullets
  remain a single coherent instructional list.
- Example word difference: original "minimizing the overall vertical distance between the data
  and the line" becomes "minimizing the sum of squared vertical distances between the data and
  the line" at lines 112-113. This corrects least squares while keeping the entire paragraph.
  Original "which yeast strain is actually producing the most PETase per fermentation batch"
  becomes "how much BSA-equivalent total protein was recovered in each preparation" at lines
  80-82. The additional protein-dependent dye-response sentence is a narrowly scientific addition.
- Original Step 1's external-spreadsheet setup is superseded by the supplied-workbook setup.
  Original Step 2 onward is an unrelated copied Microbes benchmark/t-test lesson. Its exclusion
  is correct. The current coherent Bradford calibration, residual, interpolation, dilution,
  recovered-protein, and interpretation workflow is not an omission of PETase instruction.
- The C2 blank-correction formula and C2:C8 fill instruction remain one paragraph at line 186,
  retaining both keyboard and fill-handle alternatives without duplicate action-log steps.

## Bindings, grouping, and workbook roles

Formula/value/label actions retain visible destinations in their own sentence or the parent list
item. For example, Microbes 1 D5/D8 formulas are nested beneath visible destination instructions;
Microbes 3 E16/F16/G16 and directional groups retain their distinct methods; Microbes 4's E17/G17
directions remain together; ANOVA SSR/SSE/SST formulas follow their named destination cells; and
PETase formulas and fills each identify their starting cell and range. Semantic URI targets add
machine meaning without requiring visible operational labels. No hidden duplicate formula inventory
was added.

Workbook regions appear only in Workbook sections and use disjoint source/calculation/results/
interpretation declarations. Early Microbes reserve source data through row 101 and keep alpha in
calculation, p-values/decisions in results, and the written response in interpretation. Microbes 4
retains D16:G18/D22:E24 results and D26:E26 interpretation; ANOVA retains L2:M2/H14:I14 results
and H16:I16 interpretation. PETase retains F1:G4/G13:G15 results and I12:J13 interpretation.
Student-visible teaching paragraphs do not expose region declarations.

## Verification and limits

Each of the six files passed its own `source source_me.sh && python3 make_tutorial.py lint FILE`
invocation with exit code 0. No LibreOffice command ran. Warnings describe documented spare
observation rows, two ANOVA SUMPRODUCT compatibility checks, PETase's free-text J13 response, and
optional Google mappings. These do not establish calculation or rendered-layout acceptance.

The first attempted lint command supplied six positional files; the CLI accepts one and rejected
that invocation before linting. The subsequent six independent file invocations all passed.

The source set was rechecked after the manager's freeze notification. Source hashes accepted:

| Source | SHA-256 |
| --- | --- |
| `microbes_1_z_test.md` | `2adb08ea9ce1115053ebdaa67a60b53f3b15b9e6768fc0bb609aaf1945ec658f` |
| `microbes_2_t_test.md` | `7e75603806f07ce2762833e1778774ea94fcd5775d02caee7fd504e7160b3d3f` |
| `microbes_3_two_sample_t_test.md` | `86ca0cce468641ada1dce58f22239b728e46921d96b75a753be46bcbf41e49a8` |
| `microbes_4_f_test.md` | `34c3a6e2e8d608b0dd84dd78b903cdbaac68f07f1bfcd1b94cd6ddf60bf89269` |
| `microbes_5_anova.md` | `e14c0188274ea813c7babab5076d051a2fd74c85a168c784d10797163bc5322c` |
| `petase_1_linear_regression.md` | `1831e9d7961f770884bb9debc83d24f33ab9f33bc0d218cb5a60eabce6825469` |

Remaining milestone work is actual generated PDF/DOCX/workbook review and local calculation
evidence against this frozen source set. Live Google behavior and student learning are unverified.
