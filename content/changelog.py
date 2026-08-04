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
