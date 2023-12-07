import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date


class flight_list:

    def __init__(self, driver):
        self.driver = driver

    def select_stops(self, driver):
        self.driver.find_element(By.XPATH, "//span[text()='1 Stop (s)']").click()

    def select_refund(self, driver):
        self.driver.find_element(By.XPATH, "(//span[text()='Refundable'])[1]").click()

    def select_airline(self, driver):
        self.driver.find_element(By.XPATH, "// span[text() = 'Air India']").click()

    def check_result(self, driver):
        flight_names = self.driver.find_elements(By.XPATH, "//div[@class='airline-name']")
        for n in flight_names:
            if n.text == "Air India":
                continue
            else:
                print("Search result is not correct")

    def select_flight(self, driver):
        self.driver.find_element(By.XPATH, "(//button[text()='Choose'])[1]").click()
