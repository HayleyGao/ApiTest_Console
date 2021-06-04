import  unittest
from  common.request import  Request
import  json
from api import api_login
from common.read_json import   ReadJson
from parameterized import parameterized  #作参数化 比ddt更加直观的一种方法

filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/login.json"
data = ReadJson(filename=filename).read_json2_list()
print(data)

class TestLogin(unittest.TestCase):



    @parameterized.expand(data)
    def test_case_post_001(self,accountEmail,password,url,ip,protocol):
        res=api_login.test_login(accountEmail,password,url,ip,protocol)
        print(res.status_code)
        self.assertEqual(200,res.status_code)



if __name__ == '__main__':
    unittest.main()



