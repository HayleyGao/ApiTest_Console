import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
from common.readConfig import ReadCofig
from common.getToken import GetToken
from api_page.api_login import ApiLogin


class ApiUserManage:
    def __init__(self, protocol, domain, port, apiVersion):
        self.protocol = protocol
        self.domain = domain
        self.port = port
        self.apiVersion = apiVersion
        self.url_ = f"{protocol}://{domain}:{port}/{apiVersion}"

    def add_account_get(self, base_url, params, headers):
        url = f"{self.url_}/{base_url}"
        res = requests.get(url=url, headers=headers, params=params)
        return res

    def add_account_post(self, base_url, params, headers, data):
        url = f"{self.url_}/{base_url}"
        res = requests.post(url=url, headers=headers, params=params, data=data)
        return res


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

    token = GetToken().getToken_simple(res)
    headers = {
        'Authorization': token,
        'X-Tenant': '0cc21ce8-f16c-11e9-9f12-0242ac120003',
        'X-Referer': 'Console',
        'Referer': 'http://rpa-test.datagrand.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.63 Safari/537.36',
        'Accept': 'application/json, text/plain, */*'
    }
    # params={
    #     'page':0,
    #     'perPage':999
    # }
    # base_url='roles'
    # res2=ApiUserManage(protocol, domain, port, apiVersion).add_account_get(base_url, params,headers)
    # print(res2.status_code)
    # print(res2.text)

    # post请求
    params = {
        'keep':'yes'
    }
    base_url = 'accounts'
    data={
        'accountEmail': "day090903@123.123",
        'accountName': "day090902",
        "roleIds":["e75e702f-c82a-11eb-8865-0242ac140003"]
    }
    res3 = ApiUserManage(protocol, domain, port, apiVersion).add_account_get(base_url, params, headers)
    print(res3.status_code,res3.status_code)
    print(res3.content)

