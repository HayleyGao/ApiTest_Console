import  requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
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





if __name__ == '__main__':
    protocol = 'http'
    domain= "rpa-test.datagrand.com"
    port = 80
    tenant="0cc21ce8-f16c-11e9-9f12-0242ac120003"

    # accountEmail = "gaoxiaoyan%40datagrand.com"
    # password = "b29a8e35a7eeb51fd42c6abfb93597d9"
    accountEmail = "gaoxiaoyan@datagrand.com"
    password = "Gaoxiaoyan9533"

    base_url_ = "token?_allow_anonymous=true&selfHandled=yes"
    Authorization = GetToken(accountEmail=accountEmail, password=password, domain=domain, protocol=protocol,port=port,base_url=base_url_).getToken()

    base_url = "protected/v1/app/view/queryApps"

    #case01
    res=AppsApi(protocol,domain,port,Authorization,tenant).apps_get(base_url,page=0,perPage=10)
    print(res.status_code)
    print(res.text)
    #case02
    res_ = AppsApi(protocol, domain, port, Authorization, tenant).apps_get(base_url, page='', perPage='')
    print(res_.status_code)
    print(res_.text)







