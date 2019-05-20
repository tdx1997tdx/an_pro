from basic_mysql_op import op_database as opsql
from basic_mail_op import op_email as ope
from basic_mail_op.op_storage import storage

def get_filenames_op(name):
    conn = opsql.Database()
    sql = "select mail from user where username=%s"
    para = [name]
    result = conn.select(sql, para)
    conn.close()
    return result[0][0]