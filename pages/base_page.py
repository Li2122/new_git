from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        # механизм явного ожидания
        # until - до тех пор пока
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Элемент {locator} не найден")

    def find_clickable_element(self, locator, timeout=10):  # Исп. Название метода - глагол
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator),
                                                         message=f"Элемент {locator} не кликабельный")

    def click(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_clickable_element(locator)
        element.send_keys(text)

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Элементы {locator} не найдены")

    def move_to_element(self, locator):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(locator)).perform()
