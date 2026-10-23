# Same-paragraph destination reference validation

The content validator previously checked inline cell references against the state before the
paragraph's actions ran. This made prose such as “In cell `I2`, enter `=...`” look like a read of an
unavailable input, even though `I2` is the formula's destination. The validator now exempts an
inline prose reference only when it exactly matches a write destination in that paragraph. It still
validates formula references through the ordered action replay, so a formula cannot read a cell
that is assigned later in the same paragraph.

Focused coverage checks a valid formula destination, a genuinely missing formula input, and
multiple same-paragraph actions in both dependency orders. The future-input formula remains an
`unavailable-input` diagnostic; the earlier-input formula validates cleanly.

Validation command:

```bash
source source_me.sh && pytest tests/test_tutorial_bindings.py
```

Result: 6 passed. A direct compile of `tutorial_data/microbes_5_anova.md` produces no
`unavailable-input` warning for the `I2` destination reference. Existing warnings for
`B2:F101` remain at lines 165, 174, and 175 because those cells are not supplied in the fixture's
workbook table; formula checks at lines 173–175 still run, and the formula referencing missing
`B2:F101` remains flagged.
