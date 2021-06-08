import  unittest
from  common.request import  Request
import  json
from api_page.api_login import ApiLogin
from common.read_json import   ReadJson
from parameterized import parameterized  #作参数化 比ddt更加直观的一种方法
from  common.readConfig import ReadCofig
import os

#
# top_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# filename_=os.path.join(top_dir,"config","config.ini")
# print("config_",filename_)
#
#
# data_=ReadCofig(filename_).readConfig().get("data",'login')
# print("data_",data_)


filename_ = "/Users/hayleygao/PycharmProjects/ApiTest_Console/config/config.json"
data = ReadJson(filename_).read_json()
# print(type(data),data)

#v11环境
# protocol = data["environment"]["v11"]["protocol"]
# domain = data["environment"]["v11"]["domain"]
# port = data["environment"]["v11"]["port"]
# accountEmail = data["environment"]["v11"]["accountInfo"]["accountEmail"]
# password = data["environment"]["v11"]["accountInfo"]["password"]
# tenant = data["environment"]["v11"]["accountInfo"]["tenant"]



#test_v2环境
protocol = data["environment"]["test"]["v2"]["protocol"]
domain = data["environment"]["test"]["v2"]["domain"]
port = data["environment"]["test"]["v2"]["port"]
accountEmail = data["environment"]["test"]["v2"]["accountInfo"]["accountEmail"]
password = data["environment"]["test"]["v2"]["accountInfo"]["password"]
tenant = data["environment"]["test"]["v2"]["accountInfo"]["tenant"]

print(protocol, domain, port, accountEmail, password, tenant)


filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/login_v11.json"



class TestLogin(unittest.TestCase):
    """
    登录模块的测试
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.filename=filename
        cls.protocol=protocol
        cls.domain=domain
        cls.port=port
        cls.accountEmail=accountEmail
        cls.password=password
        cls.tenant=tenant
        print("测试开始...")


    @parameterized.expand(ReadJson(filename=filename).read_json2_list())
    def test_case_post_001(self,accountEmail,password,base_url,expect_result,status_code):
        res=ApiLogin(self.protocol,self.domain,self.port).login_post(accountEmail,password,base_url)
        print(res.status_code)
        print(res.request.url)
        self.assertEqual(status_code,res.status_code)
        self.assertIn(expect_result,res.text)



    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()







