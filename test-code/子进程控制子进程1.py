import threading

def a():
    count = 0
    while 1:
        print("yes")
        count+=1
        if count == 10000:
            return 2
        if stop_threads == True:
            break

def b():
    while 1:
        print("no")
        if stop_threads == True:
            break

threads = []
m = threading.Thread(target=a)
m.daemon == 1
threads.append(m)
n = threading.Thread(target=b)
n.daemon == 1
threads.append(n)

stop_threads = False

if __name__ == '__main__':
    for thr in threads:
        thr.start()
    if (a()) == 2:
        stop_threads = True
    for thr in threads:
        thr.join()   
    print("end")
