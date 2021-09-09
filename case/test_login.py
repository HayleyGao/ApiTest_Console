import  unittest
from  common.request import  Request
import  json
from api_page.api_login import ApiLogin
from common.read_json import   ReadJson
from parameterized import parameterized  #作参数化 比ddt更加直观的一种方法
from  common.readConfig import ReadCofig
import os
from common.getData import getData


data={
    "protocol" : "http",
    "domain" : 'rpa-test.datagrand.com',
    "port" : 80,
    "apiVersion" : 'v2',
    "accountEmail" : 'gaoxiaoyan@datagrand.com',
    "password" : 'b29a8e35a7eeb51fd42c6abfb93597d9',

    "base_url" : "token",
    "params" : {"_allow_anonymous": "true", "selfHandled": "yes"}
}


class TestLogin(unittest.TestCase):
    """
    登录模块的测试
    """
    @classmethod
    def setUpClass(cls) -> None:

        cls.protocol=data["protocol"]
        cls.domain=data["domain"]
        cls.port=data["port"]
        cls.apiVersion=data["apiVersion"]
        cls.accountEmail=data["accountEmail"]
        cls.password=data["password"]
        cls.base_url=data["base_url"]
        cls.params=data["params"]
        print("测试开始...")

    def test_login_post(self):
        res=ApiLogin( self.protocol,self.domain,self.port,self.apiVersion).login_post(self.accountEmail, self.password,
                                                                                      self.base_url,self.params)
        self.assertEqual(res.status_code,200)



    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()







