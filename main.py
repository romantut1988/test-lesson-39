import telebot

token = '6781993139:AAF21HJ8FpW3CXbwciiDI77P1rje_ZY4hT4'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello 😑")


@bot.message_handler(content_types=['text'])
def new_message(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "и тебе привет!!!")
    elif message.text == "photo":
        bot.send_photo(message.chat.id,
                       photo="https://ichef.bbci.co.uk/news/640/cpsprodpb/6969/production/_93558962_istock-586160412.jpg")
    elif message.text == "/gif":
        bot.send_animation(message.chat.id,
                           "https://giphy.com/gifs/laclippers-sport-basketball-dunk-uTW3CMuOQwKGMsyM6I")
    elif message.text == "/sticker":
        bot.send_sticker(message.chat.id,
                         "https://tlgrm.ru/_/stickers/d06/e20/d06e2057-5c13-324d-b94f-9b5a0e64f2da/1.webp")
    else:
        bot.send_message(message.chat.id, "я тебя не понимаю(((!!!")


bot.polling(none_stop=True)
