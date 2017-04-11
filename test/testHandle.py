
from twisted.internet import threads

class testhandle():

    def __init__(self,data,call_back):
        self.call_back = call_back
        self.data = data

    def ret(self,data):
        self.call_back.write(data)

    def action(self,data):
        print(data)
        return data + b':after handle'

#deferToThread is a

    def handle(self):
        print('ok')
        d = threads.deferToThread(self.action,self.data.encode())
        d.addCallback(self.ret)
        d.addErrback(self.err)

    def err(self,failure):
        print(failure)

