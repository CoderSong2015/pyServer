from src import mysqlqueue
from src import config
from src.MTime import mTime
from lib.log import logger
#here store the all globla variable

#the mysql queue,store the all sql handle
Qmysql = mysqlqueue.mysql_queue(config.mysqlMaxHandle, config.Config_mysql)
rc4Flag = 12345
rc5Flag = 12345

handlelist = [0,1,2,3,4]

UsrLoginStatue = {}

Systime = mTime()

def exitinit(Ierror):
    logger.info(Ierror)
    logger.info("exitinit...")
    pass