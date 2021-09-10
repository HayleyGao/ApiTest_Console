import json
import os


class ReadJson:
    def __init__(self, filename):
        self.filename = filename

    def read_json(self):
        """
        返回dict类型
        :return:
        """
        with open(self.filename, 'rb') as f:
            return json.loads(f.read())


if __name__ == '__main__':
    pass
