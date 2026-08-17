"""Tests for the pure geometry computation functions."""
import math


def test_rectangle_area_and_perimeter():
    from geometry_skill import rectangle_area, rectangle_perimeter
    assert rectangle_area(5, 3) == 15
    assert rectangle_perimeter(5, 3) == 16


def test_square_area_and_perimeter():
    from geometry_skill import square_area, square_perimeter
    assert square_area(4) == 16
    assert square_perimeter(4) == 16


def test_triangle_area():
    from geometry_skill import triangle_area
    assert triangle_area(6, 4) == 12
    assert triangle_area(3, 5) == 7.5  # not integer-clean, still exact


def test_circle_area_and_circumference_use_real_pi():
    from geometry_skill import circle_area, circle_circumference
    assert math.isclose(circle_area(4), math.pi * 16)
    assert math.isclose(circle_circumference(4), 2 * math.pi * 4)


def test_pythagorean_hypotenuse_exact_for_known_triples():
    from geometry_skill import pythagorean_hypotenuse, PYTHAGOREAN_TRIPLES
    for a, b, c in PYTHAGOREAN_TRIPLES:
        assert pythagorean_hypotenuse(a, b) == c


def test_pythagorean_hypotenuse_irrational_for_non_triples():
    from geometry_skill import pythagorean_hypotenuse
    result = pythagorean_hypotenuse(5, 7)
    assert math.isclose(result, math.sqrt(74))
    assert result != int(result)  # genuinely not a whole number


def test_format_number_drops_trailing_zero():
    from geometry_skill import format_number
    assert format_number(15.0) == 15
    assert format_number(7.5) == 7.5
    assert format_number(math.pi * 16) == round(math.pi * 16, 2)
