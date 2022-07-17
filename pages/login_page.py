from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "not login is url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "FORM Login is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER), "REG_FORM is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        input_email.send_keys(email)
        input_pass_1 = self.browser.find_element(*LoginPageLocators.PASS_FORM_1)
        input_pass_1.send_keys(password)
        input_pass_2 = self.browser.find_element(*LoginPageLocators.PASS_FORM_2)
        input_pass_2.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.BTN_REG)
        btn.click()
