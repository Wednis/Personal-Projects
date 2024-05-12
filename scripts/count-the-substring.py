str=input("Enter the searched string:")
sub_str=input("Enter the string to search for:")
count=0
index=1
while 1:
    if index != -1:
        index = str.find(sub_str,index+1)
        count+=1
    if index == -1:
        break
print(count)
