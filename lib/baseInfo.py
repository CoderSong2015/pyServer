


class clientBInfo():
    infoDict = {}

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
