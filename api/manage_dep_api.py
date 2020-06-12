import requests


class ManageDepApi:
    def __init__(self):
        self.dep_url = "http://ihrm-test.itheima.net/api/company/department"

    def add_dep(self, name, code, headers):
        json_data = {
            "name": name,
            "code": code,
            "manager": "测试Boss",
            "introduce": "测试人员集合",
            "pid": ""
        }
        return requests.post(url=self.dep_url, json=json_data, headers=headers)

    def sel_dep(self, dep_id, headers):
        select_url = self.dep_url + "/" + dep_id
        return requests.get(url=select_url, headers=headers)

    def upd_dep(self, dep_id, jsondata, headers):
        update_url = self.dep_url + "/" + dep_id
        return requests.put(url=update_url, json=jsondata, headers=headers)

    def del_url(self, dep_id, headers):
        delete_url = self.dep_url + "/" + dep_id
        return requests.delete(url=delete_url, headers=headers)
