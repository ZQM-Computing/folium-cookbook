# 02 — Choropleth

A choropleth-style map from a plain GeoJSON dict: three synthetic
regions shaded by value bands, with name/value tooltips. No GeoPandas
is required for this variant.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare `python`
(the hermes venv).

## Expected output

```text
Regions: 3, mean value: 25.0
```

Derivation: values are 10 (North), 25 (Central), 40 (South);
(10 + 25 + 40) / 3 = 25.0. Bands: <20 pale, 20–34 mid, >=35 dark red.

## Failure behavior

- A different mean — the region values were edited; restore `REGIONS`
  from `run.py`, do not adjust the assertion.
- A region missing from the HTML — the GeoJSON dict was edited; the
  three names must all appear in the saved file.
- `ModuleNotFoundError: folium` — you are not in the wave11 venv; use
  the full venv Python path above.

## Versions and evidence

- Tool: folium 0.20.0 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked).
- Deviation, documented: the seed plans "Choropleth maps from
  GeoDataFrames". This pattern uses a GeoJSON dict + `style_function`
  so it runs without GeoPandas (not in the wave11 package list). The
  `folium.Choropleth`-class + GeoDataFrame variant is a validation
  item, not asserted here.
- Evidence level: design-only (gate 1 target). Region count, mean, and
  band thresholds were derived during drafting; running them against
  the fleet folium environment is **to confirm at validation**.
