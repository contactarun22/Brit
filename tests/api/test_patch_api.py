# File: test_patch_api.py
# Author: Arun S (GitHub: contactarun22)
# Description: This file is to test the PATCH functionality.
# Currently the resource id 7 is a reserved id and the data object of it cannot be overridden.
# Hence, we will get 405 for all the test cases that we are going to make a call.

import requests
import pytest
import logging

BASE_URL = "https://api.restful-api.dev/objects/7"

# Configure logging
logging.basicConfig(level=logging.INFO)


@pytest.mark.api
def test_initial_response():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    initial_data = response.json()
    logging.info("Initial Response: %s", initial_data)

#TODO: Currently the resource id 7 is a reserved id and the data object of it cannot be overridden.
# Hence, we will get 405 for all the test cases that we are going to make a call.
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
