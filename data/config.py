scooter_url = "https://qa-scooter.praktikum-services.ru"


class RestEndpoints:
    orders = '/api/v1/orders'
    order = orders + '/track?t='
    change_order = orders + '/accept'
    courier = '/api/v1/courier'
    courier_login = '/api/v1/courier/login'
