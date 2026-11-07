"""Synthetic Folium parcel-screening example; never interpret missing data as zero.

Run from any directory:
    python examples/05-coverage-aware-parcels/run.py --output-dir /tmp/zqm-folium

The output is a *static HTML file that references external Leaflet assets*.
It is NOT a standalone/offline PWA or a surveyed parcel/real hazard map.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import folium


# Arbitrary, fictional coordinate grid. None of these features represents
# a real parcel, landowner, environmental finding, or navigable location.
PARCELS = (
    {"id": "P-01", "ring": ((20.00, 10.00), (20.02, 10.00), (20.02, 10.02), (20.00, 10.02), (20.00, 10.00)), "covered": True, "recorded_sites": 2},
    {"id": "P-02", "ring": ((20.03, 10.00), (20.05, 10.00), (20.05, 10.02), (20.03, 10.02), (20.03, 10.00)), "covered": True, "recorded_sites": 0},
    {"id": "P-03", "ring": ((20.00, 10.03), (20.02, 10.03), (20.02, 10.05), (20.00, 10.05), (20.00, 10.03)), "covered": False, "recorded_sites": None},
)

COLORS = {
    "covered_positive": "#b45309",
    "covered_zero": "#166534",
    "unknown_missing_coverage": "#64748b",
}


def classify(parcel: dict) -> str:
    """Reject impossible semantics before drawing any potentially misleading map."""
    covered = parcel["covered"]
    count = parcel["recorded_sites"]
    if type(covered) is not bool:
        raise ValueError("Coverage flag must be boolean")
    if not covered:
        if count is not None:
            raise ValueError("Uncovered parcels must retain unknown (None) observations")
        return "unknown_missing_coverage"
    if type(count) is not int or count < 0:
        raise ValueError("Covered parcels need a non-negative integer observation count")
    return "covered_positive" if count else "covered_zero"


def as_geojson(parcels=PARCELS) -> dict:
    if len({p["id"] for p in parcels}) != len(parcels):
        raise ValueError("Duplicate parcel IDs")
    features = []
    for p in parcels:
        status = classify(p)
        ring = p["ring"]
        if len(ring) < 4 or ring[0] != ring[-1]:
            raise ValueError("Parcel polygon ring must be closed")
        features.append({
            "type": "Feature",
            "properties": {
                "parcel_id": p["id"],
                "observation_status": status,
                "recorded_sites_display": (
                    "not assessed" if p["recorded_sites"] is None else str(p["recorded_sites"])
                ),
            },
            "geometry": {"type": "Polygon", "coordinates": [[list(xy) for xy in ring]]},
        })
    return {"type": "FeatureCollection", "features": features}


def summarize(parcels=PARCELS) -> dict:
    statuses = [classify(p) for p in parcels]
    return {
        "schema_version": 1,
        "dataset": "fictional_synthetic_parcel_grid_not_real_geography",
        "source_coverage_verified": False,
        "count_semantics": "synthetic_recorded_sites_not_hazards",
        "parcels": len(parcels),
        "covered_positive": statuses.count("covered_positive"),
        "covered_zero": statuses.count("covered_zero"),
        "unknown_missing_coverage": statuses.count("unknown_missing_coverage"),
        "limitations": [
            "Synthetic observations are not environmental hazards or actual parcel records.",
            "No reliable real-world source coverage was evaluated.",
            "Zero observed records does not establish environmental safety.",
            "HTML requires external Leaflet resources; it is not guaranteed offline.",
        ],
    }


def render(output_dir: Path) -> dict:
    if output_dir.exists():
        raise ValueError("Refusing to overwrite an existing output directory")
    features = as_geojson()
    report = summarize()
    output_dir.mkdir(parents=True)
    m = folium.Map(location=[10.025, 20.025], zoom_start=13, tiles=None)
    folium.GeoJson(
        features,
        name="Synthetic coverage-aware screening",
        style_function=lambda f: {
            "fillColor": COLORS[f["properties"]["observation_status"]],
            "color": "#334155",
            "weight": 2,
            "fillOpacity": 0.65,
        },
        tooltip=folium.GeoJsonTooltip(
            fields=["parcel_id", "observation_status", "recorded_sites_display"],
            aliases=["Illustrative parcel", "Source coverage status", "Recorded sites"],
            sticky=False,
        ),
    ).add_to(m)
    folium.LayerControl().add_to(m)
    # Fixed editorial text; never interpolate untrusted property content into HTML.
    m.get_root().html.add_child(folium.Element(
        '<div role="note" style="position:fixed;bottom:18px;left:18px;'
        'z-index:9999;background:white;padding:10px;border:2px solid #334155;">'
        '<strong>Synthetic example, not environmental evidence</strong><ul>'
        '<li>Amber: covered, one or more records</li>'
        '<li>Green: covered, zero recorded sites</li>'
        '<li>Grey: unknown, missing coverage (not zero)</li></ul></div>'
    ))
    html_file = output_dir / "parcel_screening.html"
    metrics_file = output_dir / "parcel_screening.metrics.json"
    m.save(str(html_file))
    metrics_file.write_text(
        json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    if not html_file.is_file() or html_file.stat().st_size == 0:
        raise RuntimeError("Failed to render map")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True, help="Fresh directory")
    args = parser.parse_args()
    try:
        report = render(args.output_dir)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
