from basic_mysql_op import op_database as opsql
from basic_mail_op.op_email import email
from basic_mail_op.op_storage import storage

def register_op(name, mail):
    conn = opsql.Database()
    name_sql="select * from user where username=%s"
    name_para=[name]
    name_result = conn.select(name_sql,name_para)
    if name_result!=[]:
        return '2'
    mail_sql = "select * from user where mail=%s"
    mail_para=[mail]
    mail_result = conn.select(mail_sql,mail_para)
    conn.close()
    if mail_result!=[]:
        return '3'
    email.connect()
    if(email.send_email(name, mail)):
        return '1'
    else:
        return '4'

def register_verification_op(username,password,mail,v_code):
    conn = opsql.Database()
    if (storage.verification(username,v_code)):
        sql="insert into user (username,password,mail) values (%s,%s,%s)"
        para=[username, password,mail]
        is_sucess=conn.iur(sql,para)
        if (is_sucess):
            storage.remove(username)
            return '1'
        else:
            return '2'
    else:
        return '2'
