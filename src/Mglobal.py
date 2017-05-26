from src import mysqlqueue
from src import config
from src.MTime import mTime
from src.config import logername,filelogname
from lib.log import MLoger
from lib import baseMencrypt
#here store the all globla variable

#the mysql queue,store the all sql handle
Qmysql = mysqlqueue.mysql_queue(config.mysqlMaxHandle, config.Config_mysql)
rc4Flag = 12345
rc5Flag = 12345

handlelist = [0,1,2,3,4,17,55,99,98]

UsrLoginStatue = {}

Systime = mTime()

Mloger = MLoger(logername,filelogname)

RKey = baseMencrypt.RSAencrypt()

Define = {}
Define['SUCCESS'] = 0
Define['ERRORURL'] = -1
Define['ERRORTYPE'] = -2
Define['ERRORPARA']  = -3
Define['ERRORSQL']  = -4
Define['onlineSS'] = 17
Define['SSDATA'] = 55
Define['ACCOUNT'] = 99
Define['Online'] = 98
