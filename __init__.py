"""
https://github.com/cbpudding/breadpydding
"""

import json
import requests

from time import sleep


class Bot():
	"""
	Bot API that interfaces with the C.B. API.
	"""

	def __init__(self, nick, badge):
		self.nick = nick
		self.badge = badge
		self.lmsg_id = 0

	def call(self, function, data):
		"""
		Returns information of last message.
		"""

		dat["fn"] = function
		resp = requests.post("http://www.breadpudding.us/api/chat/", data=data)
		return json.loads(resp)

	def post(self, message):
		"""
		Sends message.
		"""

		return self.call("post", {nick: self.nick, badge: self.badge, message: message})

	def get(self):
		"""
		Returns message data.
		"""

		return self.call("get", {nick: self.nick})

	def onchat(self, message):
		"""
		Handler for handling new messages.
		"""

		return