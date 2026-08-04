"""
Pages layer: one module per route, each exposing a single function
that returns that page's content (a Page(...) node built via
components.layout.page_shell()). Deliberately NOT decorated with
@site.page(...) here -- ARKlight's static discovery
(arklight.parser.discover) only recognizes @<site_var>.page("/...")
decorators written directly in the entry file's own source, so the
actual route registration has to live in site.py, the composition
root. Every function here is a plain, undecorated function ARKlight's
discovery pass never sees -- site.py imports it and wires it to a
route itself.
"""
