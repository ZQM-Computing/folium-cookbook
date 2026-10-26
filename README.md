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

A **folium cookbook** — interactive Leaflet maps from Python. Queued in wave-11 (per-node adds). Patterns are planned from the design, not yet from fleet runs. It is intended for Python developers who publish interactive maps from notebooks and scripts. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public — seeding. Pattern passes land in follow-up work from fleet-verified setups; the tables below list what is planned, not what is already written.

**What this repository is:** folium patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Python developers who publish interactive maps from notebooks and scripts.

## Prerequisites

- folium in the fleet Python environment
- Python 3.11+
- GeoPandas for the data passes

## Patterns (planned)

| # | Example | What it will demonstrate |
|---|---------|--------------------------|
| 01 | `01-first-map` | A first map: markers, tiles, and layers |
| 02 | `02-choropleth` | Choropleth maps from GeoDataFrames |
| 03 | `03-vector-layers` | GeoJSON and vector overlays with popups |
| 04 | `04-export` | Exporting standalone HTML maps |

## Repository layout

```text
folium-cookbook/
├── examples/          # pattern passes, landing in follow-up work
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: the first two table rows
- Second pass: the remaining rows, from fleet-verified setups

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [keplergl-cookbook](https://github.com/ZQM-Computing/keplergl-cookbook) — Large-scale geospatial visualization in notebooks and apps
- [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) — GeoDataFrame patterns: joins, overlays, and spatial analysis
- [maplibre-cookbook](https://github.com/ZQM-Computing/maplibre-cookbook) — Custom layers, 3D terrain, performance tuning, interactive maps
