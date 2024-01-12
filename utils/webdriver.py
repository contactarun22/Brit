# webdriver.py

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

def get_driver(headless=True):
    # Set up the WebDriver (GeckoDriver in this case for Firefox)
    options = webdriver.FirefoxOptions()
    if headless:
        options.add_argument("--headless")

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    return driver
