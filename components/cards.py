from __future__ import annotations

from arklight import Container


def card_class(is_hero: bool = False) -> str:
    """
    The "card" vs. "card bento-hero" class-name decision, centralized.
    Three call sites (Home's link grid, Architecture's output-model
    cards, /playground's framework cards) all made this same decision
    independently before this split -- worth naming once rather than
    re-deriving the string each time.
    """
    return "card bento-hero" if is_hero else "card"


def card_grid(*cards):
    """
    Wraps already-built card nodes in the `.grid` bento layout.
    Deliberately takes finished nodes rather than raw data + a
    template -- card *content* varies too much across call sites
    (a plain Link, a Heading+Text pair, a full State/Action/Bind.when
    interactive panel) to usefully generalize; only the grid wrapper
    itself is common enough to share.
    """
    return Container(*cards, class_name="grid")
