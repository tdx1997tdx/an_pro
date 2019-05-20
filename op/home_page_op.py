from basic_mysql_op import op_database as opsql
from basic_mail_op import op_email as ope
from basic_mail_op.op_storage import storage

def get_mail_op(name):
    conn=opsql.Database()
    sql = "select mail from user where username=%s"
    para=[name]
    result = [i for i in conn.select(sql,para)]
    conn.close()
    return result[0][0]

def change_mail_op(name,new_mail):
    conn = opsql.Database()
    sql = "select mail from user where mail=%s"
    para=[new_mail]
    result = [i for i in conn.select(sql,para)]
    conn.close()
    if result!=[]:
        return '2'
    email = ope.Email()
    if (email.send_email(name, new_mail)):
        return '1'
    else:
        return '3'


def change_mail_verification_op(name,new_mail,verification_code):
    conn = opsql.Database()
    if (storage.verification(name,verification_code)):
        sql="update user set mail=%s where username=%s"
        para=[new_mail, name]
        is_success=conn.iur(sql,para)
        conn.close()
        if (is_success):
            storage.remove(name)
            return '1'
        else:
            return '2'
    else:
        return '2'

def change_inside_password_op(name,old_password,new_password):
    conn = opsql.Database()
    sql="select username from user where username=%s and password=%s"
    para=[name, old_password]
    result = [i for i in conn.select(sql,para)]
    if not result:
        return '2'
    sql2="update user set password=%s where username=%s"
    para2=[new_password, name]
    is_success=conn.iur(sql2,para2)
    conn.close()
    if (is_success):
        return '1'
    else:
        return '2'
