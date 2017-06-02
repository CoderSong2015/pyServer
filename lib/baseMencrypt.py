import rsa
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
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
        return self.prikey.save_pkcs1()

    def encry(self,data):
        return rsa.encrypt(data,self.pubkey)

    def decry(self,data):
        return rsa.decrypt(data,self.prikey)

    def loadPubkey(self,key,tformat = 'PEM'):
        self.pubkey = rsa.PublicKey.load_pkcs1(key,tformat)

    def loadPrikey(self,key,tformat = 'PEM'):
        self.prikey = rsa.PrivateKey.load_pkcs1(key,tformat)

class prpcrypt():
    def __init__(self,key):
        self.key = key
        self.mode = AES.MODE_CBC


    def encrypt(self,text):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        length = 16
        count = len(text)
        if count < length:
            add = (length-count)
            #\0 backspace
            text = text + (b'\0' * add)
        elif count > length:
            add = (length-(count % length))
            text = text + (b'\0' * add)
        self.ciphertext = cryptor.encrypt(text)

        return b2a_hex(self.ciphertext)

    #解密后，去掉补足的空格用strip() 去掉
    def decrypt(self,text):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        plain_text  = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip(b'\0')
