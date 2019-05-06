import unittest
from basic_mysql_op import mysql_conn_info as mci
from op import welcome_op as wmo

class WelcomeTest(unittest.TestCase):

    def setUp(self):
        print('test begin')

    def tearDown(self):
        print('test finish')

    def test_get_mail_op1(self):
        self.assertEqual('798637048@qq.com', wmo.login_op('tang',mci.conn_info2))

    def test_get_mail_op2(self):
        self.assertEqual('77777@qq.com', wmo.login_op('tang23',mci.conn_info2))



if __name__ == '__main__':
    unittest.main()