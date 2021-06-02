from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_BLANK = (By.CSS_SELECTOR, "input#id_registration-email")
    PASSWORD_BLANK1 = (By.CSS_SELECTOR, "id_registration-password1")
    PASSWORD_BLANK2 = (By.CSS_SELECTOR, "input#id_registration-password2")

class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "[value = 'Добавить в корзину']")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_ABOUT_BASKET_EMPTY = (By.CSS_SELECTOR, "div#content_inner p")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#logiv_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")