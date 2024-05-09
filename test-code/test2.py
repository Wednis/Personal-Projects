import time
import requests

count=0
t1=int(time.time())
while 1:
    re=requests.get(url="http://61.147.171.105:65468/")
    t2=int(time.time())
    count+=1
    if (t2-t1) == 1:
        break
print("end.")
print(count)