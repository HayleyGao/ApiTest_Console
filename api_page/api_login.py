import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json


"""
登录RPA console 中遇到的"content-type=form-data;boundary=..."问题。
参考至：
https://www.cnblogs.com/yuerbaobao/p/14645003.html
"""


class ApiLogin:
    def __init__(self, protocol, domain, port, apiVersion):
        self.protocol = protocol
        self.domain = domain
        self.port = port
        self.apiVersion = apiVersion
        self.url_ = f"{protocol}://{domain}:{port}/{apiVersion}"

    def login_post(self, accountEmail, password, base_url, params):
        data = MultipartEncoder(
            {
                "accountEmail": accountEmail,
                "password": password
            }
        )

        headers = {
            "Content-Type": data.content_type,
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Host": self.domain,
            "Referer": f"{self.protocol}://{self.domain}",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/90.0.4430.212 Safari/537.36",
            "X-Referer": "Console"
        }

        params = params

        url = f"{self.url_}/{base_url}"
        response = requests.post(url=url, headers=headers, params=params, data=data)
        return response


if __name__ == '__main__':
    protocol = 'http'
    domain = 'rpa-test.datagrand.com'
    port = 80
    apiVersion = 'v2'
    accountEmail = 'gaoxiaoyan@datagrand.com'
    password = 'b29a8e35a7eeb51fd42c6abfb93597d9'

    base_url = "token"
    params = {"_allow_anonymous": "true", "selfHandled": "yes"}

    res = ApiLogin(protocol, domain, port, apiVersion).login_post(accountEmail, password, base_url, params=params)
    print(res.status_code)
    print(res.text)
    print(res.request.url)
