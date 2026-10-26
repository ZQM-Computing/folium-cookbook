# 04 — Export

Exporting a standalone HTML map: `m.save()` writes one file that opens
in a browser with no server. Two synthetic markers prove the content
survived the round trip.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare `python`
(the hermes venv).

## Expected output

```text
Standalone file: standalone_map.html, bytes: <positive integer>, markers: 2
```

The byte count varies with the folium version; the assertions that
must hold are: the file exists, is non-empty, and contains both popup
texts.

## Failure behavior

- A missing popup text — the marker list was edited; restore `run.py`.
- Tiles blank when opening the file offline — expected: the HTML
  references the tile CDN, so tiles need network at view time. Markers
  and vector overlays render without tiles.
- `ModuleNotFoundError: folium` — you are not in the wave11 venv; use
  the full venv Python path above.

## Versions and evidence

- Tool: folium 0.20.0 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked).
- Evidence level: design-only (gate 1 target). Marker count and popup
  contents were derived during drafting; running them against the
  fleet folium environment is **to confirm at validation**.
