from basic_mysql_op import op_mysql as op


def update_infomation_mysql_op(username,password):
    sql="select * from user where username='%s' and password='%s'" % (username, password)
    result = [i for i in op.select(sql)]
    return 'NOTOK' if result == [] else 'OK'
