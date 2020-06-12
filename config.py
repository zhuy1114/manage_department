# 导包
import logging.handlers
from app import BASE_DIR


def set_logging():
    # 创建日志器
    logger = logging.getLogger()

    # 设置日志器级别
    logger.setLevel(level=logging.INFO)

    # 创建处理器
    # 输出到控制台
    ls = logging.StreamHandler()
    # 输出到文件
    path = BASE_DIR + "/log/ihtm_dep.log"
    lht = logging.handlers.TimedRotatingFileHandler(path, when="M", interval=1, backupCount=2, encoding="utf-8")

    # 创建格式化器
    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

    # 设置格式化器
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)

    # 设置处理器
    logger.addHandler(ls)
    logger.addHandler(lht)
