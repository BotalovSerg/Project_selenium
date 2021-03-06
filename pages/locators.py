from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_FORM_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_FORM_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_REG = (By.CSS_SELECTOR, 'button[value="Register"]')


class ProductPageLocators:
    BTN_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    NAME_BOOK_1 = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    CART_BOOK = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon."
                                  "alert-info.fade.in > div > p:nth-child(1) > strong")
    CART_BOOK_1 = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BTN_CART_HEAD = (By.CSS_SELECTOR, '[href$="basket/"]')
    BASKET_MESSAGE_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner")
    MESSAGE_ITEM_IN_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".alert.alert-success.fade.in")
