#这个进程控制比1好多了，本来想用local，但是变量作用域不允许子进程更改，啧
import threading
from queue import Queue           #用一个数据的队列来实现

def a():
    count = 0
    while 1:
        count += 1
        print("yes")
        if count == 100:
            judgement.put(1)       #满足某条件则往队列中导入一个数据
            print("load")
            break

def b():
    while 1:
        print("no")
        if judgement.full() == True:       #检测导入数据是否存在
            print("done")
            break

judgement = Queue(maxsize=1)     #限制一个数据

threads = []
m = threading.Thread(target=a)
m.daemon == 1
threads.append(m)
n = threading.Thread(target=b)
n.daemon == 1
threads.append(n)

if __name__ == '__main__':
    for thr in threads:
        thr.start()
    for thr in threads:
        thr.join()              #不要少了
    print("end")
