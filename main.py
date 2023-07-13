#библиотеки, которые загружаем из вне
import telebot
TOKEN = '6390479604:AAFI8FEd1IRDgGtPwP2QWBjce6zd-iElPsE'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.jpg', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Погода")
	item2 = types.KeyboardButton("😋 Мой гороскоп")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Привет тебе от коти,дай лапу! {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Погода':
			bot.send_message(message.chat.id, 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A3%D0%BB%D1%8C%D1%8F%D0%BD%D0%BE%D0%B2%D1%81%D0%BA%D0%B5')
		elif message.text == '😋 Мой гороскоп':
			bot.send_message(message.chat.id, 'https://horoscopes.rambler.ru/pisces/')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
