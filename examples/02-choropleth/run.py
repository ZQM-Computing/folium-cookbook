# 02-choropleth (folium) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Choropleth-STYLE map from a plain GeoJSON dict + style function.
# No GeoPandas required: the seed's GeoDataFrame variant is a validation
# item (see README). Synthetic regions and values ONLY.
# Writes choropleth.html in this directory; prints a summary.
import folium

REGIONS = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature", "properties": {"name": "North", "value": 10},
         "geometry": {"type": "Polygon", "coordinates": [[[20.00, 10.04], [20.02, 10.04], [20.02, 10.05], [20.00, 10.05], [20.00, 10.04]]]}},
        {"type": "Feature", "properties": {"name": "Central", "value": 25},
         "geometry": {"type": "Polygon", "coordinates": [[[20.00, 10.02], [20.02, 10.02], [20.02, 10.04], [20.00, 10.04], [20.00, 10.02]]]}},
        {"type": "Feature", "properties": {"name": "South", "value": 40},
         "geometry": {"type": "Polygon", "coordinates": [[[20.00, 10.00], [20.02, 10.00], [20.02, 10.02], [20.00, 10.02], [20.00, 10.00]]]}},
    ],
}


def shade(value):
    # Three fixed bands; thresholds are this pattern's own choice.
    if value < 20:
        return "#fee5d9"
    if value < 35:
        return "#fcae91"
    return "#cb181d"


values = [f["properties"]["value"] for f in REGIONS["features"]]
mean_value = sum(values) / len(values)

m = folium.Map(location=[10.025, 20.01], zoom_start=13)
folium.GeoJson(
    REGIONS,
    style_function=lambda f: {
        "fillColor": shade(f["properties"]["value"]),
        "color": "black",
        "weight": 1,
        "fillOpacity": 0.7,
    },
    tooltip=folium.GeoJsonTooltip(fields=["name", "value"]),
).add_to(m)

out = "choropleth.html"
m.save(out)
html = open(out, encoding="utf-8").read()
assert len(html) > 0 and "North" in html and "Central" in html and "South" in html
assert mean_value == 25.0
print(f"Regions: {len(values)}, mean value: {mean_value}")
