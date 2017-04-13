from twisted.internet import protocol, reactor
import struct
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

        return header + data.encode()
class TSClntProtocol(protocol.Protocol):

      p = dataConvert()

      def sendData(self):
           data = input('> ')
           if data:
               #print('...sending %s...')%(data)
               da = self.p.addHeader(data,1)
               self.transport.write(da)
           else:
               self.transport.loseConnection()


      def connectionMade(self):
            self.sendData()

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