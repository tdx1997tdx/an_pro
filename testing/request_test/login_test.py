import unittest
import requests

class Test(unittest.TestCase):

    def setUp(self):
        print('test begin')

    def tearDown(self):
        print('test finish')

    def test_login1(self):
        url = 'http://dexuannb.ml/login'
        data = {'name': 'tang','password':'tang'}
        r = requests.post(url, data)
        self.assertEqual('1', r.text)

    def test_login2(self):
        url = 'http://dexuannb.ml/login'
        data = {'name': 'tang','password':'tang22'}
        r = requests.post(url, data)
        self.assertEqual('2', r.text)

    def test_change_password1(self):
        url = 'http://dexuannb.ml/change_password'
        data = {'name': 'tabg'}
        r = requests.post(url, data)
        self.assertEqual('2', r.text)

    def test_change_password2(self):
        url = 'http://dexuannb.ml/change_password'
        data = {'mail':'798637048@qq.com'}
        r = requests.post(url, data)
        self.assertEqual('1', r.text)


    def test_change_password_verification1(self):
        url = 'http://dexuannb.ml/change_password_verification'
        data = {'name': 'tang','new_password': 'tang','verification_code': '5565'}
        r = requests.post(url, data)
        self.assertEqual('2', r.text)

    def test_change_password_verification2(self):
        url = 'http://dexuannb.ml/change_password_verification'
        data = {'name': 'tang23', 'new_password': 'tang555', 'verification_code': '9856'}
        r = requests.post(url, data)
        self.assertEqual('2', r.text)


if __name__ == '__main__':
    unittest.main()