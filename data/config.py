scooter_url = "https://qa-scooter.praktikum-services.ru"


class RestEndpoints:
    orders = scooter_url + '/api/v1/orders'
    order = orders + '/track?t='
    change_order = orders + '/accept'
    courier = scooter_url + '/api/v1/courier'
    courier_login = scooter_url + '/api/v1/courier/login'
    stations = scooter_url + '/api/v1/stations/search'
