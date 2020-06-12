# 导包
import time
import unittest

from BeautifulReport import BeautifulReport

from app import BASE_DIR

#  组织套件
suite = unittest.TestLoader().discover(BASE_DIR + "/script", pattern="test*.py")

# 设置报告名称
file_name = "/report-{}.html".format(time.strftime("%Y%m%d%H%M%S"))

# 生成报告
BeautifulReport(suite).report(filename=file_name, description="ihrm部门管理", log_path=BASE_DIR + "/report")
