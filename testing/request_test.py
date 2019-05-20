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
v_code=7193
#regist()
regist_verify(v_code)