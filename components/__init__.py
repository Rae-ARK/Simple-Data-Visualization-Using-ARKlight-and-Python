"""
Components layer: reusable presentation building blocks shared across
more than one page. Each function returns an ARKNode tree (or a list
of them) built purely from arguments -- no imports from content/ or
services/ except where a component is genuinely tied to one concern
(layout.py needs services.theming + content.routes + content.theme,
since page_shell() IS the site chrome). Pages/ compose these with
their own content.* imports; components/ never reaches into content/
on its own for page-specific data.
"""
