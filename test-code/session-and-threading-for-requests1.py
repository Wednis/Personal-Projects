#，不要开debug，会变慢
#10线程，100请求，0.5s  1000请求，3.5s
#20线程，100请求，0.3s  1000请求，2s
#下版本：异步请求/请求头优化/缓存优化
import requests
import time
import threading
from queue import Queue

all = threading.local()               #为多线程设置共享变量
data_que = Queue(maxsize=0)           #设置队列，多个线程都从该队列中取数据（这里主要是为了测试100个请求多久）

def set_session():                    #设置同一session，使多个线程都使用了该session
    if not hasattr(all,'session'):
        all.session = requests.Session()
    return all.session

def request():
    session = set_session()           #获取session
    while True:
        url=data_que.get()            #从队列中取出一个数据
        with session.get(url) as response:              #请求
            print(f'requesting to {url}')
        data_que.task_done()          #告诉队列管理器处理完成，以便进行下一步


url = "http://xxxxxx"
for i in range(100):
    data_que.put(url)                 #往队列中塞入100个url
start = time.time()
for i in range(10):               #创建10个线程
    thre = threading.Thread(target=request)         #创建线程
    thre.daemon = True           #设置全为守护进程，防止程序无法退出
    thre.start()                 #启动线程
data_que.join()                  #等待队列中数据获取结束
end = time.time()
print(f'in {end - start} seconds')
