# File: test_landing_page.py
# Author: Arun S (GitHub: contactarun22)
# Description: This file is to test the BRIT landing page.

import pytest
import logging
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.webdriver import get_driver
from .locators import BritInsuranceLocators  # Import the locator class

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

# Log the start of the test session
logging.info("Test session started.")

# Global variable to store search results dictionary
search_results_dict = {}

def capture_screenshot(driver, name):
    """Capture a screenshot and save it with the given name."""
    screenshot_file = f"screenshot_{name}_{timestamp}.png"
    driver.save_screenshot(screenshot_file)
    logging.info(f"Screenshot captured: {screenshot_file}")

@pytest.fixture(scope="module")
def driver(request):
    headless_option = request.config.getoption("--headless")
    driver = get_driver(headless=headless_option)
    yield driver
    driver.quit()

@pytest.mark.dependency(name="test_open_landing_page")
@pytest.mark.smoke
@pytest.mark.ui
def test_open_landing_page(driver):
    # Log test case start
    logging.info("Running test_open_landing_page")

    url = "https://www.britinsurance.com/"
    driver.get(url)

    # Capture screenshot after opening the landing page
    capture_screenshot(driver, "landing_page")

    try:
        # Wait for the "Allow All Cookies" button to be clickable using the locator
        allow_cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, BritInsuranceLocators.ALLOW_COOKIES_BUTTON))
        )

        # Scroll into view in case the button is not visible
        driver.execute_script("arguments[0].scrollIntoView(true);", allow_cookies_button)

        # Click the "Allow All Cookies" button
        allow_cookies_button.click()

        # Log a message indicating that the button has been clicked
        logging.info("Clicked the 'Allow All Cookies' button.")

        # Check if the page title matches the expected title
        expected_title = "Brit Insurance"
        if expected_title not in driver.title:
            # Capture screenshot on failure
            capture_screenshot(driver, "landing_page_failure")
            # Log the failure along with the actual page title
            actual_title = driver.title
            logging.error(
                f"Expected title: '{expected_title}' not found in the page title. Actual title: '{actual_title}'")
            pytest.fail(
                f"Expected title: '{expected_title}' not found in the page title. Actual title: '{actual_title}'")

    except Exception as e:
        # Capture screenshot on failure
        capture_screenshot(driver, "landing_page_exception")
        pytest.fail(f"Test failed: {str(e)}")

@pytest.mark.dependency(name="test_click_search_button", depends=["test_open_landing_page"])
@pytest.mark.ui
def test_click_search_button(driver):
    # Log test case start
    logging.info("Running test_click_search_button")

    try:
        # Add a wait before locating the element (adjust the time as needed)
        time.sleep(5)  # Wait for 3 seconds before locating the element

        search_button_locator = BritInsuranceLocators.NAV_SEARCH_BUTTON

        # Find the search button and then click
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, search_button_locator))
        )

        # Capture screenshot before clicking the search button
        capture_screenshot(driver, "before_search_button_click")

        # Click the search button
        search_button.click()

        # Log successful click on the element
        logging.info("Successfully clicked on the element.")

        # Log successful click on the search button
        logging.info("Successfully clicked on the search button.")

        # Capture screenshot after clicking the search button
        capture_screenshot(driver, "after_search_button_click")

        # Add a wait before clicking the element (if needed, adjust the time as needed)
        time.sleep(5)  # Wait for 20 seconds before clicking the element

        search_input_locator = BritInsuranceLocators.SEARCH_INPUT_FIELD

        # Find the search button and then click
        input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, search_input_locator))
        )

        # Type 'IPSF 34' into the input element
        input_element.send_keys('IFRS 17')

        # Capture screenshot after entering text into the input element
        capture_screenshot(driver, "after_entering_text")

        # Log successful input and submission
        logging.info("Successfully entered 'IFRS 17'")

        time.sleep(10)

        # Locate the search results container
        search_results_container_selector = BritInsuranceLocators.CONTAINER
        search_results_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, search_results_container_selector))
        )

        # Locate individual search result items within the container
        search_results_selector = BritInsuranceLocators.INDIVIDUAL_RESULT
        search_results = WebDriverWait(search_results_container, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, search_results_selector))
        )

        # Create a dictionary to store the search results
        global search_results_dict
        search_results_dict = {}

        # Iterate through each search result and capture the text
        for index, result in enumerate(search_results, start=1):
            result_text = result.text.strip()
            search_results_dict[f"Result_{index}"] = result_text

        # Log the dictionary
        logging.info("Search Results Dictionary:")
        logging.info(search_results_dict)

        # Log additional information for debugging
        logging.info("Number of Results: %d", len(search_results))
        logging.info("Number of Items in Dictionary: %d", len(search_results_dict))
        logging.info("Is Dictionary Empty? %s", not bool(search_results_dict))

    except Exception as e:
        # Capture screenshot on failure
        capture_screenshot(driver, "search_button_exception")
        pytest.fail(f"Test failed: {str(e)}")

@pytest.mark.dependency(name="test_search_result_contains_expected_text", depends=["test_click_search_button"])
@pytest.mark.ui
def test_search_result_contains_expected_text(driver):
    # Log test case start
    logging.info("Running test_search_result_contains_expected_text")

    try:
        # Assert that the expected text is present in the search results
        expected_text = "Interim results for the six months ended 30 June 2022"
        assert any(expected_text in result_text for result_text in search_results_dict.values()),\
            "Expected text '{expected_text}' not found in search results"

    except Exception as e:
        # Capture screenshot on failure
        capture_screenshot(driver, "search_button_exception")
        pytest.fail(f"Test failed: {str(e)}")