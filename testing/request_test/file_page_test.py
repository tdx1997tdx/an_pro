import unittest
import requests

class Test(unittest.TestCase):

    def setUp(self):
        print('test begin')

    def tearDown(self):
        print('test finish')

    def test_get_filenames1(self):
        url = 'http://dexuannb.ml/get_filenames'
        data = {'name': 'ggh'}
        r = requests.post(url, data)
        self.assertEqual('begin test.txt test2.txt end', r.text)

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
        self.assertEqual('2', r.text)

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