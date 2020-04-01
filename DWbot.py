import pyowm
import telebot


owm=pyowm.OWM('70ca04721a29f1a4e36e9b1f0f58829a', language = 'ru')
bot=telebot.TeleBot("949440384:AAEx9mxvxnwIgIXDyIs5uKn-CMENYUoRmn4")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Введи название города, в котором хочешь узнать погоду ")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius') ["temp"]

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer +="Температура в районе " + str(temp) + " градусов" + "\n\n"
	if temp < -10:
	 answer +='Даша, на улице очень холодно, одевай валенки'
	if temp < 10:
	  answer +='Даша, на улице холодно, если пойдешь гулять - оденься потеплее'
	elif temp < 20:
	  answer +='Даша, там - прохладно, лучше оденься'
	else:
	  answer +='Не холодно, хоть в трусах иди...хотя лучше ограничится шортами и рубашкой'

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True)