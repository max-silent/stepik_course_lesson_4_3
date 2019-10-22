import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.basket_user
class TestBasketByUser:
    """ Tests from lesson 4.3 step 13
    """
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        registration_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, registration_link)
        page.open()
        username = "{}@fakemail.org".format(time.time())
        password = "!@#123qweasdzxc"
        page.register_new_user(username, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.add_to_basket()
        page.should_be_correct_added_product_notifications_and_price()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.basket_guest
class TestBasketByGuest:
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty()

    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.add_to_basket()
        page.should_be_correct_added_product_notifications_and_price()
