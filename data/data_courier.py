from helpers.data_generation import DataGeneration


class CourierData:
    new_login = "ibragim" + DataGeneration.generate_random_string()
    password = "123456"
    first_name = "Ivan"
    nonexistent_courier_id = 1000000
