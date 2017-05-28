import sys
import os

from twisted.internet.protocol import  ServerFactory,ProcessProtocol
from twisted.protocols.basic import LineReceiver
from src.Mglobal import Mloger
from twisted.internet import reactor
from src import datahandle as dt
import struct
from src import Mglobal
from src.Mglobal import RKey
from src.Mglobal import Define
class MProtocol(LineReceiver):

    delimiter = '\n'
    databuf = bytes()
    uid = 0
    nowid = 0
    def connectionMade(self):

        ipinfo = self.transport.getPeer()
        if len(self.factory.clients) >= self.factory.max_client:
            self.transport.loseConnection()
        else:

            Mloger.info('ip:%s : connect successfully!'%(ipinfo))



    def connectionLost(self, reason):
        print(self.uid)
        Mglobal.UsrLoginStatue[self.uid] = 0
        Mloger.info('ip:%s : lost connect'%self.transport.getPeer())

    #you need to encode databuf before you send them,and decode them before you use those you have recived.
    #In python,the type  str is different from the type byte.


    def dataReceived(self, package):
        print(package)
        #length, command_id = struct.unpack('@2I', package)
        self.databuf += package
        while True:
            #if the length of buffer less than 8(the length of data's head)
            #break
            if len(self.databuf) < 8:
                break

            length, command_id = struct.unpack('@2I', self.databuf[:8])
            if length > len(self.databuf):
                break

            rdata = self.databuf[8:length]

            if command_id not in Mglobal.handlelist:
                #here the data need to be added a package head
                #however,im too lazy to do this
                self.transport.write('wrong command'.encode())
            else:
                self.processCmd(rdata.decode(),command_id)

            #cut the databuffer
            self.databuf = self.databuf[length:]

            if len(self.databuf) < 8:
                break

    def processCmd(self,rdata,command_id):
        Mloger.info("command_id:")
        Mloger.info(command_id)
        Mloger.info("rdata:" + rdata)
        #self.transport.write(rdata.encode())

        if command_id == Define['RECVDATA']:
            testh = dt.dataHandle(rdata,self)
            testh.handle()
        if command_id == 2:
            self.decryptdata(rdata)
            RKey.loadPubkey(rdata)
        if command_id == 3:
            self.decryptdata(rdata)
            RKey.loadPrikey(rdata)
        if command_id == Define['ACCOUNT']:
            print("getuid")
            han = dt.getuid(rdata,self)
            re = han.handle()
        if command_id == Define['Online']:
            line = ''
            flag = 0
            if Mglobal.UsrLoginStatue:
                for k,v in Mglobal.UsrLoginStatue.items():
                    if v == 1:
                        flag = 1
                        line = line + str(k) + ';'
                print(line)
                if flag:
                    self.transport.write(line.encode())
                else:
                    self.transport.write("None".encode())
            else:
                self.transport.write("None".encode())
        if command_id == Define['onlineSS']:
            self.nowid = rdata
            print(rdata)
            han = dt.getssid(rdata,self)
            re = han.handle()
        if command_id == Define['SSDATA']:
            print(rdata)
            han = dt.getssdata(rdata,self)
            re = han.handle()


    def decryptdata(self,data):
        print(data)

class MFactory(ServerFactory):

    protocol = MProtocol

    def __init__(self,max_client):
        self.max_client = max_client
        self.clients = []
        Mloger.info('reactor start...ok!')


if __name__=='__main__':
    reactor.listenTCP(8888,MFactory(3))
    reactor.run()