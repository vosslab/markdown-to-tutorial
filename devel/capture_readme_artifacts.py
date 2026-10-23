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

import tutorial_lib.compiler
import tutorial_lib.formula_io
import sheets_validation_lib


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
def prepare_workbook(source: pathlib.Path, destination: pathlib.Path, print_area: str) -> None:
	"""Change only print settings in a disposable copy of the actual workbook."""
	workbook = openpyxl.load_workbook(source)
	sheet = workbook.active
	sheet.print_area = print_area
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
def completed_workbook(source: pathlib.Path, lesson: pathlib.Path, destination: pathlib.Path) -> None:
	"""Apply the baseline authored actions to a styled disposable student workbook."""
	document = tutorial_lib.compiler.compile_document(lesson)
	cases = sheets_validation_lib.prepare_cases(document)
	case = next(item for item in cases if item["scenario"] == "baseline")
	workbook = openpyxl.load_workbook(source)
	for write in case["writes"]:
		cell = workbook[write["sheet"]][write["address"]]
		value = write["value"]
		if "formulaValue" in value:
			cell.value = tutorial_lib.formula_io.serialize_formula(value["formulaValue"])
		elif "stringValue" in value:
			cell.value = value["stringValue"]
			cell.data_type = "s"
		elif "numberValue" in value:
			cell.value = value["numberValue"]
		elif "boolValue" in value:
			cell.value = value["boolValue"]
		else:
			cell.value = None
	workbook.calculation.fullCalcOnLoad = True
	workbook.calculation.forceFullCalc = True
	workbook.save(destination)
	workbook.close()


#============================================
def libreoffice_executable() -> str:
	"""Return the host Calc binary used to recalculate a disposable workbook."""
	result = shutil.which("libreoffice") or shutil.which("soffice")
	macos_binary = pathlib.Path("/Applications/LibreOffice.app/Contents/MacOS/soffice")
	if result is None and macos_binary.is_file():
		result = str(macos_binary)
	if result is None:
		raise RuntimeError("LibreOffice Calc is required to render completed workbook evidence.")
	return result


#============================================
def recalculate_workbook(source: pathlib.Path, destination: pathlib.Path,
		temporary: pathlib.Path) -> None:
	"""Use Calc to update formulas while preserving the styled disposable workbook."""
	output = temporary / "recalculated"
	output.mkdir()
	profile = temporary / "calc_profile"
	process = subprocess.run([
		libreoffice_executable(), f"-env:UserInstallation={profile.as_uri()}", "--headless",
		"--convert-to", "xlsx:Calc MS Excel 2007 XML", "--outdir", str(output), str(source),
	], check=True, capture_output=True, text=True, timeout=120)
	converted = output / source.name
	if not converted.is_file():
		raise RuntimeError(f"Calc did not write {converted}: {process.stdout}\n{process.stderr}")
	shutil.copyfile(converted, destination)


#============================================
def capture_workbook(renderer: pathlib.Path, source: pathlib.Path, name: str,
		temporary: pathlib.Path, destination: pathlib.Path, print_area: str) -> None:
	"""Render a disposable, print-configured view of an actual styled workbook."""
	print_copy = temporary / f"print_{name}.xlsx"
	prepare_workbook(source, print_copy, print_area)
	workbook_image = temporary / f"{name}.webp"
	# The provided renderer invokes LibreOffice and must run outside the sandbox.
	subprocess.run(["bash", str(renderer), str(workbook_image), str(print_copy)], check=True)
	shutil.copyfile(workbook_image, destination / workbook_image.name)


#============================================
def main() -> None:
	"""Capture five current views and preserve canonical teaching artifacts."""
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
	caffeine = "caffeine_3_quadratic_regression"
	microbes_f = "microbes_4_f_test"
	microbes_anova = "microbes_5_anova"
	pdf = output / caffeine / f"{caffeine}.pdf"
	xlsx = output / caffeine / f"{caffeine}.xlsx"
	f_pdf = output / microbes_f / f"{microbes_f}.pdf"
	anova_xlsx = output / microbes_anova / f"{microbes_anova}.xlsx"
	destination = root / "docs" / "screenshots"
	# Fingerprint all canonical teaching sources and built student artifacts.
	canonical = sorted((root / "tutorial_data").glob("*.md"))
	canonical_stems = [path.stem for path in canonical]
	protected = canonical[:]
	for stem in canonical_stems:
		protected += [output / stem / f"{stem}{suffix}" for suffix in (".docx", ".pdf", ".xlsx")]
	before = {str(path.relative_to(root)): digest(path) for path in protected}
	temporary = pathlib.Path(tempfile.mkdtemp(prefix="readme_capture_"))
	# Clips are PDF page coordinates doubled for the 144-dpi raster.
	capture_pdf(pdf, 1, (100, 98, 1028, 1230),
		"caffeine_3_illustrated_opening", temporary, destination)
	capture_pdf(pdf, 4, (80, 82, 1064, 350),
		"caffeine_3_fill_down_instructions", temporary, destination)
	capture_workbook(args.artifact_renderer, xlsx, "caffeine_3_blank_predictor_workspace",
		temporary, destination, "A1:N26")
	capture_pdf(f_pdf, 3, (80, 270, 1064, 620),
		"microbes_4_formula_instruction", temporary, destination)
	completed_source = temporary / "microbes_5_completed_anova_source.xlsx"
	completed_workbook(anova_xlsx, root / "tutorial_data" / f"{microbes_anova}.md", completed_source)
	completed = temporary / "microbes_5_completed_anova.xlsx"
	recalculate_workbook(completed_source, completed, temporary)
	capture_workbook(args.artifact_renderer, completed, "microbes_5_completed_anova",
		temporary, destination, "H1:M16")
	after = {str(path.relative_to(root)): digest(path) for path in protected}
	if after != before:
		raise RuntimeError("A protected teaching source or canonical artifact changed")
	receipt = {
		"captured_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
		"protected_sha256": after,
		"assets_sha256": {path.name: digest(path) for path in sorted(destination.glob("*.webp"))},
		"renderer": str(args.artifact_renderer.resolve()),
		"canonical_files_unchanged": True,
		"completed_demo": {
			"asset": "microbes_5_completed_anova.webp",
			"source": "styled canonical student workbook plus baseline authored actions",
			"calculation": "LibreOffice Calc recalculation in a disposable workspace",
			"canonical_student_workbook": "unchanged and intentionally blank",
		},
	}
	receipt_path = temporary / "receipt.json"
	receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
	shutil.copyfile(receipt_path, destination / "capture_receipt.json")
	print(f"Capture receipt: {receipt_path}")


if __name__ == "__main__":
	main()
