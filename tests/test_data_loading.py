"""Tests for data integrity - the glossary and formula_words cover
every key, every locale, consistently."""
import pytest

LOCALES = ["en-us", "da-dk", "de-de", "fr-fr", "es-es"]


def test_glossary_has_24_terms():
    from geometry_skill import GLOSSARY
    assert len(GLOSSARY) == 24


@pytest.mark.parametrize("lang", LOCALES)
def test_glossary_names_cover_every_term(lang):
    from geometry_skill import GLOSSARY, GLOSSARY_NAMES
    assert set(GLOSSARY_NAMES[lang].keys()) == set(GLOSSARY.keys())


@pytest.mark.parametrize("lang", LOCALES)
def test_glossary_definitions_cover_every_term(lang):
    from geometry_skill import GLOSSARY, GLOSSARY_DEFINITIONS
    assert set(GLOSSARY_DEFINITIONS[lang].keys()) == set(GLOSSARY.keys())
    for key, definition in GLOSSARY_DEFINITIONS[lang].items():
        assert definition, f"{lang}/{key} has an empty definition"


@pytest.mark.parametrize("lang", LOCALES)
def test_formula_words_cover_every_formula_property_combination(lang):
    from geometry_skill import FORMULA_PROPERTIES, FORMULA_WORDS
    for shape, properties in FORMULA_PROPERTIES.items():
        for prop in properties:
            key = f"{shape}_{prop}"
            assert key in FORMULA_WORDS[lang], f"{lang} missing formula_words for {key}"
    assert "pythagorean" in FORMULA_WORDS[lang]


def test_term_name_to_key_roundtrips():
    from geometry_skill import GLOSSARY_NAMES, TERM_NAME_TO_KEY
    for lang in LOCALES:
        for key, name in GLOSSARY_NAMES[lang].items():
            resolved = TERM_NAME_TO_KEY[lang][name.strip().lower()]
            # da-dk/de-de: 'perimeter' and 'circumference' share a
            # spoken word - resolving that shared word won't always
            # roundtrip to the SAME key it started from, only to A
            # valid key with that name. See DEVELOPMENT.md.
            assert GLOSSARY_NAMES[lang][resolved] == name
