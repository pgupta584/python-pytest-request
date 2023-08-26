import logging
import random
import string
import time
from datetime import datetime, timedelta

import pytest

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class CommonUtils:
    @staticmethod
    def current_epoc_time() -> str:
        t = time.time()
        ml = int(t * 1000)
        epoch_time = str(ml)
        return epoch_time

    @staticmethod
    def generate_random_string(length) -> str:
        # Get all the ASCII letters in lowercase and uppercase
        letters = string.ascii_letters
        # Randomly choose characters from letters for the given length of the string
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_random_integer() -> int:
        random_integer = random.randint(1000, 9999)
        return random_integer

    @staticmethod
    def random_mobile_number(number) -> str:
        range_start = 10 ** (number - 1)
        range_end = (10 ** number) - 1
        return f'{random.randint(7, 9)}{random.randint(range_start, range_end)}'

    @staticmethod
    def random_string_by_length(number) -> str:
        return ''.join(random.sample(string.ascii_letters + string.digits, k=number))

    @staticmethod
    def json_extract(obj, key) -> any:
        """Recursively fetch values from nested JSON."""
        arr = []

        def extract(obj, arr, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        values = extract(obj, arr, key)
        return values

    @staticmethod
    def get_future_epoch_date(diff_days):
        return (datetime.today() + timedelta(days=diff_days)).strftime('%s')

    @staticmethod
    def compare_list(actual_list, expected_list):
        if actual_list == expected_list:
            logger.info("No Missing Column found")
        else:
            logger.info(f"expected column is {expected_list} but found {actual_list}")
            pytest.fail("Missing Column found, Please check")
