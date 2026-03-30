import random
import string


class DataGeneration:
    @staticmethod
    def generate_random_string(len_st=10):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=len_st))
