"""Staged tutorial bundles and fingerprint-based publication protection."""

# Standard library
import json
import shutil
import hashlib
import pathlib
import zipfile
import tempfile
import dataclasses
import collections.abc

# PIP modules
import defusedxml.ElementTree

# Local modules
import sheetlesson.model
import sheetlesson.workbook
import sheetlesson.pdf_export
import sheetlesson.docx_renderer


OWNER = "markdown-to-tutorial"
FORMATS = {"all": ("docx", "xlsx", "pdf"), "docx,xlsx": ("docx", "xlsx"),
	"docx": ("docx",), "xlsx": ("xlsx",)}


#============================================
def fingerprint(path: pathlib.Path) -> str:
	"""Return a streaming SHA256 fingerprint of one file."""
	digest = hashlib.sha256()
	with path.open("rb") as handle:
		for chunk in iter(lambda: handle.read(65536), b""):
			digest.update(chunk)
	return digest.hexdigest()


#============================================
def run_stage(name: str, operation: collections.abc.Callable, *parameters: object) -> None:
	"""Attach build context while preserving the original exception and cause."""
	try:
		operation(*parameters)
	except Exception as error:
		error.add_note(f"Tutorial build failed during {name}; previous bundle was preserved.")
		raise


#============================================
def verify_docx(path: pathlib.Path) -> None:
	"""Reopen the DOCX package and parse its document and relationship XML."""
	with zipfile.ZipFile(path) as package:
		if package.testzip() is not None:
			raise ValueError("Generated DOCX contains a corrupt ZIP member.")
		defusedxml.ElementTree.fromstring(package.read("word/document.xml"))
		defusedxml.ElementTree.fromstring(package.read("[Content_Types].xml"))
		for name in package.namelist():
			if name.endswith(".rels"):
				defusedxml.ElementTree.fromstring(package.read(name))


#============================================
def check_destination(destination: pathlib.Path, inputs: list[pathlib.Path]) -> None:
	"""Refuse input destruction, foreign directories, and edited generated files."""
	if destination.is_symlink():
		raise ValueError(f"Bundle destination cannot be a symlink: {destination}")
	for source in inputs:
		if source.resolve().is_relative_to(destination.resolve()):
			raise ValueError(f"Bundle destination contains an input: {source}")
	if not destination.exists():
		return
	manifest_path = destination / "validation.json"
	if not destination.is_dir() or not manifest_path.is_file() or manifest_path.is_symlink():
		raise ValueError(f"Destination is not an owned tutorial bundle: {destination}")
	manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
	if manifest.get("owner") != OWNER or manifest.get("schema_version") != 1:
		raise ValueError(f"Destination has no supported ownership manifest: {destination}")
	outputs = manifest["outputs"]
	expected = set(outputs) | {"validation.json"}
	if set(item.name for item in destination.iterdir()) != expected:
		raise ValueError(f"Bundle has added or removed files; preserve edits first: {destination}")
	for name, record in outputs.items():
		path = destination / name
		if pathlib.Path(name).name != name or path.is_symlink() or not path.is_file():
			raise ValueError(f"Unsafe generated artifact in ownership manifest: {name}")
		if fingerprint(path) != record["sha256"]:
			raise ValueError(f"Generated artifact was modified; preserve edits first: {path}")


#============================================
def validation_report(document: sheetlesson.model.Document) -> dict:
	"""Describe offline coverage without implying external acceptance."""
	report = {
		"owner": OWNER, "schema_version": 1,
		"source": {"path": str(document.path.resolve()),
			"sha256": fingerprint(document.path)},
		"assets": [{"path": str(path.resolve()), "sha256": fingerprint(path)}
			for path in document.assets],
		"diagnostics": [dataclasses.asdict(item) for item in document.diagnostics],
		"reference_coverage": {
			"formula_checks": [dataclasses.asdict(item) for item in document.formula_checks],
			"scope": "Offline structure, references, and instruction consistency only",
		},
		"external_behavior": {
			"google_import": "unchecked", "link_navigation": "unchecked",
			"formula_calculation": "unchecked", "pdf_visual_review": "unchecked",
		},
		"outputs": {},
	}
	return report


#============================================
def publish(staging: pathlib.Path, destination: pathlib.Path) -> None:
	"""Swap a verified bundle, rolling back if the final rename fails."""
	if not destination.exists():
		staging.rename(destination)
		return
	backup = pathlib.Path(tempfile.mkdtemp(prefix=".tutorial-backup-", dir=destination.parent))
	previous = backup / "bundle"
	destination.rename(previous)
	try:
		staging.rename(destination)
	except OSError:
		# If rollback itself fails, retain the backup for explicit recovery.
		previous.rename(destination)
		backup.rmdir()
		raise
	shutil.rmtree(backup)


#============================================
def build_document(document: sheetlesson.model.Document, destination: pathlib.Path,
	formats: str = "all") -> pathlib.Path:
	"""Verify every requested format before publishing any of them."""
	if document.has_errors:
		raise ValueError("Validation errors prevent artifact publication.")
	requested = FORMATS[formats]
	inputs = [document.path, *document.assets]
	if document.path.read_text(encoding="utf-8") != document.source:
		raise ValueError("Source changed after compilation; retry the build.")
	report = validation_report(document)
	destination = pathlib.Path(destination).absolute()
	check_destination(destination, inputs)
	destination.parent.mkdir(parents=True, exist_ok=True)
	with tempfile.TemporaryDirectory(prefix=".tutorial-stage-", dir=destination.parent) as temporary:
		staging = pathlib.Path(temporary) / "bundle"
		staging.mkdir()
		stem = document.path.stem
		if "docx" in requested:
			docx_path = staging / f"{stem}.docx"
			run_stage("DOCX rendering", sheetlesson.docx_renderer.write_document, document, docx_path)
			run_stage("DOCX package verification", verify_docx, docx_path)
		if "xlsx" in requested:
			workbook_path = staging / f"{stem}.xlsx"
			run_stage("XLSX rendering", sheetlesson.workbook.write_workbook, document, workbook_path)
			run_stage("XLSX verification", sheetlesson.workbook.verify_workbook, document, workbook_path)
		if "pdf" in requested:
			run_stage("LibreOffice PDF conversion", sheetlesson.pdf_export.export_pdf,
				staging / f"{stem}.docx", staging / f"{stem}.pdf")
		for extension in requested:
			path = staging / f"{stem}.{extension}"
			if not path.is_file() or path.stat().st_size == 0:
				raise RuntimeError(f"Exporter produced no {extension.upper()} artifact.")
			report["outputs"][path.name] = {
				"sha256": fingerprint(path), "status": "generated",
				"verification": "serialized values and types" if extension == "xlsx"
				else "conversion and PDF page-tree parse" if extension == "pdf"
				else "ZIP integrity and document/relationship XML parse",
			}
		(staging / "validation.json").write_text(
			json.dumps(report, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
		)
		# Recheck after rendering so edits made while building cannot be overwritten.
		check_destination(destination, inputs)
		for source in report["assets"] + [report["source"]]:
			if fingerprint(pathlib.Path(source["path"])) != source["sha256"]:
				raise ValueError(f"Input changed while building: {source['path']}; retry the build.")
		publish(staging, destination)
	return destination
