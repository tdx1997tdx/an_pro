import pymysql
import basic_mysql_op.mysql_conn_info as info

def select(sql,conn=info.get_now_conn_info()):
    conn = pymysql.connect(host=conn[0], port=conn[1], user=conn[2], passwd=conn[3], db=conn[4])
    cursor = conn.cursor()
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        yield row
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

def insert(sql,conn=info.get_now_conn_info()):
    conn = pymysql.connect(host=conn[0], port=conn[1], user=conn[2], passwd=conn[3], db=conn[4])
    cursor = conn.cursor()
    # 执行SQL语句
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        # 发生错误时回滚
        conn.rollback()
        return False
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return True

def update(sql,conn=info.get_now_conn_info()):
    conn = pymysql.connect(host=conn[0], port=conn[1], user=conn[2], passwd=conn[3], db=conn[4])
    cursor = conn.cursor()
    # 执行SQL语句
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()
        return False
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return True

def delete(sql,conn=info.get_now_conn_info()):
    conn = pymysql.connect(host=conn[0], port=conn[1], user=conn[2], passwd=conn[3], db=conn[4])
    cursor = conn.cursor()
    # 执行SQL语句
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()
        return False
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return True