"""
Content layer: frozen, single-source-of-truth data, one module per
domain. No ARKlight imports here, no page logic -- just data, so a
later stage (chart generation, a page module, a test) can import the
one constant it needs without pulling in anything else.

Split from the original monolithic data.py (Phase 2, Stage 8) so each
domain's source-of-truth lives next to a comment explaining where it
came from, instead of one file growing indefinitely as more pages get
added.
"""
