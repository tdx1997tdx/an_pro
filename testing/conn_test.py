from basic_mysql_op import mysql_conn_info as mci
from op import register_op as wmo
wmo.register_mysql_op('tang','dexuan',mci.conn_info2)