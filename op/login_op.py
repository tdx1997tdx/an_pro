from basic_mysql_op import op_database as opsql
from basic_mail_op import send_mail_op as ms
from basic_mail_op import temp_storage as ts

def login_op(username,password):
    conn=opsql.Database()
    sql="select * from user where username=%s and password=%s"
    para=[username, password]
    result =conn.select(sql,para)
    conn.close()
    return '2' if result==[] else '1'

def change_password_op(name,mail):
    conn = opsql.Database()
    sql = "select * from user where username=%s or mail=%s"
    para=[name,mail]
    name_result = conn.select(sql,para)
    if not name_result:
        return '2'
    if (ms.send_email(name_result[0][0], name_result[0][2])):
        return '1'
    else:
        return '3'

def change_password_verification_op(name,mail,new_password,v_code):
    if (ts.temp_storage.get(name) and ts.temp_storage[name]==v_code):
        if (mop.update("update user set password='%s' where username='%s' or mail='%s'" % (new_password, name,mail), conn=conn)):
            ts.temp_storage.pop(name)
            return '1'
        else:
            return '2'
    else:
        return '2'