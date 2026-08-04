from __future__ import annotations

from arklight import Container, Heading, Link, Text

from components.cards import card_class, card_grid
from components.layout import page_shell
from components.meters import kpi_card


def home(theme: dict[str, str]):
    kpis = Container(
        kpi_card("0.5 KB", "ARKlight, static page, zero shipped JS beyond nav-highlighting", "ARKlight static", 0.5, 0, 50),
        kpi_card("5.98 KB", "ARKlight, a page using State/Bind/Action", "ARKlight stateful", 5.98, 0, 50),
        kpi_card("42-48 KB", "React + ReactDOM baseline, before app code", "React baseline", 45, 0, 50),
        class_name="switcher",
    )
    return page_shell(
        Container(
            Heading("ARKlight vs. Traditional Frontend Frameworks"),
            Text(
                "Python compiles to static HTML on one side. Runtime "
                "JavaScript frameworks -- React, Vue, Svelte, Angular -- "
                "on the other. This site compares them on real, sourced "
                "numbers, including bundle sizes ARKlight measured on "
                "itself, not just quoted from an article.",
            ),
            class_name="hero",
        ),
        Heading("At a glance", level=2),
        kpis,
        Heading("Where to go from here", level=2),
        # Bento grid: six cards in an auto-fit .grid, one "hero" card
        # (the verdict -- the actual answer most visitors want) spans
        # two tracks via card_class(is_hero=True). `.grid`'s own
        # auto-fit/minmax sizing means this degrades safely on a
        # narrow viewport (a 1-column grid just clamps the span to
        # what exists) with no @media query, consistent with
        # ARKlight's intrinsic-only responsive model.
        card_grid(
            Link("Bundle Size & Performance", href="/bundle-size", class_name=card_class()),
            Link("Market Share & Developer Sentiment", href="/adoption", class_name=card_class()),
            Link("How Each Tool Actually Works", href="/architecture", class_name=card_class()),
            Link("Try It -- Live State/Bind/Action Demo", href="/playground", class_name=card_class()),
            Link("Methodology & Sources", href="/methodology", class_name=card_class()),
            Link("The Honest Verdict -- who should (and shouldn't) use ARKlight", href="/verdict", class_name=card_class(is_hero=True)),
        ),
        title="ARKlight vs. Traditional Frontend Frameworks",
        description="A sourced comparison of ARKlight against React, Vue, Svelte, and Angular.",
        theme=theme,
    )
