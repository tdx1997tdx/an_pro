from basic_mysql_op import op_database as op
db=op.Database(op.conn_info2)
print(next(db.select('select * from user',[])))