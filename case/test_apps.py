import  unittest
from  common.request import  Request
import  json
from api_page.api_apps import AppsApi

from common.read_json import   ReadJson
from parameterized import parameterized  #作参数化 比ddt更加直观的一种方法
from common.getToken import GetToken

filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/robot.json"

ip = "rpa-test.datagrand.com"
protocol = 'http'
port=80
accountEmail = "gaoxiaoyan%40datagrand.com"
password = "b29a8e35a7eeb51fd42c6abfb93597d9"
tenant="0cc21ce8-f16c-11e9-9f12-0242ac120003"  #达观数据租户


# data_=ReadJson(filename=filename).read_json2_list()
# print(data_)

class TestRobot(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.filename = filename
        cls.ip=ip
        cls.protocol=protocol
        cls.port=port
        cls.accountEmail=accountEmail
        cls.password=password
        cls.tenant=tenant
        cls.Authorization=GetToken(accountEmail, password, ip, protocol).getToken()
        print("测试开始...")




    def test_apps_get(self):
        res=AppsApi(protocol=self.protocol,ip=self.ip,port=self.port,Authorization=self.Authorization,tenant=self.tenant).apps_get(page=0,perPage=10)
        print(res.status_code)
        self.assertEqual(200,res.status_code)


    def test_versions_get(self):
        appId = "3a8918be-3f80-46e6-9610-6f24074b1686"
        res = AppsApi(protocol=self.protocol,ip=self.ip,port=self.port,Authorization=self.Authorization,tenant=self.tenant).versions_get(
            appId=appId, page=0, perPage=5)
        # print(res2.text)
        # print(res2.request.url)
        print(res.status_code)
        self.assertEqual(200, res.status_code)


    def test_sharedAccounts_get(self):
        appId = "3a8918be-3f80-46e6-9610-6f24074b1686"

        res = AppsApi(protocol=self.protocol,ip=self.ip,port=self.port,Authorization=self.Authorization,tenant=self.tenant).sharedAccounts(
            appId=appId, page=0, perPage=10)
        # print(res3.text)
        print(res.request.url)
        print(res.status_code)
        self.assertEqual(200, res.status_code)

    def test_apps_search_get(self):
        res = AppsApi(protocol=self.protocol,ip=self.ip,port=self.port,Authorization=self.Authorization,tenant=self.tenant).apps_search(
            appName='email', page=0, perPage=10)
        print(res.request.url)
        print(res.status_code)
        self.assertEqual(200, res.status_code)


    @classmethod
    def tearDownClass(cls):
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()







