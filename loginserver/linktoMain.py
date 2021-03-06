from twisted.internet import protocol, reactor
import struct
from loginserver.Lconfig import Mainhostname,Mainhostpost
from loginserver.Lgloble import Loginkey
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
        header = struct.pack('!2I',*value)

        return header + data
class TSClntProtocol(protocol.Protocol):

      p = dataConvert()

      def sendData(self):
           """
           data = input('> ')
           if data:
               #print('...sending %s...')%(data)
               da = self.p.addHeader(data,1)
               self.transport.write(da)
           else:
               self.transport.loseConnection()
           """
           pubk = Loginkey.getpubkey()
           prik = Loginkey.getprikey()
           da = self.p.addHeader(pubk,2)
           self.transport.write(da)
           da = self.p.addHeader(prik,3)
           self.transport.write(da)
      def connectionMade(self):
            Loginkey.generateKey()
            self.sendData()

      def dataReceived(self, data):
            print(data.decode())
            self.sendData()

class TSClntFactory(protocol.ClientFactory):
      protocol = TSClntProtocol
      clientConnectionLost = clientConnectionFailed = \
          lambda self, connector, reason: reactor.stop()


def connectMainserver():
      reactor.connectTCP(Mainhostname, Mainhostpost, TSClntFactory())
      reactor.run()

if __name__=='__main__':
       connectMainserver()
      #reactor.connectTCP(Mainhostname, Mainhostpost, TSClntFactory())
     # reactor.run()