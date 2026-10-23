#!/usr/bin/env python3
"""Build and capture native formatting-demo evidence outside the macOS sandbox."""

# Standard Library
import argparse
import datetime
import hashlib
import json
import pathlib
import subprocess
import tempfile

# Local modules
import capture_readme_artifacts


#============================================
def digest(path: pathlib.Path) -> str:
	"""Return a file's SHA-256 fingerprint."""
	result = hashlib.sha256(path.read_bytes()).hexdigest()
	return result


#============================================
def protected_hashes(root: pathlib.Path) -> dict[str, str]:
	"""Fingerprint the example source and all pre-existing canonical teaching inputs."""
	protected = [root / "docs" / "examples" / "formatting_demo.md"]
	protected += sorted((root / "tutorial_data").glob("*.md"))
	result = {str(path.relative_to(root)): digest(path) for path in protected}
	return result


#============================================
def build_example(root: pathlib.Path, temporary: pathlib.Path) -> tuple[pathlib.Path, pathlib.Path]:
	"""Build the example into an isolated output directory with native DOCX and XLSX renderers."""
	source = root / "docs" / "examples" / "formatting_demo.md"
	output = temporary / "build"
	command = [
		"python3", "make_tutorial.py", "build", str(source), "--format", "all", "--output-dir", str(output),
	]
	subprocess.run(command, cwd=root, check=True)
	stem = source.stem
	pdf = output / f"{stem}.pdf"
	xlsx = output / f"{stem}.xlsx"
	if not pdf.is_file() or not xlsx.is_file():
		raise RuntimeError("The native build did not produce both PDF and XLSX artifacts")
	return pdf, xlsx


#============================================
def main() -> None:
	"""Capture five tightly cropped proof views without changing canonical outputs."""
	parser = argparse.ArgumentParser(description=__doc__)
	parser.parse_args()
	repo_result = subprocess.run(
		["git", "rev-parse", "--show-toplevel"], check=True, capture_output=True, text=True,
	)
	root = pathlib.Path(repo_result.stdout.strip())
	destination = root / "docs" / "screenshots"
	before = protected_hashes(root)
	temporary = pathlib.Path(tempfile.mkdtemp(prefix="syntax_capture_"))
	pdf, xlsx = build_example(root, temporary)
	views = [
		("Part 1: Explore a curved relationship", "Explanation: Why square a value?",
			"syntax_headings"),
		("Explanation: Why square a value?", "Step 2: Calculate squared sleep hours",
			"syntax_text"),
		("Step 2: Calculate squared sleep hours",
			"Explanation: Read a formula before copying it", "syntax_actions"),
		("Step 3: Compare the model features", None, "syntax_table"),
	]
	metadata = [capture_readme_artifacts.capture_pdf(pdf, start, end, name, temporary, destination)
		for start, end, name in views]
	metadata.append(capture_readme_artifacts.render_workbook(xlsx, "syntax_workbook",
		temporary, destination, "A1:F4"))
	assets = [pathlib.Path(item["asset"]) for item in metadata]
	after = protected_hashes(root)
	if after != before:
		raise RuntimeError("A protected source changed during syntax capture")
	receipt = {
		"captured_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
		"source": "docs/examples/formatting_demo.md",
		"protected_sha256": after,
		"assets_sha256": {asset.name: digest(asset) for asset in assets},
		"renderer": "repository-owned LibreOffice and Poppler",
		"captures": metadata,
		"native_artifacts": {
			"document": "DOCX rendered to PDF by the project build, then cropped from PDF",
			"workbook": "generated XLSX printed through repository-owned LibreOffice Calc helper",
		},
		"protected_sources_unchanged": True,
		"build_output": "isolated temporary directory; canonical tutorial_output is not used",
	}
	receipt_path = destination / "syntax_capture_receipt.json"
	receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="ascii")
	print(f"Capture receipt: {receipt_path}")


if __name__ == "__main__":
	main()
