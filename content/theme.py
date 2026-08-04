"""
Phase 2, Stage 6 re-theme values (PLAN.md Section 7).

ARKlight's default --ark-accent (#4f46e5) is an indigo -- squarely in
the "blue-dominant default tech palette" current landing-page trend
coverage flags as generic. Picked a warm rust/terracotta instead --
distinct from every framework's own brand color in the adoption pie
chart (React cyan, Vue green, Angular red, Svelte orange-red) so it
doesn't visually blend into "just another framework color", and
distinct from ARKlight's own default indigo so the re-theme is
actually visible.

Pure data -- how this gets turned into an actual style dict / CSS
custom properties lives in services/theming.py, not here.
"""

THEME = {
    "accent": "#b8480f",       # warm rust/terracotta, not blue/indigo
    "accent_hover": "#8f3709",
    "bg": "#faf6f0",           # warm off-white, not stark #ffffff
    "border": "#e8dccb",       # warm-neutral border to match
}
