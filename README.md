# Smart Fuel — Allocation API Tests

This repository contains pytest-based tests for the fictional Smart Fuel Allocation API. The test suite demonstrates typical API test patterns and can be run locally with Python and pytest.

NOTE: To modify the server responses, I would need to update them on the Postman Mock Server.

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

## Summary of Approach and Findings

-- Approach
The approach chosen for this exercise was to use Postman to create mock API server for the purposes of simulating responses that would come from a "real API". Two basic responses were used. Using the example request provided, a simple modification of the request to change the "station_id" to distinguish between the requests and expected responses.

I used the requests library to hit the endpoint with appropriate "POST" format. I then parsed json response and passed the response into functions I created to validate against the acceptance criteria.

Some items required further details to determine proper test methods. For example: What are the requirements for verifying tank levels? What are the thresholds for the delivery constraints? How do you determine cost optimization with the given data? For these items I added a "#TODO" tag along with a brief note for further work to be done in those areas.

There are many ways to structure the tests. I chose to create two(2) tests that called the existing methods to minimize redundancy in my code. Additional cleanup and refactoring may be necessary to optimize my current approach, but this is what I followed for the sake of time contraints.

Comments were added to the code to describe the functions. In addition, the acceptance criteria was also added to the related comments for ease of traceability.

Future API testing considerations:
 - Clean up formatting
 - Create a spreadsheet/datatable to run through the various scenarios
 - Create a JSON request template to pass the datatable information into to format each request for submission


-- Findings
Based on the acceptance criteria, there are some items that don't necessarily align it the test data provided:
1) In the example request body and successful response provided, the "demand_Unit" was listed as "liters" in the request, but the response had "gallons". I would yield a failure based on the acceptance criteria.
2) There are other factors that are not clear. For example, the tank_level_percent is a percentage, but is the tank_level_threshold does not appear to be. Even though it is east to assume, it would be go to verify that any calculations done on these fields are accurate and properly formatted.
3) The API Outputs (Response Fields) lists "notes (string): Additional notes or explanations", but no example is provided in the examples of what the "notes" field should look like. It would appear that the "fallback" field could be the intended area for testing, but this also should not be assumed. It is possible that the field is missing in the response or was incorrectly named by the developer or in the requirements.
4) I would recommend doing both positive and negative testing of the scenarios. Boundary tests are also recommendd for to verify that the values accepted by and returned from the API fall within an appropriate range.