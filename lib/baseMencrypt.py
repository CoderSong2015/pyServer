import struct
from src import Mglobal

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