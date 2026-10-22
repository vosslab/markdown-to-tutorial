#!/usr/bin/env python3
"""Compile single-source Markdown tutorials and student workbooks."""

# Standard library
import sys
import pathlib
import argparse

# Local modules
import tutorial_lib.build
import tutorial_lib.compiler
import tutorial_lib.workbook


#============================================
def main(argv: list[str] | None = None) -> int:
	"""Run lint, staged build, or one-time workbook import."""
	parser = argparse.ArgumentParser(description=__doc__)
	commands = parser.add_subparsers(dest="command", required=True)
	lint = commands.add_parser("lint", help="Validate without writing deliverables")
	lint.add_argument("source", type=pathlib.Path)
	build = commands.add_parser("build", help="Generate a verified output bundle")
	build.add_argument("source", type=pathlib.Path)
	build.add_argument("--format", "-f", choices=tutorial_lib.build.FORMATS, default="all")
	build.add_argument("--output-dir", "-o", type=pathlib.Path)
	importer = commands.add_parser("import-xlsx", help="Create a Markdown draft from an XLSX")
	importer.add_argument("source", type=pathlib.Path)
	importer.add_argument("--output", "-o", type=pathlib.Path, required=True)
	args = parser.parse_args(argv)
	if args.command == "import-xlsx":
		if args.output.exists() or args.output.is_symlink():
			raise FileExistsError(f"Import destination already exists: {args.output}")
		draft = tutorial_lib.workbook.import_workbook(args.source)
		with args.output.open("x", encoding="utf-8") as handle:
			handle.write(draft)
		print(f"Wrote draft {args.output}; author the Tutorial scaffold before building.")
		return 0
	document = tutorial_lib.compiler.compile_document(args.source)
	for item in document.diagnostics:
		location = f"{item.span.path}:{item.span.start_line}"
		print(f"{location}: {item.severity} [{item.category}] {item.message}", file=sys.stderr)
		print(f"  Correction: {item.correction}", file=sys.stderr)
	if document.has_errors:
		return 1
	if args.command == "build":
		destination = args.output_dir
		if destination is None:
			destination = pathlib.Path("tutorial_output") / args.source.stem
		published = tutorial_lib.build.build_document(document, destination, args.format)
		print(f"Published {published}")
	else:
		print("Offline lint passed; Google import, navigation, and calculation are unchecked.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
