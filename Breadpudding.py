import requests

class Bot(object):

    def __init__(self):
        self.s = requests.session()
        self.nick = "Bot"
        self.badge = "0"

    def send(self,message):
        r = self.s.post("http://www.breadpudding.us/api/chat/", data={"fn":"post","nick":self.nick,"message":message,"badge":self.badge})
        return r.status_code


    def setNick(self,nick):
        self.nick = nick
        return self.nick

    def setBadge(self,badge):
        self.badge = badge
        return badge    

Client = Bot()
