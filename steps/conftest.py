import pytest
from selenium import webdriver
from constants.constants import website_url


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.get(website_url)
    driver.maximize_window()

    yield driver
    driver.close()
