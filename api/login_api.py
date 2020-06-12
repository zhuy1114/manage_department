import requests


class LoginApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"

    def login(self, data, headers):
        # 发送登录的请求对象，并返回
        return requests.post(url=self.login_url, json=data, headers=headers)
