"""Tests for parse_number(), the one place the skill reads a number."""
import pytest


@pytest.mark.parametrize("raw, lang, expected", [
    ("5", "en-us", 5.0),
    ("five", "en-us", 5.0),
    ("3.5", "en-us", 3.5),
    ("two and a half", "en-us", 2.5),
    ("fem", "da-dk", 5.0),
    ("3,5", "da-dk", 3.5),
    ("halvanden", "da-dk", 1.5),
    ("fünf", "de-de", 5.0),
    ("3,5", "de-de", 3.5),
    ("deux et demi", "fr-fr", 2.5),
    ("cinco", "es-es", 5.0),
])
def test_reads_digits_and_words_per_language(raw, lang, expected):
    from geometry_skill import parse_number
    assert parse_number(raw, lang) == expected


def test_lone_article_is_one():
    from geometry_skill import parse_number
    assert parse_number("en", "da-dk") == 1.0


def test_article_before_a_number_is_skipped():
    from geometry_skill import parse_number
    assert parse_number("en 5", "da-dk") == 5.0


@pytest.mark.parametrize("raw", [None, "", "banana"])
def test_no_number(raw):
    from geometry_skill import parse_number
    assert parse_number(raw, "en-us") is None


def test_unsupported_language_reads_no_number():
    from geometry_skill import parse_number
    assert parse_number("5", "xx-xx") is None
