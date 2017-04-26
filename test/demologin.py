import requests
from lib.baseMencrypt import RSAencrypt
import rsa
requests.adapters.DEFAULT_RETRIES = 5


cry = RSAencrypt()
#r = requests.get('http://localhost:9004?type=login&account=hao&passwd=123')
r = requests.get('http://localhost:9004?type=pubkey')
print(r.text)
pub = cry.loadPubkey(r.text)
txt = "song:123".encode()

ret = cry.encry(txt)
print(ret)
'''
print(type(ret))
rett = str(ret)
stt = {'type':'enytest','str':rett}
#r = requests.get('http://localhost:9004?type=enytest&str=%s'%(str(ret)))
r = requests.get('http://localhost:9004',params=stt)
print("url = ",r.url)
print(r.text)

'''

dd = {'dataaa':'song'}
leng = '%d'%len(dd)
r = requests.post('http://localhost:9004',data = ret)
