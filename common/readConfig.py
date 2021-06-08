import  configparser
import os


"""
解析config.ini配置文件
"""

# filename="/Users/hayleygao/PycharmProjects/ApiTest_Console/config/config.ini"

top_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filename=os.path.join(top_dir,"config","config.ini")
print(filename)


class ReadCofig:
    def __init__(self,filename):
        self.filename=filename


    def readConfig(self):
        """
        返回解析实例化对象
        :return:
        """
        configer=configparser.ConfigParser()
        configer.read(self.filename)
        return configer


if __name__ == '__main__':
    conf=ReadCofig(filename).readConfig()
    print(conf.get("environment",'ip'))
    print(conf.sections())
