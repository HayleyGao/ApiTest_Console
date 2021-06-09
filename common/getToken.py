import  unittest
from  common.request import  Request
import  json
from api_page.api_login import ApiLogin
from common.read_json import   ReadJson
from parameterized import parameterized  #作参数化 比ddt更加直观的一种方法
import os
from common.getData import getData





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
    top_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    configFile = os.path.join(top_dir, "config", "config.json")
    # print("configFile",configFile)
    data = getData(configFile, "v11")
    #print(data)

    #获取配置文件内的参数
    protocol = data["protocol"]
    domain = data["domain"]
    port = data["port"]
    accountEmail = data["accountEmail"]
    password = data["password"]
    tenant = data["tenant"]
    base_url_login=data["base_url_login"]


    token= GetToken(accountEmail,password,domain,port,protocol,base_url_login).getToken()
    print(token)









