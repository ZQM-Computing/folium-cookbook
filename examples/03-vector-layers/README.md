# 03 — Vector layers

GeoJSON polygon overlays with tooltips, plus point markers carrying
popups and tooltips. Two zones, four sites, all synthetic.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare `python`
(the hermes venv).

## Expected output

```text
Polygons: 2, markers: 4
```

The assertions that must hold are: the file exists, is non-empty, and
contains "Zone A", "Zone B", "Site 1", and "Site 4".

## Failure behavior

- A missing token in the HTML — the GeoJSON dict or the marker list
  was edited; restore `POLYGONS` / `MARKERS` from `run.py`.
- Popups showing raw HTML — the popup string was edited to include
  markup; this pattern passes plain text only.
- `ModuleNotFoundError: folium` — you are not in the wave11 venv; use
  the full venv Python path above.

## Versions and evidence

- Tool: folium 0.20.0 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked).
- Evidence level: design-only (gate 1 target). Polygon/marker counts
  and popup contents were derived during drafting; running them
  against the fleet folium environment is **to confirm at validation**.
