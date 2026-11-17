"""Writes the Adapt vocabulary for "what is <term>" in every locale.

"what is {term}" as a Padatious template matched every "what is …"
question, so "hvad er fotosyntese" got "I don't know a term called
fotosyntese" instead of reaching Common Query (Wikipedia, wiki offline). As
an Adapt intent it needs a known geometry term:

    locale/<lang>/GeometryTerm.voc   every name in glossary_names.json
    locale/<lang>/WhatIs.voc         the phrases of what_is.intent

Run after changing glossary_names.json:

    python tools/make_vocab.py
"""
import json
from pathlib import Path

LOCALE = Path(__file__).resolve().parents[1] / "locale"

PHRASES = {
    "da-dk": ["hvad er"],
    "de-de": ["was ist"],
    "en-us": ["what is", "what's"],
    "es-es": ["qué es"],
    "fr-fr": ["qu'est-ce qu'", "qu'est-ce que", "c'est quoi"],
}

for lang, phrases in PHRASES.items():
    loc = LOCALE / lang
    names = json.loads((loc / "glossary_names.json").read_text(encoding="utf-8"))
    words = []
    for key, value in names.items():
        if key.startswith("_"):
            continue
        for name in (value if isinstance(value, list) else [value]):
            if name and name.lower() not in words:
                words.append(name.lower())
    (loc / "GeometryTerm.voc").write_text("\n".join(sorted(words)) + "\n", encoding="utf-8")
    (loc / "WhatIs.voc").write_text("\n".join(phrases) + "\n", encoding="utf-8")
    print(lang, len(words), "terms")
