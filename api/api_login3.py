import  requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json


"""
登录RPA console 中遇到的"content-type=form-data;boundary=..."问题。
参考至：
https://www.cnblogs.com/yuerbaobao/p/14645003.html
"""



def test_login(accountEmail,password,url,ip,protocol):
    data = MultipartEncoder(
        {
            "accountEmail": accountEmail,
            "password": password
        }
    )

    headers={
        "Content-Type": data.content_type,
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Host": ip,
        "Referer": protocol+"://"+ip,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "X-Referer": "Console"
    }
    res=requests.post(url=url,data=data,headers=headers)
    return res


if __name__ == '__main__':
    accountEmail="gaoxiaoyan%40datagrand.com"
    password="b29a8e35a7eeb51fd42c6abfb93597d9"
    url = "http://rpa-test.datagrand.com/v2/token?_allow_anonymous=true&selfHandled=yes"
    ip= "rpa-test.datagrand.com"
    protocol='http'
    res=test_login(accountEmail,password,url,ip,protocol)
    print(res.status_code)
    print(res.text)




