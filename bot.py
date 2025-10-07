import telebot
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = telebot.types.WebAppInfo(url="https://твоёимя.onrender.com")
    play_btn = telebot.types.KeyboardButton(text="🎮 Открыть игру", web_app=btn)
    markup.add(play_btn)
    bot.send_message(message.chat.id, "Добро пожаловать! Нажми кнопку, чтобы открыть игру 👇", reply_markup=markup)

bot.polling()
