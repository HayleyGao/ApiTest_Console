from common.read_json import ReadJson


def getData(filename,env):
    """
    根据不同环境更加简短的获取配置文件的值
    :param filename:
    :return:
    """
    data = ReadJson(filename).read_json()
    if env=='v11':
        protocol = data["environment"]["v11"]["protocol"]
        domain = data["environment"]["v11"]["domain"]
        port = data["environment"]["v11"]["port"]
        accountEmail = data["environment"]["v11"]["accountInfo"]["accountEmail"]
        password = data["environment"]["v11"]["accountInfo"]["password"]
        tenant = data["environment"]["v11"]["accountInfo"]["tenant"]
        base_url_login = data["environment"]["v11"]["base_url_login"]



    else:
        #test环境,env="v2/v1"
        protocol = data["environment"]["test"][env]["protocol"]
        domain = data["environment"]["test"][env]["domain"]
        port = data["environment"]["test"][env]["port"]
        accountEmail = data["environment"]["test"][env]["accountInfo"]["accountEmail"]
        password = data["environment"]["test"][env]["accountInfo"]["password"]
        tenant = data["environment"]["test"][env]["accountInfo"]["tenant"]
        base_url_login = data["environment"]["test"][env]["base_url_login"]


    dict = {"protocol": protocol, "domain": domain, "port": port, "accountEmail": accountEmail, "password": password,
            "tenant": tenant,"base_url_login":base_url_login}
    return dict

if __name__ == '__main__':
    filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/config/config.json"
    env="v11"
    print(getData(filename,env))

