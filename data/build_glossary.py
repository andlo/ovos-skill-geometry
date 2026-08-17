"""Generates locale/*/glossary_*.json and formula_words.json for
ovos-skill-geometry - all hand-authored (no external dataset, unlike
ovos-skill-geography), but centralized in one script rather than 100+
individual file-write calls, same efficiency reasoning either way.
Run once by hand; not a build-time dependency of the shipped skill."""
import json
from pathlib import Path

REPO = Path("/home/andlo/ovos-skill-geometry")

# Bounded, well-defined glossary (24 entries) - same "veldefineret,
# stabil" philosophy as ovos-skill-geography's 194-country scope or
# ovos-skill-math-practice's operation set. category is used only for
# organizing distractor selection later (pick same-category
# distractors so multiple-choice options are at least plausible).
GLOSSARY = {
    "radius": "term", "diameter": "term", "circumference": "term",
    "area": "term", "perimeter": "term", "volume": "term",
    "hypotenuse": "term", "vertex": "term", "angle": "term", "diagonal": "term",
    "triangle": "shape2d", "right_triangle": "shape2d", "square": "shape2d",
    "rectangle": "shape2d", "rhombus": "shape2d", "pentagon": "shape2d",
    "hexagon": "shape2d", "circle": "shape2d",
    "cube": "shape3d", "sphere": "shape3d", "cylinder": "shape3d",
    "cone": "shape3d", "pyramid": "shape3d", "rectangular_prism": "shape3d",
}

NAMES = {"en-us": {
    "radius": "radius", "diameter": "diameter", "circumference": "circumference",
    "area": "area", "perimeter": "perimeter", "volume": "volume",
    "hypotenuse": "hypotenuse", "vertex": "vertex", "angle": "angle", "diagonal": "diagonal",
    "triangle": "triangle", "right_triangle": "right triangle", "square": "square",
    "rectangle": "rectangle", "rhombus": "rhombus", "pentagon": "pentagon",
    "hexagon": "hexagon", "circle": "circle",
    "cube": "cube", "sphere": "sphere", "cylinder": "cylinder",
    "cone": "cone", "pyramid": "pyramid", "rectangular_prism": "rectangular prism",
}}

DEFINITIONS = {"en-us": {
    "radius": "the distance from the center of a circle to its edge",
    "diameter": "the distance across a circle through its center, twice the radius",
    "circumference": "the distance around the outside of a circle",
    "area": "the amount of space inside a two dimensional shape",
    "perimeter": "the total distance around the outside of a shape",
    "volume": "the amount of space inside a three dimensional shape",
    "hypotenuse": "the longest side of a right triangle, opposite the right angle",
    "vertex": "the point where two or more edges of a shape meet",
    "angle": "the space between two lines that meet at a point, measured in degrees",
    "diagonal": "a straight line connecting two non-adjacent corners of a shape",
    "triangle": "a shape with three straight sides and three angles",
    "right_triangle": "a triangle with one ninety degree angle",
    "square": "a shape with four equal sides and four right angles",
    "rectangle": "a shape with four right angles and opposite sides of equal length",
    "rhombus": "a shape with four equal sides where opposite angles are equal, like a tilted square",
    "pentagon": "a shape with five straight sides",
    "hexagon": "a shape with six straight sides",
    "circle": "a round shape where every point on the edge is the same distance from the center",
    "cube": "a three dimensional shape with six equal square faces",
    "sphere": "a perfectly round three dimensional shape, like a ball",
    "cylinder": "a three dimensional shape with two parallel circular ends connected by a curved surface",
    "cone": "a three dimensional shape with a circular base that narrows to a single point",
    "pyramid": "a three dimensional shape with a polygon base and triangular sides that meet at a point",
    "rectangular_prism": "a three dimensional shape with six rectangular faces, like a box",
}}

NAMES["da-dk"] = {
    "radius": "radius", "diameter": "diameter", "circumference": "omkreds",
    "area": "areal", "perimeter": "omkreds", "volume": "rumfang",
    "hypotenuse": "hypotenuse", "vertex": "toppunkt", "angle": "vinkel", "diagonal": "diagonal",
    "triangle": "trekant", "right_triangle": "retvinklet trekant", "square": "kvadrat",
    "rectangle": "rektangel", "rhombus": "rombe", "pentagon": "femkant",
    "hexagon": "sekskant", "circle": "cirkel",
    "cube": "terning", "sphere": "kugle", "cylinder": "cylinder",
    "cone": "kegle", "pyramid": "pyramide", "rectangular_prism": "kasse",
}
DEFINITIONS["da-dk"] = {
    "radius": "afstanden fra midten af en cirkel til dens kant",
    "diameter": "afstanden tværs over en cirkel gennem dens centrum, det dobbelte af radius",
    "circumference": "afstanden rundt om en cirkel",
    "area": "hvor meget plads der er inde i en todimensionel figur",
    "perimeter": "den samlede afstand rundt om en figur",
    "volume": "hvor meget plads der er inde i en tredimensionel figur",
    "hypotenuse": "den længste side i en retvinklet trekant, modsat den rette vinkel",
    "vertex": "det punkt hvor to eller flere kanter af en figur mødes",
    "angle": "rummet mellem to linjer der mødes i et punkt, målt i grader",
    "diagonal": "en lige linje der forbinder to hjørner i en figur, som ikke ligger ved siden af hinanden",
    "triangle": "en figur med tre lige sider og tre vinkler",
    "right_triangle": "en trekant med en vinkel på halvfems grader",
    "square": "en figur med fire lige lange sider og fire rette vinkler",
    "rectangle": "en figur med fire rette vinkler og modstående sider af samme længde",
    "rhombus": "en figur med fire lige lange sider, hvor modstående vinkler er ens, som et skævt kvadrat",
    "pentagon": "en figur med fem lige sider",
    "hexagon": "en figur med seks lige sider",
    "circle": "en rund figur hvor hvert punkt på kanten har samme afstand til centrum",
    "cube": "en tredimensionel figur med seks lige store kvadratiske sider",
    "sphere": "en helt rund tredimensionel figur, som en bold",
    "cylinder": "en tredimensionel figur med to parallelle runde ender forbundet af en buet overflade",
    "cone": "en tredimensionel figur med en rund bund der smalner til et enkelt punkt",
    "pyramid": "en tredimensionel figur med en flersidet bund og trekantede sider der mødes i et punkt",
    "rectangular_prism": "en tredimensionel figur med seks rektangulære sider, som en kasse",
}

NAMES["de-de"] = {
    "radius": "Radius", "diameter": "Durchmesser", "circumference": "Umfang",
    "area": "Fläche", "perimeter": "Umfang", "volume": "Volumen",
    "hypotenuse": "Hypotenuse", "vertex": "Eckpunkt", "angle": "Winkel", "diagonal": "Diagonale",
    "triangle": "Dreieck", "right_triangle": "rechtwinkliges Dreieck", "square": "Quadrat",
    "rectangle": "Rechteck", "rhombus": "Raute", "pentagon": "Fünfeck",
    "hexagon": "Sechseck", "circle": "Kreis",
    "cube": "Würfel", "sphere": "Kugel", "cylinder": "Zylinder",
    "cone": "Kegel", "pyramid": "Pyramide", "rectangular_prism": "Quader",
}
DEFINITIONS["de-de"] = {
    "radius": "der Abstand vom Mittelpunkt eines Kreises bis zu seinem Rand",
    "diameter": "der Abstand quer durch einen Kreis durch seinen Mittelpunkt, doppelt so groß wie der Radius",
    "circumference": "der Abstand um einen Kreis herum",
    "area": "die Menge an Platz innerhalb einer zweidimensionalen Form",
    "perimeter": "die gesamte Strecke um eine Form herum",
    "volume": "die Menge an Platz innerhalb einer dreidimensionalen Form",
    "hypotenuse": "die längste Seite eines rechtwinkligen Dreiecks, gegenüber dem rechten Winkel",
    "vertex": "der Punkt, an dem zwei oder mehr Kanten einer Form zusammentreffen",
    "angle": "der Raum zwischen zwei Linien, die sich an einem Punkt treffen, gemessen in Grad",
    "diagonal": "eine gerade Linie, die zwei nicht benachbarte Ecken einer Form verbindet",
    "triangle": "eine Form mit drei geraden Seiten und drei Winkeln",
    "right_triangle": "ein Dreieck mit einem neunzig Grad Winkel",
    "square": "eine Form mit vier gleich langen Seiten und vier rechten Winkeln",
    "rectangle": "eine Form mit vier rechten Winkeln und gegenüberliegenden Seiten gleicher Länge",
    "rhombus": "eine Form mit vier gleich langen Seiten, bei der gegenüberliegende Winkel gleich sind, wie ein schiefes Quadrat",
    "pentagon": "eine Form mit fünf geraden Seiten",
    "hexagon": "eine Form mit sechs geraden Seiten",
    "circle": "eine runde Form, bei der jeder Punkt am Rand den gleichen Abstand zum Mittelpunkt hat",
    "cube": "eine dreidimensionale Form mit sechs gleich großen quadratischen Flächen",
    "sphere": "eine perfekt runde dreidimensionale Form, wie ein Ball",
    "cylinder": "eine dreidimensionale Form mit zwei parallelen runden Enden, verbunden durch eine gekrümmte Oberfläche",
    "cone": "eine dreidimensionale Form mit einer runden Grundfläche, die sich zu einem einzelnen Punkt verjüngt",
    "pyramid": "eine dreidimensionale Form mit einer vieleckigen Grundfläche und dreieckigen Seiten, die sich in einem Punkt treffen",
    "rectangular_prism": "eine dreidimensionale Form mit sechs rechteckigen Flächen, wie eine Kiste",
}

NAMES["fr-fr"] = {
    "radius": "rayon", "diameter": "diamètre", "circumference": "circonférence",
    "area": "aire", "perimeter": "périmètre", "volume": "volume",
    "hypotenuse": "hypoténuse", "vertex": "sommet", "angle": "angle", "diagonal": "diagonale",
    "triangle": "triangle", "right_triangle": "triangle rectangle", "square": "carré",
    "rectangle": "rectangle", "rhombus": "losange", "pentagon": "pentagone",
    "hexagon": "hexagone", "circle": "cercle",
    "cube": "cube", "sphere": "sphère", "cylinder": "cylindre",
    "cone": "cône", "pyramid": "pyramide", "rectangular_prism": "pavé droit",
}
DEFINITIONS["fr-fr"] = {
    "radius": "la distance entre le centre d'un cercle et son bord",
    "diameter": "la distance à travers un cercle en passant par son centre, le double du rayon",
    "circumference": "la distance autour d'un cercle",
    "area": "la quantité d'espace à l'intérieur d'une forme à deux dimensions",
    "perimeter": "la distance totale autour d'une forme",
    "volume": "la quantité d'espace à l'intérieur d'une forme à trois dimensions",
    "hypotenuse": "le côté le plus long d'un triangle rectangle, opposé à l'angle droit",
    "vertex": "le point où deux arêtes ou plus d'une forme se rencontrent",
    "angle": "l'espace entre deux lignes qui se rencontrent en un point, mesuré en degrés",
    "diagonal": "une ligne droite reliant deux coins non adjacents d'une forme",
    "triangle": "une forme à trois côtés droits et trois angles",
    "right_triangle": "un triangle avec un angle de quatre-vingt-dix degrés",
    "square": "une forme à quatre côtés égaux et quatre angles droits",
    "rectangle": "une forme à quatre angles droits et des côtés opposés de même longueur",
    "rhombus": "une forme à quatre côtés égaux où les angles opposés sont égaux, comme un carré incliné",
    "pentagon": "une forme à cinq côtés droits",
    "hexagon": "une forme à six côtés droits",
    "circle": "une forme ronde où chaque point du bord est à la même distance du centre",
    "cube": "une forme à trois dimensions avec six faces carrées égales",
    "sphere": "une forme à trois dimensions parfaitement ronde, comme une balle",
    "cylinder": "une forme à trois dimensions avec deux extrémités circulaires parallèles reliées par une surface courbe",
    "cone": "une forme à trois dimensions avec une base circulaire qui se rétrécit jusqu'à un seul point",
    "pyramid": "une forme à trois dimensions avec une base polygonale et des côtés triangulaires qui se rencontrent en un point",
    "rectangular_prism": "une forme à trois dimensions avec six faces rectangulaires, comme une boîte",
}

NAMES["es-es"] = {
    "radius": "radio", "diameter": "diámetro", "circumference": "circunferencia",
    "area": "área", "perimeter": "perímetro", "volume": "volumen",
    "hypotenuse": "hipotenusa", "vertex": "vértice", "angle": "ángulo", "diagonal": "diagonal",
    "triangle": "triángulo", "right_triangle": "triángulo rectángulo", "square": "cuadrado",
    "rectangle": "rectángulo", "rhombus": "rombo", "pentagon": "pentágono",
    "hexagon": "hexágono", "circle": "círculo",
    "cube": "cubo", "sphere": "esfera", "cylinder": "cilindro",
    "cone": "cono", "pyramid": "pirámide", "rectangular_prism": "prisma rectangular",
}
DEFINITIONS["es-es"] = {
    "radius": "la distancia desde el centro de un círculo hasta su borde",
    "diameter": "la distancia a través de un círculo pasando por su centro, el doble del radio",
    "circumference": "la distancia alrededor de un círculo",
    "area": "la cantidad de espacio dentro de una figura bidimensional",
    "perimeter": "la distancia total alrededor de una figura",
    "volume": "la cantidad de espacio dentro de una figura tridimensional",
    "hypotenuse": "el lado más largo de un triángulo rectángulo, opuesto al ángulo recto",
    "vertex": "el punto donde se encuentran dos o más aristas de una figura",
    "angle": "el espacio entre dos líneas que se encuentran en un punto, medido en grados",
    "diagonal": "una línea recta que conecta dos esquinas no adyacentes de una figura",
    "triangle": "una figura con tres lados rectos y tres ángulos",
    "right_triangle": "un triángulo con un ángulo de noventa grados",
    "square": "una figura con cuatro lados iguales y cuatro ángulos rectos",
    "rectangle": "una figura con cuatro ángulos rectos y lados opuestos de igual longitud",
    "rhombus": "una figura con cuatro lados iguales donde los ángulos opuestos son iguales, como un cuadrado inclinado",
    "pentagon": "una figura con cinco lados rectos",
    "hexagon": "una figura con seis lados rectos",
    "circle": "una figura redonda donde cada punto del borde está a la misma distancia del centro",
    "cube": "una figura tridimensional con seis caras cuadradas iguales",
    "sphere": "una figura tridimensional perfectamente redonda, como una pelota",
    "cylinder": "una figura tridimensional con dos extremos circulares paralelos conectados por una superficie curva",
    "cone": "una figura tridimensional con una base circular que se estrecha hasta un solo punto",
    "pyramid": "una figura tridimensional con una base poligonal y lados triangulares que se encuentran en un punto",
    "rectangular_prism": "una figura tridimensional con seis caras rectangulares, como una caja",
}

# ---------------------------------------------------------------
# Formula-in-words sentences, per locale - used by formula_of.intent
# ("what is the formula for the area of a rectangle") and by teach
# mode in ovos-skill-geometry-practice. IMPORTANT: these are the
# RIGHT-HAND SIDE only ("length times width"), NOT a full sentence -
# the dialog templates that use these ("the {property} of a {shape}
# is {formula}") already supply the "the X of a Y is" prefix. Storing
# a full sentence here caused a real, published (v0.0.1) bug: "the
# area of a circle is the area of a circle is pi times the radius
# squared" - fixed here, not caught by the original tests since they
# only checked `"pi" in data["formula"]`, not the full rendered text.
FORMULA_WORDS = {
    "en-us": {
        "rectangle_area": "length times width",
        "rectangle_perimeter": "two times the sum of the length and the width",
        "square_area": "the side times itself",
        "square_perimeter": "four times the side",
        "triangle_area": "half of the base times the height",
        "circle_area": "pi times the radius squared",
        "circle_circumference": "two times pi times the radius",
        "pythagorean": "in a right triangle, the square of the hypotenuse equals the sum of the squares of the other two sides",
    },
    "da-dk": {
        "rectangle_area": "længden gange bredden",
        "rectangle_perimeter": "to gange summen af længden og bredden",
        "square_area": "siden gange sig selv",
        "square_perimeter": "fire gange siden",
        "triangle_area": "det halve af grundlinjen gange højden",
        "circle_area": "pi gange radius i anden",
        "circle_circumference": "to gange pi gange radius",
        "pythagorean": "i en retvinklet trekant er hypotenusen i anden lig med summen af de to andre siders anden",
    },
    "de-de": {
        "rectangle_area": "die Länge mal die Breite",
        "rectangle_perimeter": "zwei mal die Summe aus Länge und Breite",
        "square_area": "die Seite mal sich selbst",
        "square_perimeter": "vier mal die Seite",
        "triangle_area": "die Hälfte der Grundseite mal der Höhe",
        "circle_area": "Pi mal dem Radius zum Quadrat",
        "circle_circumference": "zwei mal Pi mal dem Radius",
        "pythagorean": "in einem rechtwinkligen Dreieck ist das Quadrat der Hypotenuse gleich der Summe der Quadrate der beiden anderen Seiten",
    },
    "fr-fr": {
        "rectangle_area": "la longueur multipliée par la largeur",
        "rectangle_perimeter": "deux fois la somme de la longueur et de la largeur",
        "square_area": "le côté multiplié par lui-même",
        "square_perimeter": "quatre fois le côté",
        "triangle_area": "la moitié de la base multipliée par la hauteur",
        "circle_area": "pi multiplié par le rayon au carré",
        "circle_circumference": "deux fois pi multiplié par le rayon",
        "pythagorean": "dans un triangle rectangle, le carré de l'hypoténuse est égal à la somme des carrés des deux autres côtés",
    },
    "es-es": {
        "rectangle_area": "el largo por el ancho",
        "rectangle_perimeter": "dos veces la suma del largo y el ancho",
        "square_area": "el lado por sí mismo",
        "square_perimeter": "cuatro veces el lado",
        "triangle_area": "la mitad de la base por la altura",
        "circle_area": "pi por el radio al cuadrado",
        "circle_circumference": "dos veces pi por el radio",
        "pythagorean": "en un triángulo rectángulo, el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los otros dos lados",
    },
}

# ---------------------------------------------------------------
# Write everything out
LOCALES = ["en-us", "da-dk", "de-de", "fr-fr", "es-es"]

with open(REPO / "data" / "glossary.json", "w", encoding="utf-8") as f:
    json.dump(GLOSSARY, f, ensure_ascii=False, indent=2, sort_keys=True)
print("data/glossary.json written -", len(GLOSSARY), "terms")

for lang in LOCALES:
    with open(REPO / "locale" / lang / "glossary_names.json", "w", encoding="utf-8") as f:
        json.dump({
            "_notes": ["term key -> the term's spoken name in this language."],
            **NAMES[lang]
        }, f, ensure_ascii=False, indent=2, sort_keys=True)
    with open(REPO / "locale" / lang / "glossary_definitions.json", "w", encoding="utf-8") as f:
        json.dump({
            "_notes": ["term key -> one-sentence definition, hand-authored (no external "
                       "dataset for this skill, unlike ovos-skill-geography's country data). "
                       "da-dk/de-de use the SAME word for 'perimeter' and 'circumference' "
                       "('omkreds'/'Umfang') - a real, documented linguistic fact, not a bug; "
                       "see DEVELOPMENT.md."],
            **DEFINITIONS[lang]
        }, f, ensure_ascii=False, indent=2, sort_keys=True)
    with open(REPO / "locale" / lang / "formula_words.json", "w", encoding="utf-8") as f:
        json.dump({
            "_notes": ["formula key -> the formula spoken in words."],
            **FORMULA_WORDS[lang]
        }, f, ensure_ascii=False, indent=2, sort_keys=True)
print("locale/*/glossary_names.json, glossary_definitions.json, formula_words.json written")
