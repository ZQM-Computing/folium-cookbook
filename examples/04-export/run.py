# 04-export (folium) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Exporting a standalone HTML map: one file, no server required to open
# it. Tiles still load from the CDN at view time (see README).
# Synthetic coordinates ONLY. Writes standalone_map.html; prints a summary.
import folium

m = folium.Map(location=[10.025, 20.02], zoom_start=13)
folium.Marker(location=[10.025, 20.02], popup="Export demo marker").add_to(m)
folium.CircleMarker(
    location=[10.035, 20.030], radius=8,
    popup="Export demo circle", color="darkred", fill=True,
).add_to(m)

out = "standalone_map.html"
m.save(out)
html = open(out, encoding="utf-8").read()
assert len(html) > 0
assert "Export demo marker" in html and "Export demo circle" in html
print(f"Standalone file: {out}, bytes: {len(html)}, markers: 2")
