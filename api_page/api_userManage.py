import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
from common.readConfig import ReadCofig
from common.getToken import GetToken
from api_page.api_login import ApiLogin


class ApiUserManage:
    def __init__(self, url_):
        self.url_=url_


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
    print(res.text)

    token = GetToken().getToken_simple(res)
    # headers = {
    #     'Authorization': token,
    #     'X-Tenant': '0cc21ce8-f16c-11e9-9f12-0242ac120003',
    #     'X-Referer': 'Console',
    #     'Referer': 'http://rpa-test.datagrand.com/',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                   'Chrome/93.0.4577.63 Safari/537.36',
    #     'Accept': 'application/json, text/plain, */*'
    # }
    headers = {
        'Authorization': token,
        'Host': 'rpa-test.datagrand.com',
        'Connection': 'keep-alive',
        'Content-Length': '102',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'Accept-Language': 'zh-CN',
        'X-Referer': 'Console',
        'X-Tenant':'0cc21ce8-f16c-11e9-9f12-0242ac120003',
        'Content-Type':"application/json",
        "Origin": "http://rpa-test.datagrand.com",
        'Referer': 'http://rpa-test.datagrand.com/',
        'Accept-Encoding':"gzip, deflate",
        'Cookie':"mp_da81ae714798a5fc29a48c0d6d4b4f61_mixpanel=%7B%22distinct_id%22%3A%20%2217b52e1202017-024ce6dcab5cd8-3f3a5d0e-1fa400-17b52e12021128%22%2C%22%24device_id%22%3A%20%2217b52e1202017-024ce6dcab5cd8-3f3a5d0e-1fa400-17b52e12021128%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D"
    }

    # params={
    #     'page':0,
    #     'perPage':999
    # }
    # base_url='roles'
    # url_="http://rpa-test.datagrand.com:80/v2"
    # res2=ApiUserManage(url_).add_account_get(base_url, params,headers)
    # print(res2.status_code)
    # print(res2.text)

    # post请求
    params2 = {
        'keep':'yes'
    }
    base_url = 'accounts'
    data={
        'accountEmail': "day090903112@123.123",
        'accountName': "day090902112",
        "roleIds":["e75e702f-c82a-11eb-8865-0242ac140003"]
    }

    #
    url_="http://rpa-test.datagrand.com:80/v2"
    res3 = ApiUserManage(url_).add_account_post(base_url, params2, headers,data=json.dumps(data))
    print('res3.status_code',res3.status_code)
    print(res3.url)
    print(res3.text)

