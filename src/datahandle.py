from twisted.internet import threads
from lib import baseHandle
from src.Mglobal import Qmysql
from src.Mglobal import UsrLoginStatue
from src.Mglobal import Mloger
from src import Mglobal
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
    def __init__(self, data, call_back):
        self.call_back = call_back
        self.data = data

    def ret(self, data):
        #self.call_back.write(data)
        pass

    def action(self, data):
        self.call_back.write('data recieved'.encode())
        conn = Qmysql.get()
        Mloger.info('callback is %s'%UsrLoginStatue[self.call_back])

        insertdata = 'insert into data(id,data,time) values(%d,\'%s\',\'%s\''')'%(UsrLoginStatue[self.call_back],data.decode(),Mglobal.Systime.Datatime)
        ans = conn._insert(insertdata)

        if ans == 0:
            Mloger.info("data insert ok!")
            return ans
        else:
            Mloger.error('insert wrong')
            return '0'


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