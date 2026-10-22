# Final tutorial build and artifact verification

All twelve final sources compiled and built as DOCX, XLSX, and PDF bundles after content freeze. Each source and referenced asset fingerprint in `validation.json` matches the current file, and each artifact hash matches its manifest record. All 36 files reopened successfully; DOCX packages passed ZIP/XML parsing, XLSX data and layout checks passed, and all PDFs have readable page trees.

Builds ran sequentially with `source source_me.sh` and `python3 make_tutorial.py build tutorial_data/<stem>.md` outside the sandbox because PDF export invokes LibreOffice. Per-source command output is recorded in `tutorial_output/verification/readiness/<stem>.log`. The full source, asset, artifact SHA-256 values and check results are in `tutorial_output/verification/readiness/artifact_inventory.json`.

| Source | Source SHA-256 | PDF pages |
| --- | --- | ---: |
| `tutorial_data/babies_1_z_test.md` | `e779ee72652dccfd1c4cba0fc4462080ab2c6da9ba54150235d6c330580d9cc3` | 6 |
| `tutorial_data/babies_2_t_test.md` | `abe7089e1c3bbf1be6caadcb66d8a3123c6b9830cab5bab6816547ac383d596b` | 6 |
| `tutorial_data/babies_3_two_sample_t_test.md` | `8f512794cd41431810780a91c7de768694ad76887b86f0128082ea2d532eb8ec` | 4 |
| `tutorial_data/caffeine_1_descriptive_statistics.md` | `5d9d7e5048940f7b77e851f464aceffd987121ecd835e233d44dada2b675e052` | 3 |
| `tutorial_data/caffeine_2_linear_regression.md` | `4d8896d3711f97116ccc55a6fbfaebef20515d92510504d06ca277a003f459f0` | 7 |
| `tutorial_data/caffeine_3_quadratic_regression.md` | `b65f44854a6b0a760703bd9744d76e41882db4098fccbffb6ace547da26dd072` | 9 |
| `tutorial_data/microbes_1_z_test.md` | `d1948286197f184b2a203ea449fb30caac8405456aa7baf1f02ec10636e28799` | 4 |
| `tutorial_data/microbes_2_t_test.md` | `17f7e2845a4af25102605e50c3f72bd88e78f3ea33785109c0f7159e833b2121` | 4 |
| `tutorial_data/microbes_3_two_sample_t_test.md` | `16d11d0a3230ae8f7352970c31dbee15211a412c157606544bb28d4fc96715a0` | 6 |
| `tutorial_data/microbes_4_f_test.md` | `975374fb5ea9ae89a253480e1faba60b55e09f39ad42d7fa1e24483dc599cd06` | 5 |
| `tutorial_data/microbes_5_anova.md` | `35a16b3e938507a4972ee27999555733b3d073d2e5b32487face8fb043612347` | 5 |
| `tutorial_data/petase_1_linear_regression.md` | `7dcea47a9f506484f8faae9d6a835f1e2d41f6f1ef817e94ebb2adbe4314d572` | 6 |

The independent workbook pass confirmed every Label/Enter destination is blank, worksheet names and authored seeds are preserved, header panes and useful column widths are present, and DOCX headings, Label/Enter content, embedded source images, and native PAGE fields survive export. The build checks do not calculate formulas; local Calc execution is reported separately. Visual PDF review is also reported separately.

The final babies t-test source snapshot removed one trailing blank line after the all-lesson build. All three formats were rebuilt from that exact source; the current DOCX, XLSX, and six-page PDF hashes and sizes replace the earlier inventory values. The source fingerprint also matches the final Calc report. The refreshed PDF was rasterized at 110 dpi and all six pages were visually reviewed; no layout change or blocking defect was found. The retained earlier image set remains historical render evidence.

Current `make_tutorial.py` source workflows were also exercised. A temporary fenced `sheets` formula changed from `=A2*2` to `=A2*3`, a new Step was inserted and numbering shifted from 1–2 to 1–3, and the updated formula and instruction appeared in DOCX and PDF while the new workbook retained the changed seed. A separate workbook moved from A1 to D4 and then renamed its sheet from `Data` to `Observations`; outputs tracked the source basename, seed values moved to D5, formula and instruction targets updated to F5, and each Label/Enter target remained blank. Fingerprints, source snapshots, outputs, and per-build logs are under `tutorial_output/verification/readiness/editable_workflow/`; structured results are in `workflow_results.json`.
