from twisted.internet import threads



class baseDataHandle():

    def __init__(self,data,call_back):

        self.data = data
        self.call_back = call_back

    def ret(self,data):
        pass

    def action(self,data):
        pass

#deferToThread is a

    def handle(self):
        self.call_back.write(self.data.encode())
        print("back:"+self.data)
        """
        you need to use deffered to execute the handleprocess fuction
        :return:
        """


    def err(self,failure):
        pass