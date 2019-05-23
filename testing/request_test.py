import requests, json
import time,random,hashlib


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


def py1():
    url = 'http://fanyi.baidu.com/v2transapi'
    data = {
        'query': '人生如戏',
        'from': 'zh',
        'to': 'en',
        'transtype': 'translang',

    }

    headers = {
        'Accept-Language': 'zh - CN, zh;q = 0.9',
        'Content-Type': 'application / x - www - form - urlencoded;charset = UTF - 8',
        'Host': 'fanyi.baidu.com',
        'Origin': 'https: // fanyi.baidu.com',
        "Referer": "http://fanyi.baidu.com/",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    response = requests.post(url, data, headers=headers)
    print(response.content.decode("utf-8"))


def py2():
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = {
        'i': '燃烧',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    data['typoResult'] = 'false'
    u = 'fanyideskweb'
    f = str(int(time.time() * 1000) + random.randint(1, 10))
    c = "ebSeFb%=XZ%T[KZ)c(sy!"
    sign = hashlib.md5((u + '燃烧' + f + c).encode('utf-8')).hexdigest()
    data['salt'] = f
    data['sign'] = sign

    headers = {
        'Content-Type': 'application / x - www - form - urlencoded;charset = UTF - 8',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http: // fanyi.youdao.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    response = requests.post(url, data, headers=headers)
    print(response.content.decode("utf-8"))

v_code=7193
#regist()
#regist_verify(v_code)
#file_test3()
py2()
