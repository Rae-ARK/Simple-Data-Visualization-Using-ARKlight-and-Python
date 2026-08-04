"""PLAN.md Section 2a -- gzipped JS, minimal app (KB)."""

BUNDLE_SIZE = [
    # (name, low_kb, high_kb, note)
    ("ARKlight (static page)", 0.5, 0.5, "Measured this session -- no State() declared"),
    ("ARKlight (with State/Bind/Action)", 5.98, 5.98, "Measured this session -- vendored vdom core included"),
    ("Svelte 5", 1.6, 5.0, "State of JS 2025 / 2026 benchmark roundups"),
    ("Vue 3/4", 16.0, 35.0, "Vue perf docs / 2026 comparisons"),
    ("React 19 + ReactDOM", 42.0, 48.0, "js-framework-benchmark / 2026 sources"),
    ("Angular (core)", 50.0, 80.0, "2026 Angular performance roundups"),
]
