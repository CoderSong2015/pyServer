
from loginserver.Lgloble import Lloger
from lib.log import MLoger
from loginserver.demo import ThreadingHttpServer,Myhttpserver,hostport,hostname

def main():
    print("xx")

    Lloger.info("init server...")
    myserver = ThreadingHttpServer((hostname, hostport), Myhttpserver)
    Lloger.info("init ok..host = %s:%d "%(hostname,hostport))
    Lloger.info("login server start ok..!")
    myserver.serve_forever()

if __name__=='__main__':
    main()