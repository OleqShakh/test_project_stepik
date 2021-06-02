import time


import pytest
from selenium.webdriver.common.by import By

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        # page.go_to_login_page()
        # page.should_be_login_link()
        # page1 = LoginPage(browser, link)
        # page1.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        assert self.BasePage.is_element_present(By.CSS_SELECTOR, "#login_link")


@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_in_basket()
    page.message_should_be_in_basket()


def test_register(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user(str(time.time()) + "@fakemail.org", "parolsuka123")
    page.should_be_authorized_user()
    time.sleep(3)
