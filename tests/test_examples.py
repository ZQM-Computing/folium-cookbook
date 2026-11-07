"""End-to-end smoke tests for all five synthetic Folium patterns."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
EXISTING = (
    ("01-first-map", "first_map.html", "Markers: 5", ("Alpha", "Echo")),
    ("02-choropleth", "choropleth.html", "Regions: 3, mean value: 25.0",
     ("North", "Central", "South")),
    ("03-vector-layers", "vector_layers.html", "Polygons: 2, markers: 4",
     ("Zone A", "Zone B", "Site 1", "Site 4")),
    ("04-export", "standalone_map.html", "markers: 2",
     ("Export demo marker", "Export demo circle")),
)

SPEC = importlib.util.spec_from_file_location(
    "coverage_map", EXAMPLES / "05-coverage-aware-parcels" / "run.py"
)
coverage_map = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(coverage_map)


class ExistingExamples(unittest.TestCase):
    def test_examples_run_and_produce_real_html(self):
        for directory, filename, stdout, tokens in EXISTING:
            with self.subTest(directory=directory), tempfile.TemporaryDirectory() as temp:
                script = EXAMPLES / directory / "run.py"
                proc = subprocess.run(
                    [sys.executable, str(script)], cwd=temp,
                    capture_output=True, text=True, timeout=45, check=False,
                )
                self.assertEqual(proc.returncode, 0, proc.stderr)
                self.assertIn(stdout, proc.stdout)
                rendered = Path(temp) / filename
                self.assertTrue(rendered.is_file())
                html = rendered.read_text(encoding="utf-8")
                self.assertGreater(len(html), 2000)
                self.assertIn("leaflet", html.lower())
                if directory == "01-first-map":
                    self.assertEqual(html.count("L.tileLayer("), 1, "Avoid duplicate base tiles")
                for token in tokens:
                    self.assertIn(token, html)

    def test_four_real_scripts_are_present(self):
        self.assertEqual(
            sorted(p.name for p in EXAMPLES.glob("0[1-4]-*") if p.is_dir()),
            [row[0] for row in EXISTING],
        )


class CoverageAwareParcels(unittest.TestCase):
    def test_metrics_and_map_distinguish_missing_from_zero(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "new"
            report = coverage_map.render(output)
            self.assertEqual(
                (report["covered_positive"], report["covered_zero"],
                 report["unknown_missing_coverage"]), (1, 1, 1)
            )
            self.assertFalse(report["source_coverage_verified"])
            self.assertEqual(report["parcels"], 3)
            self.assertEqual(
                json.loads((output / "parcel_screening.metrics.json").read_text()), report
            )
            html = (output / "parcel_screening.html").read_text(encoding="utf-8")
            self.assertIn("leaflet", html.lower())
            for token in ("P-01", "P-02", "P-03", "not assessed",
                          "covered_zero", "unknown_missing_coverage",
                          "Synthetic example, not environmental evidence"):
                self.assertIn(token, html)
            # This exported HTML intentionally imports JS/CSS externally;
            # no test here asserts fully offline browser operation.
            self.assertIn("leaflet.js", html.lower())

    def test_cli_success_and_no_clobber(self):
        with tempfile.TemporaryDirectory() as temp:
            script = EXAMPLES / "05-coverage-aware-parcels" / "run.py"
            output = Path(temp) / "map"
            call = [sys.executable, str(script), "--output-dir", str(output)]
            first = subprocess.run(
                call, capture_output=True, text=True, timeout=45, check=False,
            )
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(json.loads(first.stdout)["parcels"], 3)
            second = subprocess.run(
                call, capture_output=True, text=True, timeout=45, check=False,
            )
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("Refusing to overwrite", second.stderr)

    def test_uncovered_zero_is_invalid(self):
        with self.assertRaisesRegex(ValueError, "unknown"):
            coverage_map.classify({"covered": False, "recorded_sites": 0})
        with self.assertRaisesRegex(ValueError, "boolean"):
            coverage_map.classify({"covered": 1, "recorded_sites": 0})
        with self.assertRaisesRegex(ValueError, "non-negative"):
            coverage_map.classify({"covered": True, "recorded_sites": -1})
        with self.assertRaisesRegex(ValueError, "non-negative"):
            coverage_map.classify({"covered": True, "recorded_sites": True})
        self.assertEqual(
            coverage_map.classify({"covered": False, "recorded_sites": None}),
            "unknown_missing_coverage",
        )

    def test_duplicate_ids_and_unclosed_rings_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            coverage_map.as_geojson(
                [coverage_map.PARCELS[0], coverage_map.PARCELS[0]]
            )
        item = dict(coverage_map.PARCELS[0])
        item["ring"] = item["ring"][:-1]
        with self.assertRaisesRegex(ValueError, "closed"):
            coverage_map.as_geojson([item])

    def test_known_zero_and_unknown_remain_separate_in_geojson(self):
        features = coverage_map.as_geojson()["features"]
        self.assertEqual(len(features), 3)
        self.assertEqual(
            {f["properties"]["observation_status"] for f in features},
            set(coverage_map.COLORS),
        )
        self.assertEqual(
            next(f for f in features if f["properties"]["parcel_id"] == "P-02")
            ["properties"]["recorded_sites_display"], "0"
        )
        self.assertEqual(
            next(f for f in features if f["properties"]["parcel_id"] == "P-03")
            ["properties"]["recorded_sites_display"], "not assessed"
        )


if __name__ == "__main__":
    unittest.main()
