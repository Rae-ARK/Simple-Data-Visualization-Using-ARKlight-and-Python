from __future__ import annotations

from arklight import Container, Footer, Header, Link, Main, Nav, Page, Text

from content.routes import ROUTES
from services.theming import theme_wrapper_style


def nav():
    return Nav(
        *[Link(label, href=route) for route, label in ROUTES],
        class_name="nav",
    )


def page_shell(*children, title, description, theme, og_image=None, state=None):
    """
    Shared site chrome every page routes through: nav + main + footer,
    wrapped in the theme override (see services.theming for why the
    wrapper -- not Page(...) itself -- carries the re-theme style).

    `theme` is passed explicitly rather than imported here, so this
    component stays a pure function of its arguments -- easier to
    reason about and, if this project ever needed a second theme
    (a dark-mode toggle, say), page_shell() wouldn't need to change at
    all, only what site.py passes in.

    `state`: an optional list of State(...) nodes for pages that use
    State/Bind/Action (Phase 2, Stage 8's /playground, so far -- most
    pages pass nothing). This has to be a *separate* parameter from
    `*children`, not just prepended to them, because ARKlight enforces
    State(...) may only be declared as a direct child of Page(...)
    itself (arklight/ir/validate.py::_validate_state_declaration) --
    confirmed directly, nesting one inside Main()/Container() the way
    every other child here is nested raises ValidationError. So `state`
    nodes get spliced in as literal siblings of the visual wrapper
    Container below, both direct children of Page(...), while the
    Button/Bind.when/etc. referencing that state can still live
    anywhere in the visual tree beneath Main() as normal.
    """
    return Page(
        *(state or []),
        Container(
            Header(nav(), class_name="cluster"),
            Main(*children, class_name="page"),
            Footer(
                Text(
                    "ARKlight vs. Traditional Frontend Frameworks -- a comparison site built in ARKlight, about ARKlight.",
                    class_name="muted",
                ),
                Link(
                    "Download offline bundle (.ark)",
                    href="arklight-vs-frontend.ark",
                    class_name="source-note",
                ),
            ),
            style=theme_wrapper_style(theme),
        ),
        title=title,
        description=description,
        favicon="assets/favicon.png",
        og_title=title,
        og_description=description,
        og_image=og_image or "assets/bundle-size-bar.png",
    )
