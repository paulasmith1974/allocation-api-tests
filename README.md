1. Project Title and Description:
This is a test repository for a fictional project called Smart Fuel Allocation API.
The purpose is to demonstrate various python test methods that can be executed to test the fictional API.

2. Table of Contents:
N/A

3. Installation Instructions:
Detailed steps on how to set up and install the project locally, including any prerequisites, dependencies, or configuration steps.

4. Usage Instructions:
These instructions are specific to vscode, so behavior may vary a little depending on the Operating System and the Code Editor of choice:
Here are instructions for running pytest from the command line with various options: 
    1. Basic Execution: 
    run all tests. 
        pytest

    Run tests in a specific file. 
        pytest test_filename.py

    Run tests in a specific directory. 
        pytest path/to/directory/

    2. Selecting Specific Tests: 

    • Run a specific test function within a module: 

        pytest test_module.py::test_function

    • Run a specific test method within a class: 

        pytest test_module.py::TestClass::test_method

    Run tests matching a keyword expression. 
        pytest -k "MyClass and not method"

    (Runs tests with "MyClass" in their name but not "method".) 

    • Run tests marked with a specific marker: 

        pytest -m slow

    (Runs tests decorated with @pytest.mark.slow.) 
    3. Output and Debugging Options: 

    • Show verbose output (more details on test execution): 

        pytest -v

    • Show local variables in tracebacks for failed tests: 

        pytest --showlocals

    or 
        pytest -l

    Enter the debugger on test failure. 
        pytest --pdb

    • Show output from print statements in tests: 

        pytest -s

    4. Running Failed Tests: 

    • Run only the tests that failed in the previous run: 

        pytest --lf

    • Run failed tests first, then the rest: 

        pytest --ff

    5. Configuration: 

    • Set default command-line options in pytest.ini: 

    Create a pytest.ini file in your project root and add options under [pytest] like: 
        [pytest]
        addopts = -v --showlocals

5. Contribution Guidelines:
N/A

6. License Information:
For private use only. This project is not meant to be public

7. Credits and Acknowledgments:
python
pytest
pytest-mocks
date-time
json
configured for vscode

8. Contact Information:
Paul Smith
email: paul_a_smith_1974@yahoo.com

Optional Sections:

Troubleshooting and FAQs: Common issues and their solutions.
As this is a work in progress, errors may still be found in the code.

Changelog: N/A

Badges: N/A

Project Status: Under development
Last Updated: 2025-10-20