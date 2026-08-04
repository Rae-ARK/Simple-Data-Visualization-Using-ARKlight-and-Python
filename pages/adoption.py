from __future__ import annotations

from arklight import Heading, Image, TableCell, TableRow, Text

from components.layout import page_shell
from components.tables import data_table
from content.adoption import SO2025


def adoption(theme: dict[str, str]):
    rows = [
        TableRow(TableCell(name), TableCell(f"{pop}%"), TableCell(f"{des}%"), TableCell(f"{adm}%"))
        for name, pop, des, adm in SO2025
    ]
    return page_shell(
        Heading("Market Share & Developer Sentiment"),
        Text(
            "Stack Overflow Developer Survey 2025, roughly 49,000 "
            "respondents. Popularity is current use; Desired is 'want to "
            "use next'; Admired is 'used it and would use it again.'",
        ),
        data_table(["Framework", "Popularity", "Desired", "Admired"], rows),
        Text(
            "ARKlight has no row here on purpose -- it's pre-1.0 with no "
            "survey presence yet. A comparison chart that invented a "
            "number for it would misrepresent both datasets.",
            class_name="muted",
        ),
        Image(
            src="assets/adoption-pie.png",
            alt="Pie chart: relative share of current use among React, Vue, Svelte, and Angular, normalized to 100%",
            style={"max-width": "480px", "height": "auto"},
        ),
        title="Market Share & Developer Sentiment",
        description="Stack Overflow Developer Survey 2025: popularity, desire, and admiration for React, Vue, Svelte, and Angular.",
        theme=theme,
    )
