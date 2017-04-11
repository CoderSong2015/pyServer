from src import Mglobal
from src import init
from lib import basequeue
from src import mysqlqueue
from src import config
from twisted.internet import reactor
from src.MServer import MFactory
if __name__=='__main__':
    init.Minit()
    reactor.listenTCP(8889, MFactory(3))
    reactor.run()


   # p = Mglobal.Qmysql.get()
   # sqls = "select * from test_table where id = 1 "
   # data = p._query(sqls)
   # print(data[0])
   # print(p._fetchone())
  #  print(p._fetchone())
  #p= mysqlqueue.mysql_queue(config.mysqlMaxHandle,config.Config_mysql)
  #p = mysqlqueue.mysql_queue(3)
  #p.put(1)

  #print(p.get())
   # p.clear()
