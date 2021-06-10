import  json
import  os


class ReadJson:
    def __init__(self,filename):
        self.filename=filename


    def read_json(self):
        """
        返回dict类型
        :return:
        """
        with open(self.filename,'rb') as f:
            return json.loads(f.read())


    def read_json2_list(self):
        """
        返回list类型
        :return:
        """
        list = []
        with open(self.filename,'rb') as f:
            data=json.loads(f.read())
            for item in data:
                list_=[]
                for li in data[item]:
                    list_.append(data[item][li])
                list.append(tuple(list_))
        return list


    def dict_to_parameterized(self,dict):
        """
        字典格式转换为parameterized可以使用的[(),(),()]格式。
        :param key:
        :return:
        """
        parameterized = []
        for li in dict:
            dict_ = dict[li]
            list_value = []
            for k, v in dict_.items():
                list_value.append(v)
            parameterized.append(tuple(list_value))
        return parameterized






if __name__ == '__main__':
    filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/login_v11.json"
    # filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/robot.json"
    #filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/config/config.json"

    # print("-------------------------")
    # data2=ReadJson(filename).read_json2_list()
    # print(data2)

    filename="/Users/hayleygao/PycharmProjects/ApiTest_Console/data/apps.json"
    data=ReadJson(filename).read_json()
    #print(data)
    print("===================")
    apps_dict=data["apps"]
    #print(apps_dict)
    apps=ReadJson(filename).dict_to_parameterized(apps_dict)
    print(apps)





































