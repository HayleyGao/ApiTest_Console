import  requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json


"""
登录RPA console 中遇到的"content-type=form-data;boundary=..."问题。
参考至：
https://www.cnblogs.com/yuerbaobao/p/14645003.html
"""


def test():
    data = MultipartEncoder(
        {
            "accountEmail": "gaoxiaoyan%40datagrand.com",
            "password": "b29a8e35a7eeb51fd42c6abfb93597d9"
        }
    )

    headers={
        "Content-Type": data.content_type,
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN",
        "Connection": "keep-alive",
        "Content-Length": "296",
        "Host": "rpa-test.datagrand.com",
        "Origin": "http://rpa-test.datagrand.com",
        "Referer": "http://rpa-test.datagrand.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "X-Referer": "Console"
    }
    res=requests.post(url="http://rpa-test.datagrand.com/v2/token?_allow_anonymous=true&selfHandled=yes",data=data,headers=headers)
    print(res.status_code)
    print(res.request.body)
    print(res.text)

if __name__ == '__main__':
    test()


