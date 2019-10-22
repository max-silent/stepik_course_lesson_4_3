from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_login_page(self):
        self.should_be_basket_url()
        self.should_be_shopping_link()
        self.should_be_empty()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, '"basket" text is missed at the URL'

    def should_be_shopping_link(self):
        assert self.is_element_present(*BasketPageLocators.SHOPPING_LINK), "Continue shopping link is missed at the page"

    def should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Empty basket text is missed at the page"
