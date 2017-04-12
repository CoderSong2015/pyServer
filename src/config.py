
Config_mysql = {}
Config_mysql['mysqlname'] = 'root'
Config_mysql['mysqlpasswd'] = '123456'
Config_mysql['mysqlurl'] = 'localhost'
Config_mysql['mysqldatabase'] = 'test'
Config_mysql_connect = [
    Config_mysql['mysqlname'],
    Config_mysql['mysqlpasswd'],
    Config_mysql['mysqlurl'],
    Config_mysql['mysqldatabase']
                        ]
mysqlHandleNumber = 5
mysqlMaxHandle = 10

logername = 'Mainserverlog'
filelogname ='Mainserver.log'