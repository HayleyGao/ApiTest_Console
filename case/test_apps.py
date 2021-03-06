import  unittest
from  common.request import  Request
import  json
from api_page.api_apps import AppsApi

from common.read_json import   ReadJson #read_json,dict_to_parameterized
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


#获取数据文件
filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/apps.json"
# print("filename",filename)
#获取同一模块的不同接口的参数化数据
case_data=ReadJson(filename).read_json()
apps=case_data["apps"]
versions=case_data["versions"]
search=case_data["search"]

apps_params=ReadJson(filename).dict_to_parameterized(apps)
versions_params=ReadJson(filename).dict_to_parameterized(versions)
search_params=ReadJson(filename).dict_to_parameterized(search)



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


    @parameterized.expand(apps_params)
    def test_apps_get(self,base_url,page,perPage,expect_result,status_code):
        res = AppsApi(self.protocol, self.domain, self.port, self.Authorization, self.tenant).apps_get(base_url=base_url, page=page, perPage=perPage)
        # print(self.Authorization)
        #print(res.status_code)
        print(res.request.url)
        self.assertEqual(status_code,res.status_code)
        self.assertIn(expect_result,res.text)


    @parameterized.expand(versions_params)
    def test_versions_get(self,appId,base_url,page,perPage,expect_result,status_code):
        res = AppsApi(self.protocol, self.domain, self.port, self.Authorization, self.tenant).versions_get(base_url=base_url, page=page, perPage=perPage)
        # print(res.status_code)
        print(res.request.url)
        print(res.text)
        self.assertEqual(status_code, res.status_code)
        self.assertIn(expect_result, res.text)

    @parameterized.expand(search_params)
    def test_search_get(self,base_url,appName,page,perPage,expect_result,status_code):
        print(appName,base_url,page,perPage,expect_result,status_code)
        res = AppsApi(self.protocol, self.domain, self.port, self.Authorization, self.tenant).app_search_get(base_url=base_url,appName=appName, page=page,perPage=perPage)
        print(res.status_code)
        print(res.request.url)
        self.assertEqual(status_code, res.status_code)
        self.assertIn(expect_result, res.text)


    @classmethod
    def tearDownClass(cls):
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()







