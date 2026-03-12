import requests
from actions.object_api import RestApi
from data.config import RestEndpoints
from models.get_order_response import Orders, OneOrder



class OrderActions(RestApi):

    def create_order(self, first_name: str, last_name: str, address: str, metro_station: int, phone: str, rent_time: int,
                     delivery_date: str, comment: str, color: str) -> requests.Response:
        payload = {"firstName": first_name, "lastName": last_name, "address": address, "metroStation": metro_station,
                   "phone": phone, "rentTime": rent_time, "deliveryDate": delivery_date,
                   "comment": comment, "color": color
                   }
        response = self.post(RestEndpoints.orders, json=payload)
        return response

    def get_orders(self) -> Orders:
        response = self.get(RestEndpoints.orders)
        return Orders(**response.json())

    def get_order(self, track: str) -> OneOrder:
        response = self.get(f'{RestEndpoints.order}{track}')
        return OneOrder(**response.json())

    def check_order_exist(self, track: str, orders: Orders) -> bool:
        return any([track == order.track for order in orders.orders])


    def put_order(self, order_id: str, courier_id: str) -> requests.Response:
        response = self.put(f"{RestEndpoints.change_order}/{order_id}?courierId={courier_id}")
        return response
