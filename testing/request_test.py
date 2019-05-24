import requests, json
import time,random,hashlib
import base64


def regist():
    url = 'http://dexuannb.ml/register'
    data = {'name': 'tang','password':'tang','mail':'798637048@qq.com'}
    r = requests.post(url, data)
    print(r.text)

def regist_verify(v_code):
    url = 'http://dexuannb.ml/register_verification'
    data = {'name': 'tang', 'password': 'tang', 'mail': '798637048@qq.com','verification_code':str(v_code)}
    r = requests.post(url, data)
    print(r.text)

def file_test():
    url = 'http://dexuannb.ml/get_filenames'
    data = {'name': 'ggh'}
    r = requests.post(url, data)
    print(r.text)
def file_test2():
    url = 'http://dexuannb.ml/file_upload'
    data = {'name': 'ggh','filename':'test2.txt','content':'askdfjaoidjadifaoi aoidfjaoijdfre vzxcziojdvsfcasfasf'}
    r = requests.post(url, data)
    print(r.text)

def file_test3():
    url = 'http://dexuannb.ml/file_download'
    data = {'name': 'ggh','filename':'test2.txt'}
    r = requests.post(url, data)
    print(r.text)
def image_test():
    url = 'http://dexuannb.ml/image_translation'
    with open("F:\cs_304_pro/test.jpg", "rb") as f:  # 转为二进制格式
        base64_data = base64.b64encode(f.read())  # 使用base64进行加密
        print(base64_data)
    data = {'image':base64_data,'name':'tang'}
    r = requests.post(url, data)
    print(r.text)


v_code=7193
#regist()
#regist_verify(v_code)
#file_test3()
image_test()
