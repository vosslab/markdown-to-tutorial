#!/usr/bin/env python3
"""Refresh README artifact views; run outside the macOS sandbox (LibreOffice)."""

# Standard Library
import json
import shutil
import pathlib
import hashlib
import argparse
import datetime
import tempfile
import subprocess

# PIP3 modules
import openpyxl
import openpyxl.worksheet.page
import openpyxl.worksheet.properties


#============================================
def digest(path: pathlib.Path) -> str:
	"""Return a file's SHA-256 fingerprint."""
	result = hashlib.sha256(path.read_bytes()).hexdigest()
	return result


#============================================
def capture_pdf(pdf: pathlib.Path, page: int, crop: tuple[int, int, int, int],
		name: str, temporary: pathlib.Path, destination: pathlib.Path) -> None:
	"""Render a genuine PDF clip at 144 dpi and encode quality-90 WebP."""
	stem = temporary / name
	x, y, width, height = crop
	subprocess.run([
		"pdftoppm", "-f", str(page), "-l", str(page), "-r", "144",
		"-x", str(x), "-y", str(y), "-W", str(width), "-H", str(height),
		"-singlefile", "-png", str(pdf), str(stem),
	], check=True)
	png = stem.with_suffix(".png")
	webp = stem.with_suffix(".webp")
	subprocess.run(["cwebp", "-q", "90", str(png), "-o", str(webp)], check=True)
	shutil.copyfile(webp, destination / webp.name)
	png.unlink()


#============================================
def prepare_workbook(source: pathlib.Path, destination: pathlib.Path) -> None:
	"""Change only print settings in a disposable copy of the actual workbook."""
	workbook = openpyxl.load_workbook(source)
	sheet = workbook.active
	sheet.print_area = "A1:N26"
	sheet.page_setup.orientation = "landscape"
	sheet.page_setup.paperSize = sheet.PAPERSIZE_A3
	sheet.page_setup.fitToWidth = 1
	sheet.page_setup.fitToHeight = 1
	sheet.sheet_properties.pageSetUpPr = (
		openpyxl.worksheet.properties.PageSetupProperties(fitToPage=True)
	)
	sheet.page_margins = openpyxl.worksheet.page.PageMargins(
		left=0.25, right=0.25, top=0.25, bottom=0.25,
	)
	sheet.print_options.gridLines = True
	sheet.print_options.headings = True
	workbook.save(destination)


#============================================
def main() -> None:
	"""Capture three views and record fingerprints without rebuilding artifacts."""
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
	output = root / "tutorial_output"
	family = "caffeine_3_quadratic_regression"
	pdf = output / family / f"{family}.pdf"
	xlsx = output / family / f"{family}.xlsx"
	destination = root / "docs" / "screenshots"
	# Fingerprint all canonical teaching sources and built student artifacts.
	protected = sorted((root / "tutorial_data").glob("*.md"))
	protected += sorted(output.glob("*/*.docx"))
	protected += sorted(output.glob("*/*.pdf"))
	protected += sorted(output.glob("*/*.xlsx"))
	before = {str(path.relative_to(root)): digest(path) for path in protected}
	temporary = pathlib.Path(tempfile.mkdtemp(prefix="readme_capture_", dir="/tmp"))
	# Clips are PDF page coordinates doubled for the 144-dpi raster.
	capture_pdf(pdf, 1, (100, 98, 1028, 1230),
		"caffeine_3_illustrated_opening", temporary, destination)
	capture_pdf(pdf, 4, (100, 98, 1028, 330),
		"caffeine_3_fill_down_instructions", temporary, destination)
	print_copy = temporary / "readme_caffeine_3_full_workspace.xlsx"
	prepare_workbook(xlsx, print_copy)
	workbook_image = temporary / "caffeine_3_blank_predictor_workspace.webp"
	# The provided renderer invokes LibreOffice and must run outside the sandbox.
	subprocess.run([
		"bash", str(args.artifact_renderer), str(workbook_image), str(print_copy),
	], check=True)
	shutil.copyfile(workbook_image, destination / workbook_image.name)
	after = {str(path.relative_to(root)): digest(path) for path in protected}
	if after != before:
		raise RuntimeError("A protected teaching source or canonical artifact changed")
	receipt = {
		"captured_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
		"protected_sha256": after,
		"assets_sha256": {path.name: digest(path) for path in destination.glob("*.webp")},
		"renderer": str(args.artifact_renderer.resolve()),
		"canonical_files_unchanged": True,
	}
	receipt_path = temporary / "receipt.json"
	receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
	print(f"Capture receipt: {receipt_path}")


if __name__ == "__main__":
	main()
