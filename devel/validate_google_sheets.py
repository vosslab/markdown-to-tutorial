#!/usr/bin/env python3
"""Execute authored tutorial formulas in new Google Sheets test workbooks."""

import json
import pathlib
import argparse
import datetime

import sheetlesson.compiler
import sheets_validation_lib


#============================================
def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("tutorials", nargs="+", type=pathlib.Path)
	parser.add_argument("-o", "--output", dest="output", type=pathlib.Path,
		default=pathlib.Path("build/sheets-validation"))
	parser.add_argument("-e", "--expectations", dest="expectations", type=pathlib.Path)
	mode = parser.add_mutually_exclusive_group()
	mode.add_argument("-n", "--dry-run", dest="live", action="store_false")
	mode.add_argument("-l", "--live", dest="live", action="store_true")
	parser.set_defaults(live=False)
	args = parser.parse_args()
	return args


#============================================
def save_json(path: pathlib.Path, payload: object) -> None:
	path.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n", encoding="utf-8")


#============================================
def main() -> int:
	args = parse_args()
	args.output.mkdir(parents=True, exist_ok=True)
	cases = []
	for path in args.tutorials:
		cases.extend(sheets_validation_lib.prepare_cases(
			sheetlesson.compiler.compile_document(path)))
	expectations = {}
	if args.expectations is not None:
		expectations = json.loads(args.expectations.read_text(encoding="utf-8"))["tutorials"]
	# Reject typoed scenario names instead of silently skipping scientific checks.
	for name, item in expectations.items():
		known = {case["scenario"] for case in cases if pathlib.Path(case["tutorial"]).name == name}
		if not known or set(item.get("scenarios", {})) - known:
			raise ValueError(f"Expectations name an unknown tutorial or scenario: {name}")
	save_json(args.output / "execution-cases.json", cases)
	report = {"mode": "live" if args.live else "dry_run",
		"created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
		"status": "prepared", "sheets_status": "not_run", "oracle_status": "not_run",
		"created_spreadsheets": [], "results": []}
	report_path = args.output / "report.json"
	save_json(report_path, report)
	if not args.live:
		print(f"Prepared {len(cases)} cases; no Google requests made. Report: {report_path}")
		return 0
	# Import Google dependencies only for live runs; dry runs remain entirely offline.
	import google.auth
	import google.auth.exceptions
	import googleapiclient.discovery
	try:
		credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/spreadsheets"])
	except google.auth.exceptions.DefaultCredentialsError:
		report.update(status="unavailable", reason="Application Default Credentials unavailable")
		save_json(report_path, report)
		print(f"Google Sheets unavailable: configure ADC. Report: {report_path}")
		return 2
	service = googleapiclient.discovery.build("sheets", "v4", credentials=credentials,
		cache_discovery=False)
	def record_created(created: dict) -> None:
		report["created_spreadsheets"].append(created)
		save_json(report_path, report)
	for case in cases:
		item = expectations.get(pathlib.Path(case["tutorial"]).name, {})
		expected = item.get("common", {}) | item.get("scenarios", {}).get(case["scenario"], {})
		report["status"] = "running"
		save_json(report_path, report)
		result = sheets_validation_lib.run_case(service, case, expected, record_created)
		report["results"].append(result)
		save_json(report_path, report)
	failure = any(result["sheets_status"] == "failed" or result["oracle_status"] == "failed"
		for result in report["results"])
	report["status"] = "failed" if failure else "completed"
	report["sheets_status"] = "failed" if any(result["sheets_status"] == "failed"
		for result in report["results"]) else "passed"
	statuses = {result["oracle_status"] for result in report["results"]}
	report["oracle_status"] = "failed" if "failed" in statuses else (
		"passed" if statuses == {"passed"} else "incomplete")
	save_json(report_path, report)
	print(f"Google Sheets {report['status']}. Report: {report_path}")
	return 1 if failure else 0


if __name__ == "__main__":
	raise SystemExit(main())
