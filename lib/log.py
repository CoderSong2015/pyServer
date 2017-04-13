import logging


class MLoger():
    def __init__(self,logername,filelogname):
        self.logger = logging.getLogger(logername)
        self.logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(filelogname)
        fh.setLevel(logging.DEBUG)

      #  ch = logging.StreamHandler()
      #  ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s -%(filename)s[line:%(lineno)d]'
                                      '-%(levelname)s -%(message)s')

        fh.setFormatter(formatter)
      #  ch.setFormatter(formatter)

        self.logger.addHandler(fh)
      #  self.logger.addHandler(ch)

    def info(self,data):
        print(data)
        self.logger.info(data)

    def debug(self,data):
        self.logger.debug(data)

    def warning(self,data):
        self.logger.warning(data)

    def error(self,data):
        self.logger.error(data)

'''
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
'''
if __name__=='__main__':
    pass