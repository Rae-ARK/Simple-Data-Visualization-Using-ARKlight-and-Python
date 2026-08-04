from arklight import *
from data import BUNDLE_SIZE, SO2025, FEATURES, SOURCES, PYPI_FINDING

site = Site()

site.style("hero", {
    "padding": "2.5rem 0",
    "border-bottom": "2px solid #7c3aed",
    "margin-bottom": "1.5rem",
})
site.style("kpi-value", {
    "font-size": "2rem",
    "font-weight": "700",
    "color": "#7c3aed",
})
site.style("source-note", {
    "font-size": "0.85rem",
    "color": "#666",
})
site.style("nav-brand", {
    "font-weight": "700",
    "color": "#7c3aed",
    "letter-spacing": "-0.02em",
})

ROUTES = [
    ("/", "Home"),
    ("/bundle-size", "Bundle Size"),
    ("/adoption", "Adoption"),
    ("/architecture", "Architecture"),
    ("/methodology", "Methodology"),
    ("/verdict", "Verdict"),
]


def nav():
    return Nav(
        *[Link(label, href=route) for route, label in ROUTES],
        class_name="nav",
    )


def page_shell(*children, title, description, og_image=None):
    return Page(
        Header(nav(), class_name="cluster"),
        Main(*children, class_name="page"),
        Footer(
            Text("ARKlight vs. Traditional Frontend Frameworks -- a comparison site built in ARKlight, about ARKlight.", class_name="muted"),
        ),
        title=title,
        description=description,
        favicon="assets/favicon.png",
        og_title=title,
        og_description=description,
        og_image=og_image or "assets/bundle-size-bar.png",
    )


def feature_table():
    rows = [
        TableRow(
            TableCell(Strong(axis)),
            TableCell(react),
            TableCell(vue),
            TableCell(svelte),
            TableCell(angular),
            TableCell(ark),
        )
        for axis, react, vue, svelte, angular, ark in FEATURES
    ]
    return Table(
        TableHead(
            TableRow(
                TableHeaderCell("Axis"),
                TableHeaderCell("React"),
                TableHeaderCell("Vue"),
                TableHeaderCell("Svelte"),
                TableHeaderCell("Angular"),
                TableHeaderCell("ARKlight"),
            )
        ),
        TableBody(*rows),
    )


# ---------------------------------------------------------------- Home

@site.page("/")
def home():
    kpis = Container(
        Container(
            Heading("0.5 KB", level=3, class_name="kpi-value"),
            Text("ARKlight, static page, zero shipped JS beyond nav-highlighting", class_name="muted"),
            Meter("ARKlight static", value=0.5, min=0, max=50),
            class_name="card",
        ),
        Container(
            Heading("5.98 KB", level=3, class_name="kpi-value"),
            Text("ARKlight, a page using State/Bind/Action", class_name="muted"),
            Meter("ARKlight stateful", value=5.98, min=0, max=50),
            class_name="card",
        ),
        Container(
            Heading("42-48 KB", level=3, class_name="kpi-value"),
            Text("React + ReactDOM baseline, before app code", class_name="muted"),
            Meter("React baseline", value=45, min=0, max=50),
            class_name="card",
        ),
        class_name="switcher",
    )
    return page_shell(
        Container(
            Heading("ARKlight vs. Traditional Frontend Frameworks"),
            Text(
                "Python compiles to static HTML on one side. Runtime "
                "JavaScript frameworks -- React, Vue, Svelte, Angular -- "
                "on the other. This site compares them on real, sourced "
                "numbers, including bundle sizes ARKlight measured on "
                "itself, not just quoted from an article.",
            ),
            class_name="hero",
        ),
        Heading("At a glance", level=2),
        kpis,
        Heading("Where to go from here", level=2),
        Container(
            Link("Bundle Size & Performance", href="/bundle-size", class_name="card"),
            Link("Market Share & Developer Sentiment", href="/adoption", class_name="card"),
            Link("How Each Tool Actually Works", href="/architecture", class_name="card"),
            Link("Methodology & Sources", href="/methodology", class_name="card"),
            Link("The Honest Verdict", href="/verdict", class_name="card"),
            class_name="grid",
        ),
        title="ARKlight vs. Traditional Frontend Frameworks",
        description="A sourced comparison of ARKlight against React, Vue, Svelte, and Angular.",
    )


# --------------------------------------------------------- Bundle size

@site.page("/bundle-size")
def bundle_size():
    rows = [
        TableRow(
            TableCell(name),
            TableCell(f"{low} KB" if low == high else f"{low}-{high} KB"),
            TableCell(note, class_name="source-note"),
        )
        for name, low, high, note in BUNDLE_SIZE
    ]
    meters = [
        Container(
            Text(name),
            Meter(name, value=(low + high) / 2, min=0, max=90),
            class_name="stack",
        )
        for name, low, high, _ in BUNDLE_SIZE
    ]
    return page_shell(
        Heading("Bundle Size & Performance"),
        Text(
            "Every number below is gzipped JavaScript for a minimal app, "
            "before your own application code. Ranges reflect real "
            "disagreement across sources, not false precision.",
        ),
        Container(*meters, class_name="stack"),
        Heading("Full table", level=2),
        Table(
            TableHead(TableRow(TableHeaderCell("Tool"), TableHeaderCell("Gzipped JS"), TableHeaderCell("Source"))),
            TableBody(*rows),
        ),
        Image(
            src="assets/bundle-size-bar.png",
            alt="Bar chart: gzipped JavaScript for ARKlight, Svelte, Vue, React, and Angular",
            style={"max-width": "100%", "height": "auto"},
        ),
        title="Bundle Size & Performance",
        description="Gzipped JavaScript payload comparison: React, Vue, Svelte, Angular, and ARKlight.",
    )


# ------------------------------------------------------------ Adoption

@site.page("/adoption")
def adoption():
    rows = [
        TableRow(
            TableCell(name),
            TableCell(f"{pop}%"),
            TableCell(f"{des}%"),
            TableCell(f"{adm}%"),
        )
        for name, pop, des, adm in SO2025
    ]
    return page_shell(
        Heading("Market Share & Developer Sentiment"),
        Text(
            "Stack Overflow Developer Survey 2025, roughly 49,000 "
            "respondents. Popularity is current use; Desired is 'want to "
            "use next'; Admired is 'used it and would use it again.'",
        ),
        Table(
            TableHead(
                TableRow(
                    TableHeaderCell("Framework"),
                    TableHeaderCell("Popularity"),
                    TableHeaderCell("Desired"),
                    TableHeaderCell("Admired"),
                )
            ),
            TableBody(*rows),
        ),
        Text(
            "ARKlight has no row here on purpose -- it's pre-1.0 with no "
            "survey presence yet. A comparison chart that invented a "
            "number for it would misrepresent both datasets.",
            class_name="muted",
        ),
        Image(
            src="assets/adoption-pie.png",
            alt="Pie chart: relative share of current use among React, Vue, Svelte, and Angular, normalized to 100%",
            style={"max-width": "480px", "height": "auto"},
        ),
        title="Market Share & Developer Sentiment",
        description="Stack Overflow Developer Survey 2025: popularity, desire, and admiration for React, Vue, Svelte, and Angular.",
    )


# --------------------------------------------------------- Architecture

@site.page("/architecture")
def architecture():
    return page_shell(
        Heading("How Each Tool Actually Works"),
        Text(
            "The frameworks on the left ship a runtime to the browser and "
            "keep the page alive with it. ARKlight compiles once, at "
            "build time, and the browser gets plain files.",
        ),
        feature_table(),
        Heading("ARKlight's own pipeline", level=2),
        Text(
            "Python Source -> Python AST (static discovery) -> ARK AST "
            "(executed) -> Normalization -> Validation -> Website IR -> "
            "HTML/CSS/JS backends -> static files. No step in this chain "
            "runs in the browser.",
        ),
        Image(
            src="assets/pipeline-diagram.png",
            alt="Diagram of ARKlight's compiler pipeline from Python source to static files",
            style={"max-width": "100%", "height": "auto"},
        ),
        title="How Each Tool Actually Works",
        description="Architectural comparison: virtual DOM, compile-away, and static-compiler models.",
    )


# --------------------------------------------------------- Methodology

@site.page("/methodology")
def methodology():
    return page_shell(
        Heading("Methodology & Sources"),
        Text("Every figure on this site traces back to one of the following:"),
        OrderedList(*[Item(s) for s in SOURCES]),
        Heading("How ARKlight's own numbers were measured", level=2),
        Text(
            "Two ARKlight pages were built with the alpha-branch "
            "compiler: one static page declaring no State(...), and one "
            "page using State/Bind/Action.increment. Each build's "
            "arklight.js was measured directly with wc -c for raw bytes "
            "and gzip -c | wc -c for gzipped bytes. These are not quoted "
            "from any third-party article.",
        ),
        Heading("A note on the published package", level=2),
        Text(
            f"This site itself was built with the GitHub alpha branch "
            f"(v{PYPI_FINDING['version_alpha_branch']}), not the "
            f"released PyPI package (v{PYPI_FINDING['version_pypi']}) "
            f"-- the alpha branch has the head-metadata props "
            f"({'`Site.style()`, `og_image`, etc.'}) this page uses. "
            f"While cross-checking version compatibility, installing "
            f"the PyPI release into a clean venv surfaced something "
            f"worth recording here rather than leaving unmentioned:",
        ),
        Container(
            Text(PYPI_FINDING["terms_summary"]),
            Text(PYPI_FINDING["discrepancy"], class_name="muted"),
            class_name="card",
        ),
        DescriptionList(
            DescriptionTerm("Gate module"),
            DescriptionDetails(Code(PYPI_FINDING["gate_module"])),
            DescriptionTerm("Skip for CI/scripted use"),
            DescriptionDetails(Code(f"{PYPI_FINDING['env_var']}=1")),
            DescriptionTerm("Acceptance recorded at"),
            DescriptionDetails(Code(PYPI_FINDING["marker_path"])),
        ),
        title="Methodology & Sources",
        description="Where every number on this site comes from, including how ARKlight's own bundle sizes were measured.",
    )


# -------------------------------------------------------------- Verdict

@site.page("/verdict")
def verdict():
    return page_shell(
        Heading("The Honest Verdict"),
        Text(
            "ARKlight and React/Vue/Svelte/Angular are not really "
            "competing for the same job. One question below decides "
            "which category actually applies to you.",
        ),
        Details(
            Summary("Do you need client-side interactivity beyond clicks toggling things?"),
            Text(
                "If yes -- forms with live validation, drag-and-drop, "
                "real-time dashboards -- a traditional framework is the "
                "right tool. ARKlight's JS is a closed, named vocabulary "
                "by design, not a smaller version of a full runtime.",
            ),
        ),
        Details(
            Summary("Is your team already fluent in JS/TS and an existing framework?"),
            Text(
                "If yes, switching costs likely outweigh ARKlight's "
                "benefits today -- it's a young, single-maintainer "
                "project without React/Vue/Svelte's ecosystem.",
            ),
        ),
        Details(
            Summary("Do you write Python, need a handful of static pages, and want zero npm toolchain?"),
            Text(
                "This is ARKlight's actual sweet spot: docs stubs, "
                "internal tools, a landing page templated out of a "
                "script, teaching contexts. Genuinely pleasant there.",
            ),
        ),
        title="The Honest Verdict",
        description="Who should actually use ARKlight, and who shouldn't -- a direct recommendation.",
    )
