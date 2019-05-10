import pymysql
conn_info=('127.0.0.1',3306,'tang','dexuan97','cs304_project')
conn_info2=('107.175.17.248',3306,'tang','dexuan97','cs304_project')
class Database:

    def __init__(self,conn_info=conn_info):
        self.conn_info=conn_info
        self.connection = None
        self.cursor =None
        self.connect()

    def connect(self):
        self.connection = pymysql.connect(db=self.conn_info[4], user=self.conn_info[2],
                                          passwd=self.conn_info[3], host=self.conn_info[0],
                                           port=self.conn_info[1],charset='utf8')
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()


    def select(self,sql,para):
        # 执行SQL语句
        try:
            self.cursor.execute(sql,para)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            return []

    def iur(self,sql,para):
        try:
            self.cursor.execute(sql,para)
            self.connection.commit()
        except Exception as e:
            print(e)
            # 发生错误时回滚
            self.connection.rollback()
            return False
        return True
