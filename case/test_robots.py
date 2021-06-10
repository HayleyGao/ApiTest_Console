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
filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/robots.json"
# print("filename",filename)
#获取同一模块的不同接口的参数化数据
case_data=ReadJson(filename).read_json()

robots=case_data["robots"]
robots_put=case_data["robots_put"]

#转换为(parameterized)参数化格式
robots_params=ReadJson(filename).dict_to_parameterized(robots)
robots_put_params=ReadJson(filename).dict_to_parameterized(robots_put)



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


    @parameterized.expand(robots_params)
    def test_robots_get(self,base_url,page,perPage,expect_result,status_code):
        res = RobotsApi(self.protocol, self.domain, self.port, self.Authorization, self.tenant).robots_get(base_url=base_url, page=page, perPage=perPage)
        # print(self.Authorization)
        #print(res.status_code)
        print(res.request.url)
        self.assertEqual(status_code,res.status_code)
        self.assertIn(expect_result,res.text)


    @parameterized.expand(robots_put_params)
    def test_robots_put(self,base_url,robotId,name,expect_result,status_code):
        base_url_=f"{base_url}{robotId}"
        res = RobotsApi(self.protocol, self.domain, self.port, self.Authorization, self.tenant).robots_put(base_url=base_url_,robotId=robotId,name=name)
        # print(res.status_code)
        print(res.request.url)
        self.assertEqual(status_code, res.status_code)
        self.assertIn(expect_result, res.text)


    @classmethod
    def tearDownClass(cls):
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()







