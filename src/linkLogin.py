__author__ = 'Mrsong'
from src.Mglobal import UsrLoginStatue
import requests
from lib.baseMencrypt import RSAencrypt
import time
def sendStatus():
    print('sendStatus threadstart..')

    serverid = 0
    cry = RSAencrypt()

    r = requests.get('http://127.0.0.1:9004?type=resgister&addr=192.168.155.1:8889')

    serverid = int(r.text)
    print('serverid:',serverid)
    r = requests.get('http://127.0.0.1:9004?type=pubkey')
    pub = cry.loadPubkey(r.text)
    #txt = "server:123".encode()

   # ret = cry.encry(txt)
   # print(ret)


  #  r = requests.post('http://localhost:9004',data = ret)
  #  print(r.text)
    #global UsrLoginStatue
    while(1):
        time.sleep(3)
        line = ''
        flag = 0
        for k,v in UsrLoginStatue.items():

            if v == 1:
                flag = flag + 1
                line = line + str(k) + ';'
        print('status:',line)
        txt = 'cliOnline:'+str(serverid)+':' + str(flag)
        ret = cry.encry(txt.encode())
   #     print(ret)


        r = requests.post('http://localhost:9004',data = ret)
        print(r.text)
    pass
