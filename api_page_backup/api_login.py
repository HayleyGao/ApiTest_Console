import  requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json


"""
登录RPA console 中遇到的"content-type=form-data;boundary=..."问题。
参考至：
https://www.cnblogs.com/yuerbaobao/p/14645003.html
"""
#"http://rpa-test.datagrand.com/v2/token?_allow_anonymous=true&selfHandled=yes"
#http://rpa-test.datagrand.com:80/token?_allow_anonymous=true&selfHandled=yes

def test_login(accountEmail,password,version,base_url,ip,port,protocol):
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
        # "Referer": protocol+"://"+ip,
        "Referer": f"{protocol}://{ip}",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "X-Referer": "Console"
    }
    if version=='':
        # url = f"{protocol}://{ip}:{port}/{version}{base_url}"
        url = f"{protocol}://{ip}:{port}/{base_url}"
    else:
        url = f"{protocol}://{ip}:{port}/{version}/{base_url}"
    res=requests.post(url=url,headers=headers,data=data)
    return res


if __name__ == '__main__':
    # accountEmail="gaoxiaoyan%40datagrand.com"
    # password="b29a8e35a7eeb51fd42c6abfb93597d9"
    accountEmail = "gaoxiaoyan@datagrand.com"
    password = "Gaoxiaoyan9533"
    base_url = "token?_allow_anonymous=true&selfHandled=yes"
    ip= "rpa-test.datagrand.com"
    port=80
    protocol='http'
    # version=None,和''还是不同的。
    version=''
    # version='v2'
    res=test_login(accountEmail,password,version,base_url,ip,port,protocol)
    print(res.status_code)
    print(res.text)
    print(res.request.url)




