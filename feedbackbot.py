from telebot import TeleBot, types, util, custom_filters
import time, random

bnusers = [] # Айди забаненных людей
adm_id = [0] #Айди администратора
adm_chat = 0 #тоже айди администратора, первый используется для проверки фильтра как чат айди, а второй для методов

bot = TeleBot(token='token', parse_mode='HTML', disable_web_page_preview=True, allow_sending_without_reply=True, disable_notification=False, protect_content=False, skip_pending=True)



@bot.message_handler(content_types=util.content_type_media+util.content_type_service, chat_types=['private'], chat_id=bnusers)
def banusers(msg):
	xm = bot.send_message(chat_id=msg.chat.id, text='''<b>❌ К сожалению <i>вы были <u>заблокированы</u></i> в этом боте</b>.''')
	time.sleep(15)
	bot.delete_message(chat_id=msg.chat.id, message_id=xm.message_id)

@bot.message_handler(commands=['start'], chat_types=['private'])
def start(msg):
	bot.send_message(chat_id=msg.chat.id, text='''👋 Привет <b><a href="tg://user?id={id}">{name}</a></b>!

🧑‍💻 Этот бот предназначен для <b>связи с администрацией</b>

📛 За <b>флуд и спам</b> или <b>сообщения не по теме</b> - <b><u>БАН НАВСЕГДА</u></b>

<i>❗Сообщения по типу «Привет», «как дела» и другие <b>вопросы не по теме будут игнорироваться! Пишите сразу всё в одном сообщении!</b></i>'''.format(name = msg.from_user.first_name, id = msg.from_user.id))

@bot.message_handler(content_types=util.content_type_media, is_reply=True, chat_id=adm_id, chat_types=['private'])
def reply_valid(msg):
	try:
		c = bot.copy_message(chat_id=str(msg.reply_to_message.text)[3:], from_chat_id=adm_chat, message_id=msg.message_id)
		xmm = bot.send_message(chat_id=str(msg.reply_to_message.text)[3:], text='''<b>📩 Пришло <u>новое сообщение</u> от поддержки👆</b>''', reply_to_message_id=c.message_id)
		xm = bot.send_message(chat_id=msg.chat.id, text='''<b>Ваше сообщение было <i>успешно доставлено</i> участнику ✅</b>''', reply_to_message_id=msg.message_id)
		time.sleep(10)
		bot.delete_message(chat_id=str(msg.reply_to_message.text)[3:], message_id=xmm.message_id)
		bot.delete_message(chat_id=adm_chat, message_id=xm.message_id)
	except Exception as err:
		bot.send_message(chat_id=msg.chat.id, reply_to_message_id=msg.message_id, text='''<b>⚠️ Произошла ошибка!</b>''')
 
@bot.message_handler(content_types=util.content_type_media, is_reply=False, chat_id=adm_id, chat_types=['private'])
def reply_valid(msg):
	xmm = bot.send_message(chat_id=adm_chat, text='''📩 Ответьте на сообщение, <b>в котором есть идентификатор</b> <i><u>переадресованного</u> пользователя</i>.''')
	time.sleep(15)
	bot.delete_message(chat_id=adm_chat, message_id=xmm.message_id)


@bot.message_handler(content_types=util.content_type_service, chat_types=['private'])
def servuce(msg):
	xm = bot.reply_to(chat_id=msg.chat.id, text='''❌ Тип <i>сервисных сообщений</i> <b><u>не поддерживается</u></b>!

<i>📩 Отправьте <b>другое</b></i>.''', reply_to_message_id=msg.message_id)
	time.sleep(15)
	bot.delete_message(chat_id=msg.chat.id, message_id=xm.message_id)
	bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
 
@bot.edited_message_handler(content_types=util.content_type_media, chat_types=['private'])
def edit(msg):
	xm = bot.send_message(chat_id=msg.chat.id, text='''✍️ Сообщение уже <b><u>нельзя</u> отредактировать</b>.

<i>📩 Лучше <b>отправьте новое</b></i>.''', reply_to_message_id=msg.message_id)
	time.sleep(15)
	bot.delete_message(chat_id=msg.chat.id, message_id=xm.message_id)
 
@bot.message_handler(content_types=util.content_type_media, chat_types=['private'])
def feedback(msg):
	mk = types.InlineKeyboardMarkup()
	mk.add(types.InlineKeyboardButton(text='Пользователь 👤', url='tg://user?id={id}'.format(id = msg.from_user.id)))
	f = bot.forward_message(chat_id=adm_chat, from_chat_id=msg.chat.id, message_id=msg.message_id)
	bot.send_message(chat_id=adm_chat, text='''#id{id}'''.format(id=msg.chat.id), reply_to_message_id=f.message_id, reply_markup=mk)
	xm = bot.send_message(chat_id=msg.chat.id, text='''<b>Ваше сообщение было <i>успешно доставлено</i> администратору ✅</b>''', reply_to_message_id=msg.message_id)
	time.sleep(10)
	bot.delete_message(chat_id=msg.chat.id, message_id=xm.message_id)





bot.add_custom_filter(custom_filters.IsReplyFilter())
bot.add_custom_filter(custom_filters.ChatFilter())
bot.infinity_polling(skip_pending=True, allowed_updates=util.update_types)
