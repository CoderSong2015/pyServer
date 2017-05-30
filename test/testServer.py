from twisted.internet import protocol, reactor
import struct
import random
import time
HOST='127.0.0.1'
PORT= 8889

class dataConvert():

    def __init__(self, encrypt = 0):
        pass

    def convert(self,data):

        return

    def addHeader(self,data,command_id):
        length = 8 + len(data)
        value = [length,command_id]
        header = struct.pack('@2I',*value)

        return header + data.encode()
class TSClntProtocol(protocol.Protocol):

      p = dataConvert()

      def loginData(self):
           data = input('loginname> ')
           if data:
               #print('...sending %s...')%(data)
               da = self.p.addHeader(data,99)
               self.transport.write(da)
           else:
               self.transport.loseConnection()
      def sendData(self):
           data = input('> ')
           if data == 'go':

                   self.gosenddata()
               #    time.sleep(3)

           else:
               if data=='exit':
                 self.transport.loseConnection()
               else:
                 da = self.p.addHeader(data,1)
                 self.transport.write(da)

      def gosenddata(self):
          #print('...sending %s...')%(data)
          for i in range(100):
                   data = (random.uniform(0,3.2))
                   rdata =round(data,3)
                   print(rdata)

                   da = self.p.addHeader(str(rdata),1)

                   #self.transport.write(da)
                   self.transport.getHandle().sendall(da)
                   time.sleep(1)
      def connectionMade(self):
            self.loginData()

      def dataReceived(self, data):
            print(data.decode())
            self.sendData()

class TSClntFactory(protocol.ClientFactory):
      protocol = TSClntProtocol
      clientConnectionLost = clientConnectionFailed = \
          lambda self, connector, reason: reactor.stop()



if __name__=='__main__':
      reactor.connectTCP(HOST, PORT, TSClntFactory())
      reactor.run()