import random
from datetime import datetime, timedelta


class Date:
    @staticmethod
    def generation_date():
        # Исп. Реализовать случайную генерацию даты
        today_date = datetime.now()
        end_date = datetime(2026, 12, 31)
        delta_days = (end_date - today_date).days
        # Генерируем случайное число дней в этом диапазоне
        random_days = random.randint(0, delta_days)
        random_date = today_date + timedelta(days=random_days)
        return random_date.strftime('%d.%m.%Y')
