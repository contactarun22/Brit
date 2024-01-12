# webdriver.py

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

def get_driver():
    # Set up the WebDriver (GeckoDriver in this case for Firefox)
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    return driver
