import  unittest
from  common.request import  Request
import  json
from api_page.api_robots import AppsApi

from common.read_json import   ReadJson
from parameterized import parameterized  #作参数化 比ddt更加直观的一种方法
from common.getToken import GetToken
import os
from common.getData import getData


#获取配置文件
top_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
configFile = os.path.join(top_dir, "config", "config.json")
# print("configFile",configFile)
data = getData(configFile, "v11")
# print(data)

# 获取配置文件内的参数
# protocol = data["protocol"]
# domain = data["domain"]
# port = data["port"]
# accountEmail = data["accountEmail"]
# password = data["password"]
# tenant = data["tenant"]
# base_url_login = data["base_url_login"]


#获取数据文件
filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/apps.json"
# print("filename",filename)


class TestRobot(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.protocol = data["protocol"]
        cls.domain = data["domain"]
        cls.port = data["port"]
        cls.accountEmail = data["accountEmail"]
        cls.password = data["password"]
        cls.tenant = data["tenant"]
        cls.base_url_login = data["base_url_login"]
        cls.Authorization = GetToken(accountEmail=cls.accountEmail, password=cls.password, domain=cls.domain, protocol=cls.protocol,
                                 port=cls.port, base_url=cls.base_url_login).getToken()

        print("测试开始...")



    def test_apps_get(self):
        base_url="v2/front/apps"
        page=0
        perPage=10
        res = AppsApi(self.protocol, self.domain, self.port, self.Authorization, self.tenant).apps_get(base_url=base_url, page=page, perPage=perPage)
        # print(self.Authorization)
        print(res.status_code)
        self.assertEqual(200,res.status_code)


    def test_versions_get(self):
        appId = "ecc7921d-9720-4a25-80f2-49630dd40ed5"
        base_url_versions = f"v2/front/apps/{appId}/versions"
        page = 0
        perPage = 10
        res = AppsApi(self.protocol, self.domain, self.port, self.Authorization, self.tenant).apps_get(base_url=base_url_versions,
                                                                                       page=page, perPage=perPage)
        print(res.status_code)
        print(res.request.url)
        self.assertEqual(200, res.status_code)

    def test_search_get(self):
        base_url_search = "v2/front/apps"
        appName = "args"
        page = 0
        perPage = 10
        res = AppsApi(self.protocol, self.domain, self.port, self.Authorization, self.tenant).app_search_get(base_url=base_url_search,
                                                                                           appName=appName, page=page,
                                                                                           perPage=perPage)
        print(res.status_code)
        print(res.request.url)
        self.assertEqual(200, res.status_code)



    @classmethod
    def tearDownClass(cls):
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()







