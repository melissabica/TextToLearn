from rapidsms.apps.base import AppBase

class PingPong(AppBase):
	
	def handle(self, msg):
		if msg.text == 'ping':
			msg.respond('pong')
			return True
		return False
