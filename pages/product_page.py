from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def item_added_to_cart(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_CART)
        btn.click()
        self.solve_quiz_and_get_code()

    def is_name_book(self):
        title = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        assert title == "The shellcoder's handbook", "Title book does not match"

