import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
from POM.searchresult_page import flight_list

class Login:
    # textbox_username_id = "Email"
    # textbox_password_id = "Password"
    # button_Login_xpath = "//button[text() = 'Log in']"
    # link_Logout = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def from_source(self, from_source):
        self.driver.find_element(By.ID, "search-form_origin").send_keys(from_source)
        self.driver.find_element(By.XPATH, "//span[text()='New1 Goa Manohar International Airport']").click()

    def to_destination(self, to_dest):
        self.driver.find_element(By.ID, "search-form_destination").send_keys(to_dest)
        self.driver.find_element(By.XPATH, "//span[text()='Chennai International Airport']").click()

    def date_select(self, driver):
        today = str(date.today())
        curr_date = today[-2:].lstrip('0')
        xpath_str = "//input[@value='"+curr_date+"']"
        self.driver.find_element(By.XPATH, xpath_str).click()

    def click_search(self,driver):
        self.driver.find_element(By.XPATH, "//button[@type = 'submit']").click()





