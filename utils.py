import json

import app


def assert_common(self, http_code, success, code, message, response):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


# 定义管理部门数据的函数
def load_dep_data(filepath, interface_name):
    with open(filepath, mode="r", encoding="utf-8")as f:
        # 加载数据
        jsondata = json.load(f)
        # 读取加载的json数据当中对应接口的数据
        dep_data = jsondata.get(interface_name)
        # 定义空列表
        data_list = []
        # 遍历数据转换为元祖格式，并添加到列表
        data_list.append(tuple(dep_data.values()))
        print(data_list)
        # 返回数据
    return data_list


if __name__ == '__main__':
    # 定义员工数据路径
    filepath2 = app.BASE_DIR + "/data/dep_data.json"
    # 读取员工数据
    load_dep_data(filepath2, 'add_dep')
    load_dep_data(filepath2, 'sel_dep')
    load_dep_data(filepath2, 'upd_dep')
    load_dep_data(filepath2, 'del_dep')
