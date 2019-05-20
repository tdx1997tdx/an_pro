from basic_mysql_op import op_database as op
db=op.Database(op.conn_info2)
l=[i for i in db.select('select file_id from file where username=%s',['ggh'])]
print(l)