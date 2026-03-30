from data.locators import Locators
from pages.base_page import BasePage
from selenium.common import TimeoutException


class OrderStatus(BasePage):

    def click_button_order_status(self):
        self.click(Locators.button_order_status_on_header)

    def input_order_number(self, number):
        self.send_keys(Locators.input_order_number, number)

    def click_button_go(self):
        self.click(Locators.button_go)

    def check_text_scooter_on_warehouse(self):
        try:
            self.find_element(Locators.text_scooter_on_warehouse)
            return True
        except TimeoutException:
            return False

    def check_text_unreal_order(self):
        try:
            self.find_element(Locators.pic_not_found)
            return True
        except TimeoutException:
            return False
