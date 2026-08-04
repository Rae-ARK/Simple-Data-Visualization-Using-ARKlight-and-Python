from __future__ import annotations

from arklight import Container, Heading, Image, TableCell, TableRow, Text

from components.layout import page_shell
from components.meters import labeled_meter
from components.tables import data_table
from content.bundle_size import BUNDLE_SIZE


def bundle_size(theme: dict[str, str]):
    rows = [
        TableRow(
            TableCell(name),
            TableCell(f"{low} KB" if low == high else f"{low}-{high} KB"),
            TableCell(note, class_name="source-note"),
        )
        for name, low, high, note in BUNDLE_SIZE
    ]
    meters = [labeled_meter(name, (low + high) / 2, 0, 90) for name, low, high, _ in BUNDLE_SIZE]

    return page_shell(
        Heading("Bundle Size & Performance"),
        Text(
            "Every number below is gzipped JavaScript for a minimal app, "
            "before your own application code. Ranges reflect real "
            "disagreement across sources, not false precision.",
        ),
        Container(*meters, class_name="stack"),
        Heading("Full table", level=2),
        data_table(["Tool", "Gzipped JS", "Source"], rows),
        Image(
            src="assets/bundle-size-bar.png",
            alt="Bar chart: gzipped JavaScript for ARKlight, Svelte, Vue, React, and Angular",
            style={"max-width": "100%", "height": "auto"},
        ),
        title="Bundle Size & Performance",
        description="Gzipped JavaScript payload comparison: React, Vue, Svelte, Angular, and ARKlight.",
        theme=theme,
    )
