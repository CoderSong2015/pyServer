from src import mysqlqueue
from src import config
from src.MTime import mTime
from src.config import logername,filelogname
from lib.log import MLoger
#here store the all globla variable

#the mysql queue,store the all sql handle
Qmysql = mysqlqueue.mysql_queue(config.mysqlMaxHandle, config.Config_mysql)
rc4Flag = 12345
rc5Flag = 12345

handlelist = [0,1,2,3,4]

UsrLoginStatue = {}

Systime = mTime()

Mloger = MLoger(logername,filelogname)

