"""
Services layer: cross-cutting concerns used by more than one place in
the site, kept out of both content/ (pure data) and pages/ (per-route
view logic). Deliberately small -- only two modules -- because most of
what a smaller site like this needs is genuinely page-local, and
wrapping every three-line helper in its own "service" would be
boilerplate for its own sake, not real separation of concerns:

- compatibility.py -- the ARKlight alpha-branch version guard. Cross-
  cutting because it has to run before anything else in the composition
  root, and has nothing to do with any single page's content.
- theming.py -- turns content.theme.THEME (pure data) into the actual
  CSS-custom-property / repaint style dict every page needs. Cross-
  cutting because every page goes through components.layout.page_shell(),
  which needs this; it's "how do we apply the theme", not page content
  or reusable markup, so it doesn't belong in components/ either.
"""
