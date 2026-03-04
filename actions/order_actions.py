from actions.object_api import RestApi
from data.config import scooter_url, RestEndpoints
from models.get_order_response import Orders, OneOrder


class OrderActions:
    @staticmethod
    def create_order(first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment,
                     color):
        post = RestApi(scooter_url)
        payload = {"firstName": first_name, "lastName": last_name, "address": address, "metroStation": metro_station,
                   "phone": phone, "rentTime": rent_time, "deliveryDate": delivery_date,
                   "comment": comment, "color": color
                   }
        response = post.post(RestEndpoints.orders, json=payload)
        return response

    @staticmethod
    def get_orders() -> Orders:
        get = RestApi(scooter_url)
        response = get.get(RestEndpoints.orders)
        return Orders(**response.json())

    @staticmethod
    def get_order(track):
        get = RestApi(scooter_url)
        response = get.get(RestEndpoints.order + str(track))
        return OneOrder(**response.json())

    @staticmethod
    def check_order_exist(track: int, orders: Orders) -> bool:
        z = []
        for i in orders.orders:
            if track == i.track:
                z.append(True)
            else:
                z.append(False)
        return any(z)

    @staticmethod
    def put_order(order_id, courier_id):
        put = RestApi(scooter_url)
        response = put.put(RestEndpoints.change_order + '/' + str(order_id) + '?courierId=' + str(courier_id))
        return response
