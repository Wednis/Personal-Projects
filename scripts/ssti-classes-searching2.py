import re

def class_searching(classes_dict, input_str):
    match = re.findall(r'<([^>]+)>', input_str)
    count = 0
    for i in classes_dict:
        for j in match:
            pattern = r"['\"]"+i+r"['\"]"
            if re.findall(pattern, j):
                class_match_dict[i] = count
                break
            else:
                count += 1
        count = 0
    if class_match_dict == {}:
        print("Not Found.")
    else:
        print("Found.")
    return class_match_dict

class_match_dict = {}
class_personal = {}
class_RCE = {
    "os._wrap_close":"1",
    "warnings.WarningMessage":"2",
    "warnings.catch_warnings":"3",
    "site._Printer":"4",
    "file":"5",
    "subprocess.Popen":"6",            #有需要自己添加即可

}
input_str=input("Input your string:")
methods=input(
"""Choose the following options:
1.Search for the specific class. (input it yourself,example:type)
2.Search for the class that could be used for RCE.
Input your choice:""")
if methods == "1":
    pclass = input("Input the class you want to search for:")
    class_personal[pclass] = "1"
    class_searching(class_personal, input_str)
if methods == "2":
    class_searching(class_RCE, input_str)
print(class_match_dict)
