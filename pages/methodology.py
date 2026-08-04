from __future__ import annotations

from arklight import (
    Code,
    Container,
    DescriptionDetails,
    DescriptionList,
    DescriptionTerm,
    Heading,
    Item,
    OrderedList,
    Text,
)

from components.layout import page_shell
from content.sources import PYPI_FINDING, SOURCES


def methodology(theme: dict[str, str]):
    return page_shell(
        Heading("Methodology & Sources"),
        Text("Every figure on this site traces back to one of the following:"),
        OrderedList(*[Item(s) for s in SOURCES]),
        Heading("How ARKlight's own numbers were measured", level=2),
        Text(
            "Two ARKlight pages were built with the alpha-branch "
            "compiler: one static page declaring no State(...), and one "
            "page using State/Bind/Action.increment. Each build's "
            "arklight.js was measured directly with wc -c for raw bytes "
            "and gzip -c | wc -c for gzipped bytes. These are not quoted "
            "from any third-party article.",
        ),
        Heading("A note on the published package", level=2),
        Text(
            f"This site itself was built with the GitHub alpha branch "
            f"(v{PYPI_FINDING['version_alpha_branch']}), not the "
            f"released PyPI package (v{PYPI_FINDING['version_pypi']}) "
            f"-- the alpha branch has the head-metadata props "
            f"({'`Site.style()`, `og_image`, etc.'}) this page uses. "
            f"While cross-checking version compatibility, installing "
            f"the PyPI release into a clean venv surfaced something "
            f"worth recording here rather than leaving unmentioned:",
        ),
        Container(
            Text(PYPI_FINDING["terms_summary"]),
            Text(PYPI_FINDING["discrepancy"], class_name="muted"),
            class_name="card",
        ),
        DescriptionList(
            DescriptionTerm("Gate module"),
            DescriptionDetails(Code(PYPI_FINDING["gate_module"])),
            DescriptionTerm("Skip for CI/scripted use"),
            DescriptionDetails(Code(f"{PYPI_FINDING['env_var']}=1")),
            DescriptionTerm("Acceptance recorded at"),
            DescriptionDetails(Code(PYPI_FINDING["marker_path"])),
        ),
        title="Methodology & Sources",
        description="Where every number on this site comes from, including how ARKlight's own bundle sizes were measured.",
        theme=theme,
    )
