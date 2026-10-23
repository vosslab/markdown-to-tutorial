# Illustrated Authoring Course: Plan and Task Ledger

## Outcome

Create a polished, self-teaching tutorial that teaches an instructor how to author tutorials with this project. The student edits one continuous Markdown project source across the course. The course is published as three compiled Parts, organized into Steps and Substeps. Each of eight checkpoints has a saved source for comparison and resumption. Keep authored source ASCII.

The three conceptual Parts are: create a first tutorial; complete a beginner statistics tutorial using `COUNT`, `AVERAGE`, and `STDEV.S`; and optionally grow, maintain, and share the tutorial. Preserve instructor-authored prose and scientific voice. Automation may structure, format, check, and capture materials, but does not author publication prose.

## Data and workbook contract

Use synthetic root-length observations in millimeters: `12, 15, 18, 20, 25`. The initial workbook has sheet `Roots`, observations in `A1:A6` (header plus five values), and a summary in `D1:E4`: row 2 count, row 3 mean, row 4 sample standard deviation. Expected values are `n=5`, mean `18`, and sample SD `4.949747468305833`.

The growth checkpoint adds `30` in row 7 and deviations `=A2-$E$3` filled through `B2:B7`; the six-value result is `n=6`, mean `20`, and sample SD approximately `6.603` (verify with an independent calculation). The shifted-layout checkpoint inserts a column A: observations move to B, summary to E:F, deviations to C, and the formula becomes `=B2-$F$3`.

## Decisions

| ID | Decision | Reason |
| --- | --- | --- |
| D1 | Use the synthetic root-length dataset and cell addresses above as the shared course example. | One small data set can carry the beginner course through formulas, growth, and layout changes. |
| D2 | Students edit one continuous Markdown project source across three compiled course Parts; save eight checkpoint sources as references. | Learners have one project to complete while retaining concrete comparison and resume points. |
| D3 | Provide a starter workbook with supplied labels and blank calculation cells, plus a disposable completed example. | Students need an editable starting state and a clear finished reference without confusing the two. |
| D4 | Agents and manager complete their work autonomously; there are no human approval gates in this plan. | The approved project should proceed through implementation and integration without waiting for additional sign-offs. |
| D5 | Capture an overview excerpt by selecting semantic document headings and including the complete first inspection Step. | A useful opening view should show both the course context and a novice's first concrete action. |
| D6 | Permit exactly two non-visible screenshot comment markers; reject other HTML in course source. | Capture boundaries need a narrow, deterministic source convention without adding visible prose. |
| D7 | Validate captured WebP files by decoding them locally; convert to in-memory PNG only at the DOCX insertion boundary. | Keep native capture assets compact and preserve their source bytes. |
| D8 | Fit images within printable width and available page height while preserving aspect ratio; keep code blocks together. | Avoid clipping and code-line splits in exported course Parts. |
| D9 | Merge the redundant summary-location Step into `Inspect the supplied data`; retain the complete first inspection Step in the overview. | The overview remains informative without leaving a two-bullet capstone orphan. |

Invite clarification, challenge, or escalation questions when consequential uncertainty appears. Investigate available repository evidence first and continue independent work while resolving it.

## Task ledger

Statuses: `in progress`, `pending`, `complete`, or `blocked`. Each owner should update their row with evidence and any remaining limitation.

| ID | Work | Status | Evidence / completion condition |
| --- | --- | --- | --- |
| examples | Author checkpoint sources `docs/examples/authoring_course/root_01_meet.md` through `root_08_share.md`, including the specified workbook stages and handoffs. | complete | Eight coherent ASCII checkpoint files; calculations and cell references agree with the data contract. Final SPEC review accepted all 15 literal excerpts. |
| course | Build `docs/learn/PART_1_CREATE.md`, `PART_2_STATISTICS.md`, and `PART_3_IMPROVE.md` as Parts of one continuous learner experience. | complete | One student project source continues through three compiled Parts; novice gaps, overview clipping, and page spills are resolved. Final QUALITY review accepted. |
| visualreference | Make six focused reference pages under `docs/reference/` and native visual starter/completed examples. | complete | Six linked reference pages; starter labels are supplied and calculation cells blank; completed examples are disposable. |
| capture/nativeoutputs | Produce and review the published capstone Markdown, DOCX, PDF, and XLSX under `docs/examples/authoring_course/published/`. | complete | All four outputs exist; the final refresh command exited 0 at 12:23 UTC and regenerated 16 course / 25 total screenshots. The visual review reports clipping, code widows, and capstone overflow fixed; the published capstone is one balanced page. Calculation evidence and report limitations are recorded in [the visual refresh report](../reports/illustrated_course_visual.md). LibreOffice stages run outside the sandbox. |
| navigation | Add `docs/STUDENT_GUIDE.md` as the student-facing hub and connect the Parts, references, checkpoints, and capstone. | complete | Hub links the three Parts, six references, eight checkpoints, and published examples. |
| freshSPEC | Have a fresh reviewer inspect the course specification and source continuity. | complete | Final SPEC review accepted. All 15 literal excerpts match; links, source continuity, calculations, published outputs, captures, and protected/source hashes agree with current receipts. |
| freshQUALITY | Have a fresh reviewer assess teaching quality, clarity, calculations, and visuals. | complete | Fresh QUALITY review accepted after inspecting the hub, three Parts, six references, checkpoints, all 16 course images, 17 Part PDF pages, and the one-page capstone. Prior clipping, novice execution gaps, and page spills are resolved. The sparse Part 1 page 6 and a table continuation are nonblocking; this is expert review, not student testing. |
| freshintegration | Have a fresh reviewer check the integrated navigation and published native outputs. | complete | Fresh integration review accepted with no findings. It verified 131 receipt hashes, 135 navigation links/anchors, 11 clean compiles, current screenshot/native annotations, four published files matching checkpoint 5, and the stated local-only limits. See the [final integration report](../reports/illustrated_course_integration.md). |

## Environment and verification

Run Python as `source source_me.sh && python3`. Do not use `py_compile`. Any command that invokes LibreOffice, including PDF export and document conversion/import, must run outside the sandbox using repository scripts. Keep generated native outputs within the stated published directory. Record substantive implementation changes in `docs/CHANGELOG.md`; record durable human guidance and design decisions in their canonical docs when applicable.

## Updates

| Date | Update |
| --- | --- |
| 2026-10-23 | Created the approved plan and initialized the task ledger. |
| 2026-10-23 | Completed course products and corrected the student-source/compiled-Part distinction. Merged the redundant summary-location Step into Inspect the supplied data, then refreshed captures successfully: 16 course and 25 total images. The full suite passes 2,036 tests. Fresh SPEC, PDF visual, QUALITY, and integration reviews are accepted; external Google behavior and student outcomes remain unverified. |
