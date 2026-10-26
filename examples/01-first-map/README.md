# 01 — First map

A first folium map: five synthetic markers, a tile layer, and a layer
control. All coordinates are a made-up grid (lat 10.01–10.05, lon
20.01–20.04) — not a real place.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare `python`
(the hermes venv).

## Expected output

```text
Markers: 5, HTML bytes: <positive integer>
```

The HTML byte count varies with the folium version; the assertions that
must hold are: the file exists, is non-empty, and contains the first
marker popup ("Alpha") and a Leaflet reference.

## Failure behavior

- `ModuleNotFoundError: folium` — you are not in the wave11 venv; use
  the full venv Python path above.
- Empty HTML or missing "Alpha" — the marker loop was edited; restore
  `POINTS` from `run.py`, do not adjust the assertions.
- Tiles blank at view time — the HTML references the tile CDN; tiles
  load only with network access. Markers render regardless.

## Versions and evidence

- Tool: folium 0.20.0 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked).
- Evidence level: design-only (gate 1 target). Marker count and HTML
  assertions were derived during drafting; running them against the
  fleet folium environment is **to confirm at validation**.
