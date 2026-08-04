"""PLAN.md Section 2c -- feature / architecture comparison table."""

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

# Reused by the Architecture page's bento-grid "output model" cards
# (components/cards.py) and by Stage 8's /playground per-card detail
# panel -- (name, summary, detail, is_hero). Kept next to FEATURES
# since the copy is a restatement of that table's "Output model" row,
# not new content.
OUTPUT_MODEL_CARDS = [
    ("React", "Runtime + virtual DOM diffing", "Runtime + virtual DOM diffing", False),
    ("Vue", "Runtime + reactive proxies", "Runtime + reactive proxies", False),
    ("Svelte", "Compiles away -- vanilla JS, no runtime", "Compiles away -- vanilla JS, no runtime", False),
    ("Angular", "Runtime + zone.js/signals", "Runtime + zone.js/signals", False),
    (
        "ARKlight",
        "Compiles to static HTML at build time",
        "Compiles to static HTML at build time. JS is optional, "
        "closed-vocabulary, and only shipped if a page actually "
        "declares State(...) -- nothing runs in the browser unless "
        "the page asked for it.",
        True,
    ),
]
