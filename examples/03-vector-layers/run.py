# 03-vector-layers (folium) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# GeoJSON polygons + point markers with popups and tooltips.
# Synthetic geometries ONLY (a made-up grid, not a real place).
# Writes vector_layers.html in this directory; prints a summary.
import folium

POLYGONS = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature", "properties": {"name": "Zone A"},
         "geometry": {"type": "Polygon", "coordinates": [[[20.00, 10.00], [20.02, 10.00], [20.02, 10.02], [20.00, 10.02], [20.00, 10.00]]]}},
        {"type": "Feature", "properties": {"name": "Zone B"},
         "geometry": {"type": "Polygon", "coordinates": [[[20.02, 10.02], [20.04, 10.02], [20.04, 10.04], [20.02, 10.04], [20.02, 10.02]]]}},
    ],
}

MARKERS = [
    ("Site 1", 10.010, 20.010, "First synthetic site"),
    ("Site 2", 10.030, 20.030, "Second synthetic site"),
    ("Site 3", 10.045, 20.015, "Third synthetic site"),
    ("Site 4", 10.015, 20.035, "Fourth synthetic site"),
]

m = folium.Map(location=[10.025, 20.02], zoom_start=13)
folium.GeoJson(
    POLYGONS,
    tooltip=folium.GeoJsonTooltip(fields=["name"]),
).add_to(m)
for name, lat, lon, note in MARKERS:
    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(f"{name}: {note}"),
        tooltip=name,
    ).add_to(m)

out = "vector_layers.html"
m.save(out)
html = open(out, encoding="utf-8").read()
assert len(html) > 0
for token in ["Zone A", "Zone B", "Site 1", "Site 4"]:
    assert token in html, f"missing {token}"
print(f"Polygons: {len(POLYGONS['features'])}, markers: {len(MARKERS)}")
