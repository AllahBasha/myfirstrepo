from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_Login_xpath = "//button[text() = 'Log in']"
    link_Logout = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, username):
        print(self.driver)
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_Logout).click()
