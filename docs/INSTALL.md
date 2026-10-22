# Install

The converter runs on Python 3 with the packages in `pip_requirements.txt`. The default build also
uses LibreOffice Writer to export PDF; the `docx,xlsx` build does not need LibreOffice.

## macOS setup

Install the repository's Homebrew dependencies, LibreOffice, and Python packages:

```bash
brew bundle
brew install --cask libreoffice
python3 -m pip install -r pip_requirements.txt
```

For other systems, install Python 3, LibreOffice, and the same Python requirements with that
system's package tools. Keep LibreOffice available on `PATH` for PDF builds.

On this macOS host, agents must invoke the build command that calls the project's LibreOffice
conversion wrapper with `sandbox_permissions="require_escalated"`. LibreOffice must run outside
the agent sandbox. Commands run directly in a human terminal use the ordinary command shown in
[USAGE.md](USAGE.md).

Before running a repository command, load the shell environment:

```bash
source source_me.sh
```

See [USAGE.md](USAGE.md) for lint, build, and import commands. See
[AUTHORING_GUIDE.md](AUTHORING_GUIDE.md) for the Markdown format.
