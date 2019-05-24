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

    def test_get_mail1(self):
        url = 'http://dexuannb.ml/get_mail'
        data = {'name': 'tang'}
        r = requests.post(url, data)
        self.assertEqual('11610103@mail.sustc.edu.cn', r.text)

    def test_get_mail2(self):
        url = 'http://dexuannb.ml/get_mail'
        data = {'name': 'ggh'}
        r = requests.post(url, data)
        self.assertEqual('690076053@qq.com', r.text)

    def test_change_mail1(self):
        url = 'http://dexuannb.ml/change_mail'
        data = {'name': 'tang', 'new_mail': '123@qq.com'}
        r = requests.post(url, data)
        self.assertEqual('3', r.text)

    def test_change_mail2(self):
        url = 'http://dexuannb.ml/change_mail'
        data = {'name': 'tang','new_mail': '99648990@qq.com'}
        r = requests.post(url, data)
        self.assertEqual('1', r.text)

    def test_change_mail_verification1(self):
        url = 'http://dexuannb.ml/change_mail_verification'
        data = {'name': 'tang', 'new_mail': '123@qq.com','verification_code': '2560'}
        r = requests.post(url, data)
        self.assertEqual('2', r.text)

    def test_change_mail_verification2(self):
        url = 'http://dexuannb.ml/change_mail_verification'
        data = {'name': 'tang','new_mail': '99648990@qq.com','verification_code': '5585'}
        r = requests.post(url, data)
        self.assertEqual('2', r.text)

    def test_change_inside_password1(self):
        url = 'http://dexuannb.ml/change_inside_password'
        data = {'name': 'tang', 'old_password': 'tang','new_password': 'tang'}
        r = requests.post(url, data)
        self.assertEqual('1', r.text)

    def test_change_inside_password2(self):
        url = 'http://dexuannb.ml/change_inside_password'
        data = {'name': 'tang','old_password': 'sadasdas','new_password': 'sadasd'}
        r = requests.post(url, data)
        self.assertEqual('2', r.text)

    def test_get_filenames1(self):
        url = 'http://dexuannb.ml/get_filenames'
        data = {'name': 'gght'}
        r = requests.post(url, data)
        self.assertEqual('begin end', r.text)

    def test_get_filenames2(self):
        url = 'http://dexuannb.ml/get_filenames'
        data = {'name': 'hhh'}
        r = requests.post(url, data)
        self.assertEqual('begin end', r.text)

    def test_file_upload1(self):
        url = 'http://dexuannb.ml/file_upload'
        data = {'name': 'ggh', 'filename': 'test2.txt',
                'content': 'askdfjaoidjadifaoi aoidfjaoijdfre vzxcziojdvsfcasfasf'}
        r = requests.post(url, data)
        self.assertEqual('1', r.text)

    def test_file_upload2(self):
        url = 'http://dexuannb.ml/file_upload'
        data = {'name': 'ggt', 'filename': 'test2.txt',
                'content': 'askdfjaoidjadifaoi aoidfjaoijdfre vzxcziojdvsfcasfasf'}
        r = requests.post(url, data)
        self.assertEqual('1', r.text)

    def test_file_download1(self):
        url = 'http://dexuannb.ml/file_download'
        data = {'name': 'ggh', 'filename': 'test2.txt'}
        r = requests.post(url, data)
        self.assertEqual('askdfjaoidjadifaoi aoidfjaoijdfre vzxcziojdvsfcasfasf', r.text)

    def test_file_download2(self):
        url = 'http://dexuannb.ml/file_download'
        data = {'name': 'ggh', 'filename': 'tes.txt'}
        r = requests.post(url, data)
        self.assertEqual('nodata', r.text)

if __name__ == '__main__':
    unittest.main()