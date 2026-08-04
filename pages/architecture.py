from __future__ import annotations

from arklight import Container, Heading, Image, Strong, TableCell, TableRow, Text

from components.cards import card_class, card_grid
from components.layout import page_shell
from components.tables import data_table
from content.features import FEATURES, OUTPUT_MODEL_CARDS


def _output_model_cards():
    # Bento grid: one card per tool's output model, ARKlight's own card
    # as the "hero" (it's the one genuinely different answer among
    # five, not just a smaller/larger number like the others).
    return card_grid(*[
        Container(
            Heading(name, level=3),
            Text(desc, class_name="muted"),
            class_name=card_class(is_hero=hero),
        )
        for name, _summary, desc, hero in OUTPUT_MODEL_CARDS
    ])


def _feature_table():
    rows = [
        TableRow(
            TableCell(Strong(axis)),
            TableCell(react),
            TableCell(vue),
            TableCell(svelte),
            TableCell(angular),
            TableCell(ark),
        )
        for axis, react, vue, svelte, angular, ark in FEATURES
    ]
    return data_table(["Axis", "React", "Vue", "Svelte", "Angular", "ARKlight"], rows)


def architecture(theme: dict[str, str]):
    return page_shell(
        Heading("How Each Tool Actually Works"),
        Text(
            "The frameworks on the left ship a runtime to the browser and "
            "keep the page alive with it. ARKlight compiles once, at "
            "build time, and the browser gets plain files.",
        ),
        Heading("Output model, at a glance", level=2),
        _output_model_cards(),
        Heading("Full comparison", level=2),
        _feature_table(),
        Heading("ARKlight's own pipeline", level=2),
        Text(
            "Python Source -> Python AST (static discovery) -> ARK AST "
            "(executed) -> Normalization -> Validation -> Website IR -> "
            "HTML/CSS/JS backends -> static files. No step in this chain "
            "runs in the browser.",
        ),
        Image(
            src="assets/pipeline-diagram.png",
            alt="Diagram of ARKlight's compiler pipeline from Python source to static files",
            style={"max-width": "100%", "height": "auto"},
        ),
        title="How Each Tool Actually Works",
        description="Architectural comparison: virtual DOM, compile-away, and static-compiler models.",
        theme=theme,
    )
