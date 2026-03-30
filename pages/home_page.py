from selenium.common import TimeoutException

from data.locators import Locators
from pages.base_page import BasePage


class HomePage(BasePage):
    def scroll_important_question(self):
        self.move_to_element(Locators.text_important_question)

    def click_text_question(self, question):
        self.move_to_element(question)
        self.click(question)

    def check_text_answer(self, answer):
        try:
            self.find_element(answer)
            return True
        except TimeoutException:
            return False

    def click_cookie_button(self):
        self.find_element(Locators.cookie_button).click()
