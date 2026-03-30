import random

from data.locators import Locators
from helpers.data_generation import DataGeneration
from helpers.date import Date
from pages.base_page import BasePage
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):

    def click_button_order(self):
        self.click(Locators.button_order_on_header)

    def input_name(self, name):
        self.send_keys(Locators.input_name, name)

    def input_last_name(self, lastname):
        self.send_keys(Locators.input_last_name, lastname)

    def input_address(self, address):
        self.send_keys(Locators.input_address, address)

    def select_metro_station(self):
        # кликаем по полю
        self.click(Locators.input_metro)
        # находим все элементы по общему классу(в локаторе)
        metro_station_el = self.find_element(Locators.dropdown_list_metro)
        list_station = metro_station_el.text.split('\n')
        locator_metro_station_name = (
            By.XPATH,
            f"//li[@class='select-search__row']//div[text()='{random.choice(list_station)}']")
        # переходим к выбранному элементу
        self.move_to_element(locator_metro_station_name)
        self.click(locator_metro_station_name)

    def input_phone(self):
        self.send_keys(Locators.input_phone, DataGeneration.generation_phone())

    def click_button_further(self):
        self.click(Locators.button_further)

    def input_date(self):
        self.send_keys(Locators.input_date, Date.generation_date() + Keys.ENTER)

    def select_term_station(self):
        self.click(Locators.input_term)
        terms = self.find_element(Locators.dropdown_list_terms)
        list_terms = terms.text.split('\n')
        locator_term = (By.XPATH, f"//div[@class='Dropdown-option'][text()='{random.choice(list_terms)}']")
        self.click(locator_term)

    def click_checkbox_color(self):
        self.click(random.choice((Locators.checkbox_black, Locators.checkbox_grey)))

    def input_comment(self, comment):
        self.send_keys(Locators.input_comment, comment)

    def click_button_in_list(self):
        self.click(Locators.button_order_in_list)

    def check_text_in_modal_window(self) -> bool:
        try:
            self.find_element(Locators.text_in_modal_window_to_order)
            return True
        except TimeoutException:
            return False

    def check_text_error_in_lastname(self) -> bool:
        try:
            self.find_element(Locators.text_error_in_lastname)
            return True
        except TimeoutException:
            return False

    def input_phone_invalid_data(self, number):
        self.send_keys(Locators.input_phone, number)

    def check_text_error_in_phone(self) -> bool:
        try:
            self.find_element(Locators.text_error_in_phone)
            return True
        except TimeoutException:
            return False

    def check_header_second_page_order(self) -> bool:
        try:
            self.find_element(Locators.text_header_second_page_order)
            return True
        except TimeoutException:
            return False
