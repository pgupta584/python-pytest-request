import json
import os
import sys
from typing import Any

sys.path.append(os.getcwd())

class EnvironmentUtils:
    def __init__(self, env):
        with open('config/endpoints_config.json', 'r') as config_file:
            extracts_config = json.load(config_file)
            self.__dict__ = extracts_config[env]

def get_test_config(env: str) -> Any:
    test_config = EnvironmentUtils(env)
    return test_config
