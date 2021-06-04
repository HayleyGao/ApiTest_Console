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

    @parameterized.expand([(2, 3, 5),(3, 5, 8)])
    def test_add(self,a, b, expected):
        self.assertEqual(a + b, expected)


if __name__ == '__main__':
    unittest.main()

