import  logging
import time


def logs(filename):
    logger = logging.getLogger()  # 1.实例化Logger对象
    logger.setLevel(logging.DEBUG)  # 2.等级

    fmt = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
    logging.Formatter(fmt)  # 3.格式

    c_handler = logging.StreamHandler()  # 输出方向，流，console

    f_handler = logging.FileHandler(filename)  # 4.输出方向,输出到文件。默认是append方式。

    logger.addHandler(c_handler)  # 5.添加处理方向
    logger.addHandler(f_handler)
    #logger.debug("hello,this is first test.")
    return logger






if __name__ == '__main__':
    filename = r"/Users/hayleygao/PycharmProjects/ApiTest_Console/logs/console_api_.log"

    logger=logs(filename).warning("no support.")










