import unittest

from api.login_api import LoginApi


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()

    # 成功登录
    def test_01_login(self):
        response_login = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                              {"Content-Type": "application/json"})
        print("登录的结果为：", response_login.json())
