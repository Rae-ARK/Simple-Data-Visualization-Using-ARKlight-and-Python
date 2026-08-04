"""PLAN.md Section 2d -- Methodology page sources, and the PyPI license-gate finding."""

SOURCES = [
    "Stack Overflow Developer Survey 2025 (~49,000 respondents) -- popularity/desired/admired figures.",
    "State of JS 2025 (2025.stateofjs.com) -- satisfaction/retention framing.",
    "js-framework-benchmark (Stefan Krause) and multiple independent 2026 bundle-size roundups -- React/Vue/Svelte/Angular gzip figures, given as ranges since sources vary.",
    "ARKlight's own repository (README.md, CHANGELOG.md, PROGRESS.md, docs/DESIGN-NOTES.md, docs/ARCHITECTURE.md) -- all architecture/feature claims.",
    "ARKlight bundle-size figures -- measured directly by building real pages with the alpha-branch compiler and running gzip -c arklight.js | wc -c.",
]

# Discovered while cross-checking the published package against the
# alpha-branch source used to build this site. Verified directly by
# installing `arklight` from PyPI into a clean venv and reading the
# shipped source, not inferred or assumed.
PYPI_FINDING = {
    "version_pypi": "0.42.0",
    "version_alpha_branch": "0.043",
    "gate_module": "arklight/cli/license_gate.py",
    "env_var": "ARKLIGHT_ACCEPT_LICENSE",
    "marker_path": "~/.arklight/license-accepted",
    "terms_summary": (
        "The PyPI package (0.42.0) enforces a one-time interactive "
        "license-acceptance gate on first CLI use, tied to GPLv3 "
        "Section 7 additional terms bundled in its LICENSE file. Those "
        "terms require conveyed copies of ARKlight's own source (or a "
        "work based on it) to keep a visible 'Based on ARKlight' / "
        "'Powered by ARKlight' attribution, and require the "
        "attribution comment in ARKlight's own embedded runtime file "
        "(arklight.js) to stay intact. The terms are explicit that "
        "they do not apply to a site's own source or to the HTML/CSS "
        "output arklight build produces -- only to ARKlight's own code "
        "and runtime files."
    ),
    "discrepancy": (
        "This gate, and the additional-terms LICENSE text it enforces, "
        "is not mentioned anywhere in the alpha branch's README.md, "
        "CHANGELOG.md, PROGRESS.md, or docs/DESIGN-NOTES.md as of this "
        "build. It may be release-packaging-only, added after those "
        "docs were last written, or simply undocumented -- this site "
        "states what was directly observed, not which of those it is."
    ),
}
