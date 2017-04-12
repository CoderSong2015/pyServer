from lib.log import MLoger
from lib.baseMencrypt import RSAencrypt
from loginserver.Lconfig import logername,filelogname

Lloger = MLoger(logername,filelogname)

Loginkey = RSAencrypt()