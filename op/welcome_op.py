from basic_mysql_op import op_mysql as mop
from basic_mysql_op import mysql_conn_info as mci
from basic_mail_op import mail_server as ms
from basic_mail_op import temp_storage as ts

def login_op(username,password,conn=mci.get_now_conn_info()):
    sql="select * from user where username='%s' and password='%s'" % (username, password)
    result = [i for i in mop.select(sql, conn=conn)]
    return '2' if not result else '1'

def register_op(name, mail, conn=mci.get_now_conn_info()):
    name_sql="select * from user where username='%s'" % (name)
    name_result = [i for i in mop.select(name_sql, conn=conn)]
    if name_result:
        return '2'
    mail_sql = "select * from user where mail='%s'" % (mail)
    mail_result = [i for i in mop.select(mail_sql, conn=conn)]
    if mail_result:
        return '3'

    if(ms.send_email(name, mail)):
        return '1'
    else:
        return '4'

def register_verification_op(username,password,mail,v_code, conn=mci.get_now_conn_info()):
    if (ts.temp_storage.get(username) and ts.temp_storage[username]==v_code):
        if (mop.insert("insert into user (username,password,mail) values ('%s','%s','%s')" % (username, password,mail), conn=conn)):
            ts.temp_storage.pop(username)
            return '1'
        else:
            return '2'
    else:
        return '2'


def change_password_op(name,mail, conn=mci.get_now_conn_info()):
    sql = "select * from user where username='%s' and  mail='%s'" % (name,mail)
    name_result = [i for i in mop.select(sql, conn=conn)]
    if not name_result:
        return '2'
    if (ms.send_email(name, mail)):
        return '1'
    else:
        return '3'

def change_password_verification_op(name,new_password,v_code, conn=mci.get_now_conn_info()):
    if (ts.temp_storage.get(name) and ts.temp_storage[name]==v_code):
        if (mop.update("update user set password='%s' where username='%s'" % (new_password, name), conn=conn)):
            ts.temp_storage.pop(name)
            return '1'
        else:
            return '2'
    else:
        return '2'