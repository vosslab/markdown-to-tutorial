# Authoring guide assessment rubric

## Purpose and audience

Assess whether BIOL 318 students who have completed several biostatistics tutorials can use the
guides to create original tutorials. They know the learner experience but may be new to Markdown
and command-line tools. Their work contributes to open pedagogy and Student-Generated Content.

Use this rubric to identify useful improvements, not as an automated gate or a measure of student
learning. Review the README, authoring hub, three Parts, visual reference, and linked references.

## Scoring

Score each dimension separately. Cite a page and section, an observed task result, or a specific
source/output comparison. Mark unexamined evidence as unverified rather than assigning a score.

- **4 - Strong:** clear and usable throughout the sampled tasks; no material obstacle observed.
- **3 - Useful:** task succeeds with a small, recoverable ambiguity or extra lookup.
- **2 - Needs revision:** repeated guessing, missing guidance, or a misleading example impedes work.
- **1 - Obstructive:** a core task fails or the guidance directs the author toward the wrong outcome.

| Dimension | What strong evidence looks like |
| --- | --- |
| Audience and purpose | Welcomes experienced tutorial learners who are new authors; explains why their original contributions matter; teaches authoring rather than basic statistics or spreadsheets. |
| Clarity and navigation | Students can find an entry point, feature, runnable example, and build instructions; prerequisites and terms are explained when needed; copyable source is distinct from placeholders. |
| Visual demonstrations | Important features pair literal Markdown with readable, tightly cropped actual output; prose and alt text explain the effect; screenshots agree with source. |
| Capability coverage | Document structure, text, lists, tables, images, workbook layout, data, blanks, formulas, actions, and build/revision are discoverable; limits and advanced tools have appropriate references. |
| Student independence | Techniques transfer to an independently chosen scenario without completing Roots; students control scientific content and teaching approach; examples do not prescribe a lesson. |
| Technical accuracy and recovery | Documented commands work; source produces intended DOCX/XLSX content; blanks and action targets behave as described; a diagnostic can be understood and corrected from the docs. |
| Quality and maintainability | Technical requirements are distinct from scientific/instructional advice; links and GitHub formatting work; useful examples have clear ownership without unnecessary duplication or infrastructure. |

## Independent walkthrough

Use a fresh reviewer who did not author these guides. Begin at README.md. Use only student-facing
documentation and linked examples to learn syntax; do not read compiler internals or tests to solve
the task. Tools may inspect generated files. Record any outside help separately.

1. Choose a small original biological scenario and an intended reader task. Do not use Roots or
   reproduce an instructor scenario. Define intended results before building.
2. Find the required syntax and write a disposable tutorial with a title, Part, Step, prose,
   numbered instructions, supplied data and labels, a blank calculation area, and a response area.
   Include a formula-entry instruction and a fill action. Use a document table or image as well.
3. Lint and build DOCX/XLSX using the documented commands. Inspect both files, including visible
   formatting and workbook values/blanks. Compare each result against the declared intent.
4. Change a data range or destination. Introduce one plausible source error, use the diagnostic and
   documentation to correct it, and rebuild. Record failed attempts and what resolved them.
5. Sample the visual reference and compare representative snippets with actual generated output.

Record task completion, navigation route, errors, guesses, outside help, and output evidence.
Do not interpret an AI reviewer's speed as student time-on-task. Label environment limitations
separately from documentation problems. Preserve the original review before making corrections.

## Findings and follow-up

For each finding, state the affected task, evidence, student impact, and smallest useful correction.
Prioritize blockers and misleading instructions, then repeated friction, then cosmetic preferences.
Do not use a total score to hide a weak dimension. Recheck affected tasks after corrections and
record what changed without rewriting the reviewer's original scores.

The next source of stronger evidence is an observed session with representative BIOL 318 students:
ask them to create a small tutorial on their chosen topic, think aloud, find a feature, and repair an
error. Record where help is needed and inspect their files. Ask what they believe they contribute
to the class collection. Such sessions can reveal problems an expert or AI reviewer misses; this
rubric alone does not establish learning outcomes or classroom readiness.
