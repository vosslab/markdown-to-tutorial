# Local calculation readiness

Path note (2026-10-22): paths and command examples below use the current repository layout.
Recorded observations belong to their stated snapshots; renamed output manifests retain their
original contents until the final rebuild and verification refresh.

## Execution scope

[`validate_libreoffice.py`](../../../devel/validate_libreoffice.py) executes prepared tutorial
scenarios through the installed LibreOffice Calc executable. It applies typed initial seeds and
authored assignments in order to a fresh XLSX workbook. Later assignments replace earlier values.
Each conversion uses a private temporary LibreOffice profile and a new output directory.
It reads Calc's saved cached results with `openpyxl` in `data_only` mode, then compares them with
the independently generated expectations through `sheets_validation_lib.compare_expectations`.
It does not calculate formula results in Python.

This verifies final workbook states. It does not observe intermediate formula errors, recalculate
after each authored step, or execute Google Sheets. Local engine evidence cannot establish Google
Sheets compatibility or a successful student workflow in that application.

## Reproduction

```bash
source source_me.sh && python3 devel/check_tutorial_calculations.py -o tutorial_output/validation/local_calc
source source_me.sh && python3 devel/validate_libreoffice.py tutorial_data/*.md \
  -e tutorial_output/validation/local_calc/tutorial_expectations.json -o tutorial_output/validation/local_calc/calc
```

On this macOS installation, launch Calc outside the restricted execution sandbox. Every run retains
its calculated workbooks and `report.json` under a unique `run-*` directory. The JSON records engine
version, tutorial source SHA256 hashes, expectation file SHA256, validator SHA256, source lines,
authored values, expected and actual values, and engine diagnostics. A calculation error, missing
final formula cache, missing expectation mapping, or numerical mismatch fails validation.

## Initial engine evidence

The first raw-formula run used LibreOffice `26.2.6.3`, build
`8221e31b3ac356a1623c672912a3d2b492f7e3d1`, and exercised all 13 scenarios against
254 expectations. It passed 185 comparisons and failed 69. Only the PETase scenario passed every
comparison. The retained evidence is
`tutorial_output/validation/local_calc_initial/calc/run-__6f3dyi/report.json`.

Modern function names such as `STDEV.S`, `T.DIST`, and `NORM.S.DIST` produced `#NAME?` when their raw
authored names were stored directly in XLSX. This is a serialization issue before mathematical
agreement can be assessed: [openpyxl documentation](https://openpyxl.readthedocs.io/en/3.1/simple_formulae.html)
requires `_xlfn.` for functions outside the original spreadsheet specification. Additionally,
[Calc documentation](https://help.libreoffice.org/latest/en-GB/text/scalc/01/04060185.html)
specifies two parameters for `NORM.S.DIST`, while the Google-authored formulas supply one.

These results are failed local engine evidence. They do not establish that the intended mathematics
or the Google formulas are wrong. Sources were being revised during this initial run; the source
hashes in the retained JSON identify the exact snapshot.

## Portable statistical formulas (2026-10-22)

After OOXML serialization was corrected, Calc passed 239 of 254 comparisons. The remaining
15 failures identified two authored formula incompatibilities, rather than missing expectations:

- The two Z-test lessons used Google's one-argument `NORM.S.DIST`, whereas Calc requires a second
  argument. They now teach `NORM.DIST(z, 0, 1, TRUE)`, explicitly explaining the standard mean,
  standard deviation, and cumulative flag. Google's [official function
  table](https://support.google.com/docs/table/25273?hl=en) lists the four-argument signature.
- The Microbes Welch lesson preserved fractional df in E13, but Calc's `T.DIST` family truncated
  it. The manual route now uses `BETADIST(df/(df+t^2), df/2, 0.5)` for the two-tail probability,
  then uses half that probability or its complement according to the signed statistic. This
  retains the manually calculated t and fractional df; column G remains the direct `T.TEST`
  comparison on observations. F16 checks twice the smaller directional tail; F18 checks the
  complement of the lower tail. These checks reuse the manual calculation and are labeled as
  such in the explanation. No oracle values or numerical tolerances were changed.

The beta identity follows the [Boost Math Student t implementation
documentation](https://www.boost.org/doc/libs/latest/libs/math/doc/html/math_toolkit/dist_ref/dists/students_t_dist.html).
The positive-t survival probability is half the regularized beta probability; symmetry supplies
the negative-t case. At t = 0, the beta argument is 1, so the two-tail probability is 1 and both
directional probabilities are 0.5. [Google's dedicated beta
documentation](https://support.google.com/docs/answer/9084228) documents the `BETADIST` alias and
default bounds, while [Calc's statistical
documentation](https://help.libreoffice.org/latest/en-US/text/scalc/01/04060181.html) explicitly
documents the three-argument cumulative default. The legacy spelling avoids a discrepancy between
Google's function table and dedicated page about the modern `BETA.DIST` cumulative argument. It
needs no OOXML future-function prefix; only the checked function vocabulary gained `BETADIST`.

All three changed lessons passed offline lint, retaining advisory spare-range and explanatory
input warnings. Independent oracle regeneration produced 12 tutorials, 13 scenarios, 254
expectations, and eight model direction checks. Calc `26.2.6.3` passed all 254 comparisons across
all 13 scenarios in `tutorial_output/validation/local_calc_portable/calc/run-eehzg5wq/report.json`.
The actual Welch two-tail result was 0.0628180587792008, versus the independent SciPy t oracle
0.06281805877920066. This supersedes the integer-df result 0.06291083538786.

A temporary three-scenario check used the repository's Calc runner for t = -1.91452, 0, and
+1.91452 with df = 39.49524. All 15 beta-tail, directional, and complement comparisons passed
against independent SciPy t CDF/survival probabilities. Evidence is retained in
`tutorial_output/validation/local_calc_portable/signed_t_probe/report.json`. The probe remains a
one-time verification rather than a permanent implementation-mirroring test.

This establishes final-state calculation in the installed Calc engine. Google Sheets execution
and student interaction remain unverified by these local checks.

## Final source snapshot refresh

After removing a trailing blank line from the babies t-test source, the independent expectations
were regenerated and the complete Calc suite was rerun against the final source tree. LibreOffice
`26.2.6.3` passed all 254 comparisons across 13 scenarios with zero failures. The current report is
`tutorial_output/validation/final_readiness/calc/run-o6vh03zz/report.json`; it records the final
babies source SHA-256 `abe7089e1c3bbf1be6caadcb66d8a3123c6b9830cab5bab6816547ac383d596b`, expectation
SHA-256 `5bea9e0aa660cb6d8ccaa5ddcd17bdc9b628ed8c9952af7559d4218ee0af3543`, validator SHA-256
`d783fa77dc5fb23e02762e9eef98074346bf53f3d520785a1f590b23c435d22e`, and formula I/O SHA-256
`54b800b80ed432c49c83b7622108111f1cd58c547b9da7b8d53e237358fde029`. This supersedes the earlier
portable-run source snapshot for current readiness. Google Sheets execution remains unverified.
