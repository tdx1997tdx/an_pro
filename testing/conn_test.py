from basic_mysql_op import op_database as op
db=op.Database(op.conn_info2)
l=[i for i in db.select('select * from user where username=%s',['dfdf'])]
print(l)