import json

json_content_type = 'application/json'
user_agent = 'Google Chrome 112.0.5615.49'
end_point_config_path = "config/endpoints_config.json"


class FunctionalParam:
    @staticmethod
    def get_custom_header():
        header = {'Content-Type': json_content_type,
                  'Authorization': "",
                  'User-Agent': user_agent}
        return header

    @staticmethod
    def get_default_end_point():
        with open(end_point_config_path) as json_file:
            properties = json.load(json_file)
        env = properties["testingEndPoint"]["env"]
        return properties[env]["defaultEndPoint"]

    @staticmethod
    def get_tachyon_end_point():
        with open(end_point_config_path) as json_file:
            properties = json.load(json_file)
        env = properties["testingEndPoint"]["env"]
        return properties[env]["basic_host"]
