import  requests


class Request:
    def get(self,url, params=None, **kwargs):
        requests.get(url=url, params=params, **kwargs)

    def post(self,url, data=None, json=None, **kwargs):
        requests.post(url=url, data=data, json=json, **kwargs)

    def put(self,url, data=None, **kwargs):
        requests.put(url=url, data=data, **kwargs)

    def delete(self,url, **kwargs):
        requests.delete(url=url, **kwargs)


    def request(self,method,url, data=None, json=None, **kwargs):
        response=None
        if method=='get':
            response=self.get(url=url, params=None, **kwargs)
        elif method=='post':
            response=self.post(url=url, data=data, json=json, **kwargs)
        elif method=='put':
            response=self.put(url=url, data=data, **kwargs)
        elif method=='delete':
            response=self.delete(url=url, **kwargs)
        else:
            print('method不在支持范围内。')

        return response

if __name__ == '__main__':
    response1=Request().request(method='get',url="http://www.baidu.com")
    print(response1)

    response2=requests.get("http://www.baidu.com")
    print(response2.status_code)
    