import sys
import os

from twisted.internet.protocol import  ServerFactory,ProcessProtocol
from twisted.protocols.basic import LineReceiver
from lib.log import logger
from twisted.internet import reactor
from src import datahandle as dt
import struct
from src import Mglobal
class MProtocol(LineReceiver):

    delimiter = '\n'
    databuf = bytes()

    def connectionMade(self):

        ipinfo = self.transport.getPeer()
        if len(self.factory.clients) >= self.factory.max_client:
            self.transport.loseConnection()
        else:

            logger.info('ip:%s : connect successfully!'%(ipinfo))
        Mglobal.UsrLoginStatue[self.transport] = 1


    def connectionLost(self, reason):
        logger.info('a connection lost')

    #you need to encode databuf before you send them,and decode them before you use those you have recived.
    #In python,the type  str is different from the type byte.


    def dataReceived(self, package):
        self.databuf += package

        while True:
            #if the length of buffer less than 8(the length of data's head)
            #break
            if len(self.databuf) < 8:
                break

            length, command_id = struct.unpack('!2I', self.databuf[:8])
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
        #self.transport.write(rdata.encode())
        print(Mglobal.UsrLoginStatue[self.transport])
        if command_id == 0:
            han = dt.identificationHandle(rdata,self.transport)
            han.handle()
        else:
            testh = dt.dataHandle(rdata,self.transport)
            testh.handle()



class MFactory(ServerFactory):

    protocol = MProtocol

    def __init__(self,max_client):
        self.max_client = max_client
        self.clients = []
        logger.info('reactor start...ok!')


if __name__=='__main__':
    reactor.listenTCP(8888,MFactory(3))
    reactor.run()