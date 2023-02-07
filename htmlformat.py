#This is a simple bot that can send various fonts of text using parse_mode (HTML)
from telebot import TeleBot

bot = TeleBot('token', parse_mode='html')


@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(chat_id=message.chat.id, text='''Hi! I can send text with different fonts, look!

Bold - <b>Bold text</b>
Italic - <i>Italic text</i>
Code - <code>Code text</code>
Underline - <u>Underline text</u>
Strikethrough - <s>Strikethrough text</s>
Spoiler - <tg-spoiler>Spoiler text</tg-spoiler>
Link - <a href="example.com">Link text</a>''')

	
bot.infinity_polling()