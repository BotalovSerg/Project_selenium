import pytest

from .pages.basket_page import BasketPage
from .pages.locators import BasePageLocators
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        """
        тестовый гость может перейти на страницу входа
        :param browser:
        :return:
        """
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    browser.delete_all_cookies()
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.checkout_there_are_no_items_in_the_cart()
    cart_page.checking_that_the_product_was_not_added_to_the_cart()
    cart_page.pending_element_disappeared()


def test_guest_should_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_should_see_login_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
