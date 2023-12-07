import openpyxl
from selenium import webdriver
import pytest
from POM.home_page import Login
from POM.searchresult_page import flight_list
from POM.userdata_entry_page import user_details
from Utilities import read_excel_data
import time

from Utilities.read_excel_data import excel_data


@pytest.mark.parametrize("from_source, to_dest", excel_data())
class Test_001_flight:
    # @pytest.mark.parametrize("from_source, to_dest", excel_data())
    def test_flight_search(self, from_source, to_dest, browser):
        self.driver = browser
        self.lp = Login(self.driver)
        self.lp.from_source(from_source)
        self.lp.to_destination(to_dest)
        self.lp.date_select(self.driver)
        self.lp.click_search(self.driver)
        # time.sleep(10)

    def test_flight_selection(self, from_source, to_dest, browser):
        self.driver = browser
        self.test_flight_search(from_source, to_dest, self.driver)
        self.lp = flight_list(self.driver)
        self.lp.select_stops(self.driver)
        self.lp.select_refund(self.driver)
        self.lp.select_airline(self.driver)
        self.lp.select_flight(self.driver)
        # time.sleep(20)

    def test_user_details_input(self, from_source, to_dest, browser):
            self.driver = browser
            self.test_flight_selection(from_source, to_dest, self.driver)
            self.lp = user_details(self.driver)
            self.lp.enter_mobile_no(self.driver)
            self.lp.enter_email_add(self.driver)
            self.lp.select_title(self.driver)
            self.lp.enter_firstname(self.driver)
            self.lp.enter_lastname(self.driver)
            self.lp.click_continue(self.driver)
            # time.sleep(10)

