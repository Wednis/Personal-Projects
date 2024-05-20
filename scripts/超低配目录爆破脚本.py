#对于一些有访问请求限制，经常爆429的，可以挂这个脚本慢慢跑，牺牲时间换来不是满地429
import requests

def explosion(target_url, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            for line in file:
                url=target_url+line
                res = requests.get(url=url)
                if res.status_code == 200 :
                    print(url, end='')
            exit()

if __name__ == '__main__':
    url = input("Input the target url:")
    file_path = input("Inupt the file path:")
    explosion(target_url=url, file_path=file_path)
