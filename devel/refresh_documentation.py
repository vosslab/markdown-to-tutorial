#!/usr/bin/env python3
"""Rebuild all documentation artifacts and native screenshots; run outside the sandbox."""

# Standard Library
import sys
import pathlib
import subprocess

# Local modules
import tutorial_lib.build
import tutorial_lib.compiler


#============================================
def build(source: pathlib.Path, destination: pathlib.Path) -> None:
	"""Refresh an owned output bundle with the current native renderer styles."""
	print(f"Build documentation artifact: {source.name}", flush=True)
	document = tutorial_lib.compiler.compile_document(source)
	if document.has_errors:
		messages = [item.message for item in document.diagnostics if item.severity == "error"]
		raise ValueError(f"Cannot build {source}: {messages}")
	tutorial_lib.build.build_document(document, destination, "all")


#============================================
def main() -> None:
	"""Run LibreOffice stages sequentially, capturing images before illustrated Part builds."""
	root = pathlib.Path(__file__).resolve().parent.parent
	# Keep canonical outputs current; the build API preserves manually edited bundles.
	for stem in ("caffeine_3_quadratic_regression", "microbes_4_f_test", "microbes_5_anova"):
		build(root / "tutorial_data" / f"{stem}.md", root / "tutorial_output" / stem)
	for script in ("capture_readme_artifacts.py", "capture_syntax_examples.py",
		"capture_authoring_course.py"):
		print(f"Capture documentation: {script}", flush=True)
		# ASVS 1.2.5: executable and script paths remain distinct argv values.
		subprocess.run([sys.executable, str(root / "devel" / script)], cwd=root, check=True)
	for stem in ("PART_1_CREATE", "PART_2_STATISTICS", "PART_3_IMPROVE"):
		build(root / "docs" / "learn" / f"{stem}.md",
			root / "tutorial_output" / "authoring_course" / "parts" / stem)
	print("Documentation artifacts and all screenshot receipts refreshed.", flush=True)


if __name__ == "__main__":
	main()
