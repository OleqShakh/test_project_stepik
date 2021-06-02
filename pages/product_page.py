from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()


    def should_be_added(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name in message, "No product name in the message"

    def should_be_message_about_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in message_basket_total, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Success message is not presented"