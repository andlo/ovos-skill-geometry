"""Generates all intent/dialog files (+ skill.json) for
ovos-skill-geometry across 5 locales - hand-authored content,
centralized in one script for efficiency rather than 100+ individual
file writes. Run once by hand; not part of the shipped skill."""
from pathlib import Path

REPO = Path("/home/andlo/ovos-skill-geometry")

INTENTS = {
    "en-us": {
        "what_is": ["what is a {term}", "what is {term}"],
        "formula_of": ["what is the formula for the {property} of a {shape}"],
        "pythagoras_theorem": ["what is pythagoras' theorem", "what is the pythagorean theorem"],
        "area_of_rectangle": ["what is the area of a rectangle with length {length} and width {width}"],
        "perimeter_of_rectangle": ["what is the perimeter of a rectangle with length {length} and width {width}"],
        "area_of_square": ["what is the area of a square with side {side}"],
        "perimeter_of_square": ["what is the perimeter of a square with side {side}"],
        "area_of_triangle": ["what is the area of a triangle with base {base} and height {height}"],
        "area_of_circle": ["what is the area of a circle with radius {radius}"],
        "circumference_of_circle": ["what is the circumference of a circle with radius {radius}"],
        "hypotenuse_of_right_triangle": ["what is the hypotenuse of a right triangle with legs {leg_a} and {leg_b}"],
    },
}

INTENTS["da-dk"] = {
    "what_is": ["hvad er en {term}", "hvad er {term}"],
    "formula_of": ["hvad er formlen for {property} af en {shape}"],
    "pythagoras_theorem": ["hvad er pythagoras' sætning"],
    "area_of_rectangle": ["hvad er arealet af et rektangel med længden {length} og bredden {width}"],
    "perimeter_of_rectangle": ["hvad er omkredsen af et rektangel med længden {length} og bredden {width}"],
    "area_of_square": ["hvad er arealet af et kvadrat med siden {side}"],
    "perimeter_of_square": ["hvad er omkredsen af et kvadrat med siden {side}"],
    "area_of_triangle": ["hvad er arealet af en trekant med grundlinjen {base} og højden {height}"],
    "area_of_circle": ["hvad er arealet af en cirkel med radius {radius}"],
    "circumference_of_circle": ["hvad er omkredsen af en cirkel med radius {radius}"],
    "hypotenuse_of_right_triangle": ["hvad er hypotenusen i en retvinklet trekant med kateterne {leg_a} og {leg_b}"],
}

INTENTS["de-de"] = {
    "what_is": ["was ist ein {term}", "was ist {term}"],
    "formula_of": ["wie lautet die formel für {property} eines {shape}"],
    "pythagoras_theorem": ["was ist der satz des pythagoras"],
    "area_of_rectangle": ["was ist die fläche eines rechtecks mit der länge {length} und der breite {width}"],
    "perimeter_of_rectangle": ["was ist der umfang eines rechtecks mit der länge {length} und der breite {width}"],
    "area_of_square": ["was ist die fläche eines quadrats mit der seite {side}"],
    "perimeter_of_square": ["was ist der umfang eines quadrats mit der seite {side}"],
    "area_of_triangle": ["was ist die fläche eines dreiecks mit der grundseite {base} und der höhe {height}"],
    "area_of_circle": ["was ist die fläche eines kreises mit dem radius {radius}"],
    "circumference_of_circle": ["was ist der umfang eines kreises mit dem radius {radius}"],
    "hypotenuse_of_right_triangle": ["was ist die hypotenuse eines rechtwinkligen dreiecks mit den katheten {leg_a} und {leg_b}"],
}

INTENTS["fr-fr"] = {
    "what_is": ["qu'est-ce qu'un {term}", "qu'est-ce que {term}"],
    "formula_of": ["quelle est la formule pour {property} d'un {shape}"],
    "pythagoras_theorem": ["quel est le théorème de pythagore"],
    "area_of_rectangle": ["quelle est l'aire d'un rectangle de longueur {length} et de largeur {width}"],
    "perimeter_of_rectangle": ["quel est le périmètre d'un rectangle de longueur {length} et de largeur {width}"],
    "area_of_square": ["quelle est l'aire d'un carré de côté {side}"],
    "perimeter_of_square": ["quel est le périmètre d'un carré de côté {side}"],
    "area_of_triangle": ["quelle est l'aire d'un triangle de base {base} et de hauteur {height}"],
    "area_of_circle": ["quelle est l'aire d'un cercle de rayon {radius}"],
    "circumference_of_circle": ["quelle est la circonférence d'un cercle de rayon {radius}"],
    "hypotenuse_of_right_triangle": ["quelle est l'hypoténuse d'un triangle rectangle avec des côtés {leg_a} et {leg_b}"],
}

INTENTS["es-es"] = {
    "what_is": ["qué es un {term}", "qué es {term}"],
    "formula_of": ["cuál es la fórmula para {property} de un {shape}"],
    "pythagoras_theorem": ["cuál es el teorema de pitágoras"],
    "area_of_rectangle": ["cuál es el área de un rectángulo con largo {length} y ancho {width}"],
    "perimeter_of_rectangle": ["cuál es el perímetro de un rectángulo con largo {length} y ancho {width}"],
    "area_of_square": ["cuál es el área de un cuadrado con lado {side}"],
    "perimeter_of_square": ["cuál es el perímetro de un cuadrado con lado {side}"],
    "area_of_triangle": ["cuál es el área de un triángulo con base {base} y altura {height}"],
    "area_of_circle": ["cuál es el área de un círculo con radio {radius}"],
    "circumference_of_circle": ["cuál es la circunferencia de un círculo con radio {radius}"],
    "hypotenuse_of_right_triangle": ["cuál es la hipotenusa de un triángulo rectángulo con catetos {leg_a} y {leg_b}"],
}

DIALOGS = {
    "en-us": {
        "definition": "a {term} is {definition}",
        "term_not_understood": "I don't know a term called {term}",
        "formula_of": "the {property} of a {shape} is {formula}",
        "formula_not_understood": "I don't have a formula for the {property} of a {shape}",
        "pythagoras_theorem": "pythagoras' theorem says that {formula}",
        "number_not_understood": "I didn't catch that number",
        "area_of_rectangle": "the area of a rectangle with length {length} and width {width} is {area}",
        "perimeter_of_rectangle": "the perimeter of a rectangle with length {length} and width {width} is {perimeter}",
        "area_of_square": "the area of a square with side {side} is {area}",
        "perimeter_of_square": "the perimeter of a square with side {side} is {perimeter}",
        "area_of_triangle": "the area of a triangle with base {base} and height {height} is {area}",
        "area_of_circle": "the area of a circle with radius {radius} is {area}",
        "circumference_of_circle": "the circumference of a circle with radius {radius} is {circumference}",
        "hypotenuse_of_right_triangle": "the hypotenuse of a right triangle with legs {leg_a} and {leg_b} is {hypotenuse}",
    },
    "da-dk": {
        "definition": "en {term} er {definition}",
        "term_not_understood": "jeg kender ikke et begreb der hedder {term}",
        "formula_of": "{property} af en {shape} er {formula}",
        "formula_not_understood": "jeg har ikke en formel for {property} af en {shape}",
        "pythagoras_theorem": "pythagoras' sætning siger at {formula}",
        "number_not_understood": "jeg hørte ikke det tal",
        "area_of_rectangle": "arealet af et rektangel med længden {length} og bredden {width} er {area}",
        "perimeter_of_rectangle": "omkredsen af et rektangel med længden {length} og bredden {width} er {perimeter}",
        "area_of_square": "arealet af et kvadrat med siden {side} er {area}",
        "perimeter_of_square": "omkredsen af et kvadrat med siden {side} er {perimeter}",
        "area_of_triangle": "arealet af en trekant med grundlinjen {base} og højden {height} er {area}",
        "area_of_circle": "arealet af en cirkel med radius {radius} er {area}",
        "circumference_of_circle": "omkredsen af en cirkel med radius {radius} er {circumference}",
        "hypotenuse_of_right_triangle": "hypotenusen i en retvinklet trekant med kateterne {leg_a} og {leg_b} er {hypotenuse}",
    },
}

DIALOGS["de-de"] = {
    "definition": "ein {term} ist {definition}",
    "term_not_understood": "ich kenne keinen begriff namens {term}",
    "formula_of": "{property} eines {shape} ist {formula}",
    "formula_not_understood": "ich habe keine formel für {property} eines {shape}",
    "pythagoras_theorem": "der satz des pythagoras besagt dass {formula}",
    "number_not_understood": "ich habe die zahl nicht verstanden",
    "area_of_rectangle": "die fläche eines rechtecks mit der länge {length} und der breite {width} ist {area}",
    "perimeter_of_rectangle": "der umfang eines rechtecks mit der länge {length} und der breite {width} ist {perimeter}",
    "area_of_square": "die fläche eines quadrats mit der seite {side} ist {area}",
    "perimeter_of_square": "der umfang eines quadrats mit der seite {side} ist {perimeter}",
    "area_of_triangle": "die fläche eines dreiecks mit der grundseite {base} und der höhe {height} ist {area}",
    "area_of_circle": "die fläche eines kreises mit dem radius {radius} ist {area}",
    "circumference_of_circle": "der umfang eines kreises mit dem radius {radius} ist {circumference}",
    "hypotenuse_of_right_triangle": "die hypotenuse eines rechtwinkligen dreiecks mit den katheten {leg_a} und {leg_b} ist {hypotenuse}",
}

DIALOGS["fr-fr"] = {
    "definition": "un {term} est {definition}",
    "term_not_understood": "je ne connais pas de terme appelé {term}",
    "formula_of": "{property} d'un {shape} est {formula}",
    "formula_not_understood": "je n'ai pas de formule pour {property} d'un {shape}",
    "pythagoras_theorem": "le théorème de pythagore dit que {formula}",
    "number_not_understood": "je n'ai pas compris ce nombre",
    "area_of_rectangle": "l'aire d'un rectangle de longueur {length} et de largeur {width} est {area}",
    "perimeter_of_rectangle": "le périmètre d'un rectangle de longueur {length} et de largeur {width} est {perimeter}",
    "area_of_square": "l'aire d'un carré de côté {side} est {area}",
    "perimeter_of_square": "le périmètre d'un carré de côté {side} est {perimeter}",
    "area_of_triangle": "l'aire d'un triangle de base {base} et de hauteur {height} est {area}",
    "area_of_circle": "l'aire d'un cercle de rayon {radius} est {area}",
    "circumference_of_circle": "la circonférence d'un cercle de rayon {radius} est {circumference}",
    "hypotenuse_of_right_triangle": "l'hypoténuse d'un triangle rectangle avec des côtés {leg_a} et {leg_b} est {hypotenuse}",
}

DIALOGS["es-es"] = {
    "definition": "un {term} es {definition}",
    "term_not_understood": "no conozco ningún término llamado {term}",
    "formula_of": "{property} de un {shape} es {formula}",
    "formula_not_understood": "no tengo una fórmula para {property} de un {shape}",
    "pythagoras_theorem": "el teorema de pitágoras dice que {formula}",
    "number_not_understood": "no entendí ese número",
    "area_of_rectangle": "el área de un rectángulo con largo {length} y ancho {width} es {area}",
    "perimeter_of_rectangle": "el perímetro de un rectángulo con largo {length} y ancho {width} es {perimeter}",
    "area_of_square": "el área de un cuadrado con lado {side} es {area}",
    "perimeter_of_square": "el perímetro de un cuadrado con lado {side} es {perimeter}",
    "area_of_triangle": "el área de un triángulo con base {base} y altura {height} es {area}",
    "area_of_circle": "el área de un círculo con radio {radius} es {area}",
    "circumference_of_circle": "la circunferencia de un círculo con radio {radius} es {circumference}",
    "hypotenuse_of_right_triangle": "la hipotenusa de un triángulo rectángulo con catetos {leg_a} y {leg_b} es {hypotenuse}",
}

SKILL_JSON = {
    "en-us": {
        "name": "Geometry",
        "description": "Geometry knowledge - shape and term definitions, formulas, and applied calculations for rectangles, squares, triangles, circles, and the Pythagorean theorem. Fully offline.",
        "examples": [
            "what is a rhombus", "what is the formula for the area of a circle",
            "what is the area of a rectangle with length 5 and width 3",
            "what is the hypotenuse of a right triangle with legs 3 and 4",
            "what is pythagoras' theorem",
        ],
        "tags": ["geometry", "reference", "math", "shapes"],
    },
    "da-dk": {
        "name": "Geometri",
        "description": "Geometrisk viden - definitioner af former og begreber, formler, og udregninger for rektangler, kvadrater, trekanter, cirkler og pythagoras' sætning. Fuldstændig offline.",
        "examples": [
            "hvad er en rombe", "hvad er formlen for arealet af en cirkel",
            "hvad er arealet af et rektangel med længden 5 og bredden 3",
            "hvad er hypotenusen i en retvinklet trekant med kateterne 3 og 4",
            "hvad er pythagoras' sætning",
        ],
        "tags": ["geometri", "opslag", "matematik", "former"],
    },
    "de-de": {
        "name": "Geometrie",
        "description": "Geometrisches Wissen - Definitionen von Formen und Begriffen, Formeln und Berechnungen für Rechtecke, Quadrate, Dreiecke, Kreise und den Satz des Pythagoras. Vollständig offline.",
        "examples": [
            "was ist eine Raute", "wie lautet die formel für die fläche eines kreises",
            "was ist die fläche eines rechtecks mit der länge 5 und der breite 3",
            "was ist die hypotenuse eines rechtwinkligen dreiecks mit den katheten 3 und 4",
            "was ist der satz des pythagoras",
        ],
        "tags": ["geometrie", "nachschlagewerk", "mathematik", "formen"],
    },
    "fr-fr": {
        "name": "Géométrie",
        "description": "Connaissances en géométrie - définitions des formes et termes, formules et calculs pour rectangles, carrés, triangles, cercles et le théorème de Pythagore. Entièrement hors ligne.",
        "examples": [
            "qu'est-ce qu'un losange", "quelle est la formule pour l'aire d'un cercle",
            "quelle est l'aire d'un rectangle de longueur 5 et de largeur 3",
            "quelle est l'hypoténuse d'un triangle rectangle avec des côtés 3 et 4",
            "quel est le théorème de pythagore",
        ],
        "tags": ["géométrie", "référence", "mathématiques", "formes"],
    },
    "es-es": {
        "name": "Geometría",
        "description": "Conocimiento de geometría - definiciones de formas y términos, fórmulas y cálculos para rectángulos, cuadrados, triángulos, círculos y el teorema de Pitágoras. Totalmente sin conexión.",
        "examples": [
            "qué es un rombo", "cuál es la fórmula para el área de un círculo",
            "cuál es el área de un rectángulo con largo 5 y ancho 3",
            "cuál es la hipotenusa de un triángulo rectángulo con catetos 3 y 4",
            "cuál es el teorema de pitágoras",
        ],
        "tags": ["geometría", "referencia", "matemáticas", "formas"],
    },
}

# ---------------------------------------------------------------
# Write everything out
import json

LOCALES = ["en-us", "da-dk", "de-de", "fr-fr", "es-es"]

for lang in LOCALES:
    lang_dir = REPO / "locale" / lang
    lang_dir.mkdir(parents=True, exist_ok=True)

    for name, lines in INTENTS[lang].items():
        (lang_dir / f"{name}.intent").write_text("\n".join(lines) + "\n", encoding="utf-8")

    for name, text in DIALOGS[lang].items():
        (lang_dir / f"{name}.dialog").write_text(text + "\n", encoding="utf-8")

    sj = SKILL_JSON[lang]
    skill_json = {
        "skill_id": "ovos-skill-geometry.andlo",
        "source": "https://github.com/andlo/ovos-skill-geometry",
        "package_name": "ovos-skill-geometry",
        "pip_spec": "ovos-skill-geometry",
        "license": "GPL-3.0-or-later",
        "author": "andlo",
        "name": sj["name"],
        "description": sj["description"],
        "examples": sj["examples"],
        "tags": sj["tags"],
        "icon": "https://raw.githubusercontent.com/andlo/ovos-skill-geometry/main/icon.png",
    }
    with open(lang_dir / "skill.json", "w", encoding="utf-8") as f:
        json.dump(skill_json, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(INTENTS['en-us'])} intents x {len(LOCALES)} locales,",
      f"{len(DIALOGS['en-us'])} dialogs x {len(LOCALES)} locales, skill.json x {len(LOCALES)}")
