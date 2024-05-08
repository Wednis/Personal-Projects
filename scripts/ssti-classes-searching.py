def  classes_searching(classes_dict, input_str):
    count_no = 0
    for i in classes_dict:              #遍历传入字典的元素
        count = 0
        if i in input_str:              #判断在传入字符串中是否含有待匹配类
            index = input_str.find(sub_str)         #从头开始匹配
            while index != -1:                      #有匹配项则执行
                count += 1                
                if (input_str.find(i,index+1,index+10+len(i))!=-1):    #在(index+1,index+10+len(i))匹配到i时执行
                    break
                index = input_str.find(sub_str, index+1)         #把下标增加1，越过当前匹配项，使得可以往后匹配
            classes_match_dict[i]=(count-1)       #break跳出while，把匹配到的i作为key，索引作为value赋给classes_match_dict
        else:
            count_no += 1
            continue
    if count_no == len(classes_dict):      #当所有i都匹配不到时执行，即没有匹配的类
        print("No classes found.")
        exit()
    return classes_match_dict

classes_dict1={}                      #1号待匹配字典（输入）
classes_dict2={                       #2号待匹配字典
    "os._wrap_close":"1",
    "warnings.WarningMessage":"2",
    "warnings.catch_warnings":"3",
}
#classes_dict3,classes_dict4....      此处可扩展
classes_match_dict={}              #储存匹配项的字典
sub_str="class "
input_str=input("Input your string:")
methods=input(
"""Choose the following options:
1.search for the specific class (input it yourself,like:type)
2.search for the class that could be used for RCE
Input your choice:""")             #此处可扩展
if methods == "1":
    str2 = input("Input the class you want to search for:")
    classes_dict1[str2]="1"
    classes_searching(classes_dict1, input_str)
if methods == "2":
    classes_searching(classes_dict2, input_str)
#if methoods == "3":      此处可扩展
print("Classes found.")
print(classes_match_dict)



