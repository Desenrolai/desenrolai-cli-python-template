# desenrolai-cli-python-template

Template for CLI tools (Python 3.12 + click).

## Stack

- Python 3.12
- `click` — argument parsing
- `pytest` + `click.testing.CliRunner` — tests
- `ruff` — lint/format
- `mypy` — strict type checking

## Structure

```
src/
  __init__.py
  cli.py       # CLI entrypoint — add your commands here
tests/
  __init__.py
  test_cli.py  # example tests
```

## Getting started

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

python -m src.cli hello
python -m src.cli hello --name Desenrolai

pytest tests/ -v
ruff check src/ tests/
mypy src/
```

## Adding commands

Add new `@main.command()` functions to `src/cli.py`.

## Distribution

CLI tools are distributed as packages (`pip install` / `pipx`), not deployed to Kubernetes.
See `forge.yaml`: `deploy: none`.
