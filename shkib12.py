import telebot;
import constants, os, re
from telebot import types
bot = telebot.TeleBot('819389271:AAEmgpuZd_pheHnF7IG3lhGzdLZxUxIqlYw');

markup_menu = types.ReplyKeyboardMarkup ( resize_keyboard=True, row_width=1)
btn_adress = types.KeyboardButton ('Покажи где ты, ща приеду!!!!', request_location=True)
btn_payment = types.KeyboardButton ( 'Кинь номерок свой, ща позвоню!!!', request_contact=True)
btn_delivery = types.KeyboardButton ( 'Начнем сначала?')
markup_menu.add(btn_adress,  btn_payment, btn_delivery)

@bot.message_handler(commands=["start"])
def inline(message):
  key = types.InlineKeyboardMarkup()
  but_1 = types.InlineKeyboardButton(text="КОНЕЧНО!!!", callback_data="FirstOne")
  key.add(but_1)
  bot.send_message(message.chat.id, "ЗДАРОВА, МЕНЯ ЗОВУТ БОТ ОЛЕГ !!! \n Хочешь я покажу тебе чему я пока научился? \n Садись поудобнее. Расслабься. \n Готов?", reply_markup=key)

@bot.callback_query_handler(func=lambda c:True)
def inline(c):
  if c.data == 'FirstOne':
      key = types.InlineKeyboardMarkup()
      but_3 = types.InlineKeyboardButton(text="ДА!", callback_data="NumberTwo")
      key.add(but_3)
      bot.send_photo(c.message.chat.id, 'https://sun9-11.userapi.com/c624821/v624821501/359dc/0zQLDFtYdGc.jpg', caption='\n А еще я раньше писал неплохую музычку, хочешь послушать?',reply_markup=key);

  if c.data == 'NumberTwo':
      key = types.InlineKeyboardMarkup()
      but_2 = types.InlineKeyboardButton(text="ДАВАЙ!", url='https://t.me/MDKaka' )
      key.add(but_2 )
      bot.send_audio(c.message.chat.id, 'https://i46.kissvk.com/api/song/download/get/10/%D0%9D%D0%B5%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%B5%D0%BD-%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-kissvk.com.mp3?origin=kissvk.com&url=sid%3A%2F%2F285402691_456239024_5ebe5da7ff842a52ad_8357ecb6cfb0ef7a3a&artist=%D0%9D%D0%B5%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%B5%D0%BD&title=%D0%91%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F&index=0&future_urls=sid%3A%2F%2F285402691_456239023_9f9d967fe0414d6ddb_c4e04a2c46c5fbc739', caption='Вообще я люблю рэп. Но в последнее время я перестал уделять ему внимание. Надеюсь скоро мои настройки обновяться и снова смогу писать клевую музычку и читать классные тексты. Ну пока немного юмора!',reply_markup=key)


@bot.message_handler(func=lambda message: True)
def echo_all(message):

    if message.text == "Начнем сначала?":
        bot.send_message(message.chat.id, "/start")
    else:
        bot.send_message(message.chat.id, "Я не всасываю что ты пишешь! Давай жми /start")
        bot.send_message(message, reply_markup=markup_menu)
bot.polling()
