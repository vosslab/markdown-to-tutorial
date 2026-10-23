# Voice restoration build checkpoint

Build checkpoint: 2026-10-22 18:05 CDT.

## Baseline preservation

Before rebuilding, the 12 canonical tutorial bundles were copied from their existing
`tutorial_output/<tutorial-name>/` directories into
`tutorial_output/voice_restoration/before/<tutorial-name>/`. The preserved set contains 48
files: one DOCX, PDF, XLSX, and `validation.json` for each tutorial. The copies preserve the
pre-restoration state for later comparison.

## Caffeine rebuilds

Each build used the repository bootstrap and CLI, with `--format all`. PDF generation ran outside
the sandbox as required by `AGENTS.md`.

```sh
source source_me.sh && python3 make_tutorial.py build tutorial_data/caffeine_1_descriptive_statistics.md --format all
source source_me.sh && python3 make_tutorial.py build tutorial_data/caffeine_2_linear_regression.md --format all
source source_me.sh && python3 make_tutorial.py build tutorial_data/caffeine_3_quadratic_regression.md --format all
```

| Source | Bundle directory | PDF pages | Result |
| --- | --- | ---: | --- |
| `tutorial_data/caffeine_1_descriptive_statistics.md` | `tutorial_output/caffeine_1_descriptive_statistics/` | 3 | Published |
| `tutorial_data/caffeine_2_linear_regression.md` | `tutorial_output/caffeine_2_linear_regression/` | 10 | Published |
| `tutorial_data/caffeine_3_quadratic_regression.md` | `tutorial_output/caffeine_3_quadratic_regression/` | 7 | Published |

Each published bundle contains `<tutorial-name>.docx`, `<tutorial-name>.pdf`,
`<tutorial-name>.xlsx`, and `validation.json`. PDF page counts came from `pdfinfo` on the newly
published files. The builds emitted informational `google-unmapped` notes for all three sources
and formula-coverage warnings for `INDEX` and `LINEST` in the two regression tutorials; all three
builds completed and published.

## Checkpoint boundary

The current canonical layout is one directory per tutorial directly under `tutorial_output/`;
each directory holds the three deliverables and validation JSON. The pre-restoration copies are
nested under `tutorial_output/voice_restoration/before/`. Only the three Caffeine sources were
rebuilt at this checkpoint. The other nine bundles still reflect the prior source state. No
calculation oracle was regenerated or checked here; the manager will release the remaining builds
and repository calculation-check workflow once all sources are ready. Successful compilation and
publication establish build completion only, not classroom-quality review.

The requested report location was interpreted as `docs/active_plans/reports/`, the existing
reports directory in this repository.
