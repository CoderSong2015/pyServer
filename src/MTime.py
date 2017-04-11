import time

class mTime:
    def __init__(self):
        self.time = self.__getNowtime()
        self.Data = self.__getData()
        self.Datatime = self.__getDatatime()
    def time(self):
        return self.__getNowtime()

    def Data(self):
        return self.__getData()

    def Datatime(self):
        return self.__getDatatime()

    def __getData(self):
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))

    def __getDatatime(self):
        return time.strftime('%Y-%m-%d,%H-%M-%S', time.localtime(time.time()))

    def __getNowtime(self):
        return time.strftime('%H-%M-%S', time.localtime(time.time()))