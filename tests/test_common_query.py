"""Tests for the Common Query safety net (handle_common_query,
_strip_question_prefix) - see DEVELOPMENT.md for why this exists."""
from unittest.mock import MagicMock


def test_strip_question_prefix_recognizes_what_is_a(skill):
    from geometry_skill import _strip_question_prefix
    assert _strip_question_prefix("what is a rhombus", "en-us") == "rhombus"
    assert _strip_question_prefix("What is a Rhombus?", "en-us") == "Rhombus"


def test_strip_question_prefix_no_match_returns_none(skill):
    from geometry_skill import _strip_question_prefix
    assert _strip_question_prefix("tell me a joke", "en-us") is None


def test_strip_question_prefix_danish_and_german(skill):
    from geometry_skill import _strip_question_prefix
    assert _strip_question_prefix("hvad er en rombe", "da-dk") == "rombe"
    assert _strip_question_prefix("was ist eine Raute", "de-de") == "Raute"


def test_handle_common_query_resolves_known_term(skill):
    answer, confidence = skill.handle_common_query("what is a rhombus", "en-us")
    assert "four equal sides" in answer
    assert confidence == 0.8


def test_handle_common_query_resolves_pythagoras(skill):
    answer, confidence = skill.handle_common_query("what is pythagoras' theorem", "en-us")
    assert "hypotenuse" in answer
    assert confidence == 0.8


def test_handle_common_query_unknown_subject_returns_none(skill):
    result = skill.handle_common_query("what is a spaceship", "en-us")
    assert result is None


def test_handle_common_query_non_matching_phrase_returns_none(skill):
    result = skill.handle_common_query("play some music", "en-us")
    assert result is None
