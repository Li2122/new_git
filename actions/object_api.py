import requests


class RestApi:
    @staticmethod
    def get(url, **kwargs):
        response = requests.get(url, **kwargs)
        return response

    @staticmethod
    def post(url, **kwargs):
        response = requests.post(url, **kwargs)
        return response

    @staticmethod
    def put(url, **kwargs):
        response = requests.put(url, **kwargs)
        return response

    @staticmethod
    def delete(url):
        response = requests.delete(url)
        return response
