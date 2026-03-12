import requests

from actions.object_api import RestApi
from data.config import RestEndpoints


class CourierActions(RestApi):

    def create_courier(self, login: str, password: str, first_name: str) -> requests.Response:
        payload = {"login": login, "password": password,
                   "firstName": first_name}
        response = self.post(RestEndpoints.courier, json=payload)
        return response

    def auth_courier(self, login: str, password: str) -> requests.Response:
        payload = {"login": login, "password": password}
        response = self.post(RestEndpoints.courier_login, json=payload)
        return response

    def delete_courier(self, courier_id: str) -> requests.Response:
        response = self.delete(f"{RestEndpoints.courier}/{courier_id}")
        return response
