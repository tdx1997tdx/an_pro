import requests, json

url = 'http://dexuannb.ml/login'
data = {'name': 'tang'}
r = requests.post(url, data)
print(r)
print(r.text)
print(r.content)