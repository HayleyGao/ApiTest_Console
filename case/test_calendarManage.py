import unittest
from api_page.api_login import ApiLogin
from common.getToken import GetToken
import json
import requests

data = {
    "protocol": "http",
    "ip": 'rpa-test.datagrand.com',
    "port": 80,
    "apiVersion": 'v2',
    "accountEmail": 'gaoxiaoyan@datagrand.com',
    "password": 'b29a8e35a7eeb51fd42c6abfb93597d9',
    "tenant": '0cc21ce8-f16c-11e9-9f12-0242ac120003',
    "base_url": "token",
    "params": {"_allow_anonymous": "true", "selfHandled": "yes"},

}


class TestCalendarManage(unittest.TestCase):
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
        res = ApiLogin(cls.protocol, cls.ip, cls.port, cls.apiVersion).login_post(cls.accountEmail, cls.password,
                                                                                  cls.base_url, cls.params)
        cls.token = GetToken().getToken_simple(res)
        cls.tenant = data["tenant"]
        cls.headers = {
            'Authorization': cls.token,
            'X-Tenant': cls.tenant,
            'X-Referer': 'Console',
            'Referer': 'http://rpa-test.datagrand.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/93.0.4577.63 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
        }
        print("测试开始...")

    def test_calendar_get(self):
        params = {
            'page': 0,
            'perPage': 10,
            'selfHandled': 'yes'
        }
        base_url = 'calendars'
        url = f"{self.url_}/{base_url}"
        response = requests.get(url=url, params=params, headers=self.headers)
        print(response.text)
        self.assertEqual(response.status_code, 200)

    def test_calendar_post(self):
        params = {
            'keep': 'yes'
        }
        base_url = 'calendars'
        url = f"{self.url_}/{base_url}"
        data = {"name": "carlendar_day091012", "nonWorkingDays": [{"date": "2021-09-14"}, {"date": "2021-09-23"}]}
        response = requests.post(url=url, params=params, headers=self.headers, data=json.dumps(data))
        print(response.text)
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()
