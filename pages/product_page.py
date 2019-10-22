from .base_page import BasePage
from .locators import ProductPageLocators
import time
import re


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_added_product_notifications_and_price(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name.text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product_price.text
        product_price = re.search(r"\d+(\.\d+)*", product_price).group(0)
        assert self.is_element_contains_text(*ProductPageLocators.ADDED_PRODUCT_NOTIFICATION, product_name)
        assert self.is_element_contains_text(*ProductPageLocators.BENEFIT_NOTIFICATION, "Deferred benefit offer")
        assert self.is_element_contains_price(*ProductPageLocators.NOTIFICATION_PRICE, product_price)
        assert self.is_element_contains_price(*ProductPageLocators.BASKET_TOTAL_PRICE, product_price)
        time.sleep(1)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
