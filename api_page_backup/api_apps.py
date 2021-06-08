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
    def __init__(self,protocol,ip,port,Authorization,tenant):
        self.url=f"{protocol}://{ip}:{port}/v2/front/apps/"
        self.Authorization=Authorization
        self.tenant=tenant
        self.headers={
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Host": ip,
            "Referer": protocol+"://"+ip,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "X-Referer": "Console",
            "Authorization":self.Authorization,
            "X-Tenant":self.tenant
        }


    def apps_get(self,page,perPage):
        """
        查询所有的应用，按照默认指定的分页。
        :param page:
        :param perPage:
        :return:
        """
        headers=self.headers
        url = self.url
        params={"page":page,"perPage":perPage}
        res=requests.get(url=url,headers=headers,params=params)
        return res

    def versions_get(self,appId,page,perPage):
        """
        查询appId为关键字的版本名称。
        :param appId:
        :param page:
        :param perPage:
        :return:
        """
        headers = self.headers
        url = self.url+'{0}/versions/'.format(appId)
        params={"page":page,"perPage":perPage}
        res = requests.get(url=url, headers=headers, params=params)
        return res


    def sharedAccounts(self,appId,page,perPage):
        """
         查询该应用下的"共享账户/用户"
        :param appId:
        :param page:
        :param perPage:
        :return:
        """
        headers = self.headers
        url = self.url + '{0}/sharedAccounts/'.format(appId)
        params = {"page": page, "perPage": perPage}
        res = requests.get(url=url, headers=headers, params=params)
        return res


    def apps_search(self,appName,page,perPage):
        """
        搜索appName为关键字的应用app.
        :param appName:
        :param page:
        :param perPage:
        :return:
        """
        headers = self.headers
        url = self.url
        params = {"appName":appName,"page": page, "perPage": perPage}
        res = requests.get(url=url, headers=headers, params=params)
        return res





if __name__ == '__main__':
    protocol = 'http'
    ip= "rpa-test.datagrand.com"
    port = 80
    tenant="0cc21ce8-f16c-11e9-9f12-0242ac120003"

    accountEmail = "gaoxiaoyan%40datagrand.com"
    password = "b29a8e35a7eeb51fd42c6abfb93597d9"

    Authorization = GetToken(accountEmail, password, ip, protocol).getToken()


    res=AppsApi(protocol=protocol,ip=ip,port=port,Authorization=Authorization,tenant=tenant).apps_get(page=0,perPage=10)
    print(res.status_code)
    #print(res.text)

    appId="3a8918be-3f80-46e6-9610-6f24074b1686"
    res2=AppsApi(protocol=protocol, ip=ip, port=port, Authorization=Authorization, tenant=tenant).versions_get(appId=appId,page=0,perPage=5)
    #print(res2.text)
    #print(res2.request.url)
    print(res2.status_code)

    res3 = AppsApi(protocol=protocol, ip=ip, port=port, Authorization=Authorization, tenant=tenant).sharedAccounts(
        appId=appId, page=0, perPage=10)
    # print(res3.text)
    print(res3.request.url)
    print(res3.status_code)

    res4 = AppsApi(protocol=protocol, ip=ip, port=port, Authorization=Authorization, tenant=tenant).apps_search(
        appName='email', page=0, perPage=10)
    # print(res3.text)
    print(res4.request.url)
    print(res4.status_code)













