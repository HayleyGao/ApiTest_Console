import  unittest
from  common.request import  Request
import  json
from api_page import api_login
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


filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/login.json"
# filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/login_v2.json"



class TestLogin(unittest.TestCase):
    """
    登录模块的测试
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.filename=filename
        print("测试开始...")


    @parameterized.expand(ReadJson(filename=filename).read_json2_list())
    def test_case_post_001(self,accountEmail,password,url,ip,port,protocol,expect_result,status_code):
        res=api_login.test_login(accountEmail,password,url,ip,port,protocol)
        print(res.status_code)
        print(res.text)
        self.assertEqual(status_code,res.status_code)
        self.assertIn(expect_result,res.text)



    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()







