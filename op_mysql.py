import pymysql
#conn = pymysql.connect(host='107.175.17.248', port=3306, user='tang', passwd='dexuan97', db='cs304_project')
def select(sql,host='127.0.0.1', port=3306, user='tang', passwd='dexuan97', db='cs304_project'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
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

def insert(sql,host='127.0.0.1', port=3306, user='tang', passwd='dexuan97', db='cs304_project'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
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

def update(sql,host='127.0.0.1', port=3306, user='tang', passwd='dexuan97', db='cs304_project'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
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

def delete(sql,host='127.0.0.1', port=3306, user='tang', passwd='dexuan97', db='cs304_project'):
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
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

#x=[i for i in select("select * from user",host="107.175.17.248")]
#print(x)

#print(insert("insert into user (username,password) values ('%s','%s')"%('tang23','tang2'),host="107.175.17.248"))