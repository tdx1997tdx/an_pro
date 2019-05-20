import requests, json


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

v_code=7193
#regist()
#regist_verify(v_code)
file_test3()
