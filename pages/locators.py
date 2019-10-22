from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_FORM_EMAIL = (By.XPATH, "//input[contains(@id, 'id_registration') and contains(@id, 'email')]")
    REGISTER_FORM_PASSWORD_1 = (By.XPATH, "//input[contains(@id, 'id_registration') and contains(@id, 'password1')]")
    REGISTER_FORM_PASSWORD_2 = (By.XPATH, "//input[contains(@id, 'id_registration') and contains(@id, 'password2')]")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ADDED_PRODUCT_NOTIFICATION = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div.alertinner strong")
    BENEFIT_NOTIFICATION = (By.CSS_SELECTOR, "div.alert:nth-child(2) > div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    NOTIFICATION_PRICE = (By.CSS_SELECTOR, "div.alert:nth-child(3) > div.alertinner strong")
    BASKET_TOTAL_PRICE = (By.CLASS_NAME, "basket-mini")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alertinner ' and contains(string(), 'has been added to your basket')]")


class BasketPageLocators:
    SHOPPING_LINK = (By.LINK_TEXT, "Continue shopping")
    EMPTY_BASKET_TEXT = (By.XPATH, "//p[contains(text(), 'Your basket is empty')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, r"div.basket\-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, r"div.basket\-mini a.btn")
