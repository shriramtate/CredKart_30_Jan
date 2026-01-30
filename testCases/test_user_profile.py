import pytest

from pageObjects.Login_page import Login_page_class


@pytest.mark.usefixtures("browser_setup")
class Test_user_profile:
    driver=None

    def test_verifty_url_001(self):
        self.driver.get("https://automation.credence.in/")
        if self.driver.title == "CredKart":
            print(f"driver.title --> {self.driver.title}")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_Credkart_url_001_pass.png")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_verify_Credkart_url_001_fail.png")
            assert False

    def test_login_002(self):
        self.driver.get("https://automation.credence.in/login")
        mail_id = "Credencetest@test.com"
        pass_word = "Credence@123"
        self.lp=Login_page_class(self.driver)
        self.lp.enter_email_id(mail_id)
        self.lp.enter_password_id()
        self.lp.click_menu_button_Xpath
        self.lp.click_logout_button_Xpath()
        if self.


