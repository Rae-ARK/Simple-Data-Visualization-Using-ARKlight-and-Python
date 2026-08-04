"""
Single source of truth for the site's route list, consumed by both
components/layout.py's nav() (labels + hrefs) and site.py (which
routes actually get a @site.page(...) decorator).

Note: this list alone does NOT register routes -- ARKlight's static
`arklight.parser.discover` only recognizes `@<site_var>.page("/...")`
decorators written directly in the entry file's own source (site.py),
so ROUTES driving nav() and the actual @site.page(...) calls in
site.py have to be kept consistent by hand. Adding an entry here
without a matching decorator in site.py gives a nav link to a page
that was never built; a decorator in site.py without an entry here
just means that route won't show up in the nav (both are mistakes
worth catching in review, not something ARKlight enforces for you).
"""

ROUTES = [
    ("/", "Home"),
    ("/bundle-size", "Bundle Size"),
    ("/adoption", "Adoption"),
    ("/architecture", "Architecture"),
    ("/methodology", "Methodology"),
    ("/verdict", "Verdict"),
    ("/getting-started", "Getting Started"),
    ("/changelog", "Changelog"),
    ("/faq", "FAQ"),
    ("/playground", "Playground"),
]
