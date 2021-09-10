import unittest
from api_page.api_login import ApiLogin
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import  logging


data = {
    "protocol": "http",
    "ip": 'rpa-test.datagrand.com',
    "port": 80,
    "apiVersion": 'v2',
    "accountEmail": 'gaoxiaoyan@datagrand.com',
    "password": 'b29a8e35a7eeb51fd42c6abfb93597d9',

    "base_url": "token",
    "params": {"_allow_anonymous": "true", "selfHandled": "yes"}
}


class TestLogin(unittest.TestCase):
    """
    登录模块的测试
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.protocol = data["protocol"]
        cls.ip = data["ip"]
        cls.port = data["port"]
        cls.apiVersion = data["apiVersion"]
        cls.accountEmail = data["accountEmail"]
        cls.password = data["password"]
        cls.base_url = data["base_url"]
        cls.params = data["params"]
        cls.url_ = f"{cls.protocol}://{cls.ip}:{cls.port}/{cls.apiVersion}"
        cls.headers = {
            'X-Referer': 'Console',
            'Referer': "http://rpa-test.datagrand.com",
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/93.0.4577.63 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
        }
        print("测试开始...")

    def test00_login_post(self):
        url = f"{self.url_}/{self.base_url}"
        params = {
            '_allow_anonymous': 'yes',
            'selfHandled': 'yes'
        }

        data_ = MultipartEncoder(
            {
                "accountEmail": self.accountEmail,
                "password": self.password
            }
        )

        # response = requests.post(url=url, params=params, headers=self.headers, data=data_)
        response = ApiLogin(self.protocol, self.ip, self.port, self.apiVersion).login_post(self.accountEmail,
                                                                                           self.password, self.base_url,
                                                                                           self.params)
        print(response.url)
        print(response.text)
        self.assertEqual(response.status_code, 200)
        logging.info(f"case:login:{response.url},method:{response.request.method},headers:{response.request.headers},body：{response.request.body}")


    def test01_login_post(self):
        url = f"{self.url_}/{self.base_url}"
        params = {
            '_allow_anonymous': 'true',
            'selfHandled': 'yes'
        }

        data_ = MultipartEncoder(
            {
                "accountEmail": self.accountEmail,
                "password": self.password
            }
        )
        self.headers["Content-Type"] = data_.content_type  # 添加该字段
        # 考虑到请求头中有个特殊的字段：Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryhrQYt10rQO3cYws3

        response = requests.post(url=url, headers=self.headers, params=params, data=data_)
        # response=ApiLogin( self.protocol,self.ip,self.port,self.apiVersion).login_post(self.accountEmail,
        # self.password, self.base_url,self.params)

        print(response.url)
        print(response.text)
        self.assertEqual(response.status_code, 200)
        logging.info(f"case:login:{response.url},method:{response.request.method},headers:{response.request.headers},body：{response.request.body}")


    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()
