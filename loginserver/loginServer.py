from http.server import BaseHTTPRequestHandler,HTTPServer
from lib.sql_operator import sql_operate
from loginserver.Header import Define
from loginserver.Lconfig import handleObj
from loginserver.Lconfig import mysql_conf
from socketserver import ThreadingMixIn
from loginserver.Lconfig import hostname,hostport
from loginserver.Lgloble import Loginkey
from loginserver.Lgloble import systime
from loginserver.Lconfig import Mainhostname
class handleThread():
    def __init__(self,arg):
        #super(handleThread, self).__init__()
        self.se = arg
        self.Obj_mysql = sql_operate(mysql_conf)

    def run(self):
        ret = self.handleUrl(self.se)
        if(ret[0] == Define['SUCCESS']):
          #  print(ret[1])
            re = self.handleObj(self.se,ret[1])
            if re == Define['ERRORPARA']:
                self.se.send_response(200)
                self.se.send_header("Content-type", "kkk")
                self.se.end_headers()
                self.se.wfile.write(bytes("ERRORPARA", "utf-8"))
            if re == Define['ERRORTYPE']:
                self.se.send_response(200)
                self.se.send_header("Content-type", "kkk")
                self.se.end_headers()
                self.se.wfile.write(bytes("ERRORTYPE", "utf-8"))


    def handleObj(self,se,kv):

        print(kv)
        print(kv['type'])
        if kv['type'] not in handleObj:
            print('no:',kv['type'])
            return Define['ERRORTYPE']

        if kv['type'] == 'login':
            if 'account' not in kv or 'passwd' not in kv:
                return Define['ERRORPARA']

            return self.handleLogin(se,kv)

        if kv['type'] == 'pubkey':
            return self.returnPubkey(se,kv)

        if kv['type'] == 'resgister':
            print(kv)

            return self.resgiSer(se,kv['addr'])


    def resgiSer(self,se,addr):
        se.serverStatus['servernum'] = se.serverStatus['servernum'] + 1
        se.serverStatus[se.serverStatus['servernum']] = [0,addr]

        se.send_response(200)
        se.send_header("Content-type", "src")
        se.end_headers()
        se.wfile.write(bytes(str(se.serverStatus['servernum']), "utf-8"))

    def returnPubkey(self,se,kv):
        self.se.send_response(200)
        self.se.send_header("Content-type", "pubkey")
        self.se.end_headers()
        self.se.wfile.write(Loginkey.getpubkey())

    def handleLogin(self,se,kv):
        sqls = "select uid from user where usrname = \'%s\' && passwd = \'%s\'" % (kv['account'], kv['passwd'])

        re = self.Obj_mysql._query(sqls)
        if(re == False):
            return Define['ERRORSQL']
        if(re[0] == None):
            se.send_response(200)
            se.send_header("Content-type", "src")
            se.end_headers()
            se.wfile.write(bytes("wrong", "utf-8"))
        else:
            print(re)
            se.send_response(200)
            se.send_header("Content-type", "src")
            se.end_headers()
            se.wfile.write(bytes("hello", "utf-8"))

    def handleUrl(self,se):
         print(se.path)
         if '?' in se.path:
              para = se.path.split('?')[1]

              paradic = {}
              for qp in para.split('&'):
                    kv = qp.split('=')
                    paradic[kv[0]] = kv[1]

              return (Define['SUCCESS'],paradic)
         else:
              se.send_response(200)
              se.send_header("Content-type", "kkk")
              se.end_headers()
              se.wfile.write(bytes("None", "utf-8"))
              return (Define['ERRORURL'],None)

class handleThread_Post:
    def __init__(self,arg,data):
        #super(handleThread, self).__init__()
        self.se = arg
        self.data = data
        self.Obj_mysql = sql_operate(mysql_conf)
    def run(self):
        kv = self.handleDATA(self.data)
        print(kv)
        if kv[0] == 'cliOnline':
            self.se.serverStatus[int(kv[1])][0] = int(kv[2])
            print(self.se.serverStatus[int(kv[1])][1])
            self.se.send_response(200)
            self.se.send_header("Content-type", "src")
            self.se.end_headers()
            self.se.wfile.write(bytes("update", "utf-8"))
        else:
            self.checkaccount(kv)

    def checkaccount(self,kv):
        sqls = "select uid from user where usrname = \'%s\' && passwd = \'%s\'" % (kv[0], kv[1])

        re = self.Obj_mysql._query(sqls)

        uid = (re[0])[0]
        print('uid:',uid)
        if(re == False):
            return Define['ERRORSQL']
        if(re[0] == None):
            self.se.send_response(200)
            self.se.send_header("Content-type", "src")
            self.se.end_headers()
            self.se.wfile.write(bytes("wrong", "utf-8"))
        else:
            print(re)
            sqls = "update user set lastlogin = \'%s\' where usrname = \'%s\' " % ( systime.getmysqltime(),kv[0])
            re = self.Obj_mysql._update(sqls)
            print(re)
            print(sqls)
            self.se.send_response(200)
            self.se.send_header("Content-type", "src")
            self.se.end_headers()

            host = self.choseServer(self.se)
            self.se.wfile.write(bytes(host, "utf-8"))

    def choseServer(self,se):

            min = 1000
            addr = ''
            flag = 0
            for k,v in se.serverStatus.items():
                if not k == 'servernum':
                    if v[0] < min:
                        flag = 1
                        min = v[0]
                        addr = v[1]
            if flag == 1:
                return addr

            return "noserver"

    def handleDATA(self,data):
        kv = data.split(':')
        print(kv)
        return kv


"""
def handleUrl(se):
    if '?' in se.path:
        para = se.path.split('?')[1]
        for qp in para.split('&'):
            kv = qp.split('=')
            paradic = {}
            paradic[kv[0]] = kv[1]
            print(paradic)
            se.send_response(200)
            se.send_header("Content-type", "src")
            se.end_headers()
            se.wfile.write(bytes("hello", "utf-8"))
    else:
        se.send_response(200)
        se.send_header("Content-type", "kkk")
        se.end_headers()
        se.wfile.write(bytes("None", "utf-8"))

"""
class Posthandle():
    def __init__(self,arg):
        self.se = arg
        self.Obj_mysql = sql_operate(mysql_conf)

    def run(self):
        pass

class Myhttpserver(BaseHTTPRequestHandler):

    serverStatus = {}

    serverStatus['servernum'] = 0
    def do_GET(self):
        #handleUrl(self)
        print(self)
        t = handleThread(self)
        t.run()


    def do_POST(self):
        print("do read...")
        head = self.headers
        print(head)
        length = head['Content-Length']
        print(length)
        nbytes = int(length)
        data = self.rfile.read(nbytes)
        clientdata = Loginkey.decry(data)
        print(clientdata)
        t = handleThread_Post(self,clientdata.decode())
        t.run()




class ThreadingHttpServer(ThreadingMixIn, HTTPServer ):
    pass

if __name__=='__main__':
     myserver = ThreadingHttpServer((hostname,hostport),Myhttpserver)

     myserver.serve_forever()

