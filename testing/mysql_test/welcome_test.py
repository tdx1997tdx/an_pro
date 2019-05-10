import unittest
from basic_mysql_op import mysql_conn_info as mci
from op import register_op as wmo
cnn=mci.conn_info2
class WelcomeTest(unittest.TestCase):

    def setUp(self):
        print('test begin')

    def tearDown(self):
        print('test finish')

    def test_login_op1(self):
        self.assertEqual('2', wmo.login_op('tang','dexuan',cnn))

    def test_login_op2(self):
        self.assertEqual('1', wmo.login_op('tang','tang',cnn))

    def test_register_op1(self):
        self.assertEqual('2', wmo. register_op('tang','798637048@qq.com',cnn))

    def test_register_op2(self):
        self.assertEqual('2', wmo. register_op('tang23','tang2',cnn))

    def test_register_verification_op1(self):
        self.assertEqual('2', wmo. register_verification_op('tang23','tang2','4403',cnn))

    def test_register_verification_op2(self):
        self.assertEqual('2', wmo. register_verification_op('tang23','tang2','7785',cnn))

    def test_change_password_op1(self):
        self.assertEqual('3', wmo. change_password_op('tang23','4403',cnn))

    def test_change_password_op2(self):
        self.assertEqual('1', wmo. change_password_op('tang','798637048@qq.com',cnn))

    def test_change_password_verification_op1(self):
        self.assertEqual('2', wmo. change_password_verification_op('tang','798637048@qq.com','4399',cnn))

    def test_change_password_verification_op2(self):
        self.assertEqual('2', wmo. change_password_verification_op('dddd','sedfasdf','4455',cnn))

if __name__ == '__main__':
    unittest.main()