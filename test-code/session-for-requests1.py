#性能与w-f-q2差不多，不过随着requests增多，性能差距必然会逐渐增加
import requests
from requests.sessions import Session
import time


def request(url,session):
    for i in range(100):
        with session.get(url) as response:
            res=response.content
            print(f'requesting to {url}')

session=requests.Session()
url="http://61.147.171.105:49872/"
start = time.time()
request(url=url,session=session)
end = time.time()
print(f'in {end - start} seconds')
