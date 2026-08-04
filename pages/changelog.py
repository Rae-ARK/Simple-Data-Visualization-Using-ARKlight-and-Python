from __future__ import annotations

from arklight import Code, Heading, TableCell, TableRow, Text

from components.layout import page_shell
from components.tables import data_table
from content.changelog import CHANGELOG_MILESTONES

# Page-local presentation mapping (not a service -- used only here,
# nothing cross-cutting about it).
_STATUS_CLASS = {
    "DONE": "status-done",
    "PLANNED": "status-planned",
    "IN PROGRESS": "status-in-progress",
}


def changelog(theme: dict[str, str]):
    rows = [
        TableRow(
            TableCell(Code(version)),
            TableCell(what),
            TableCell(status, class_name=_STATUS_CLASS.get(status, "")),
        )
        for version, what, status in CHANGELOG_MILESTONES
    ]
    done_count = sum(1 for *_, status in CHANGELOG_MILESTONES if status == "DONE")

    return page_shell(
        Heading("Changelog"),
        Text(
            f"ARKlight's own milestone roadmap ({done_count} of "
            f"{len(CHANGELOG_MILESTONES)} shipped as of this build), "
            "surfaced here as a real Table instead of linking off to "
            "GitHub. Source: ARKlight's docs/ARCHITECTURE.md.",
        ),
        data_table(["Version", "What", "Status"], rows),
        Text(
            "This site itself targets v0.043 on the alpha branch -- see "
            "the \"Built against ARKlight's alpha branch\" note on this "
            "project's own README for what that gets you over main.",
            class_name="muted",
        ),
        title="Changelog",
        description="ARKlight's full milestone history, shipped and planned.",
        theme=theme,
    )
