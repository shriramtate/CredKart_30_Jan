
import pytest
import selenium
from selenium.webdriver.common.by import By


class Login_page_class:
    text_email_id = "email"
    text_password_id = "password"
    click_login_register_button_Xpath = "//button[@type='submit']"
    click_menu_button_Xpath = "//a[@role='button']"
    click_logout_button_Xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver=driver

    def enter_email_id(self, email):
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def enter_password_id(self, password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def click_login_button_Xpath(self):
        self.driver.find_element(By.ID, self.click_login_register_button_Xpath).click()

    def click_menu_button_Xpath(self):
        self.driver.find_element(By.ID, self.click_menu_button_Xpath).click()

    def click_logout_button_Xpath(self):
        self.driver.find_element(By.ID, self.click_logout_button_Xpath).click()



