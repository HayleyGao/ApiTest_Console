import  requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
from common.getToken import  GetToken

"""
登录RPA console 中遇到的"content-type=form-data;boundary=..."问题。
参考至：
https://www.cnblogs.com/yuerbaobao/p/14645003.html
"""



def test_roles_put(name,robotId,ip,protocol,tenant,Authorization):
    """
    修改机器人名称的接口
    :param name:
    :param robotId:
    :param ip:
    :param protocol:
    :param tenant:
    :return:
    """

    #Authorization = GetToken(accountEmail, password, ip, protocol).getToken()

    data = MultipartEncoder(
        {
            "name": name,
            "robotId": robotId
        }
    )

    headers={
        "Content-Type": data.content_type,
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Host": ip,
        "Referer": protocol+"://"+ip,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "X-Referer": "Console",
        "Authorization":Authorization,
        "X-Tenant":tenant
    }

    #url="http://rpa-test.datagrand.com/v2/roles?keep=yes"
    url = protocol + "://" + ip + '/v2/roles?keep=yes'
    res=requests.put(url=url,data=data,headers=headers)
    return res


if __name__ == '__main__':
    name="%E9%AB%98%E5%B0%8F%E8%89%B3%E7%9A%84robot"
    robotId="5f91d051-cd7f-4385-abee-5a2c75c882f1"

    ip= "rpa-test.datagrand.com"
    protocol='http'
    tenant="0cc21ce8-f16c-11e9-9f12-0242ac120003"

    accountEmail = "gaoxiaoyan%40datagrand.com"
    password = "b29a8e35a7eeb51fd42c6abfb93597d9"

    Authorization = GetToken(accountEmail, password, ip, protocol).getToken()

    res=test_roles_put(name,robotId,ip,protocol,tenant,Authorization)

    print(res.status_code)
    print(res.text)
    print(res.request.url)








