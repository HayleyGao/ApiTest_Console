import  unittest
from api_page.api_login import ApiLogin
from api_page.api_userManage import ApiUserManage
from  common.getToken import GetToken
import  json




data={
    "protocol" : "http",
    "ip" : 'rpa-test.datagrand.com',
    "port" : 80,
    "apiVersion" : 'v2',
    "accountEmail" : 'gaoxiaoyan@datagrand.com',
    "password" : 'b29a8e35a7eeb51fd42c6abfb93597d9',
    "tenant":'0cc21ce8-f16c-11e9-9f12-0242ac120003',
    "base_url" : "token",
    "params" : {"_allow_anonymous": "true", "selfHandled": "yes"},

}



class TestLogin(unittest.TestCase):
    """
    登录模块的测试
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.protocol=data["protocol"]
        cls.ip=data["ip"]
        cls.port=data["port"]
        cls.apiVersion=data["apiVersion"]
        cls.accountEmail=data["accountEmail"]
        cls.password=data["password"]
        cls.base_url=data["base_url"]
        cls.params=data["params"]

        cls.url_=f"{cls.protocol}://{cls.ip}:{cls.port}/{cls.apiVersion}"
        res=ApiLogin( cls.protocol,cls.ip,cls.port,cls.apiVersion).login_post(cls.accountEmail, cls.password,
                                                                              cls.base_url,cls.params)
        cls.token = GetToken().getToken_simple(res)
        cls.tenant=data["tenant"]

        cls.headers = {
            'Authorization': cls.token,
            'X-Tenant': cls.tenant,
            'X-Referer': 'Console',
            'Referer': 'http://rpa-test.datagrand.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/93.0.4577.63 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',

        }

        print("测试开始...")



    def test_add_account_get(self):
        params={
            'page':0,
            'perPage':999
        }
        base_url='roles'

        response=ApiUserManage(self.url_).add_account_get(base_url=base_url,params=params,headers=self.headers)
        print(response.text)
        self.assertEqual(response.status_code,200)

    def test_add_account_post(self):
        params={
            'keep':'yes'
        }
        data={
            "accountEmail":"day1sss@13.23",
            "accountName":"day1sss",
            "roleIds":["6afbfe62-e133-41fa-9564-5b6f67fa06e5"]
        }
        base_url='accounts'

        response = ApiUserManage(self.url_).add_account_post(base_url, params, self.headers,data=json.dumps(data))
        print('response.status_code',response.status_code)
        print(response.url)
        print(response.text)
        self.assertEqual(response.status_code,200)



    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束...")


if __name__ == '__main__':
    unittest.main()







