"""
Compatibility guard: this site uses alpha-branch-only ARKlight
features (Site.style(), Page(...) head-metadata props like
description/favicon/og_*). There is no published PyPI package that
provides these -- if you ran `pip install arklight`, that installed
either nothing (no such name published as of this writing) or an
unrelated/older package, and this guard turns the resulting crash
into a clear instruction instead of a raw AttributeError deep inside
a page module. See README.md ("Built against ARKlight's alpha branch")
for the full explanation and the correct install command.

Kept as its own service module (not inline in site.py) because it's
infrastructure -- "can this even run" -- not site content or routing,
and the composition root should stay a thin list of route
registrations, not carry a multi-line diagnostic routine inline.
"""

from __future__ import annotations

import inspect

from arklight import Page, Site

_REQUIRED_FEATURES = ("style",)  # Site.style, alpha-only


def check_arklight_compatibility() -> None:
    """Raise SystemExit with a clear message if ARKlight isn't alpha-branch-compatible."""
    installed_version = getattr(__import__("arklight"), "__version__", "unknown")
    missing = [f for f in _REQUIRED_FEATURES if not hasattr(Site(), f)]

    head_meta_ok = True
    try:
        # Page(...) must accept the alpha-only head-metadata kwargs. A
        # cheap way to check without building a real page: inspect the
        # signature rather than calling Page() with throwaway args.
        sig = inspect.signature(Page)
        head_meta_ok = "description" in sig.parameters or any(
            p.kind == inspect.Parameter.VAR_KEYWORD
            for p in sig.parameters.values()
        )
    except (TypeError, ValueError):
        head_meta_ok = False

    if missing or not head_meta_ok:
        raise SystemExit(
            "\n"
            "This site requires ARKlight's 'alpha' branch --\n"
            "it uses Site.style(...) and Page(...) head-metadata props\n"
            "that don't exist in the ARKlight currently installed\n"
            f"(reported version: {installed_version!r}).\n\n"
            "There is no working 'pip install arklight' path for this\n"
            "project -- install the alpha branch from source instead:\n\n"
            "    git clone --branch alpha https://github.com/Rae-ARK/ARKlight.git\n"
            "    cd ARKlight && pip install -e .\n\n"
            "See this repo's README.md for the full compatibility table.\n"
        )
