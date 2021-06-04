import  unittest
from  common.request import  Request
import  json
from api import api_robots
from common.read_json import   ReadJson
from parameterized import parameterized  #作参数化 比ddt更加直观的一种方法
from common.getToken import GetToken

filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/robot.json"

ip = "rpa-test.datagrand.com"
protocol = 'http'
accountEmail = "gaoxiaoyan%40datagrand.com"
password = "b29a8e35a7eeb51fd42c6abfb93597d9"

# data_=ReadJson(filename=filename).read_json2_list()
# print(data_)

class TestRobot(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.filename = filename
        cls.Authorization=GetToken(accountEmail, password, ip, protocol).getToken()
        print("测试开始...")


    @parameterized.expand(ReadJson(filename=filename).read_json2_list())
    def test_robot_put(self,name,robotId,ip,protocol,tenant,expect_result,status_code):
        res = api_robots.test_robot_put(name,robotId,ip,protocol,tenant,self.Authorization)
        self.assertEqual(status_code,res.status_code)
        self.assertIn(expect_result,res.text)


    @classmethod
    def tearDownClass(cls):
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()







