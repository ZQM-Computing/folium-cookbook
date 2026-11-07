# folium Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **folium cookbook** — interactive Leaflet maps from Python. Installed in wave-11 (Node-1 wave11-venv, Wally spot-checked 2026-10-25). First pattern pass written below (design-only, gate 1 target). It is intended for Python developers who publish interactive maps from notebooks and scripts. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public. First pattern pass written (design-only, gate 1 target — none runtime-validated on the fleet yet).

**What this repository is:** folium patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Python developers who publish interactive maps from notebooks and scripts.

## Prerequisites

- folium 0.20.0 in Node-1's wave11-venv (`C:\geo-tools\wave11-venv`, Python 3.12.10) — invoke the venv Python by full path, never bare `python` (hermes venv)
- GeoJSON dicts for the data passes; GeoPandas is optional, not required by any pattern here

## Patterns

| # | Example | What it demonstrates | Status |
|---|---------|----------------------|--------|
| 01 | [examples/01-first-map](examples/01-first-map) | A first map: markers, tiles, and layers | Written (design-only) |
| 02 | [examples/02-choropleth](examples/02-choropleth) | Choropleth-style maps from GeoJSON dicts | Written (design-only) |
| 03 | [examples/03-vector-layers](examples/03-vector-layers) | GeoJSON and vector overlays with popups | Written (design-only) |
| 04 | [examples/04-export](examples/04-export) | Exporting standalone HTML maps | Written (design-only) |
| 05 | [examples/05-coverage-aware-parcels](examples/05-coverage-aware-parcels) | Map synthetic screened parcels without conflating unknown coverage and numeric zero | Automated tests added; CI validation pending |

## Reproducible CI and end-to-end tests

The repository now has a pinned `folium==0.20.0` dependency and a Python 3.11/3.12 GitHub Actions workflow. The unit-test suite executes **all four original scripts** in fresh temporary directories and verifies the HTML that Folium actually renders; it also tests the fifth coverage-aware example's negative cases and exact synthetic JSON report.

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -p "test_*.py" -v
python examples/05-coverage-aware-parcels/run.py --output-dir output/coverage
```

**Evidence scope:** Linux GitHub-hosted test execution is distinct from validation on Node-1/Node-3 hardware and from real browser/offline acceptance. Older notes about the fleet environment remain historical until a separate exact-version fleet test is documented. Leaflet/CDN resources in the output HTML generally require internet access; creating a map HTML is not offline-first PWA support.

## Repository layout

```text
folium-cookbook/
├── examples/
│   ├── 01-first-map/
│   ├── 02-choropleth/
│   ├── 03-vector-layers/
│   ├── 04-export/
│   └── 05-coverage-aware-parcels/
├── tests/test_examples.py
├── .github/workflows/ci.yml
├── requirements.txt
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: all four table rows (design-only, gate 1 target)
- Validation pass: run each pattern against the fleet environment and promote to gate 3

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [keplergl-cookbook](https://github.com/ZQM-Computing/keplergl-cookbook) — Large-scale geospatial visualization in notebooks and apps
- [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) — GeoDataFrame patterns: joins, overlays, and spatial analysis
- [maplibre-cookbook](https://github.com/ZQM-Computing/maplibre-cookbook) — Custom layers, 3D terrain, performance tuning, interactive maps
