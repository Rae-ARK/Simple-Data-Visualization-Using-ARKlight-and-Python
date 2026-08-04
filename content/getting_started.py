# --------------------------------------------------------------------
# /getting-started -- the exact CLI section from ARKlight's own
# README.md, reproduced as real commands (not paraphrased or
# reformatted), since these are the literal commands a visitor would
# run -- inventing a different-but-equivalent command would be the
# actual inaccuracy here.
GETTING_STARTED_STEPS = [
    (
        "1. Install (alpha branch -- see the compatibility note below)",
        "git clone --branch alpha https://github.com/Rae-ARK/ARKlight.git\n"
        "cd ARKlight\n"
        "pip install -e .",
        "Installs the `arklight` package and the `arklight` CLI command.",
    ),
    (
        "2. Build a site",
        "arklight build site.py -o ARK --no-open --verbose",
        "`site.py` must define `site = Site()` and at least one "
        "`@site.page(\"/route\")`-decorated function. `--verbose` prints "
        "a line as each compiler stage starts.",
    ),
    (
        "3. Pack it into a single file",
        "arklight pack ARK -o mysite.ark",
        "Sealed by default -- opaque to generic archive tools, but "
        "still opens directly in a browser (see this site's own "
        "\"Download offline bundle\" link in the footer).",
    ),
    (
        "4. Unpack it back",
        "arklight unpack mysite.ark -o restored",
        "Auto-detects sealed vs. plain bundles.",
    ),
    (
        "5. Look up a component's schema",
        "arklight search Picture",
        "Prints required props, whether it allows children, and "
        "whether it's a Bind(...)-able target. Typo-tolerant -- "
        "`arklight search pictur` suggests `Picture, PictureSource`.",
    ),
]
