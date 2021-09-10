import unittest
import json
from api_page.api_login import ApiLogin
import os



class GetToken:

    def getToken(self, protocol, domain, port, apiVersion, accountEmail, password, base_url, params):
        """
        获取登录后的token。
        :return:
        """
        res = ApiLogin(protocol, domain, port, apiVersion).login_post(accountEmail, password, base_url, params)

        result_json = res.json()
        token_ = result_json["result"]["token"]  # dict type.
        token = "Bearer " + token_
        return token

    def getToken_simple(self, responseObject):
        """
        通过响应对象直接获取token。
        :return:
        """
        result_json = responseObject.json()
        token_ = result_json["result"]["token"]  # dict type.
        token = "Bearer " + token_
        return token


if __name__ == '__main__':
    protocol = 'http'
    domain = 'rpa-test.datagrand.com'
    port = 80
    apiVersion = 'v2'
    accountEmail = 'gaoxiaoyan@datagrand.com'
    password = 'b29a8e35a7eeb51fd42c6abfb93597d9'

    base_url = "token"
    params = {"_allow_anonymous": "true", "selfHandled": "yes"}

    token1 = GetToken().getToken(protocol, domain, port, apiVersion, accountEmail, password, base_url, params)
    print('token1:',token1)

    response = ApiLogin(protocol, domain, port, apiVersion).login_post(accountEmail, password, base_url, params)
    token2=GetToken().getToken_simple(response)
    print('token2:',token2)

