from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def item_added_to_cart(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_CART)
        btn.click()
        # self.solve_quiz_and_get_code()

    def is_name_book(self):
        title = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        title_1 = self.browser.find_element(*ProductPageLocators.NAME_BOOK_1).text
        assert title == title_1, "Title book does not match"

    def is_cart_cost(self):
        cost = self.browser.find_element(*ProductPageLocators.CART_BOOK).text
        cost_1 = self.browser.find_element(*ProductPageLocators.CART_BOOK_1).text
        assert cost == cost_1, "Prices do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def there_should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message gone"
