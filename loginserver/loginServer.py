from http.server import BaseHTTPRequestHandler,HTTPServer
from lib.sql_operator import sql_operate
from loginserver.Header import Define
from loginserver.Lconfig import handleObj
from loginserver.Lconfig import mysql_conf
from socketserver import ThreadingMixIn
from loginserver.Lconfig import hostname,hostport
from loginserver.Lgloble import Loginkey

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


    def handleObj(self,se,kv):

        print(kv)
        if kv['type'] not in handleObj:
            return Define['ERRORTYPE']

        if kv['type'] == 'login':
            if 'account' not in kv or 'passwd' not in kv:
                return Define['ERRORPARA']

            return self.handleLogin(se,kv)

        if kv['type'] == 'pubkey':
            return self.returnPubkey(se,kv)

    def returnPubkey(self,se,kv):
        self.se.send_response(200)
        self.se.send_header("Content-type", "pubkey")
        self.se.end_headers()
        self.se.wfile.write((Loginkey.getpubkey(),"utf-8"))

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
class Myhttpserver(BaseHTTPRequestHandler):
    def do_GET(self):
        #handleUrl(self)
        #print(self.path)
        t = handleThread(self)
        t.run()


    def do_POST(self):
        pass


class ThreadingHttpServer(ThreadingMixIn, HTTPServer ):
    pass

if __name__=='__main__':
     myserver = ThreadingHttpServer((hostname,hostport),Myhttpserver)

     myserver.serve_forever()
