import  requests
import  json
from collections import OrderedDict
import requests
import re


class Request:


    def request(self,method,url, data=None, json=None,params=None, **kwargs):
        response=None
        if method=='get':
            response=requests.get(url=url, params=params, **kwargs)
        elif method=='post':
            response=requests.post(url=url, data=data, json=json, **kwargs)
        elif method=='put':
            response=requests.put(url=url, data=data, **kwargs)
        elif method=='delete':
            response=requests.delete(url=url, **kwargs)
        else:
            print('method %s 不在支持范围内。'%method)


        return response

if __name__ == '__main__':
    response1=Request().request(method='get',url="http://www.baidu.com")
    #print(response1.status_code)

    response2=requests.get("http://www.baidu.com")
    #print(response2.status_code)

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN",
        "Connection": "keep-alive",
        "Content-Length":"296",
        "Content-Type":"multipart/form-data",
        "Host": "rpa-test.datagrand.com",
        "Origin": "http://rpa-test.datagrand.com",
        "Referer": "http://rpa-test.datagrand.com/",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
        "X-Referer": "Console"

    }
    print(type(headers))
    print(type(json.dumps(headers)))

    params = OrderedDict([("accountEmail", (None, 'gaoxiaoyan%40datagrand.com')),
                  ("password", (None, 'b29a8e35a7eeb51fd42c6abfb93597d9'))])

    res = requests.post('http://www.baidu.com', files=params,headers=headers)
    print(res.status_code)
    print(res.text)
    print(res.request.body.decode("utf-8"))














