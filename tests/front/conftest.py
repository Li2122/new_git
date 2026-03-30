import pytest
from selenium import webdriver

from actions.order_actions import OrderActions
from data.config import scooter_url
from data.data_order import OrderData
from pages.home_page import HomePage
from pages.order_page import OrderPage


@pytest.fixture
def browser():
    """Фикстура для инициализации браузера"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(scooter_url)  # Исп. Урлы вынести в отдельный модуль с данными
    yield driver
    driver.quit()


@pytest.fixture
def full_fields_except_phone_number(browser):
    """Фикстура для заполнения обязательных полей, кроме телефона, на первой странице"""
    order = OrderPage(browser)
    order.click_button_order()
    order.input_name(OrderData.first_name)
    order.input_last_name(OrderData.last_name)
    order.input_address(OrderData.address)
    order.select_metro_station()
    yield browser
    order.click_button_further()


@pytest.fixture
def full_fields_except_lastname(browser):
    """Фикстура для заполнения обязательных полей, кроме фамилии, на первой странице"""
    order = OrderPage(browser)
    order.click_button_order()
    order.input_name(OrderData.first_name)
    order.input_address(OrderData.address)
    order.select_metro_station()
    order.input_phone()
    yield browser
    order.click_button_further()


@pytest.fixture
def create_order():
    """Фикстура для создания заказа"""
    order = OrderActions()
    response = order.create_order(
        OrderData.first_name, OrderData.last_name, OrderData.address, OrderData.metro_station,
        OrderData.phone, OrderData.rent_time, OrderData.delivery_date, OrderData.comment,
        OrderData.color
    )
    res_json = response.json()
    return res_json['track']


@pytest.fixture
def agree_with_cookies(browser):
    """Фикстура согласия с куками"""
    home = HomePage(browser)
    home.click_cookie_button()
