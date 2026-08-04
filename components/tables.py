from __future__ import annotations

from arklight import Table, TableBody, TableHead, TableHeaderCell, TableRow


def data_table(headers: list[str], rows: list[TableRow]):
    """
    Generic Table(TableHead(...), TableBody(...)) wrapper -- the one
    piece of markup that was near-identical across four different
    pages (bundle-size, adoption, architecture's feature table,
    changelog) before this split, differing only in headers and how
    each page wanted its own cells formatted (Code(), Strong(), a
    status class_name, ...). Pages build their own list[TableRow] with
    whatever per-cell formatting they need and hand it here -- this
    function only owns the header row + Table/TableHead/TableBody
    structure, not cell content or formatting decisions.
    """
    return Table(
        TableHead(TableRow(*[TableHeaderCell(h) for h in headers])),
        TableBody(*rows),
    )
