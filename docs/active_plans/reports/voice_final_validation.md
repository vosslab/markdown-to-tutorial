# Voice restoration final validation

Date: 2026-10-22.

The integrated validation run passed after the rendering-spec acceptance and source freeze. The complete repository suite reported **1,545 passed**, exit status 0, in 3.33 seconds. The captured full log is `tutorial_output/voice_restoration/final_build/full_suite.log` (SHA-256 `447b5eaf9b5d8c08f7b8b4259f42ed487610f496c498db52c692f9d3bf65f54b`).

All 12 canonical tutorials rebuilt successfully as DOCX, XLSX, and PDF. The PDFs total **92 pages**. Their per-tutorial page counts and source/artifact hashes are in the [final build receipt](voice_restoration_final_build.md). The ignored generated manifest at `tutorial_output/voice_restoration/final_build/manifest.json` contains the same data in JSON form.

LibreOffice Calc 26.2.6.3 passed **13 scenarios and 254 formula comparisons** using the existing `tutorial_output/validation/tutorial_expectations.json`. Its SHA-256 remained `5bea9e0aa660cb6d8ccaa5ddcd17bdc9b628ed8c9952af7559d4218ee0af3543` before and after validation. The execution report is in `tutorial_output/voice_restoration/final_build/calc/`; this validates final-state calculation only. It does not establish intermediate-state behavior or Google Sheets compatibility.

The exact Calc command was:

```sh
source source_me.sh && python3 devel/validate_libreoffice.py tutorial_data/*.md \
  -e tutorial_output/validation/tutorial_expectations.json \
  -o tutorial_output/voice_restoration/final_build/calc
```

The expectation-generation script was deliberately not used because it rewrites the expectation file. LibreOffice suite/build/calculation commands ran outside the sandbox as required by the repository instructions.

Build diagnostics remain scoped to authored practice ranges that extend beyond the supplied data, optional Google worksheet mappings that are absent, and offline coverage limits for `INDEX`, `LINEST`, and `SUMPRODUCT`; per-line records are in each bundle’s `validation.json`. Fresh independent review of the rebuilt student materials is a separate acceptance step; this receipt does not claim material-quality acceptance.
