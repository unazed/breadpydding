"""
Module for the bot handler class that interfaces with the C.B. website API.
"""

import requests


class Bot(object):
    """
    Class for interfacing with C.B. API.
    """
    
    def __init__(self, name, badge):
        self.session = requests.session()
        self.nick = nick
        self.badge = badge

    def send(self, message):
        "Sends message via API"
        
        req = self.session.post("http://www.breadpudding.us/api/chat/", data=
                                {"fn": "post", "nick": self.nick,
                                 "badge": self.badge, "message": message})
        return req.status_code


    def set_nick(self, nick):
        "Sets nickname for the bot via API"
        self.nick = nick
        return self.nick

    def set_badge(self, badge):
        "Sets guild badge via API"
        self.badge = badge
        return badge    

    
client = Bot("Nickname","Badge GUID")

# Bot stuff here.

