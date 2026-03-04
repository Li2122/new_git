import pytest

from data.data_order import OrderData
from pages.order_page import OrderPage
from pages.order_status_page import OrderStatus


class TestOrderCreation:
    def test_order_creation_all_fields(self, browser):
        order = OrderPage(browser)
        order.click_button_order()
        order.input_name(OrderData.first_name)
        order.input_last_name(OrderData.last_name)
        order.input_address(OrderData.address)
        order.select_metro_station()
        order.input_phone()
        order.click_button_further()
        order.input_date()
        order.select_term_station()
        order.click_checkbox_color()
        order.input_comment(OrderData.comment)
        order.click_button_in_list()
        assert order.check_text_in_modal_window(), "Модальное окно не отобразилось"

    def test_order_creation_without_lastname(self, browser, full_fields_except_lastname):
        order = OrderPage(browser)
        assert order.check_text_error_in_lastname(), "Не отобразилась ошибка при не заполнении фамилии"


class TestPhoneNumber:
    @pytest.mark.parametrize("number", [
        "", 1234567890, 12345678901234
    ])
    def test_phone_number_invalid_data(self, browser, full_fields_except_phone_number, number):
        order = OrderPage(browser)
        order.input_phone_invalid_data(number)
        assert order.check_text_error_in_phone(), \
            "Не отобразилась ошибка при заполнении телефона недопустимым значением"

    def test_phone_number_limit_valid_data(self, browser, full_fields_except_phone_number):
        order = OrderPage(browser)
        order.input_phone()
        assert order.check_header_second_page_order, "Не произошел переход на вторую страницу создания заказа"


class TestOrderStatusCheck:
    def test_order_status_check(self, browser, create_order):
        order_status = OrderStatus(browser)
        order_status.click_button_order_status()
        order_status.input_order_number(create_order)
        order_status.click_button_go()
        assert order_status.check_text_scooter_on_warehouse(), "Поле не отобразилось"

    def test_status_unreal_order(self, browser):
        order_status = OrderStatus(browser)
        order_status.click_button_order_status()
        order_status.input_order_number(OrderData.unreal_order)
        order_status.click_button_go()
