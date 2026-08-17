# Data credits and licensing

## Glossary, definitions, and formulas

Hand-authored, not sourced from an external dataset - this is
standard, well-established mathematical vocabulary (shape names,
geometric terms, formulas), not idiosyncratic like place names or
capital-city spellings, so it's translated directly by hand rather
than via an authoritative source like Unicode CLDR (which
`ovos-skill-geography` uses for country/currency/language names).

See `data/build_glossary.py` (the glossary + formula-words content)
and `data/build_locale_files.py` (intents/dialogs/skill.json) for the
full English source text and its da-dk/de-de/fr-fr/es-es translations.

## A documented linguistic fact, not a bug

Danish and German use the SAME word for "perimeter" and
"circumference" (`omkreds` / `Umfang`) - unlike English, which has
two distinct words. `resolve_term()` and `TERM_NAME_TO_KEY` handle
this correctly (the shared word resolves to A valid matching key, not
necessarily always the same one), but it's worth knowing about if
you're reading or extending the da-dk/de-de glossary files. See
DEVELOPMENT.md.

## License

The skill's own code is GPL-3.0-or-later, see `LICENSE`. The
hand-authored glossary/definition/formula content in `data/` and
`locale/` is original writing for this project, not a derivative of
any external source, so no separate attribution is required for it.
