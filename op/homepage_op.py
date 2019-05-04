from basic_mysql_op import op_mysql as op
from basic_mysql_op import op_mysql as mop
from basic_mysql_op import mysql_conn_info as mci
from basic_mail_op import mail_server as ms
from basic_mail_op import temp_storage as ts

def change_mail_op(name,old_password,new_password,conn=mci.get_now_conn_info()):
    pass

def change_inside_password_op(name,old_password,new_password,conn=mci.get_now_conn_info()):
    sql="select * from user where username='%s' and password='%s'" % (name, old_password)
    result = [i for i in op.select(sql)]
    if not result:
        return '2'
    if (mop.update("update user set password='%s' where username='%s'" % (new_password, name), conn=conn)):
        return '1'
    else:
        return '2'
