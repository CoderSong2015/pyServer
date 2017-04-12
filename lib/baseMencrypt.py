import struct
from src import Mglobal
import rsa
class Bencrypt():



    def setFun(self):
        pass
    def rc4(self,data):
        return data

    def derc4(self,data):
        return data

    def rc5(self,data):
        return data

    def derc5(self,data):
        return data

    def hash(self,data):
        return data

    def dehash(self,data):
        return data

    def setrc4Flag(self,flag):
        self.rc4flag = flag

    def setrc5Flag(self,flag):
        self.rc5flag = flag

    def setfNow(self,encryptFun):
        self.nowFun = encryptFun

    def encrypt(self,data):
        pass

    def encrypt_u(self,encryptFun,data):
        pass


class RSAencrypt():
    def __init__(self):
        pass

    def generateKey(self,bit = 512,poolsize = 1):
        self.pubkey,self.prikey = rsa.newkeys(bit,poolsize)

    def getpubkey(self):
        return self.pubkey.save_pkcs1()

    def getprikey(self):
        return self.prikey

    def encry(self,data):
        return rsa.encrypt(data,self.pubkey)

    def decry(self,data):
        return rsa.decrypt(data,self.prikey)