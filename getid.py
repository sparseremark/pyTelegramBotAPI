#This is a simple bot that will send you the ID of the current chat, the user ID and the ID of the chat being forwarded.
from telebot import TeleBot, util

bot = TeleBot('TOKEN', parse_mode='html')

#HANDLE FORWARD MESSAGES
@bot.message_handler(func=lambda message: message.forward_from, content_types=util.content_type_media)
def hh(msg):
	bot.send_message(msg.chat.id, '''Ваш ID: <code>{u_id}</code>
ID Текущего чата: <code>{c_id}</code>
Переслано из: <code>{f_id}</code>'''.format(u_id = msg.from_user.id, c_id = msg.chat.id, f_id = msg.forward_from.id))
@bot.message_handler(func=lambda message: message.forward_from_chat, content_types=util.content_type_media)
def hh(msg):
	bot.send_message(msg.chat.id, '''Ваш ID: <code>{u_id}</code>
ID Текущего чата: <code>{c_id}</code>
Переслано из: <code>{f_id}</code>'''.format(u_id = msg.from_user.id, c_id = msg.chat.id, f_id = msg.forward_from_chat.id))

#HANDLE OTHER MESSAGES			
@bot.message_handler(content_types=util.content_type_media)
def usually_messages(msg):
	bot.send_message(msg.chat.id, '''Ваш ID: <code>{user_id}</code>
ID Текущего чата: <code>{chat_id}</code>'''.format(user_id = msg.from_user.id, chat_id = msg.chat.id))
@bot.message_handler(content_types=util.content_type_service)
def service_messages(msg):
	bot.send_message(msg.chat.id, '''Ваш ID: <code>{user_id}</code>
ID Текущего чата: <code>{chat_id}</code>'''.format(user_id = msg.from_user.id, chat_id = msg.chat.id))

bot.infinity_polling(allowed_updates=util.update_types)