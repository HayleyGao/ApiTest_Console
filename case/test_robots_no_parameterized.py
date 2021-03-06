import  unittest
from  common.request import  Request
import  json
from api_page.api_robots import RobotsApi

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


    def test_robots_get(self):
        base_url = "v2/robots"
        page = 0
        perPage = 10
        res = RobotsApi(self.protocol, self.domain, self.port, self.Authorization, self.tenant).robots_get(base_url=base_url, page=page, perPage=perPage)
        print(res.request.url)
        self.assertEqual(200,res.status_code)


    def test_robots_put(self):
        robotId = "a56e0a6b-1e27-42c1-9ca3-f6162eb23177"
        base_url = f"v2/robots/{robotId}"
        name = "robot_caiwenjie_PC_updated"
        res = RobotsApi(self.protocol, self.domain, self.port, self.Authorization, self.tenant).robots_put(base_url=base_url,robotId=robotId,name=name)
        # print(res.status_code)
        print(res.request.url)
        self.assertEqual(200, res.status_code)

    def test_robots_put_v2(self):
        robotId = "a56e0a6b-1e27-42c1-9ca3-f6162eb23177"
        base_url = f"v2/robots/{robotId}"
        #base_url = "v2/robots/robotId"
        name = "robot_caiwenjie_PC_updated"
        res = RobotsApi(self.protocol, self.domain, self.port, self.Authorization, self.tenant).robots_put(base_url=base_url,robotId=robotId,name=name)
        # print(res.status_code)
        print(res.request.url)
        print(res.text)
        self.assertEqual(200, res.status_code)


    @classmethod
    def tearDownClass(cls):
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()








