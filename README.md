# Smart Fuel — Allocation API Tests

This repository contains pytest-based tests for the fictional Smart Fuel Allocation API. The test suite demonstrates typical API test patterns and can be run locally with Python and pytest.

## Contents

- `data/` — example request/response JSON files used by tests
- `tests/` — pytest test files (currently `test_sfaapi.py`)
- `pyproject.toml` — project metadata and test dependencies

## Prerequisites

- Python 3.8+ (recommend 3.10 or newer)
- Git (optional)
- A POSIX-like shell or PowerShell (instructions below use PowerShell on Windows)

This project uses standard pytest for running tests. No external services are required to run the included tests.

## Recommended setup (using venv + pip)

1. Open PowerShell and create a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies from `pyproject.toml`. If you use pip directly, you can install pytest:

```powershell
python -m pip install --upgrade pip
pip install pytest
```

If you prefer Poetry (project includes `pyproject.toml`), see the Poetry section below.

## Optional: setup with Poetry

If you use Poetry to manage the project, install Poetry first (https://python-poetry.org). Then from the project root:

```powershell
poetry install
poetry shell
```

Poetry will create an isolated environment and install dependencies defined in `pyproject.toml`.

## Running tests

From the project root (where `pyproject.toml` is located) run pytest.

PowerShell example:

```powershell
# Run all tests
pytest

# Run a single test file
pytest tests/test_sfaapi.py

# Run a specific test by nodeid
pytest tests/test_sfaapi.py::test_some_function
```

Common pytest flags:

- `-v` verbose
- `-s` show print output
- `--maxfail=1` stop after first failure
- `-k <expr>` run tests that match the expression

## Running tests in VS Code

1. Open the folder in VS Code.
2. Install the Python extension.
3. Select the interpreter from `.venv` (or Poetry environment).
4. Use the Test Explorer or run pytest from the integrated terminal.

## Troubleshooting

- "pytest: command not found" — ensure virtual environment is activated or use `python -m pytest`.
- Dependency errors — install pytest into the active environment: `pip install pytest` or use `poetry install`.
- If PowerShell blocks script execution when activating venv, you may need to set the execution policy (run PowerShell as admin):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Example: quick smoke test

1. Activate the virtualenv (see above).
2. Run `pytest -q` and expect output like `1 passed` (or tests failing if issues exist):

```powershell
pytest -q
```

## Contact

Paul Smith — paul_a_smith_1974@yahoo.com

## License and Status

Private repository. For private/internal use only. Project status: under development.

---
Last updated: 2025-10-21