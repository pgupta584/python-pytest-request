from functional_test.functional_param import FunctionalParam
class ApiURLs:
    @staticmethod
    def get_user_info(user_id):
        return FunctionalParam.get_default_end_point() + f'api/users?page={user_id}'

    CREATE_USER = FunctionalParam.get_default_end_point() + 'api/users'
