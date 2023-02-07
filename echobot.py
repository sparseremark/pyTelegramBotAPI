#This is a simple echo bot using the decorator mechanism.
#It echoes any incoming text messages.
from telebot import TeleBot, util

bot = TeleBot('TOKEN')

#Handle '/start'
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(chat_id=message.chat.id, text='''Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!''')

#Handle all other messages
@bot.message_handler(content_types=util.content_type_media)
def message_handler(message):
	bot.copy_message(chat_id=message.chat.id, from_chat_id=message.chat.id, message_id=message.message_id)
	
bot.infinity_polling(allowed_updates=util.update_types)