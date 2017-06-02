#encoding=utf-8


import pymysql as mysql_module
import queue
import threading


class sql_operate():
    dcur = 0
    USER = 0
    PASSWD = 1
    HOST = 2
    DB = 3
    CHAR_SET = 4
    g_conn = 0
    workqueue = queue.Queue(100)


    def __init__(self,sql_init):
        if isinstance(sql_init,list) and (len(sql_init) >= 4):


            try:
                conn = mysql_module.connect(user=sql_init[self.USER],passwd=sql_init[self.PASSWD],host=sql_init[self.HOST],db=sql_init[self.DB],charset = 'utf8')

                self.g_conn = conn


             #   print(type(dd))
            except:
                print('connect err')
                self.dcur = 'connect err'
            #self.dcur = conn.cursor(mysql_module.cursors.DictCursor) #返回字典cursor（K-V存储结构，python中最重要的类型之一）)
            self.dcur = conn.cursor()
        else:
            dcur =  'not a dict'
    def _query(self,sqls):
        try:
            self.dcur.execute(sqls)
            data = self.dcur.fetchone()
            num = self.dcur.rowcount
            return (data,num)
        except:
            return False


    def _insert(self,sqls):
        try:
     #       self.dcur.execute('set ')
            self.dcur.execute(sqls)
            self.g_conn.commit()
            return self.g_conn.insert_id()
        except:
            return False
    def _update(self,sqls):
        try:
            self.dcur.execute(sqls)
            self.g_conn.commit()
            return True
        except:
            return False

    def _queryall(self,sqls):
        try:
            self.dcur.execute(sqls)
            data = self.dcur.fetchall()
            num = self.dcur.rowcount
            return (data,num)
        except:
            return False
    def _fetchall(self):
        return self.dcur.fetchall()


    def _fetchone(self):
        #返回一行结果，知道返回为NONE
        return self.dcur.fetchone()


    def _getrowcount(self):
        #返回结果的条数
        return self.dcur.rowcount
    def _rollback(self):
        return self.g_conn.rollback()
    def __del__(self):
        try:
            self.dcur.close()
            self.g_conn.close()
        except:
            pass


if __name__ == '__main__':
    c = ['root','123456','localhost','test']
    p = sql_operate(c)
    sqls = "select * from data where id = 1 "
    print(sqls)
    data =  p._query(sqls)
    print(data[0])
    print(p._fetchone())
    print(p._fetchone())
    del p
#data = p.query('update mes_1 set name = \'hao\' where name = \'dwa\'')


#if data[1] != 0:
#    print(data[0])