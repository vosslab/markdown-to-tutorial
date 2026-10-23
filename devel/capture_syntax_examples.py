#!/usr/bin/env python3
"""Build and capture native formatting-demo evidence outside the macOS sandbox."""

# Standard Library
import argparse
import datetime
import hashlib
import json
import pathlib
import shutil
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
def crop_pdf(pdf: pathlib.Path, page: int, crop: tuple[int, int, int, int], name: str,
		temporary: pathlib.Path, destination: pathlib.Path) -> pathlib.Path:
	"""Capture a precise PDF area using the shared quality-90 WebP helper."""
	capture_readme_artifacts.capture_pdf(pdf, page, crop, name, temporary, destination)
	result = destination / f"{name}.webp"
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
		"python3", "make_tutorial.py", "build", str(source), "--format", "all", "--output", str(output),
	]
	subprocess.run(command, cwd=root, check=True)
	stem = source.stem
	pdf = output / f"{stem}.pdf"
	xlsx = output / f"{stem}.xlsx"
	if not pdf.is_file() or not xlsx.is_file():
		raise RuntimeError("The native build did not produce both PDF and XLSX artifacts")
	return pdf, xlsx


#============================================
def capture_workbook(renderer: pathlib.Path, xlsx: pathlib.Path, temporary: pathlib.Path,
		destination: pathlib.Path) -> pathlib.Path:
	"""Render a printed copy of the actual starter workbook with supplied labels and blank entries."""
	print_copy = temporary / "formatting_demo_workbook.xlsx"
	capture_readme_artifacts.prepare_workbook(xlsx, print_copy, "A1:F4")
	result = temporary / "syntax_workbook.webp"
	# The screenshot-docs renderer launches LibreOffice; this whole script runs outside the sandbox.
	subprocess.run(["bash", str(renderer), str(result), str(print_copy)], check=True)
	destination_path = destination / result.name
	shutil.copyfile(result, destination_path)
	return destination_path


#============================================
def main() -> None:
	"""Capture five tightly cropped proof views without changing canonical outputs."""
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument(
		"-r", "--artifact-renderer", dest="artifact_renderer", required=True,
		type=pathlib.Path, help="Path to screenshot-docs render_artifact_libreoffice.sh",
	)
	args = parser.parse_args()
	repo_result = subprocess.run(
		["git", "rev-parse", "--show-toplevel"], check=True, capture_output=True, text=True,
	)
	root = pathlib.Path(repo_result.stdout.strip())
	destination = root / "docs" / "screenshots"
	before = protected_hashes(root)
	temporary = pathlib.Path(tempfile.mkdtemp(prefix="syntax_capture_"))
	pdf, xlsx = build_example(root, temporary)
	# PDF points use the 144-dpi native PDF coordinate space; inspect and adjust these focused clips.
	assets = [
		crop_pdf(pdf, 1, (78, 280, 1092, 420), "syntax_headings", temporary, destination),
		crop_pdf(pdf, 1, (78, 675, 1092, 185), "syntax_text", temporary, destination),
		crop_pdf(pdf, 1, (78, 850, 1092, 240), "syntax_actions", temporary, destination),
		crop_pdf(pdf, 1, (78, 1330, 1092, 140), "syntax_table", temporary, destination),
	]
	assets.append(capture_workbook(args.artifact_renderer, xlsx, temporary, destination))
	after = protected_hashes(root)
	if after != before:
		raise RuntimeError("A protected source changed during syntax capture")
	receipt = {
		"captured_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
		"source": "docs/examples/formatting_demo.md",
		"protected_sha256": after,
		"assets_sha256": {asset.name: digest(asset) for asset in assets},
		"renderer": str(args.artifact_renderer.resolve()),
		"native_artifacts": {
			"document": "DOCX rendered to PDF by the project build, then cropped from PDF",
			"workbook": "generated XLSX rendered through screenshot-docs LibreOffice renderer",
		},
		"protected_sources_unchanged": True,
		"build_output": "isolated temporary directory; canonical tutorial_output is not used",
	}
	receipt_path = destination / "syntax_capture_receipt.json"
	receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="ascii")
	print(f"Capture receipt: {receipt_path}")


if __name__ == "__main__":
	main()
