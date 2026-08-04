"""
Registers every custom Site.style(...) class this project defines.
Kept as its own service (not inline literal dicts in site.py) so the
class *definitions* are data-driven from content.theme, and site.py
itself only has to make one call, not carry ~30 lines of style dicts
inline. Has to be a function taking `site` as an argument (not a
module-level side effect) because Site.style() is an instance method
-- the Site() instance only exists once site.py constructs it, in the
composition root.
"""

from __future__ import annotations


def register_site_styles(site, theme: dict[str, str]) -> None:
    # The custom classes below read var(--ark-accent) instead of a
    # hardcoded hex, so they automatically follow whatever
    # --ark-accent is in scope -- including the theme override applied
    # in page_shell() -- rather than needing their own separate
    # re-theme. `theme` itself isn't read here (the CSS variable
    # reference is enough), but it's accepted as an argument rather
    # than imported directly so this function stays a pure function of
    # its inputs, consistent with the rest of the components/services
    # split.
    del theme  # not needed directly -- see comment above

    site.style("hero", {
        "padding": "2.5rem 0",
        "border-bottom": "2px solid var(--ark-accent)",
        "margin-bottom": "1.5rem",
    })
    site.style("kpi-value", {
        "font-size": "2rem",
        "font-weight": "700",
        "color": "var(--ark-accent)",
    })
    site.style("source-note", {
        "font-size": "0.85rem",
        "color": "#666",
    })
    site.style("nav-brand", {
        "font-weight": "700",
        "color": "var(--ark-accent)",
        "letter-spacing": "-0.02em",
    })

    # Bento-grid "hero" card -- a .grid child that spans two tracks
    # instead of one (PLAN.md Section 7/10). Shared by Home,
    # Architecture, and (Stage 8) /playground's card grid.
    site.style("bento-hero", {
        "grid-column": "span 2",
    })

    # /changelog status badges.
    site.style("status-done", {
        "color": "#3f6212",
        "font-weight": "600",
    })
    site.style("status-planned", {
        "color": "var(--ark-muted)",
    })
    site.style("status-in-progress", {
        "color": "var(--ark-accent)",
        "font-weight": "600",
    })

    # Phase 2, Stage 8: /playground's per-card detail panel. No
    # inline <style>/@media/CSS transition escape hatch needed --
    # transition is just another property style={} already passes
    # through untouched, same mechanism as every other inline style on
    # this site, applied here via Site.style() instead since both
    # states (collapsed/expanded) need to share one base rule.
    #
    # Naming note, confirmed by reading arklight/backend/css/render.py
    # (_render_custom_styles): Site.style() classes are emitted
    # `sorted(custom_styles)` by name, NOT registration order -- so
    # with equal selector specificity, whichever name sorts *later*
    # wins the cascade when both classes are applied to the same
    # element at once. "playground-panel" < "playground-panel-open"
    # alphabetically (shorter prefix sorts first), which is exactly
    # the order needed: the base (collapsed) rule first, the
    # bind_class-toggled override second, so the override actually
    # overrides instead of being silently shadowed. Verified directly
    # against the generated ARK/styles.css, not assumed.
    site.style("playground-panel", {
        "max-height": "0",
        "overflow": "hidden",
        "opacity": "0",
        "transition": "max-height 0.25s ease, opacity 0.2s ease",
    })
    site.style("playground-panel-open", {
        "max-height": "400px",
        "opacity": "1",
    })
