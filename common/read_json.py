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





if __name__ == '__main__':
    filename = "/Users/hayleygao/PycharmProjects/ApiTest_Console/data/login.json"
    data=ReadJson(filename).read_json()
    #print(data)

    print("-------------------------")
    data2=ReadJson(filename).read_json2_list()
    print(data2)


















