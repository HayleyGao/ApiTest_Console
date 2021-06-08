import  requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
from common.readConfig import ReadCofig
from common.read_json import  ReadJson

"""
登录RPA console 中遇到的"content-type=form-data;boundary=..."问题。
参考至：
https://www.cnblogs.com/yuerbaobao/p/14645003.html
"""
#"http://rpa-test.datagrand.com/v2/token?_allow_anonymous=true&selfHandled=yes"
#http://rpa-test.datagrand.com:80/token?_allow_anonymous=true&selfHandled=yes


class ApiLogin:
    def __init__(self,protocol,domain,port):
        self.protocol = protocol
        self.domain=domain
        self.port = port
        self.url_= f"{protocol}://{domain}:{port}"


    def login_post(self,accountEmail,password,base_url):
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
            "Host": self.domain,
            "Referer": f"{self.protocol}://{self.domain}",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "X-Referer": "Console"
        }

        url = f"{self.url_}/{base_url}"
        res=requests.post(url=url,headers=headers,data=data)
        return res


if __name__ == '__main__':
    filename="/Users/hayleygao/PycharmProjects/ApiTest_Console/config/config.ini"
    conf=ReadCofig(filename).readConfig()
    print(conf.options("environment_v11"))

    protocol=conf.get("environment_v11","protocol")
    domain=conf.get("environment_v11", "domain")
    port=conf.get("environment_v11", "port")
    accountEmail=conf.get("environment_v11", "protocol")
    password=conf.get("environment_v11", "protocol")

    base_url = "token?_allow_anonymous=true&selfHandled=yes"


    res=ApiLogin(protocol,domain,port).login_post(accountEmail,password,base_url)
    print(res.status_code)
    print(res.text)
    print(res.request.url)








