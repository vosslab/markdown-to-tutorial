"""Export the generated DOCX through LibreOffice Writer."""

# Standard library
import shutil
import pathlib
import tempfile
import subprocess

# Third-party modules
import pypdf
import pypdf.errors


#============================================
def export_pdf(source: pathlib.Path, destination: pathlib.Path) -> None:
	"""Convert a staged DOCX without sharing the user's LibreOffice profile."""
	executable = shutil.which("libreoffice") or shutil.which("soffice")
	macos_binary = pathlib.Path("/Applications/LibreOffice.app/Contents/MacOS/soffice")
	if executable is None and macos_binary.is_file():
		executable = str(macos_binary)
	if executable is None:
		raise RuntimeError("PDF export requires LibreOffice Writer; install LibreOffice.")
	with tempfile.TemporaryDirectory(prefix="tutorial-writer-") as temporary:
		profile = pathlib.Path(temporary) / "profile"
		command = [
			executable, f"-env:UserInstallation={profile.as_uri()}",
			"--headless", "--convert-to", "pdf:writer_pdf_Export",
			"--outdir", str(destination.parent), str(source),
		]
		result = subprocess.run(command, capture_output=True, text=True, timeout=120)
	if result.returncode != 0:
		raise RuntimeError(
			f"LibreOffice PDF conversion failed ({result.returncode}): "
			f"{result.stderr.strip()} {result.stdout.strip()}"
		)
	if not destination.is_file() or destination.stat().st_size < 5:
		raise RuntimeError(f"LibreOffice produced no PDF: {result.stdout.strip()}")
	with destination.open("rb") as handle:
		header = handle.read(5)
	if header != b"%PDF-":
		raise RuntimeError("LibreOffice output does not have a PDF signature.")
	# A successful process and PDF header do not establish a readable document.
	try:
		reader = pypdf.PdfReader(destination, strict=True)
		page_count = len(reader.pages)
	except pypdf.errors.PdfReadError as error:
		raise RuntimeError(f"LibreOffice produced an unreadable PDF: {error}") from error
	if page_count == 0:
		raise RuntimeError("LibreOffice produced a PDF with no readable pages.")
