import logging

logger = logging.getLogger('MainServerloger')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('MainServer.log')
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s - %(name)s -%(filename)s[line:%(lineno)d]'
                              '-%(levelname)s -%(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
#logger.addHandler(ch2)
#logger.addHandler(ch3)