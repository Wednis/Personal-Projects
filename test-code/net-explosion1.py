import requests

def explosion(target_url, file_path, thread):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            for line in file:
                res = requests.get(url=target_url+line)
                print(res.content)
                print()
            break
        exit()

if __name__ == '__main__':
    url = input("Input the target url:")
    file_path = input("Inupt the file path:")
    thread = input("Input the thread :")
    explosion(target_url=url, file_path=file_path, thread=thread)
