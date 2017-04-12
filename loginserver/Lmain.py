from loginserver.config import logername,filelogname
#from loginserver.Lgloble import Lloger
from lib.log import MLoger
from loginserver.demo import ThreadingHttpServer,Myhttpserver,hostport,hostname

def main():

    Lloger = MLoger(logername,filelogname)
    Lloger.info("login server start ok..!")
    myserver = ThreadingHttpServer((hostname, hostport), Myhttpserver)
    myserver.serve_forever()

if __name__ == '__main__':
    print("x" )
    #main()