from lib.log import MLoger
from lib.baseMencrypt import RSAencrypt
from loginserver.Lconfig import logername,filelogname
from loginserver.MTime import mTime
Lloger = MLoger(logername,filelogname)

Loginkey = RSAencrypt()

systime = mTime()