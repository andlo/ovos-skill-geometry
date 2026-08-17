"""
skill OVOS Geometry
Copyright (C) 2026  Andreas Lorensen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

---

Geometry knowledge for OVOS - a glossary of 24 terms and shapes
(radius, area, triangle, cylinder, ...), formulas (both recited in
words and applied numerically) for rectangles, squares, triangles,
circles, and Pythagoras' theorem. Fully offline: the glossary is
hand-authored (standard, well-established mathematical vocabulary,
not sourced from an external dataset the way ovos-skill-geography's
country data is - see data/build_glossary.py and CREDITS.md).

This is a UTILITY skill, not an educational one -
ovos-skill-geometry-practice depends on this package directly for its
quiz data and functions, the same relationship
ovos-skill-geography-practice has with ovos-skill-geography. See
DEVELOPMENT.md for why some quiz questions built on this data need a
REAL tolerance-band (circle/non-triple-Pythagoras calculations
involve genuinely irrational numbers) rather than the "construct
exact" approach the rest of this project family uses by default -
that grading distinction lives in geometry-practice, not here, since
this package only computes and speaks facts, it never grades anything.
"""

import math
import json
from pathlib import Path

from ovos_number_parser import extract_number
from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler

SKILL_ROOT = Path(__file__).resolve().parent
DATA_DIR = SKILL_ROOT / "data"
LOCALE_DIR = SKILL_ROOT / "locale"


def _load_json(path):
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _load_locale_json(filename):
    """locale/<lang>/<filename> -> {lang: {...}}, "_notes" dropped -
    same convention the rest of this project family uses."""
    merged = {}
    if not LOCALE_DIR.is_dir():
        return merged
    for lang_dir in sorted(LOCALE_DIR.iterdir()):
        if not lang_dir.is_dir():
            continue
        path = lang_dir / filename
        if not path.exists():
            continue
        data = _load_json(path)
        lang = lang_dir.name.lower()
        merged[lang] = {k: v for k, v in data.items() if not k.startswith("_")}
    return merged


# key -> category ("term" | "shape2d" | "shape3d") - the category is
# used by ovos-skill-geometry-practice to pick PLAUSIBLE multiple-
# choice distractors (a shape's wrong-answer options are other real
# shapes, not random terms), not used by this package itself.
GLOSSARY = _load_json(DATA_DIR / "glossary.json")

GLOSSARY_NAMES = _load_locale_json("glossary_names.json")
GLOSSARY_DEFINITIONS = _load_locale_json("glossary_definitions.json")
FORMULA_WORDS = _load_locale_json("formula_words.json")

# shape key -> which numeric properties it supports a formula for.
# Deliberately NOT every shape in GLOSSARY - e.g. rhombus/pentagon/
# hexagon/every 3D shape don't have a formula intent in v1 (only a
# glossary definition) - see DEVELOPMENT.md "Scope: which shapes get
# formulas".
FORMULA_PROPERTIES = {
    "rectangle": ["area", "perimeter"],
    "square": ["area", "perimeter"],
    "triangle": ["area"],
    "circle": ["area", "circumference"],
}


def _reverse_lookup(name_dict):
    return {name.strip().lower(): key for key, name in name_dict.items()}


TERM_NAME_TO_KEY = {lang: _reverse_lookup(names) for lang, names in GLOSSARY_NAMES.items()}


# ---------------------------------------------------------------
# Public, reusable functions - plain functions (not skill methods)
# so ovos-skill-geometry-practice can import and call them directly,
# same relationship ovos-skill-geography-practice has with
# ovos-skill-geography.
# ---------------------------------------------------------------

def resolve_term(raw, lang):
    """Exact match only (case-insensitive) against a spoken glossary
    term OR shape name - covers all 24 GLOSSARY keys, since shapes
    (circle, rectangle, ...) and properties (area, perimeter, ...)
    used by formula_of.intent are themselves glossary terms. Returns
    a GLOSSARY key, or None.

    da-dk/de-de note: 'perimeter' and 'circumference' share the same
    spoken word ('omkreds'/'Umfang') - a real linguistic fact. Since
    this is a plain dict, that shared word resolves to whichever key
    was written last when TERM_NAME_TO_KEY was built - readers should
    not assume it always resolves to a SPECIFIC one of the two, only
    to A valid key with that spoken name. See DEVELOPMENT.md."""
    if not raw:
        return None
    lang = lang.lower()
    lookup = TERM_NAME_TO_KEY.get(lang) or TERM_NAME_TO_KEY.get("en-us", {})
    return lookup.get(raw.strip().lower())


def term_name(key, lang):
    lang = lang.lower()
    names = GLOSSARY_NAMES.get(lang) or GLOSSARY_NAMES.get("en-us", {})
    return names.get(key, key)


def term_definition(key, lang):
    lang = lang.lower()
    definitions = GLOSSARY_DEFINITIONS.get(lang) or GLOSSARY_DEFINITIONS.get("en-us", {})
    return definitions.get(key)


def formula_words(key, lang):
    """key is e.g. 'circle_area' or 'pythagorean'."""
    lang = lang.lower()
    words = FORMULA_WORDS.get(lang) or FORMULA_WORDS.get("en-us", {})
    return words.get(key)


def parse_number(raw, lang):
    """Wraps ovos_number_parser.extract_number(), which returns False
    (not None) on failure - normalized to None here so callers can
    use a plain truthy/None check. Handles both digit strings ('5')
    and spoken number words ('five', 'fem', 'cinco', ...)."""
    if raw is None:
        return None
    result = extract_number(str(raw), lang=lang)
    if result is False:
        return None
    return float(result)


# ---------------------------------------------------------------
# Formulas - pure math, language-agnostic, reusable by
# ovos-skill-geometry-practice's quiz-question generation as well as
# this package's own numeric fact intents below.
# ---------------------------------------------------------------

def rectangle_area(length, width):
    return length * width


def rectangle_perimeter(length, width):
    return 2 * (length + width)


def square_area(side):
    return side ** 2


def square_perimeter(side):
    return 4 * side


def triangle_area(base, height):
    return 0.5 * base * height


def circle_area(radius):
    return math.pi * radius ** 2


def circle_circumference(radius):
    return 2 * math.pi * radius


def pythagorean_hypotenuse(leg_a, leg_b):
    return math.sqrt(leg_a ** 2 + leg_b ** 2)


# A small set of well-known Pythagorean triples (a, b, c) where
# a^2 + b^2 = c^2 exactly - used by ovos-skill-geometry-practice's
# "easy" Pythagoras quiz tier so the hypotenuse comes out as a clean
# integer, no tolerance-band grading needed. Includes a few scaled
# multiples of 3-4-5 alongside other primitive triples for variety.
PYTHAGOREAN_TRIPLES = [
    (3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17),
    (7, 24, 25), (20, 21, 29), (12, 35, 37), (9, 40, 41), (28, 45, 53),
]


def format_number(value):
    """Rounds an irrational result (pi-based, or a non-perfect-square
    hypotenuse) to 2 decimals for natural speech output, and drops a
    trailing .0 for whole numbers - a rounding-for-DISPLAY choice,
    not a grading tolerance (this package never grades anything, see
    DEVELOPMENT.md)."""
    rounded = round(value, 2)
    if rounded == int(rounded):
        return int(rounded)
    return rounded


class Geometry(OVOSSkill):
    """Thin wrappers around the module-level glossary lookups and
    formula functions above - each handler resolves slots, computes
    or looks up the answer, and speaks a dialog."""

    def _parse_or_complain(self, raw):
        """Returns a float, or speaks 'number_not_understood' and
        returns None - callers check for None and return early."""
        value = parse_number(raw, self.lang)
        if value is None:
            self.speak_dialog("number_not_understood")
        return value

    @intent_handler("what_is.intent")
    def handle_what_is(self, message):
        term_raw = message.data.get("term")
        key = resolve_term(term_raw, self.lang)
        if key is None:
            self.speak_dialog("term_not_understood", {"term": term_raw or ""})
            return
        self.speak_dialog("definition", {"term": term_name(key, self.lang),
                                          "definition": term_definition(key, self.lang)})

    @intent_handler("formula_of.intent")
    def handle_formula_of(self, message):
        property_raw = message.data.get("property")
        shape_raw = message.data.get("shape")
        property_key = resolve_term(property_raw, self.lang)
        shape_key = resolve_term(shape_raw, self.lang)
        if property_key not in FORMULA_PROPERTIES.get(shape_key, []):
            self.speak_dialog("formula_not_understood", {
                "property": property_raw or "", "shape": shape_raw or ""})
            return
        formula = formula_words(f"{shape_key}_{property_key}", self.lang)
        self.speak_dialog("formula_of", {
            "property": term_name(property_key, self.lang),
            "shape": term_name(shape_key, self.lang),
            "formula": formula})

    @intent_handler("pythagoras_theorem.intent")
    def handle_pythagoras_theorem(self, message):
        self.speak_dialog("pythagoras_theorem", {"formula": formula_words("pythagorean", self.lang)})

    @intent_handler("area_of_rectangle.intent")
    def handle_area_of_rectangle(self, message):
        length = self._parse_or_complain(message.data.get("length"))
        width = self._parse_or_complain(message.data.get("width")) if length is not None else None
        if length is None or width is None:
            return
        area = format_number(rectangle_area(length, width))
        self.speak_dialog("area_of_rectangle", {
            "length": format_number(length), "width": format_number(width), "area": area})

    @intent_handler("perimeter_of_rectangle.intent")
    def handle_perimeter_of_rectangle(self, message):
        length = self._parse_or_complain(message.data.get("length"))
        width = self._parse_or_complain(message.data.get("width")) if length is not None else None
        if length is None or width is None:
            return
        perimeter = format_number(rectangle_perimeter(length, width))
        self.speak_dialog("perimeter_of_rectangle", {
            "length": format_number(length), "width": format_number(width), "perimeter": perimeter})

    @intent_handler("area_of_square.intent")
    def handle_area_of_square(self, message):
        side = self._parse_or_complain(message.data.get("side"))
        if side is None:
            return
        area = format_number(square_area(side))
        self.speak_dialog("area_of_square", {"side": format_number(side), "area": area})

    @intent_handler("perimeter_of_square.intent")
    def handle_perimeter_of_square(self, message):
        side = self._parse_or_complain(message.data.get("side"))
        if side is None:
            return
        perimeter = format_number(square_perimeter(side))
        self.speak_dialog("perimeter_of_square", {"side": format_number(side), "perimeter": perimeter})

    @intent_handler("area_of_triangle.intent")
    def handle_area_of_triangle(self, message):
        base = self._parse_or_complain(message.data.get("base"))
        height = self._parse_or_complain(message.data.get("height")) if base is not None else None
        if base is None or height is None:
            return
        area = format_number(triangle_area(base, height))
        self.speak_dialog("area_of_triangle", {
            "base": format_number(base), "height": format_number(height), "area": area})

    @intent_handler("area_of_circle.intent")
    def handle_area_of_circle(self, message):
        radius = self._parse_or_complain(message.data.get("radius"))
        if radius is None:
            return
        area = format_number(circle_area(radius))
        self.speak_dialog("area_of_circle", {"radius": format_number(radius), "area": area})

    @intent_handler("circumference_of_circle.intent")
    def handle_circumference_of_circle(self, message):
        radius = self._parse_or_complain(message.data.get("radius"))
        if radius is None:
            return
        circumference = format_number(circle_circumference(radius))
        self.speak_dialog("circumference_of_circle", {
            "radius": format_number(radius), "circumference": circumference})

    @intent_handler("hypotenuse_of_right_triangle.intent")
    def handle_hypotenuse_of_right_triangle(self, message):
        leg_a = self._parse_or_complain(message.data.get("leg_a"))
        leg_b = self._parse_or_complain(message.data.get("leg_b")) if leg_a is not None else None
        if leg_a is None or leg_b is None:
            return
        c = format_number(pythagorean_hypotenuse(leg_a, leg_b))
        self.speak_dialog("hypotenuse_of_right_triangle", {
            "leg_a": format_number(leg_a), "leg_b": format_number(leg_b), "hypotenuse": c})
