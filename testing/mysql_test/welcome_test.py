import unittest
from basic_mysql_op import mysql_conn_info as mci
from op import welcome_op as wmo

class WelcomeTest(unittest.TestCase):

    def setUp(self):
        print('test begin')

    def tearDown(self):
        print('test finish')

    def test_login_op1(self):
        self.assertEqual('2', wmo.login_op('tang','dexuan',mci.conn_info2))

    def test_login_op2(self):
        self.assertEqual('1', wmo.login_op('tang','tang',mci.conn_info2))

    def test_register_op1(self):
        self.assertEqual('2', wmo. register_op('tang','798637048@qq.com',mci.conn_info2))

    def test_register_op2(self):
        self.assertEqual('2', wmo. register_op('tang23','tang2',mci.conn_info2))

    def test_register_verification_op1(self):
        self.assertEqual('2', wmo. register_verification_op('tang23','tang2','4403',mci.conn_info2))

    def test_register_verification_op2(self):
        self.assertEqual('2', wmo. register_verification_op('tang23','tang2','7785',mci.conn_info2))

    def test_change_password_op_op1(self):
        self.assertEqual('2', wmo. register_verification_op('tang23','tang2','4403',mci.conn_info2))

    def test_change_password_op_op2(self):
        self.assertEqual('2', wmo. register_verification_op('tang23','tang2','4403',mci.conn_info2))

if __name__ == '__main__':
    unittest.main()