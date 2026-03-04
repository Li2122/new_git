from selenium.webdriver.common.by import By


class Locators:
    button_order_on_header = (By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']")
    input_name = (By.XPATH, "//input[@placeholder='* Имя']")
    input_last_name = (By.XPATH, "//input[@placeholder='* Фамилия']")
    input_address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    input_metro = (By.XPATH, "//input[@placeholder='* Станция метро']")
    input_phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    dropdown_list_metro = (By.XPATH, "//div[@class='select-search__select']")
    button_further = (By.XPATH, "//button[text()='Далее']")
    input_date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    input_term = (By.XPATH, "//div[text()='* Срок аренды']")
    dropdown_list_terms = (By.XPATH, "//div[@class='Dropdown-menu']")
    checkbox_black = (By.XPATH, "//input[@id='black']")
    checkbox_grey = (By.XPATH, "//input[@id='grey']")
    button_order_in_list = (
        By.XPATH, "//button[text()='Назад']/following-sibling::button")
    input_comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    text_in_modal_window_to_order = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    text_error_in_lastname = (By.XPATH, "//div[text()='Введите корректную фамилию']")
    text_error_in_phone = (By.XPATH, "//div[text()='Введите корректный номер']")
    text_header_second_page_order = (By.XPATH, "//div[text()='Про аренду']")
    button_order_status_on_header = (By.XPATH, "//button[text()='Статус заказа']")
    input_order_number = (By.XPATH, "//input[@placeholder='Введите номер заказа']")
    button_go = (By.XPATH, "//button[text()='Go!']")
    text_scooter_on_warehouse = (By.XPATH, "//div[text()='Имя']")
    pic_not_found = "//img[@alt='Not found']"
