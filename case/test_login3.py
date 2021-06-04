import  unittest
from  common.request import  Request
import  json
from api import api_login
from common.read_json import   ReadJson



class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.filename="/Users/hayleygao/PycharmProjects/ApiTest_Console/data/login.json"
        print("测试开始...")



    def test_case_post_001(self):
        data=ReadJson(filename=self.filename).read_json()
        accountEmail=data["login_001"]["accountEmail"]
        password=data["login_001"]["password"]
        url=data["login_001"]["url"]
        ip=data["login_001"]["ip"]
        protocol=data["login_001"]["protocol"]
        res=api_login.test_login(accountEmail=accountEmail,password=password,url=url,ip=ip,protocol=protocol)
        self.assertEqual(200,res.status_code)



    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()

