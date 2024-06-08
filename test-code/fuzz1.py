import requests
import os

class fuzz:
    script_dir = os.path.dirname(os.path.abspath(__file__))       #获取当前目录
    dicts = {
        '1':'linux-fuzz.txt',
        '2':'php-linux-fuzz.txt',
        }
    result = {}
    def start(self, dict_number, url, req_method):
        session = requests.Session()
        fuzz_dict = os.path.join(self.script_dir, self.dicts[dict_number])       #获取字典路径
        id = 0
        if req_method == 'GET':
            with open(fuzz_dict, 'r') as file:
                for line in file:
                    line = line.rstrip("\n")           #去除换行符
                    url = url.replace('!#!', line)     #替换指定位置
                    res = session.get(url=url)
                    id += 1
                    if res.status_code != 429 and res.status_code != 404:
                        print(f'line:{line}\tstatus_code:{res.status_code}\tresponse_length:{len(res.text)}')
                        self.result[id] = [line, res.status_code, len(res.text)]
        print(self.result)

    #接口
    def start(self):
        dict_number = input('Input the dict_number:')
        url = input('Input the url:')
        req_method = input('Input the req_methods:')
        self.fuzz(dict_number=dict_number, url=url, req_method=req_method)

if __name__ == '__main__':
    Fuzz =fuzz()
    dict_number = input('Input the dict_number:')
    url = input('Input the url:')
    req_method = input('Input the req_methods:')
    Fuzz.start(dict_number=dict_number, url=url, req_method=req_method)
