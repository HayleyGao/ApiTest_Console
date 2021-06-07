import  unittest
from  common.request import  Request
import  json
from api_page import api_login
from common.read_json import   ReadJson
from parameterized import parameterized  #作参数化 比ddt更加直观的一种方法


filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/login.json"

accountEmail="gaoxiaoyan%40datagrand.com"
password="b29a8e35a7eeb51fd42c6abfb93597d9"
url="http://rpa-test.datagrand.com/v2/token?_allow_anonymous=true&selfHandled=yes"
ip="rpa-test.datagrand.com"
protocol="http"


class GetToken:
    def __init__(self,accountEmail,password,ip,protocol):
        self.accountEmail=accountEmail
        self.password=password
        self.ip=ip
        self.protocol=protocol
        self.url = protocol + "://" + ip + '/v2/token?_allow_anonymous=true&selfHandled=yes'


    def getToken(self):
        """
        获取登录后的token。
        :return:
        """
        res = api_login.test_login(self.accountEmail, self.password, self.url, self.ip, self.protocol)
        result_json = res.json()
        #print(result_json)
        token_ = result_json["result"]["token"]  # dict type.
        token = "Bearer " + token_
        return token


if __name__ == '__main__':
   token= GetToken(accountEmail, password, ip, protocol).getToken()
   print(token)









