# File: test_landing_page.py
# Author: Arun S (GitHub: contactarun22)
# Description: This file is to test the BRIT landing page.

import requests
import pytest
import logging
from datetime import datetime

BASE_URL = "https://api.restful-api.dev/objects/7"

# Generate timestamp for log file name
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"test_log_{timestamp}.log"

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Add a file handler for logging to a file with the dynamic name
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_handler)


@pytest.mark.api
def test_initial_response():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    initial_data = response.json()
    logging.info("Initial Response: %s", initial_data)


@pytest.mark.api
@pytest.mark.parametrize("update_data, expected_status_code", [
    ({"name": "Updated Name"}, 405),  # Example 1: Trying to update name
    ({"data": {"price": 2000}}, 405),  # Example 2: Trying to update price
    ({"data": {"year": 2022}}, 405),  # Example 3: Trying to update year
    ({"data": {"new_field": "New Field"}}, 405),  # Example 4: Trying to add a new field
    ({"name": "", "data": {"price": 1500}}, 405),  # Example 5: Trying to set name to empty
    ({"data": {"price": "invalid_price"}}, 405),  # Example 6: Trying to set an invalid price
    ({"name": "New Name", "data": {"new_field": "New Field"}}, 405),  # Example 7: Updating name and adding a new field
    ({}, 405),  # Example 8: Trying to send an empty update
    ({"non_existent_field": "Value"}, 405),  # Example 9: Trying to update a non-existent field
    ({"name": "Updated Name", "data": {"price": 2000, "new_field": "New Field"}}, 405),
    # Example 10: Updating multiple fields
    ({"id": 8}, 405),  # Example 11: Trying to update the ID (should be ignored)
    ({"data": {"year": "Two thousand twenty-two"}}, 405),  # Example 12: Trying to set a non-integer year
    ({"data": {"price": -100}}, 405),  # Example 13: Trying to set a negative price
    ({"name": None}, 405),  # Example 14: Trying to set name to None
    ({"data": {"price": 2000, "extra_field": "Extra Field"}}, 405)  # Example 15: Updating with an unrecognized field
])
def test_patch_scenarios(update_data, expected_status_code):
    headers = {"Content-Type": "application/json"}
    response = requests.patch(BASE_URL, json=update_data, headers=headers)

    logging.info("PATCH Request for %s - Response Code: %s", update_data, response.status_code)
    assert response.status_code == expected_status_code
