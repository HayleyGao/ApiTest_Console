import  unittest
from  common.request import  Request
import  json
from api_page.api_login import ApiLogin
from common.read_json import   ReadJson
from parameterized import parameterized  #作参数化 比ddt更加直观的一种方法

accountEmail = "gaoxiaoyan@datagrand.com"
password = "Gaoxiaoyan9533"
base_url = "token?_allow_anonymous=true&selfHandled=yes"
domain = "rpa-test.datagrand.com"
port = 80
protocol = 'http'


class GetToken:
    def __init__(self,accountEmail,password,domain,port,protocol,base_url):
        self.accountEmail=accountEmail
        self.password=password
        self.domain=domain
        self.port = port
        self.protocol=protocol
        self.base_url=base_url


    def getToken(self):
        """
        获取登录后的token。
        :return:
        """
        res=ApiLogin(self.protocol,self.domain,self.port).login_post(self.accountEmail,self.password,self.base_url)
        # print(res.status_code)
        # print(res.text)
        # print(res.request.url)
        # return res
        result_json = res.json()
        # print(result_json)
        token_ = result_json["result"]["token"]  # dict type.
        token = "Bearer " + token_
        return token



if __name__ == '__main__':
   token= GetToken(accountEmail,password,domain,port,protocol,base_url).getToken()
   print(token)









