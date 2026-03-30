import pytest
from selenium.webdriver.common.by import By

from data.data_question_answer_text import QuestionText, AnswerText
from pages.home_page import HomePage


class TestHomePage:
    def test_important_question(self, browser):
        homepage = HomePage(browser)
        homepage.scroll_important_question()


    @pytest.mark.parametrize("question, answer", [
        (QuestionText.pay_question, AnswerText.pay_answer),
        (QuestionText.quantity_question, AnswerText.quantity_answer),
        (QuestionText.rent_question, AnswerText.rent_answer),
        (QuestionText.today_question, AnswerText.today_answer),
        (QuestionText.rent_question, AnswerText.rent_answer),
        (QuestionText.charger_question, AnswerText.charger_answer),
        (QuestionText.cancel_question, AnswerText.cancel_answer),
        (QuestionText.mkad__question, AnswerText.mkad_answer)
    ]
                             )
    def test_important_question(self, browser, agree_with_cookies, question, answer):
        homepage = HomePage(browser)
        homepage.scroll_important_question()
        homepage.click_text_question((By.XPATH, f"//*[text()='{question}']"))
        assert homepage.check_text_answer((By.XPATH, f"//*[text()='{answer}']"))
