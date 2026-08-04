"""
Frozen dataset for the comparison site -- matches PLAN.md Section 2
exactly. Kept separate from site.py so later stages (charts, copy) don't
need to touch page logic to update a number.
"""

# 2a. Bundle size, gzipped JS, minimal app (KB)
BUNDLE_SIZE = [
    # (name, low_kb, high_kb, note)
    ("ARKlight (static page)", 0.5, 0.5, "Measured this session -- no State() declared"),
    ("ARKlight (with State/Bind/Action)", 5.98, 5.98, "Measured this session -- vendored vdom core included"),
    ("Svelte 5", 1.6, 5.0, "State of JS 2025 / 2026 benchmark roundups"),
    ("Vue 3/4", 16.0, 35.0, "Vue perf docs / 2026 comparisons"),
    ("React 19 + ReactDOM", 42.0, 48.0, "js-framework-benchmark / 2026 sources"),
    ("Angular (core)", 50.0, 80.0, "2026 Angular performance roundups"),
]

# 2b. Stack Overflow Developer Survey 2025 (~49,000 respondents), percent
SO2025 = [
    # (name, popularity, desired, admired)
    ("React", 44.7, 30.7, 52.1),
    ("Angular", 18.2, 12.6, 44.7),
    ("Vue.js", 17.6, 15.3, 50.9),
    ("Svelte", 7.2, 11.1, 62.4),
]

# 2c. Feature / architecture comparison
FEATURES = [
    # (axis, react, vue, svelte, angular, arklight)
    ("Output model", "Runtime + virtual DOM", "Runtime + reactive proxies", "Compiles away, vanilla JS", "Runtime + signals/zone.js", "Compiles to static HTML; JS optional & closed-vocabulary"),
    ("Authoring language", "JS/JSX", "JS/Vue SFC", "JS/Svelte SFC", "TypeScript", "Python"),
    ("Client-side state", "Full (hooks)", "Full (reactivity)", "Full (runes)", "Full (RxJS/signals)", "Closed State/Bind/Action registry"),
    ("Arbitrary custom JS", "Yes", "Yes", "Yes", "Yes", "No -- permanent non-goal"),
    ("Build toolchain", "Bundler required", "Bundler required", "Compiler required", "CLI/AOT required", "None -- pip install + one CLI"),
    ("SSR / meta-framework", "Next.js", "Nuxt", "SvelteKit", "Angular Universal", "N/A -- output already static"),
    ("Responsive styling", "@media, full CSS", "@media, full CSS", "@media, full CSS", "@media, full CSS", "Intrinsic layout only, no @media yet"),
    ("Ecosystem size", "Largest", "Large", "Small, growing", "Large (enterprise)", "New -- one package"),
    ("Single-file distribution", "No", "No", "No", "No", "Yes -- sealed .ark bundle"),
]

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

