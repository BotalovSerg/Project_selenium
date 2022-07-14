from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def checkout_there_are_no_items_in_the_cart(self):
        assert self.is_element_present(*BasePageLocators.BASKET_MESSAGE_IS_EMPTY), "No message that cart is empty"
