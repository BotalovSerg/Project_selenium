from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def checkout_there_are_no_items_in_the_cart(self):
        assert self.is_element_present(*BasePageLocators.BASKET_MESSAGE_IS_EMPTY), "No message that cart is empty"

    def checking_that_the_product_was_not_added_to_the_cart(self):
        assert self.is_not_element_present(*BasePageLocators.MESSAGE_ITEM_IN_CART), "The item is in the cart"
