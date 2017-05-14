
from loginserver.Lgloble import Lloger
from loginserver.Lgloble import Loginkey
from loginserver.loginServer import ThreadingHttpServer,Myhttpserver,hostport,hostname

def main():
    print("xx")

    Lloger.info("init server...")
    Loginkey.generateKey()
    Lloger.info("generate rsa key..ok!")
    myserver = ThreadingHttpServer((hostname, hostport), Myhttpserver)

    Lloger.info("init ok..host = %s:%d "%(hostname,hostport))
    Lloger.info("login server start ok..!")
    myserver.serve_forever()
    print("asd")

if __name__=='__main__':
    main()