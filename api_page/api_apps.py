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

class AppsApi:
    """
    apps模块的api封装。
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

    def apps_get(self,base_url,page,perPage):
        """
        查询所有的应用，按照默认指定的分页。
        :param page:
        :param perPage:
        :return:
        """
        headers=self.headers
        url=f"{self.url_}/{base_url}"
        params = {"page": page, "perPage": perPage}
        res=requests.get(url=url,headers=headers,params=params)
        return res

    def versions_get(self,base_url,page,perPage):
        """
        查询某个流程的所有版本
        :param page:
        :param perPage:
        :return:
        """
        headers=self.headers
        url=f"{self.url_}/{base_url}"
        params = {"page": page, "perPage": perPage}
        res=requests.get(url=url,headers=headers,params=params)
        return res



    def app_search_get(self,base_url,appName,page,perPage):
        """
        根据流程名称搜索
        :return:
        """
        headers = self.headers
        url = f"{self.url_}/{base_url}"
        params = {"appName": appName, "page": page, "perPage": perPage}
        res = requests.get(url=url, headers=headers, params=params)
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

    base_url="v2/front/apps"
    #case01
    res=AppsApi(protocol,domain,port,Authorization,tenant).apps_get(base_url,page=0,perPage=10)
    print(res.status_code)
    #print(res.text)
    # print(res.request.url)
    # print(res.request.headers)

    appId="ecc7921d-9720-4a25-80f2-49630dd40ed5"
    base_url_versions=f"v2/front/apps/{appId}/versions"
    res_versions = AppsApi(protocol, domain, port, Authorization, tenant).apps_get(base_url=base_url_versions, page=0, perPage=10)
    print(res_versions.status_code)
    print(res_versions.request.url)
    print(res_versions.request.headers)

    base_url_search="v2/front/apps"
    appName = "args"
    res_search = AppsApi(protocol, domain, port, Authorization, tenant).app_search_get(base_url=base_url_search,appName = "args", page=0,
                                                                                   perPage=10)
    print(res_search.status_code)
    print(res_search.request.url)
    print(res_search.request.headers)










