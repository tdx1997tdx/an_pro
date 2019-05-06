import unittest
from basic_mysql_op import mysql_conn_info as mci
from op import homepage_op as ho
cnn=mci.conn_info2
class WelcomeTest(unittest.TestCase):

    def setUp(self):
        print('test begin')

    def tearDown(self):
        print('test finish')

    def test_get_mail_op1(self):
        self.assertEqual('798637048@qq.com', ho.get_mail_op('tang',cnn))

    def test_get_mail_op2(self):
        self.assertEqual('77777@qq.com', ho.get_mail_op('tang23',cnn))

    def test_change_mail_op1(self):
        self.assertEqual('1',ho.change_mail_op('tang','798637048@qq.com',cnn))

    def test_change_mail_op2(self):
        self.assertEqual('2', ho.change_mail_op('tang23','7777@qq.com',cnn))

    def test_change_mail_verification_op1(self):
        self.assertEqual('2', ho.change_mail_verification_op('tang23','7777@qq.com','4444',cnn))

    def test_change_mail_verification_op2(self):
        self.assertEqual('2', ho.change_mail_verification_op('dfdf','798637048@qq.com','8585',cnn))

    def test_change_inside_password_op1(self):
        self.assertEqual('1', ho.change_inside_password_op('tang','tang','tang',cnn))

    def test_change_inside_password_op2(self):
        self.assertEqual('2', ho.change_inside_password_op('dfdf','798637048@qq.com','8585',cnn))

if __name__ == '__main__':
    unittest.main()