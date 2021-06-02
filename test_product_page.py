import time
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest
from selenium.webdriver.common.by import By



# product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
#
#
# @pytest.mark.parametrize('link', urls)


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.solve_quiz_and_get_code()
    page.should_be_added()
    page.should_be_message_about_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    assert page.is_not_element_present(By.CSS_SELECTOR, "div.alertinner"), "Can see the message after basket"


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(By.CSS_SELECTOR, "div.alertinner"), "Can see the message"


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    time.sleep(1)
    assert page.is_disappeared(By.CSS_SELECTOR, "div.alertinner"), "message is not disappeared"


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review #зафейлится, если корзина не будет пуста на ваше странице
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    assert page.is_not_element_present(By.CSS_SELECTOR, "div.product_main h1"), "Корзина не пуста"
    assert page.is_element_present(By.CSS_SELECTOR, "div#content_inner p"), "Нет сообщения о пустой корзине"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.browser  = browser
        page = LoginPage(self.browser, self.link)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", "parolsuka123")
        page.should_be_authorized_user()
        time.sleep(3)

    def test_reg1(self):
        page = LoginPage(self.browser, self.link)
        page.register_new_user(str(time.time()) + "@fakemail.org", "parolsuka123")
        page.should_be_authorized_user()
        time.sleep(3)

    # def test_user_can_go_to_login_page_from_product_page(browser):
    #     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #     page = ProductPage(browser, link)
    #     page.open()
    #     page.go_to_login_page()
    #
    # def test_user_cant_see_product_in_basket_opened_from_product_page(browser):
    #     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    #     page = ProductPage(browser, link)
    #     page.open()
    #     page.go_to_basket_page()
    #     assert page.is_not_element_present(By.CSS_SELECTOR, "div.product_main h1"), "Корзина не пуста"
    #     assert page.is_element_present(By.CSS_SELECTOR, "div#content_inner p"), "Нет сообщения о пустой корзине"