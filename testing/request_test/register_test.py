import unittest
import requests

class Test(unittest.TestCase):

    def setUp(self):
        print('test begin')

    def tearDown(self):
        print('test finish')

    def test_register1(self):
        url = 'http://dexuannb.ml/register'
        data = {'name': 'tang','password':'tang','mail':'798637048@qq.com'}
        r = requests.post(url, data)
        self.assertEqual('2', r.text)

    def test_register2(self):
        url = 'http://dexuannb.ml/register'
        data = {'name': 'tangdddd','password':'tang22','mail':'798637048@qq.com'}
        r = requests.post(url, data)
        self.assertEqual('3', r.text)

    def test_register_verification1(self):
        url = 'http://dexuannb.ml/register_verification'
        data = {'name': 'tangdddd','password':'tang22','mail':'798637048@qq.com','verification_code':'2562'}
        r = requests.post(url, data)
        self.assertEqual('2', r.text)

    def test_register_verification2(self):
        url = 'http://dexuannb.ml/register_verification'
        data = {'name': 'tabg','password':'sdasd','mail':'798637048@qq.com','verification_code':'5562'}
        r = requests.post(url, data)
        self.assertEqual('2', r.text)


if __name__ == '__main__':
    unittest.main()