from src import config
from lib import sql_operator
from src import Mglobal

#here init all

def Minit():
    if config.mysqlMaxHandle < config.mysqlHandleNumber:
        Mglobal.exitinit("wrong config:101")

    for i in range (config.mysqlHandleNumber):
        p = sql_operator.sql_operate(config.Config_mysql_connect)
        Mglobal.Qmysql.put(p)