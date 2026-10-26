# 01-first-map (folium) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Synthetic coordinates ONLY (a made-up grid, not a real place).
# Writes first_map.html in this directory; prints a summary.
import folium

POINTS = [
    ("Alpha", 10.010, 20.010),
    ("Bravo", 10.020, 20.030),
    ("Charlie", 10.030, 20.010),
    ("Delta", 10.040, 20.040),
    ("Echo", 10.050, 20.020),
]

m = folium.Map(location=[10.030, 20.025], zoom_start=13)
for name, lat, lon in POINTS:
    folium.Marker(location=[lat, lon], popup=name).add_to(m)
folium.TileLayer("OpenStreetMap").add_to(m)
folium.LayerControl().add_to(m)

out = "first_map.html"
m.save(out)
html = open(out, encoding="utf-8").read()
assert len(html) > 0 and "Alpha" in html and "Leaflet" in html
print(f"Markers: {len(POINTS)}, HTML bytes: {len(html)}")
