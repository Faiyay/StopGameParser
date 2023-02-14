
import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests

url = "https://stopgame.ru/news" 

requests = requests.get(url)


bs = BeautifulSoup(requests.text, "html.parser")


links = bs.find("div", class_="items")
p = links.text

bot = telebot.TeleBot('6116860887:AAFNVx1HsvcDFOzY9tLR3q8APBwD55PIX9o')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я  бот для парсинга новостей с сайта StopGame!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Начать')
        markup.add(btn1,)
        bot.send_message(message.from_user.id, 'Начать парсинг?', reply_markup=markup) #ответ бота


    elif message.text == 'Начать':
        bot.send_message(message.from_user.id, p + "Полныен новости вы можите прочитать здесь:https://stopgame.ru/news", parse_mode='Markdown')

bot.polling(none_stop=True, interval=0) #обязательная для работы бота