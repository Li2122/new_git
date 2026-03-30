from actions.object_api import RestApi
from data.config import scooter_url, RestEndpoints


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
