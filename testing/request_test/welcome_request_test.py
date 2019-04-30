import unittest
from basic_mysql_op import mysql_conn_info as mci
from mysql_op import welcome_mysql_op as wmo
import requests

class WelcomeTest(unittest.TestCase):

    def setUp(self):
        print('test begin')

    def tearDown(self):
        print('test finish')

    def test_login_respond1(self):
        url = 'http://dexuannb.ml/login'
        data = {'username': 'tang','password':'tang'}
        r = requests.post(url, data)
        self.assertEqual('OK', r.text)

    def test_login_respond2(self):
        url = 'http://dexuannb.ml/login'
        data = {'username': 'tang','password':'tang22'}
        r = requests.post(url, data)
        self.assertEqual('NOTOK', r.text)

    def test_register_respond1(self):
        url = 'http://dexuannb.ml/register'
        data = {'username': 'tang','password':'tang22'}
        r = requests.post(url, data)
        self.assertEqual('EXIST', r.text)

    def test_register_respond2(self):
        url = 'http://dexuannb.ml/register'
        data = {'username': 'tang23','password':'tang22'}
        r = requests.post(url, data)
        self.assertEqual('EXIST', r.text)

if __name__ == '__main__':
    unittest.main()