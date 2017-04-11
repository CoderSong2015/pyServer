import time

def sayhello():
    print('hello')

if __name__=='__main__':
    print('%s--%d'%('dwa',2))
    str = 'test'.encode()
    print(str)
    print(str.decode())
    ntime = time.strftime('%Y-%m-%d,%H-%M-%S',time.localtime(time.time()))
    print(ntime)