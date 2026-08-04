# Simple Data Visualization Using ARKlight and Python

A small comparison site -- **"ARKlight vs. Traditional Frontend
Frameworks"** -- built *in* ARKlight, *about* ARKlight, shipped as a
single sealed `.ark` bundle. Six static pages (bundle-size chart,
adoption/sentiment chart, feature-by-feature table, methodology, and
an honest verdict page) built entirely from Python, with no
hand-written HTML/CSS/JS.

It exists as a working example of what ARKlight can and can't do,
not just a write-up describing it -- see [`PLAN.md`](./PLAN.md) for the
full design brief, the frozen dataset, and the source list.

## ⚠️ Built against ARKlight's `alpha` branch, not `main`

This project targets ARKlight's **`alpha` branch**, which is ahead of
`main` and is **not** what you get from a default clone or a
released package. Concretely, at the time this was built:

| | `main` | `alpha` (used here) |
|---|---|---|
| Version | v0.041 | v0.043 |
| `Site.style(name, rules)` (custom CSS classes) | No | Yes |
| `arklight search <name>` / `arklight --help` | No | Yes |
| `Page(...)` head metadata (`description`, `favicon`, `og_*`) | No | Yes |
| `Backend.postprocess(...)` hook | No | Yes |
| Reactive-core vdom staging (Stage 1-2 of 8) | No | Yes |

None of this is a criticism of `main` -- `alpha` is simply where active
development lands first. But it means **this site will not build
against a `main`-branch checkout or an `arklight` install from PyPI**
if one predates these features. If you're cloning ARKlight yourself to
run this project, clone the `alpha` branch specifically:

```bash
git clone --branch alpha https://github.com/Rae-ARK/ARKlight.git
cd ARKlight
pip install -e .
```

Then check `arklight/__init__.py`'s `__version__` (or `pyproject.toml`)
reads `0.043` or later before building this project. If ARKlight has
since merged `alpha` into `main`, or moved further ahead, treat the
table above as a snapshot of what was true when this project was
built, not a live diff.

## What's in this repo

```
data.py               Frozen dataset -- bundle sizes, SO2025 survey
                       numbers, feature comparison table. Single
                       source of truth; site.py and
                       generate_assets.py both import from here.
generate_assets.py    One-off matplotlib script. Not part of
                       ARKlight -- ARKlight never touches matplotlib
                       directly, it only ever sees the finished PNGs
                       this script drops into assets/.
site.py               The actual ARKlight site: six pages, all
                       Python, using Table/Meter/Picture/Details and
                       friends from the ARKlight component vocabulary.
PLAN.md                Design brief written before the build: the
                       constraint that shapes everything (no live
                       charting libraries -- see below), the dataset,
                       page-by-page component mapping, and sources.
arklight-vs-frontend.ark   Final build output -- a sealed ARK Bundle.
                       Double-click/open it directly in a browser; it
                       renders like a normal page even though the
                       rest of the site's files are archived
                       (encrypted) alongside it.
```

## Building it yourself

```bash
# 1. Generate the chart PNGs (matplotlib, outside ARKlight)
python generate_assets.py

# 2. Compile the site
arklight build site.py -o ARK --verbose

# 3. (Optional) pack it back into a single sealed .ark file
arklight pack ARK -o arklight-vs-frontend.ark
```

Step 1 needs `matplotlib` (`pip install matplotlib`); steps 2-3 need
`alpha`-branch ARKlight installed, per the warning above.

## The constraint that shapes the whole site

ARKlight has no live charting library and never will -- accepting
arbitrary JS/HTML is a permanent non-goal, not a current gap. So "data
visualization" here comes from exactly two places ARKlight actually
supports: pre-rendered matplotlib PNGs (the bar and pie charts, dropped
into `assets/` and embedded with `Picture`/`Image`), and native
zero-JS widgets ARKlight already has schema support for (`Meter`/
`Progress`, used for the KPI strip). Both are deliberate -- the site
itself demonstrates ARKlight's real ceiling rather than just
describing it. Full reasoning in `PLAN.md` Section 1.

## Notes from building this

Some honest, specific observations from actually building a multi-page
site in ARKlight's `alpha` branch, worth keeping alongside the code
rather than filing away:

**What worked well:**
- Staying in Python the entire time, start to finish -- the data
  (`data.py`), the chart generation (`generate_assets.py`), and the
  page structure (`site.py`) all share the same syntax and mental
  model. No JSX context-switch, no `.vue` file sections, no bundler
  config.
- ARKlight's validation is genuinely useful, not just strict. Nesting
  something invalid inside a text-only component fails the build with
  an exact node path, before any file is written -- rather than a
  broken render that has to be debugged visually after the fact.
- The schema (`arklight/ir/schema.py`) is small enough to read once
  and then *know*, with certainty, every component's required props
  and nesting rules for the rest of the build -- rather than working
  from statistical pattern-matching against a large, only-partly-
  relevant training corpus (the way generating React/Vue/Svelte code
  from memory tends to work).

**What had a real cost:**
- The chart workaround (matplotlib PNGs, generated offline, then
  wired in as static images) is a genuine two-step process, not a
  stylistic choice -- there's no inline, live `<BarChart data={...}>`
  equivalent, and there won't be, per ARKlight's own non-goals.
- Hit one non-obvious bug specific to ARKlight's two-phase execution
  model: `from data import X` inside a page function behaved
  differently than the same import at module level, because the site
  file's top-level code and its page functions run in different
  compiler stages. Nothing about knowing Python in general predicts
  that -- it came from reading the traceback and reasoning about
  ARKlight's loader specifically, not from recalling a known pattern.

Net take: for a task like this one -- static pages, tables, and
pre-computed data, no live interactivity -- ARKlight's closed-
vocabulary ceiling was rarely a real constraint, except at the charts.
A task that needed genuine client-side interactivity would look
different, and would probably lean on `v0.044`'s in-progress reactive-
core work (see the main ARKlight repo's `docs/DESIGN-NOTES.md`) rather
than this project's approach.

## Sources

See [`PLAN.md`](./PLAN.md) Section 2d for the full list -- Stack
Overflow Developer Survey 2025, State of JS 2025, js-framework-
benchmark, and ARKlight's own repo docs. ARKlight's own bundle-size
figures were measured directly during this build, not sourced from an
article; the exact commands are documented on the site's own
Methodology page.
