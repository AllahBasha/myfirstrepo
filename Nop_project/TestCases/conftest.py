import pytest
import openpyxl
from selenium import webdriver

url_link = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get(url_link)
    return driver

