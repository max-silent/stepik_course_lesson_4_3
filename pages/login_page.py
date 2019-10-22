from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_1)
        password_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_2)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_field.send_keys(email)
        password_field.send_keys(password)
        password_confirm_field.send_keys(password)
        register_button.click()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, '"login" text is missed at the URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missed at the page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is missed at the page"
