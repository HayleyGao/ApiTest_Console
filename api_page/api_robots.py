import  requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
import os
from common.getData import getData
from common.getToken import  GetToken
#Authorization = GetToken(accountEmail, password, ip, protocol).getToken()


"""
登录RPA console 中遇到的"content-type=form-data;boundary=..."问题。
参考至：
https://www.cnblogs.com/yuerbaobao/p/14645003.html
"""

class RobotsApi:
    """
    robots模块的api封装。
    """
    def __init__(self,protocol,domain,port,Authorization,tenant):
        self.protocol=protocol
        self.domain=domain
        self.port=port
        self.url_=f"{protocol}://{domain}:{port}"
        self.Authorization=Authorization
        self.tenant=tenant
        self.headers={
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Host": domain,
            "Referer":f"{self.protocol}://{self.domain}",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "X-Referer": "Console",
            "Authorization":self.Authorization,
            "X-Tenant":self.tenant
        }

    def robots_get(self,base_url,page,perPage):
        """
        查询所有的robots，按照默认指定的分页。
        :param page:
        :param perPage:
        :return:
        """
        headers=self.headers
        url=f"{self.url_}/{base_url}"
        params = {"page": page, "perPage": perPage}
        res=requests.get(url=url,headers=headers,params=params)
        return res

    def robots_put(self,base_url,robotId,name):
        """
        修改robots名称
        :return:
        """
        headers = self.headers
        url = f"{self.url_}/{base_url}"
        data = {"robotId": robotId,"name": name}
        res = requests.put(url=url, headers=headers,data=data)
        return res






if __name__ == '__main__':
    top_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    configFile = os.path.join(top_dir, "config", "config.json")
    # print("configFile",configFile)
    data = getData(configFile, "v11")
    # print(data)

    # 获取配置文件内的参数
    protocol = data["protocol"]
    domain = data["domain"]
    port = data["port"]
    accountEmail = data["accountEmail"]
    password = data["password"]
    tenant = data["tenant"]
    base_url_login = data["base_url_login"]

    Authorization = GetToken(accountEmail, password, domain, port, protocol, base_url_login).getToken()
    print('Authorization',Authorization)

    base_url="v2/robots"
    #robots
    res=RobotsApi(protocol,domain,port,Authorization,tenant).robots_get(base_url,page=0,perPage=10)
    print(res.status_code)
    # print(res.text)
    print(res.request.url)
    # print(res.request.headers)
    print("==================================")

    #put
    robotId="a56e0a6b-1e27-42c1-9ca3-f6162eb23177"
    base_url=f"v2/robots/{robotId}"
    name="robot_caiwenjie_PC_updated"
    res_put = RobotsApi(protocol, domain, port, Authorization, tenant).robots_put(base_url,robotId,name)
    print(res_put.status_code)
    print(res_put.text)
    print(res_put.request.url)
    print("==================================")






