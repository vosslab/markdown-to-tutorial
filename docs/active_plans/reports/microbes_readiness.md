# Microbial tutorial readiness

Path note (2026-10-22): paths and command examples below use the current repository layout.
Recorded observations belong to their stated snapshots; renamed output manifests retain their
original contents until the final rebuild and verification refresh.

All five active microbial lessons now provide an explanation before each calculation, explicit
student-entered labels, and a conclusion consistent with the supplied observations. Original
artifacts and image assets remain untouched. This report concerns source readiness; live Google
Sheets execution is not claimed.

## Reconciliation and intentional adaptations

The five original `2025_Artifacts/Microbes_*Tutorial_Fall_2025.md` guides and the original microbial
XLSX workbook were consulted. Their mean, variance, tail-comparison, IF-decision, sample-size
practice, and ANOVA-table construction objectives remain. Explanations now directly precede
the corresponding actions. Repetitive prose and empty Guide wrappers were replaced with complete
instructions; the Welch degrees-of-freedom comparison table remains.

- Generated workbook import replaces the historical shared-tab copying workflow. The original
  Google workbook remains a source reference, without asserting that its original tab names or
  screenshots match the generated workbook. Historical UI screenshots were removed from active
  instruction; original images were preserved. No substitute Google UI was fabricated.
- Students construct calculation labels as the originals teach. Duplicate migrated calculation
  label seeds were cleared and replaced by explicit Label actions. The former two-sample t-test
  F-statistic label is now T-Statistic. ANOVA now explicitly supplies every H1:M1 header, H2:H4
  source label, H6:M6 year label, H7:H9 group-summary label, and later summary/decision labels.
- Observation ranges still extend to row 101 for practice; instructions identify the actual
  counts, preserve empty cells, and keep hypothetical changes in a separate practice copy.
- No calculation formula or numeric parameter was changed in this readiness revision. The
  previously corrected directional tails, Welch approximation, variance-ratio orientation,
  F.TEST tail recovery, reciprocal F cross-check, and weighted ANOVA grand mean remain.
- Ecological motivation remains Busse Woods, Shannon diversity, sequencing, and the historical
  culture-method scenario. Assertions that scalar-index tests establish causation, species
  homogenization, resilience loss, or a time trend were replaced by the actual statistical
  questions. Matched sites, culture-versus-sequencing confounding, and separate ANOVA 2014 values
  are addressed where they affect the model.
- Expected decisions now occur in the interpretation steps. Nonsignificant outcomes explicitly
  mean insufficient evidence, replacing inconsistent has/has-not-changed templates. Part 3's
  lower directional rejection and two-tailed nonrejection are both explained. ANOVA uses only
  its right-tail p-value; generic three-tail wording has been removed from that lesson.

## Seed and formula comparison

An independent table comparison against pre-edit copies checked every raw-data cell, including
headers, identifiers, spacing, and blank positions. Numeric source checks also compared every
numeric raw cell against the original XLSX. ANOVA numeric counts include its 24 numeric IDs;
there are 93 actual Shannon observations. All comparisons had zero mismatches.

| Lesson | Raw cells including headers/blanks | Numeric XLSX comparisons | Intentional calculation labels cleared | Formula actions unchanged |
| --- | --- | --- | --- | --- |
| Z | 50 | 24 | 0 | 9 |
| One-sample t | 50 | 24 | 0 | 13 |
| Welch t | 75 | 48 | 11 | 19 |
| F | 75 | 48 | 11 | 17 |
| ANOVA | 150 | 117 | 22 | 27 |

In the two-sample sheets the cleared cells are D5, D6, D8, D9, D11, D13, D14,
D16:D18, and D20. These contained calculation labels/year markers, not observations.
The ANOVA cleared calculation cells are H1:M1, H2:H4, H6:M6, H7:H9, H11, H13,
H14, and H16. The source separator dot G1 is retained. No raw-data header was cleared.

## Instruction walkthrough

Each formula cell was checked in source order against its inputs and each final interpretation
against the independent calculation report. Label actions target blank calculation cells;
all formulas reference either supplied observations, previously entered numeric parameters,
or earlier calculated cells. Interpretation destinations are D19, D19, E26, E26, and I16.

| Lesson | Input-to-conclusion walkthrough |
| --- | --- |
| Z | D2/D3 parameters -> D5/D6 summaries -> D8 Z -> D10:D12 tails -> D14 alpha -> D15:D17 decisions -> D19 interpretation. Lower p 0.04864 rejects; two-tail p 0.09728 fails to reject. |
| One-sample t | D2 benchmark -> D4:D6 summaries -> D8 t/D9 df -> D10:D12 tails and E10/E12 checks -> D14 alpha -> D15:D17 decisions -> D19 interpretation. Lower p 0.14043 fails to reject. |
| Welch t | E2/E3 means, E5/E6 SDs, E8/E9 counts -> E11 signed t -> E13 fractional df -> E16:E18 tails with F/G checks -> E21 alpha -> E22:E24 decisions -> E26 interpretation. Lower p 0.03141 rejects; two-tail p 0.06282 fails to reject. |
| F | E5/E6 SDs, E8/E9 counts -> E11 2024/2014 ratio -> E13/E14 df -> E16:E18 tails with F/G checks -> E20 alpha -> E22:E24 decisions -> E26 interpretation. Lower p 0.02207 and two-tail p 0.04413 reject; numerator df follows 2024 throughout. |
| ANOVA | I7:M9 year summaries -> I11 weighted grand mean -> I2:I4 df 4/88/92 -> J2:J4 sums of squares -> K2/K3 mean squares -> L2 F -> M2 right-tail p -> I13 alpha/I14 decision -> I16 interpretation. Right-tail p 0.47999 fails to reject. |

The walkthrough corrected missing ANOVA construction steps, mislabeled two-sample calculations,
formulas appearing before explanation, unsigned one-tail descriptions, causal introductions,
and incompatible interpretation templates. The text distinguishes the chosen lower hypothesis
from teaching comparisons, and variance of indices from taxonomic community composition.

## Verification

Each of the five files passed `source source_me.sh && python3 make_tutorial.py lint <file>`.
Warnings cover intentional ranges through row 101, unconstrained student interpretation cells,
unmapped Google URLs, and ANOVA SUMPRODUCT compatibility requiring target-engine verification.
These are not claimed as live spreadsheet evidence.

`source source_me.sh && python3 -m devel.check_tutorial_calculations` passed after the revisions:
12 lessons, 13 scenarios, 254 formula expectations, and eight synthetic direction checks.
For these five lessons, all 85 formula-action target/formula pairs are byte-for-byte unchanged
from the pre-edit active sources. Independent numerical expectations validate the intended
statistics, not Google Sheets evaluation or fractional-df behavior in its distribution functions.

Final source review and generated output review remain separate evidence lanes owned by the
coordinating agent.

## Teaching-content corrections (2026-10-22)

The Z-test practice prompt now follows its fixed-known-SD design: students compare changes in the
sample mean, count, Z-statistic, p-value, and decision while the stipulated population SD in D3
remains 0.6. It no longer asks students to calculate an SD or variance that the worksheet does not
use. The restored `microbes_1_z_test_image2.png` is captioned as a lower-tail standard-normal
illustration and explicitly separated from this dataset's result.

The F-test practice prompt now focuses on the sample SDs, sample sizes, variance ratio, p-value,
and decision; it no longer asks for means that are absent from the F-test calculation. The ANOVA
scenario again explains the original historical premise: hypothetical 1994/2004/2009 thesis
datasets used culture, colony observations, and staining, while 2014/2024 use sequencing. It also
states why those methods differ and that the narrative is not verified provenance or causal evidence.
