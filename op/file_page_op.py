from basic_mysql_op import op_database as opsql

def get_filenames_op(name):
    conn = opsql.Database()
    sql = "select filename from file where username=%s"
    para = [name]
    result = 'begin '
    for i in conn.select(sql, para):
        result+= i[0]+' '
    result+='end'
    conn.close()
    return result

def file_upload_op(name,filename,content):
    conn = opsql.Database()
    sql = "select file_id from file where username=%s and filename=%s"
    para = [name,filename]
    result = [i for i in conn.select(sql, para)]
    if result==[]:
        insert_sql = 'insert into file (filename,username,content) values (%s,%s,%s)'
        insert_para=[filename,name,content]
        is_success = conn.iur(insert_sql, insert_para)
        conn.close()
        return '1' if is_success else '2'
    else:
        update_sql = 'update file set content=%s where file_id=%s'
        update_para = [content,result[0][0]]
        is_success = conn.iur(update_sql, update_para)
        conn.close()
        return '1' if is_success else '2'

def file_download_op(name,filename):
    conn = opsql.Database()
    sql = "select content from file where username=%s and filename=%s"
    para = [name,filename]
    result = [i for i in conn.select(sql, para)]
    if result:
        return result[0][0]
    else:
        return 'nodata'
