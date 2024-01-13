# conftest.py

import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=True,  # Set the default value to False
        help="Run tests in headless mode by default."
    )

def pytest_configure(config):
    config._metadata["Project Name"] = "Your Project Name"
    config._metadata["Test Environment"] = "Your Test Environment"

# This hook is used to configure HTML report options
def pytest_configure(config):
    config.option.htmlpath = "reports/report.html"

# Add the following hook to include additional metadata in the HTML report
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Plugins-Version", None)
    metadata["Custom Metadata"] = "Your custom metadata value"