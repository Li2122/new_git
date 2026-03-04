import requests


class RestApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        response = requests.get(url, **kwargs)
        return response

    def post(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        response = requests.post(url, **kwargs)
        return response

    def put(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        response = requests.put(url, **kwargs)
        return response

    def delete(self, endpoint):
        url = self.base_url + endpoint
        response = requests.delete(url)
        return response
