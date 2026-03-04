from actions.object_api import RestApi
from data.config import scooter_url, RestEndpoints


class CourierActions:
    @staticmethod
    def create_courier(login, password, first_name):
        post = RestApi(scooter_url)
        payload = {"login": login, "password": password,
                   "firstName": first_name}
        response = post.post(RestEndpoints.courier, json=payload)
        return response

    @staticmethod
    def auth_courier(login, password):
        post = RestApi(scooter_url)
        payload = {"login": login, "password": password}
        response = post.post(RestEndpoints.courier_login, json=payload)
        return response

    @staticmethod
    def delete_courier(courier_id):
        delete = RestApi(scooter_url)
        response = delete.delete(RestEndpoints.courier + '/' + str(courier_id))
        return response
