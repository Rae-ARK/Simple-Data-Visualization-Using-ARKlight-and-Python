"""
Frozen dataset for the comparison site -- matches PLAN.md Section 2
exactly. Kept separate from site.py so later stages (charts, copy) don't
need to touch page logic to update a number.

Phase 2, Stage 7 additions (GETTING_STARTED / CHANGELOG_MILESTONES /
FAQ) follow the same discipline: every entry traces back to a real
source already read from ARKlight's own repo -- its README's CLI
section, docs/ARCHITECTURE.md's milestone table, and this project's own
README ("Notes from building this") plus existing per-page copy on this
site -- not new copy invented for the FAQ page.
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

# --------------------------------------------------------------------
# /getting-started -- the exact CLI section from ARKlight's own
# README.md, reproduced as real commands (not paraphrased or
# reformatted), since these are the literal commands a visitor would
# run -- inventing a different-but-equivalent command would be the
# actual inaccuracy here.
GETTING_STARTED_STEPS = [
    (
        "1. Install (alpha branch -- see the compatibility note below)",
        "git clone --branch alpha https://github.com/Rae-ARK/ARKlight.git\n"
        "cd ARKlight\n"
        "pip install -e .",
        "Installs the `arklight` package and the `arklight` CLI command.",
    ),
    (
        "2. Build a site",
        "arklight build site.py -o ARK --no-open --verbose",
        "`site.py` must define `site = Site()` and at least one "
        "`@site.page(\"/route\")`-decorated function. `--verbose` prints "
        "a line as each compiler stage starts.",
    ),
    (
        "3. Pack it into a single file",
        "arklight pack ARK -o mysite.ark",
        "Sealed by default -- opaque to generic archive tools, but "
        "still opens directly in a browser (see this site's own "
        "\"Download offline bundle\" link in the footer).",
    ),
    (
        "4. Unpack it back",
        "arklight unpack mysite.ark -o restored",
        "Auto-detects sealed vs. plain bundles.",
    ),
    (
        "5. Look up a component's schema",
        "arklight search Picture",
        "Prints required props, whether it allows children, and "
        "whether it's a Bind(...)-able target. Typo-tolerant -- "
        "`arklight search pictur` suggests `Picture, PictureSource`.",
    ),
]

# --------------------------------------------------------------------
# /changelog -- the milestone table from ARKlight's own
# docs/ARCHITECTURE.md, reproduced as structured data (a real Table on
# this page) instead of just linking off to GitHub. Status values match
# that table exactly, read directly rather than re-derived.
CHANGELOG_MILESTONES = [
    # (version, what, status)
    ("v0.001", "Python -> HTML", "DONE"),
    ("v0.002", "CSS (default stylesheet)", "DONE"),
    ("v0.003", "JavaScript helpers, incl. two vocabulary extension addenda", "DONE"),
    ("v0.0035", "Stateful JS -- registry-driven behaviors + actions; State/Bind/Action.*", "DONE"),
    ("v0.004a", "CLI scaffolding (arklight new <name> --template simple|production)", "DONE"),
    ("v0.036", "ARK Bundle spec v1 -- single-file .ark packaging (arklight pack)", "DONE"),
    ("v0.037", "Sealed ARK Bundles -- archive half encrypted by default, arklight unpack", "DONE"),
    ("v0.041", "CLI/pipeline/JS runtime hardening + stateful JS vocabulary addenda I & II", "DONE"),
    ("v0.042", "Extra CSS features -- Site.style(), arklight search, arklight --help", "DONE"),
    ("v0.043", "Optional <head> metadata props + Backend.postprocess(...) hook", "DONE"),
    ("v0.0438", "Android backend -- arklight android (androidx.webkit.WebViewAssetLoader)", "PLANNED"),
    ("v0.044", "JS backend capability expansion -- reactive core parity with Vue 3", "PLANNED"),
    ("vdom-staging", "Reactive-core vdom staging (Stage 1-2 of 8 done: snabbdom core, reactive class binding)", "IN PROGRESS"),
    ("v0.048", "CSS @media queries + structured <head>/<header> extension", "PLANNED"),
    ("v0.010", "User-defined, reusable components", "PLANNED"),
    ("v0.100", "Alternate backends (Vue, Svelte)", "PLANNED"),
    ("v1.0", "Stable compiler", "PLANNED"),
]

# --------------------------------------------------------------------
# /faq -- questions pulled from this project's own README ("Notes from
# building this") and existing per-page copy already on this site (the
# Architecture page's feature table, the Verdict page's constraints) --
# repackaged as Q&A, nothing new invented for this page specifically.
FAQ = [
    (
        "Why no live charting library -- Chart.js, D3, Plotly?",
        "Not a current gap -- a permanent design choice. Accepting "
        "arbitrary JS/HTML is a hard non-goal of ARKlight (confirmed "
        "directly against arklight.ir.schema.SCHEMA), so this site's "
        "own charts are pre-rendered matplotlib PNGs, generated by a "
        "step outside ARKlight and embedded like any other image.",
    ),
    (
        "Can Site.style() define hover or focus states?",
        "No. Custom class names are validated against "
        "^[a-zA-Z_]\\w*$ (letters, digits, underscore, hyphen only) -- "
        "a name like cta:hover is rejected before it reaches the "
        "generated stylesheet. Per-node style={...} has no such "
        "limit, but inline styles can't express pseudo-classes either; "
        "there's currently no ARKlight-native way to style :hover.",
    ),
    (
        "Does ARKlight support @media queries yet?",
        "Not yet -- v0.048 is designed but not implemented. Today's "
        "responsive layout is intrinsic-only: .stack/.switcher/.grid "
        "adapt from a container's own available width via flexbox/grid "
        "sizing keywords, with no breakpoint tied to a device or "
        "screen size at all.",
    ),
    (
        "Can one on_click fire more than one Action?",
        "No -- on_click takes a single ActionRef or a single behavior "
        "string, never a list, verified directly against "
        "arklight/ir/validate.py's _validate_action. This is why this "
        "site's own /playground stage (Section 9 of PLAN.md) builds "
        "independent per-card toggles instead of a mutually-exclusive "
        "tab switcher.",
    ),
    (
        "Is there a pip install arklight package?",
        "No -- there is no published arklight package on PyPI as of "
        "this writing. The only real install path is cloning "
        "ARKlight's own repository (alpha or main) and running "
        "pip install -e . inside it. See the Methodology page for what "
        "installing the alpha branch vs. the (nonexistent) PyPI "
        "release actually looks like, including a license-acceptance "
        "gate found in main that alpha doesn't have.",
    ),
    (
        "What broke while building this site?",
        "One non-obvious bug specific to ARKlight's two-phase "
        "execution model: `from data import X` inside a page function "
        "behaved differently than the same import at module level, "
        "because a site file's top-level code and its page functions "
        "run in different compiler stages. Nothing about knowing "
        "Python in general predicts that -- it came from reading the "
        "traceback and reasoning about ARKlight's loader specifically.",
    ),
]

