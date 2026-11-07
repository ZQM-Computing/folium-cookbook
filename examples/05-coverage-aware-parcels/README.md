# Example 05: coverage-aware synthetic parcel screening

**Question:** What should a map display when an environmental observation source does not cover a parcel?

**Answer:** Preserve **unknown / not assessed**. Do not substitute numeric zero for missing coverage. A zero recorded-site count is meaningful only for a *covered* source and is not evidence that a parcel is safe.

This executable Folium example renders three fictional polygons: P-01 has two recorded synthetic sites; P-02 is covered but has zero recorded sites; P-03 is missing coverage and has **no numeric count**. A fixed legend and hover tooltips distinguish all three states. The code rejects a missing-coverage parcel assigned a numeric zero.

## Run

From the repository root, with Python 3.11 or 3.12:

```bash
python -m pip install -r requirements.txt
python examples/05-coverage-aware-parcels/run.py --output-dir output/parcel-demo
python -m unittest discover -s tests -v
```

The output directory must not exist. The program writes `parcel_screening.html` and `parcel_screening.metrics.json`. The JSON is marked synthetic and states real source coverage has **not** been verified.

The HTML loads Folium/Leaflet JavaScript and CSS from remote CDNs, even though basemap tiles are disabled. Generating the HTML does not turn it into an offline PWA or a production location game; browsers may need an internet connection to display the file.

## Test and operational boundaries

The suite executes all four existing map examples in isolated temporary directories, checks their rendered HTML and tests the new example's statuses and error cases: duplicate IDs, unclosed rings, invalid booleans/counts, unknown mapped to zero, and overwrite refusal.

These tests are **synthetic map correctness checks**, not proof of real parcel coverage, field observations, safe environmental conditions, regulatory assessment, fully offline browser behavior, browser compatibility or performance at scale. Real inputs require reviewed data lineage, license/coverage footprints, CRS and accessibility validation.

ZQM Computing owns reusable GIS patterns; ZQM Labs separately owns games, QR/GPS player logic and event releases.
