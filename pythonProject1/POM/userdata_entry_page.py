import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date


class user_details:

    def __init__(self, driver):
        self.driver = driver

    def enter_mobile_no(self, driver):
        self.driver.find_element(By.XPATH, "//input[@id='contactForm_mobile']").send_keys("98765h3210")
        error = self.driver.find_element(By.XPATH, "//div[@class ='ant-form-item-explain-error']").text
        if error != "":
            assert error

    def enter_email_add(self, driver):
        self.driver.find_element(By.ID, "contactForm_email").send_keys("hhhhh123@gmail.com")

    def select_title(self, driver):
        self.driver.find_element(By.XPATH, "(//span[@class='ant-select-selection-item'])[2]").click()
        self.driver.find_element(By.XPATH, "//div[text()='Ms.']").click()

    def enter_firstname(self, driver):
        self.driver.find_element(By.ID, "passengers_0_FirstName").send_keys("hhhhh1")

    def enter_lastname(self, driver):
        self.driver.find_element(By.ID, "passengers_0_LastName").send_keys("hhhhh1")

    def click_continue(self, driver):
        self.driver.find_element(By.XPATH, "(//button)[3]").click()
