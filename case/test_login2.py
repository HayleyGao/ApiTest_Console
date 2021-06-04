import  unittest
from  common.request import  Request
import  json
from api import api_login

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("测试开始...")


    def test_case_get(self):
        respose=Request().request(method='get',url='http://rpa-test.datagrand.com/')
        expect_status=respose.status_code
        print('expect_status',expect_status)
        self.assertEqual(200,expect_status)

    def test_case_post_001(self):
        accountEmail = "gaoxiaoyan%40datagrand.com"
        password = "b29a8e35a7eeb51fd42c6abfb93597d9"

        res=api_login.test_login(accountEmail=accountEmail,password=password)
        self.assertEqual(200,res.status_code)



    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()

