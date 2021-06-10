import  unittest
from  common.request import  Request
import  json
from api_page.api_login import ApiLogin
from common.read_json import   ReadJson
#作参数化 比ddt更加直观的一种方法
from  parameterized import parameterized
from  common.readConfig import ReadCofig
import os
from common.getData import getData


top_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
configFile=os.path.join(top_dir,"config","config.json")
# print("configFile",configFile)
data=getData(configFile,"v11")

filename=os.path.join(top_dir,"data","login_v11.json")
# print("filename",filename)



class TestLogin(unittest.TestCase):
    """
    登录模块的测试
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.filename=filename
        cls.protocol=data["protocol"]
        cls.domain=data["domain"]
        cls.port=data["port"]
        cls.accountEmail=data["accountEmail"]
        cls.password=data["password"]
        cls.tenant=data["tenant"]
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







