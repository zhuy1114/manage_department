import logging
import unittest

from parameterized import parameterized

import app
from api.login_api import LoginApi
from api.manage_dep_api import ManageDepApi
from utils import assert_common, load_dep_data


class TestDepart(unittest.TestCase):
    def setUp(self):
        # 实例化登录
        self.login_api = LoginApi()
        # 实例化部门
        self.dep_api = ManageDepApi()

    # 登录
    def test01_login(self):
        data = {"mobile": "13800000002", "password": "123456"}
        response_login = self.login_api.login(data=data, headers={"Content-Type": "application/json"})
        # 提取数据
        print("数据为：", response_login.json().get("data"))
        # 拼接令牌
        token = "Bearer " + response_login.json().get("data")
        # 保存到全局变量
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 打印请求头
        logging.info("请求头为:{}".format(app.HEADERS))
        # 添加断言
        assert_common(self, 200, True, 10000, "操作成功！", response_login)

    # 添加部门
    dep_path = app.BASE_DIR + "/data/dep_data.json"

    @parameterized.expand(load_dep_data(dep_path, "add_dep"))
    def test02_add_dep(self, name, code2, http_code, success, code, message):
        response_add = self.dep_api.add_dep(name, code2, app.HEADERS)
        # 打印添加员工的结果
        logging.info("添加员工：{}".format(response_add.json()))
        # 保存部门id到全局变量
        app.DEP_ID = response_add.json().get("data").get("id")
        # 打印部门id
        logging.info("员工id为：{}".format(app.DEP_ID))
        # 添加断言
        assert_common(self, http_code, success, code, message, response_add)

    @parameterized.expand(load_dep_data(dep_path, "sel_dep"))
    # 查看部门信息
    def test03_sel_dep(self, http_code, success, code, message):
        response_sel = self.dep_api.sel_dep(app.DEP_ID, app.HEADERS)
        # 打印部门信息
        logging.info("部门信息：{}".format(response_sel.json()))
        # 引用断言
        assert_common(self, http_code, success, code, message, response_sel)

    @parameterized.expand(load_dep_data(dep_path, "upd_dep"))
    # 修改部门
    def test04_upd_dep(self, name, http_code, success, code, message):
        response_upd = self.dep_api.upd_dep(app.DEP_ID, {"name": name}, app.HEADERS)
        # 查看修改后的部门信息
        logging.info("部门信息：{}".format(response_upd.json()))
        # 引用断言
        assert_common(self, http_code, success, code, message, response_upd)

    @parameterized.expand(load_dep_data(dep_path, "del_dep"))
    # 删除部门
    def test05_del_dep(self, http_code, success, code, message):
        response_del = self.dep_api.del_url(app.DEP_ID, app.HEADERS)
        # 查看删除后的部门信息
        logging.info("部门信息：{}".format(response_del.json()))
        # 引用断言
        assert_common(self, http_code, success, code, message, response_del)
