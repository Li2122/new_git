import pytest
from actions.courier_actions import CourierActions
from actions.order_actions import OrderActions
from data.data_courier import CourierData
from data.data_order import OrderData


# fixture для создания нового заказа
@pytest.fixture
def new_order():
    order = OrderActions()
    response = order.create_order(
        OrderData.first_name, OrderData.last_name, OrderData.address, OrderData.metro_station,
        OrderData.phone, OrderData.rent_time, OrderData.delivery_date, OrderData.comment,
        OrderData.color
    )
    res_json = response.json()
    return res_json


# fixture для получения track созданного заказа
@pytest.fixture
def track_new_order(new_order):
    return new_order['track']


# fixture для получения логин и пароля нового курьера
@pytest.fixture
def create_courier():
    courier = CourierActions()
    login = CourierData.new_login
    password = CourierData.password
    response = courier.create_courier(
        login, password, CourierData.first_name
    )
    return {"login": login, "password": password}


# fixture для получения id курьера
@pytest.fixture
def id_courier(create_courier):
    courier = CourierActions()
    response = courier.auth_courier(create_courier["login"], create_courier["password"])
    return response.json()['id']


@pytest.fixture
def id_order(track_new_order):
    order = OrderActions()
    response = order.get_order(track_new_order)
    return response.order["id"]
