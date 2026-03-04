import requests


class RestApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, **kwargs):
        url = self.base_url + endpoint
        response = requests.post(url, **kwargs)
        return response
