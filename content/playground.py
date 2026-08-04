"""
Phase 2, Stage 8 -- /playground content (PLAN.md Section 9).

Per-card expand/collapse data, one entry per framework, reusing
content.features.OUTPUT_MODEL_CARDS (the same copy already used on
/architecture) rather than inventing new text for the same claim --
(key, name, summary, detail, is_hero). `key` becomes the State name
suffix (`show_detail_<key>`), so it has to be a valid Python-identifier
-ish token; kept lowercase/no-punctuation for that reason.
"""

from content.features import OUTPUT_MODEL_CARDS

PLAYGROUND_CARDS = [
    (name.lower(), name, summary, detail, is_hero)
    for name, summary, detail, is_hero in OUTPUT_MODEL_CARDS
]

# Small second demo alongside the per-card toggles: a real
# State/Action.increment/decrement/reset counter with a live Bind(...)
# text readout, demonstrating text binding (not just class binding) on
# the same page -- this is the same *kind* of page the Methodology
# page's bundle-size measurement describes building ("a page using
# State/Bind/Action.increment"), now actually visitable rather than
# only described in prose.
COUNTER_INITIAL = 0
