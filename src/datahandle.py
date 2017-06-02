from twisted.internet import threads
from lib import baseHandle
from src.Mglobal import Qmysql
from src.Mglobal import UsrLoginStatue
from src.Mglobal import Mloger
from src import Mglobal
from src.Mglobal import Define
class identificationHandle(baseHandle.baseDataHandle):

    def __init__(self,data,call_back):
        self.call_back = call_back
        self.data = data

    def ret(self,data):
        print('now is ret %s',data)
        #self.call_back.write(data.encode())

    def action(self,data):
        self.call_back.write('data recieved'.encode())
        conn = Qmysql.get()
        ans = conn._query(data)
        if ans:
            print(ans)
            return ans[0][0]
        else:
            print('can not find data %s',data)
            return '0'

#deferToThread is a

    def handle(self):
        print('ok')
        d = threads.deferToThread(self.action,self.data)
        d.addCallback(self.ret)
        d.addErrback(self.err)

    def err(self,failure):
        print(failure)

class dataHandle(baseHandle.baseDataHandle):
    def __init__(self, ssid,data, se):
        self.se = se
        self.call_back = se.transport
        self.data = data
        self.ssid = ssid

    def ret(self, data):
        #self.call_back.write(data)
        pass

    def action(self, data):
        self.call_back.write('data recieved'.encode())
        conn = Qmysql.get()
        #Mloger.info('callback is %s'%UsrLoginStatue[self.call_back])

        insertdata = 'insert into message(uid,message,data,ssid) values(%d,\'%s\',\'%s\',%s)'%(self.se.uid,data.decode(),Mglobal.Systime.getmysqltime(),self.ssid)
        print(insertdata)
        ans = conn._insert(insertdata)

        if (type(ans) is int) and (ans == 0):
            Mloger.info("data insert ok!")
            Qmysql.put(conn)
            return ans
        else:
            Mloger.error('insert wrong!')
            return '0'


            # deferToThread is a

    def handle(self):
        d = threads.deferToThread(self.action, self.data.encode())
        d.addCallback(self.ret)
        d.addErrback(self.err)

    def err(self, failure):
        Mloger.error(failure)

class getuid(baseHandle.baseDataHandle):
    def __init__(self, data, se):
        self.se = se
        self.call_back = se.transport
        self.data = data

    def ret(self, re):
        #self.call_back.write(data)
        if re != Define['ERRORSQL']:
           self.se.uid = re[0]
           print(re[0])
           Mglobal.UsrLoginStatue[self.se.uid] = 1
        return 0

    def action(self, data):
        self.call_back.write('data recieved'.encode())
        conn = Qmysql.get()
       # Mloger.info('callback is %s'%UsrLoginStatue[self.call_back])

        insertdata = 'select uid from user where usrname=\'%s\''%(data.decode())
        print(insertdata)
        ans = conn._query(insertdata)
        print(ans)
        if (ans[0] == None):
            Mloger.error('query wrong!')
            return Define['ERRORSQL']
        else:
            Mloger.info("select  ok!")
            Qmysql.put(conn)
            return ans[0]



            # deferToThread is a

    def handle(self):
        d = threads.deferToThread(self.action, self.data.encode())
        d.addCallback(self.ret)
        d.addErrback(self.err)

    def err(self, failure):
        Mloger.error(failure)



class getssid(baseHandle.baseDataHandle):
    def __init__(self, uid, se):
        self.se = se
        self.call_back = se.transport
        self.data = uid

    def ret(self, re):
        #self.call_back.write(data)
        if re != Define['ERRORSQL']:
           num = re[1]
           ret = re[0]
           print('num = %d'%num)
           print(ret)
           ans = ''
           for i in range(num):
               da = ret[i]
               ssid = da[0]
               ans = ans + '%d;'%ssid
           self.call_back.write(ans.encode())
        return 0

    def action(self, data):
        conn = Qmysql.get()
       # Mloger.info('callback is %s'%UsrLoginStatue[self.call_back])

        insertdata = 'select ssid  from sensor where uid =%s'%(data.decode())
        print(insertdata)
        ans = conn._queryall(insertdata)
        print(ans)
        if (ans[0] == None):
            Mloger.error('query wrong!')
            return Define['ERRORSQL']
        else:
            Mloger.info("select  ok!")
            Qmysql.put(conn)
            return ans



            # deferToThread is a

    def handle(self):
        d = threads.deferToThread(self.action, self.data.encode())
        d.addCallback(self.ret)
        d.addErrback(self.err)

    def err(self, failure):
        Mloger.error(failure)


class getssdata(baseHandle.baseDataHandle):
    def __init__(self, uid, se):
        self.se = se
        self.call_back = se.transport
        self.data = uid

    def ret(self, re):
        #self.call_back.write(data)
        if re != Define['ERRORSQL']:

           num = re[1]
           ret = re[0]
           print('num = %d'%num)
           print(ret)
           ans = ''
           ans = ans + '%d;'%num
           for i in range(num):
               da = ret[i]
               ssid = da[0]
               ans = ans + '%s;'%ssid
           print(ans)
           self.call_back.write(ans.encode())
        return 0

    def action(self, data):
        conn = Qmysql.get()
       # Mloger.info('callback is %s'%UsrLoginStatue[self.call_back])
        print('do action..')
        insertdata = 'select SQL_NO_CACHE message  from message where uid =%s && ssid = %s order by data desc limit 0,%d'%(self.se.nowid,data.decode(),self.se.shownum)
        print(insertdata)
        ans = conn._queryall(insertdata)
        print(ans)
        if (ans[0] == None):
            Mloger.error('query wrong!')
            return Define['ERRORSQL']
        else:
            Mloger.info("select  ok!")
            Qmysql.put(conn)
            return ans



            # deferToThread is a

    def handle(self):
        d = threads.deferToThread(self.action, self.data.encode())
        d.addCallback(self.ret)
        d.addErrback(self.err)

    def err(self, failure):
        Mloger.error(failure)

class dataSaveHandle(baseHandle.baseDataHandle):
    def __init__(self,info,data):
        pass

    pass