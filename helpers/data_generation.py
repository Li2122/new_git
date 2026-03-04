import random
import string


class DataGeneration:
    @staticmethod
    def generation_phone():
        n = random.randint(000000000, 999999999)
        return int('89' + str(n))
