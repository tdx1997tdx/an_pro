from basic_mysql_op import op_database as opsql
from basic_mail_op.op_email import email
from basic_mail_op.op_storage import storage

def login_op(username,password):
    conn=opsql.Database()
    sql="select * from user where username=%s and password=%s"
    para=[username, password]
    result =conn.select(sql,para)
    conn.close()
    return '2' if result==[] else '1'

def change_password_op(name,mail):
    conn = opsql.Database()
    sql = "select username,mail from user where username=%s or mail=%s"
    para=[name,mail]
    result = conn.select(sql,para)
    conn.close()
    if not result:
        return '2'
    email.connect()
    if (email.send_email(result[0][0],result[0][1])):
        return '1'
    else:
        return '3'

def change_password_verification_op(name,mail,new_password,v_code):
    conn = opsql.Database()
    if (storage.verification(name,v_code)):
        sql="update user set password=%s where username=%s or mail=%s"
        para=[new_password, name,mail]
        is_success=conn.iur(sql,para)
        conn.close()
        if (is_success):
            storage.remove(name)
            return '1'
        else:
            return '2'
    else:
        return '2'