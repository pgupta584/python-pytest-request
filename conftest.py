import json
import logging
from pytest import fixture
import pytest

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="lzuat")

@pytest.hookimpl()
def pytest_configure(config):
    update_env(config)

def read_host_from_config_json(env, host_name):
    with open("config/endpoints_config.json") as json_file:
        properties = json.load(json_file)
        url = properties[env][host_name]
        with open("endPointUserConf.json", 'w') as f:
            f.write(json.dumps(properties, indent=4))
            f.close()
        json_file.close()
    return url

def update_env(config):
    with open("config/endpoints_config.json", "r+") as jsonFile:
        logger.info(" $$$ ------ Updating Env & COA ----$$$ ")
        data = json.load(jsonFile)
        jsonFile.truncate(0)
        jsonFile.seek(0)
        logger.info("--- Truncating file & Updating Host & COA---")
        data["testingEndPoint"]['env'] = config.getoption("--host").lower()
        data["testingEndPoint"]['coa'] = config.getoption("--coa").lower()
        json.dump(data, jsonFile, indent=4)
        jsonFile.close()

@fixture(scope='session')
def environment(request):
    env = (request.config.getoption("--host")).lower()
    return env
