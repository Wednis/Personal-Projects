#采用session结合while，达到六秒上下一百个请求
#在while中嵌入判断导致了速度的下降，果然还是不能用while
session=requests.Session()
url="http://xxxxxx"
count=0
start = time.time()
while 1:
    count+=1
    with session.get(url) as response:
        res=response.content
        print(f'requesting')
    if count ==100:
        break
end = time.time()
print(f'{end - start} seconds')
