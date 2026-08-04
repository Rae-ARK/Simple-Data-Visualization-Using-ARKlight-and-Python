from __future__ import annotations

from arklight import Container, Heading, Meter, Text


def kpi_card(value_label: str, description: str, meter_name: str, meter_value: float, meter_min: float, meter_max: float):
    """One of Home's three top-of-page KPI cards (big number + Meter)."""
    return Container(
        Heading(value_label, level=3, class_name="kpi-value"),
        Text(description, class_name="muted"),
        Meter(meter_name, value=meter_value, min=meter_min, max=meter_max),
        class_name="card",
    )


def labeled_meter(name: str, value: float, min: float, max: float):
    """One row of Bundle Size's per-tool Meter list -- label above a bar."""
    return Container(
        Text(name),
        Meter(name, value=value, min=min, max=max),
        class_name="stack",
    )
