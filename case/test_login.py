import  unittest
from  common.request import  Request
import  json
from api import api_login
from common.read_json import   ReadJson
from parameterized import parameterized  #作参数化 比ddt更加直观的一种方法


filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/login.json"


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.filename=filename
        print("测试开始...")


    @parameterized.expand(ReadJson(filename=filename).read_json2_list())
    def test_case_post_001(self,accountEmail,password,url,ip,protocol,expect_result,status_code):
        res=api_login.test_login(accountEmail,password,url,ip,protocol)
        #print(res.status_code)
        #self.assertEqual(status_code,res.status_code)
        self.assertIn(expect_result,res.text)



    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()







