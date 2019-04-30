import unittest
from basic_mysql_op import mysql_conn_info as mci
from mysql_op import welcome_mysql_op as wmo

class WelcomeTest(unittest.TestCase):

    def setUp(self):
        print('test begin')

    def tearDown(self):
        print('test finish')

    def test_login_mysql_op1(self):
        self.assertEqual('NOTOK', wmo.login_mysql_op('tang','dexuan',mci.conn_info2))

    def test_login_mysql_op2(self):
        self.assertEqual('OK', wmo.login_mysql_op('tang','tang',mci.conn_info2))

    def test_register_mysql_op1(self):
        self.assertEqual('EXIST', wmo. register_mysql_op('tang','tang',mci.conn_info2))

    def test_register_mysql_op2(self):
        self.assertEqual('EXIST', wmo. register_mysql_op('tang23','tang2',mci.conn_info2))

if __name__ == '__main__':
    unittest.main()