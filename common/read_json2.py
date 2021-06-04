import  json
import  os

filename="/Users/hayleygao/PycharmProjects/ApiTest_Console/data/login.json"

def read_json(filename):
    with open(filename,'rb') as f:
        data=json.loads(f.read())
        print(data)


if __name__ == '__main__':
    read_json(filename)

    