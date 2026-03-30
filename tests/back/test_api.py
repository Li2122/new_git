from actions.courier_actions import CourierActions
from actions.order_actions import OrderActions
from actions.stations_action import StationsActions
from data.data_courier import CourierData
from data.data_order import OrderData
from data.response_text import CourierErrorText


class TestApiOrder:
    def test_create_order(self):
        order = OrderActions()
        response = order.create_order(
            OrderData.first_name, OrderData.last_name, OrderData.address, OrderData.metro_station,
            OrderData.phone, OrderData.rent_time, OrderData.delivery_date, OrderData.comment,
            OrderData.color
        )
        assert 'track' in response.json()
        assert response.status_code == 201

    # def test_get_orders(self, new_order, track_new_order):
    #     order = OrderActions()
    #     orders = order.get_orders()
    #     assert order.check_order_exist(track_new_order, orders)

    def test_get_order(self, track_new_order):
        order = OrderActions()
        response = order.get_order(track_new_order)
        assert response.order["track"] == track_new_order

    def test_put_order_courier(self, id_order, id_courier):
        order = OrderActions()
        response = order.put_order(id_order, id_courier)
        assert response.status_code == 200
        assert response.json() == {"ok": True}


class TestApiCourier:
    def test_create_courier(self):
        courier = CourierActions()
        response = courier.create_courier(
            CourierData.new_login, CourierData.password, CourierData.first_name
        )
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_login_courier(self, create_courier):
        courier = CourierActions()
        response = courier.auth_courier(create_courier["login"], create_courier["password"])
        assert "id" in response.json()
        assert response.status_code == 200

    def test_delete_courier(self, id_courier):
        courier = CourierActions()
        response = courier.delete_courier(id_courier)
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    def test_delete_nonexistent_courier(self):
        courier = CourierActions()
        response = courier.delete_courier(CourierData.nonexistent_courier_id)
        assert response.status_code == 404
        assert response.json() == CourierErrorText.error_nonexistent_courier

class TestApiStations:
    def test_get_stations(self):
        stations = StationsActions()
        response = stations.get_stations()
        assert len(response) == 225
