import struct
from src import Mglobal
from lib.baseMencrypt import Bencrypt
from lib.baseInfo import clientBInfo

class Mencrypt(Bencrypt):

    def __init__(self):
        self.funDict = {}
        self.Mrc4 = 0
        self.Mrc5 = 1
        self.Mhash = 2
        self.rc4flag = Mglobal.rc4Flag
        self.rc5flag = Mglobal.rc5Flag
        self.nowFun = self.rc4
        self.setFun()

    def setFun(self):
        self.funDict[0] = self.rc4
        self.funDict[1] = self.rc5
        self.funDict[2] = self.hash

    def rc4(pkey, keylen, data, dlen):
        N = 65536
        S = list(range(N))
        j = 0
        for i in range(N):
            j = (j + S[i] + pkey[i % keylen]) % N
            temp = S[i]
            S[i] = S[j]
            S[j] = temp
        i = j = 0
        dataout = b''
        for x in range(dlen):
            i = i + 1
            j = (j + S[i]) % N
            temp = S[i]
            S[i] = S[j]
            S[j] = temp
            dataout += data[x] ^ S[(S[i] + S[j]) % N]
        return (dataout)

    def rc4key(self,rc4flag):
        pl = len(rc4flag)
        Key = b''
        r = 0
        for i in range(32):
            k = (rc4flag[r % pl] + i) % 256
            Key += struct.pack('B', k)
            r += 1
        return Key
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
        return self.funDict[self.nowFun](data)

    def encrypt_u(self,encryptFun,data):
        if encryptFun in self.funDict:
            return self.funDict[encryptFun](data)
        else:
            return False

class dataConvert():

    def __init__(self, encrypt = 0):
        self.encrypt = encrypt
        self.Encrypt = Mencrypt()

    def convert(self,data):
        rdata = self.Encrypt.rc4(data)
        return

    def addHeader(self,data,command_id):
        length = 8 + len(data)
        value = [length,command_id]
        header = struct.pack('!2I',*value)

        return header + data.encode()



class clientInfo(clientBInfo):
    def __init__(self):
        self.infoDict = {}

    def addInfo(self,uid,info):
        self.infoDict[uid] = info

    def removeInfo(self,uid):
        if uid in self.infoDict:
            del self.infoDict[uid]
            #log
            return True
        else:
            return False

    def getinfo(self,uid):
        if uid in self.infoDict:
            return self.infoDict[uid]
        else:
            #log
            return False

    def getInfolen(self):
        return len(self.infoDict)

    def listall(self):
        print(self.infoDict)

    def __del__(self):
        del self.infoDict


if __name__ == '__main__':
    p = dataConvert()
    da = p.addHeader("asdc",3)
    print(da)
    print(da.decode())
    ll,cc = struct.unpack('!2I',da[:8])
    print(ll,cc)