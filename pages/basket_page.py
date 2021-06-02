from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BasketPage(BasePage):
    def should_be_in_basket(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, "div.product_main h1"), "Корзина не пуста"

    def message_should_be_in_basket(self):
        assert self.is_element_present(By.CSS_SELECTOR, "div#content_inner p"), "Нет сообщения о пустой корзине"
