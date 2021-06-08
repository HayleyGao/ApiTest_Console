import  unittest
from  common.request import  Request
import  json
from api_page.api_apps import AppsApi

from common.read_json import   ReadJson
from parameterized import parameterized  #作参数化 比ddt更加直观的一种方法
from common.getToken import GetToken

filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/robot.json"

domain = "rpa-test.datagrand.com"
protocol = 'http'
port=80
# accountEmail = "gaoxiaoyan%40datagrand.com"
# password = "b29a8e35a7eeb51fd42c6abfb93597d9"
accountEmail = "gaoxiaoyan@datagrand.com"
password = "Gaoxiaoyan9533"
tenant="0cc21ce8-f16c-11e9-9f12-0242ac120003"  #达观数据租户
# base_url_ = "token?_allow_anonymous=true&selfHandled=yes"
base_url_ = "/v2/token?_allow_anonymous=true&selfHandled=yes"

# data_=ReadJson(filename=filename).read_json2_list()
# print(data_)

class TestRobot(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.filename = filename
        cls.domain=domain
        cls.protocol=protocol
        cls.port=port
        cls.accountEmail=accountEmail
        cls.password=password
        cls.tenant=tenant
        cls.Authorization = GetToken(accountEmail=accountEmail, password=password, domain=domain, protocol=protocol,
                                 port=port, base_url=base_url_).getToken()

        print("测试开始...")



    def test_apps_get(self):
        base_url = "protected/v1/app/view/queryApps"
        #base_url="v2/front/apps"
        res = AppsApi(self.protocol, self.domain, self.port, self.Authorization, self.tenant).apps_get(base_url, page=0, perPage=10)
        # print(self.Authorization)
        print(res.status_code)
        self.assertEqual(200,res.status_code)





    @classmethod
    def tearDownClass(cls):
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()







