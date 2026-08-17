"""Tests for the 11 intent handlers, en-us locale."""
from unittest.mock import MagicMock


def _msg(**data):
    m = MagicMock()
    m.data = data
    return m


def test_what_is_known_term(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_what_is(_msg(term="rhombus"))
    dialog_name, data = skill.speak_dialog.call_args[0]
    assert dialog_name == "definition"
    assert data["term"] == "rhombus"
    assert "four equal sides" in data["definition"]


def test_what_is_unknown_term(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_what_is(_msg(term="Narnia"))
    skill.speak_dialog.assert_called_once_with("term_not_understood", {"term": "Narnia"})


def test_formula_of_known_shape_and_property(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_formula_of(_msg(property="area", shape="circle"))
    dialog_name, data = skill.speak_dialog.call_args[0]
    assert dialog_name == "formula_of"
    assert "pi" in data["formula"]


def test_formula_of_unsupported_combination(skill):
    """triangle only supports 'area', not 'perimeter' - see
    FORMULA_PROPERTIES."""
    skill.speak_dialog = MagicMock()
    skill.handle_formula_of(_msg(property="perimeter", shape="triangle"))
    dialog_name, data = skill.speak_dialog.call_args[0]
    assert dialog_name == "formula_not_understood"


def test_pythagoras_theorem(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_pythagoras_theorem(_msg())
    dialog_name, data = skill.speak_dialog.call_args[0]
    assert dialog_name == "pythagoras_theorem"
    assert "hypotenuse" in data["formula"]


def test_area_of_rectangle(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_area_of_rectangle(_msg(length="5", width="3"))
    skill.speak_dialog.assert_called_once_with(
        "area_of_rectangle", {"length": 5, "width": 3, "area": 15})


def test_area_of_rectangle_unparseable_number(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_area_of_rectangle(_msg(length="banana", width="3"))
    skill.speak_dialog.assert_called_once_with("number_not_understood")


def test_perimeter_of_rectangle(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_perimeter_of_rectangle(_msg(length="5", width="3"))
    skill.speak_dialog.assert_called_once_with(
        "perimeter_of_rectangle", {"length": 5, "width": 3, "perimeter": 16})


def test_area_of_square(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_area_of_square(_msg(side="4"))
    skill.speak_dialog.assert_called_once_with(
        "area_of_square", {"side": 4, "area": 16})


def test_perimeter_of_square(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_perimeter_of_square(_msg(side="4"))
    skill.speak_dialog.assert_called_once_with(
        "perimeter_of_square", {"side": 4, "perimeter": 16})


def test_area_of_triangle(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_area_of_triangle(_msg(base="6", height="4"))
    skill.speak_dialog.assert_called_once_with(
        "area_of_triangle", {"base": 6, "height": 4, "area": 12})


def test_area_of_circle(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_area_of_circle(_msg(radius="4"))
    dialog_name, data = skill.speak_dialog.call_args[0]
    assert dialog_name == "area_of_circle"
    assert data["radius"] == 4
    assert 50.2 < data["area"] < 50.3  # pi * 16 ~= 50.27


def test_circumference_of_circle(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_circumference_of_circle(_msg(radius="4"))
    dialog_name, data = skill.speak_dialog.call_args[0]
    assert dialog_name == "circumference_of_circle"
    assert 25.1 < data["circumference"] < 25.2  # 2*pi*4 ~= 25.13


def test_hypotenuse_of_right_triangle_exact_triple(skill):
    skill.speak_dialog = MagicMock()
    skill.handle_hypotenuse_of_right_triangle(_msg(leg_a="3", leg_b="4"))
    skill.speak_dialog.assert_called_once_with(
        "hypotenuse_of_right_triangle", {"leg_a": 3, "leg_b": 4, "hypotenuse": 5})
