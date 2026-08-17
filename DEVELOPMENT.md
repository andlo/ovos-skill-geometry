# Development

## Architecture at a glance

Two content types: a **glossary** (24 terms/shapes, `GLOSSARY`/
`GLOSSARY_NAMES`/`GLOSSARY_DEFINITIONS`, one-sentence definitions,
`what_is.intent`) and **formulas** (`FORMULA_PROPERTIES`/
`FORMULA_WORDS`, both recited in words via `formula_of.intent` and
applied numerically via 8 per-shape intents like `area_of_rectangle.intent`).
All hand-authored in `data/build_glossary.py` / `data/build_locale_files.py`
(one-off scripts, not runtime dependencies - see CREDITS.md for why
this content is translated by hand rather than sourced from CLDR the
way `ovos-skill-geography`'s country names are).

**Public API, not just intent handlers** - same pattern as
`ovos-skill-geography`: module-level data and plain functions
(`resolve_term()`, `term_name()`, `term_definition()`,
`formula_words()`, `rectangle_area()`, `pythagorean_hypotenuse()`,
`PYTHAGOREAN_TRIPLES`, `format_number()`, all taking `lang` explicitly)
are what `ovos-skill-geometry-practice` imports directly.

## Scope: which shapes get formulas

`FORMULA_PROPERTIES` deliberately covers only rectangle/square/
triangle/circle - not every glossary shape. Rhombus/pentagon/hexagon
and every 3D shape have a glossary DEFINITION (`what is a rhombus`)
but no formula-application intent. Extending this list is
straightforward (add a computation function, formula-words entries
per locale, and an intent+dialog per locale) but wasn't done for v1
scope reasons, not a technical blocker.

## `resolve_term()` doubles as shape/property resolution

`formula_of.intent` ("what is the formula for the area of a circle")
captures `{property}` and `{shape}` slots - both are resolved via the
SAME `resolve_term()` used for `what_is.intent`, since properties
(area, perimeter, circumference) and shapes (circle, rectangle, ...)
are themselves glossary terms. No separate property/shape vocabulary
to maintain.

## da-dk/de-de: "perimeter" and "circumference" share a word

Danish `omkreds` and German `Umfang` both mean "the distance around
the outside" regardless of whether the shape is a circle or a
polygon - unlike English, which distinguishes "perimeter" (polygons)
from "circumference" (circles). This is real, not a translation gap:
`glossary_names.json` for da-dk/de-de maps BOTH the `perimeter` and
`circumference` keys to the same spoken word. `TERM_NAME_TO_KEY`'s
reverse lookup means that shared word resolves to whichever key was
written last when the dict was built - callers should treat this as
"resolves to A valid key with that name", not "resolves to a specific
one of the two". `test_term_name_to_key_roundtrips` documents and
locks in this behavior rather than treating it as a bug to silently
paper over.

## Formula recitation and Pythagoras use `format_number()`-free text

`FORMULA_WORDS` stores the formula already spelled out in natural
words per language ("the area of a circle is pi times the radius
squared") - not a template with `{radius}` slots, since formula
RECITATION never has actual numbers to substitute (only formula
APPLICATION, the 8 per-shape intents, computes real numbers and uses
`format_number()`).

## Setup
```bash
git clone https://github.com/andlo/ovos-skill-geometry.git
cd ovos-skill-geometry
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
pip install -r requirements-test.txt
```

## Running tests
```bash
pytest tests/ -v
```
`tests/test_data_loading.py` checks glossary/formula-word coverage
across all 5 locales. `tests/test_computations.py` covers the pure
math functions, including the Pythagorean-triples-are-exact /
non-triples-are-irrational distinction. `tests/test_intents.py`
covers all 11 intent handlers, en-us locale.

## Versioning

`version.py` follows `VERSION_MAJOR.VERSION_MINOR.VERSION_BUILD[aVERSION_ALPHA]`,
same convention as the rest of this project family.

## Releasing

Releases are tag-triggered (`v*`):
```bash
git add version.py
git commit -m "chore: bump version to 0.0.X"
git tag vX.Y.Z
git push && git push --tags
```
Triggers `.github/workflows/test.yml` then `.github/workflows/publish.yml`
(PyPI via trusted publishing - needs a one-time per-package browser
setup on PyPI before the first tagged release, same as every other
package in this project family).

## Style / conventions

- License: GPL-3.0-or-later.
- `locale/<lang-code>/` layout, `skill.json` inside each locale
  folder.
- Present design changes for review before implementing.
