from basic_mysql_op import op_mysql as op
from basic_mysql_op import op_mysql as mop
from basic_mysql_op import mysql_conn_info as mci
from basic_mail_op import send_mail_op as ms
from basic_mail_op import temp_storage as ts

def get_mail_op(name):
    sql = "select mail from user where username='%s'" % (name)
    result = [i for i in op.select(sql)]
    return result[0][0]

def change_mail_op(name,new_mail):
    if (ms.send_email(name, new_mail)):
        return '1'
    else:
        return '2'


def change_mail_verification_op(name,new_mail,verification_code,conn=mci.get_now_conn_info()):
    if (ts.temp_storage.get(name) and ts.temp_storage[name] == verification_code):
        if (mop.update("update user set mail='%s' where username='%s'" % (new_mail, name), conn=conn)):
            ts.temp_storage.pop(name)
            return '1'
        else:
            return '2'
    else:
        return '2'

def change_inside_password_op(name,old_password,new_password,conn=mci.get_now_conn_info()):
    sql="select * from user where username='%s' and password='%s'" % (name, old_password)
    result = [i for i in op.select(sql)]
    if not result:
        return '2'
    if (mop.update("update user set password='%s' where username='%s'" % (new_password, name), conn=conn)):
        return '1'
    else:
        return '2'
