
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators, LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self) -> object:
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_link = self.browser.current_url
        assert 'login' in current_link
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not present"
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
        assert True

    def register_new_user(self, email, password):
        email_blank = self.browser.find_element(By.CSS_SELECTOR, "input#id_registration-email")
        email_blank.send_keys(email)
        password_blank1 = self.browser.find_element(By.CSS_SELECTOR, "input#id_registration-password1")
        password_blank1.send_keys(password)
        password_blank2 = self.browser.find_element(By.CSS_SELECTOR, "input#id_registration-password2")
        password_blank2.send_keys(password)
        register_button = self.browser.find_element(By.CSS_SELECTOR, "button[name = registration_submit]")
        register_button.click()

