class Tg ():

	def __init__ (self, api_token:str):		
		""""""

		import telebot

		self.API_TOKEN = api_token
		self.bot = telebot.TeleBot(self.API_TOKEN)

	def check_input (self, text, f):
		""""""
		@self.bot.message_handler(func=lambda message: True)
		def handle_message(message):
			if message.text == text:
				f ()

	def send_message (self, text):
		""""""
		@self.bot.message_handler(func=lambda message: True)
		def f (message):
			self.bot.send_message(message.chat.id, text)

	def send_reply (self, text):
		@self.bot.message_handler(func=lambda message: True)
		def f (message):
			self.bot.reply_to (message, text)

	def run (self):
		""""""
		self.bot.infinity_polling(none_stop=True)

def test_f ():
	print ('ok')


tg = Tg ('7207423391:AAFozqYA_9KgGj4dD9nFotPtVd6teZGZ3Bk')

tg.check_input ('test', tg.send_reply ('test_0000'))
tg.run ()
