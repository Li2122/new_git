import pytest
from actions.order_actions import OrderActions
from data.config import scooter_url
from data.data_order import OrderData
from pages.order_page import OrderPage
from selenium import webdriver


# фикстура для инициализации браузера
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(scooter_url)  # Исп. Урлы вынести в отдельный модуль с данными
    yield driver
    driver.quit()


# фикстура для заполнения обязательных полей, кроме телефона, на первой странице
@pytest.fixture
def full_fields_except_phone_number(browser):
    order = OrderPage(browser)
    order.click_button_order()
    order.input_name(OrderData.first_name)
    order.input_last_name(OrderData.last_name)
    order.input_address(OrderData.address)
    order.select_metro_station()
    yield browser
    order.click_button_further()


# фикстура для заполнения обязательных полей, кроме фамилии, на первой странице
@pytest.fixture
def full_fields_except_lastname(browser):
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
    order = OrderActions()
    response = order.create_order(
        OrderData.first_name, OrderData.last_name, OrderData.address, OrderData.metro_station,
        OrderData.phone, OrderData.rent_time, OrderData.delivery_date, OrderData.comment,
        OrderData.color
    )
    res_json = response.json()
    return res_json['track']
