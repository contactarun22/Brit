# conftest.py

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,  # Set the default value to False
        help="Run tests in headless mode by default."
    )
