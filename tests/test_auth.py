import time

from selene.api import *
from pages.locators import LoginPageLocators, MainPageLocators


class PaymentButtonError(AssertionError):
    """Кнопка 'Оплата' - не найдена"""


def test_auth(url, login, password):
    browser.open(url).driver.maximize_window()
    browser.element(LoginPageLocators.input_login).type(login)
    browser.element(LoginPageLocators.input_password).type(password)
    browser.element(LoginPageLocators.button_submit).click()
    browser.element(MainPageLocators.header_wrapper).should(be.visible)
    try:
        browser.element(MainPageLocators.sidebar_menu_payment_button).should(have.text('Оплата'))
    except AssertionError:
        raise PaymentButtonError
    time.sleep(0)
