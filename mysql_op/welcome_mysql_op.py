from basic_mysql_op import op_mysql as op
from basic_mysql_op import mysql_conn_info as mci

def login_mysql_op(username,password,conn=mci.get_now_conn_info()):
    sql="select * from user where username='%s' and password='%s'" % (username, password)
    result = [i for i in op.select(sql,conn=conn)]
    return 'NOTOK' if result == [] else 'OK'

def register_mysql_op(username,password,conn=mci.get_now_conn_info()):
    sql="select * from user where username='%s'" % (username)
    result = [i for i in op.select(sql,conn=conn)]
    def insert_new_user():
        if (op.insert("insert into user (username,password) values ('%s','%s')" % (username, password),conn=conn)):
            return 'ROK'
        else:
            return 'RNOTOK'
    return insert_new_user() if result == [] else 'EXIST'