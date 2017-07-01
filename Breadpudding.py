import requests

class Bot(object):

    def __init__(self,nick="Bot",badge="0"):
        self.s = requests.session()
        self.nick = nick
        self.badge = badge

    def send(self,message): # Sends a message.
        r = self.s.post("http://www.breadpudding.us/api/chat/", data={"fn":"post","nick":self.nick,"message":message,"badge":self.badge})
        return r.status_code


    def setNick(self,nick): # Sets the nickname of the bot.
        self.nick = nick
        return self.nick

    def setBadge(self,badge): # Sets the badge of the bot.
        self.badge = badge
        return badge    

Client = Bot("Nickname","Badge GUID")

# Bot stuff here.

