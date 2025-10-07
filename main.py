from flask import Flask, request
import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running!", 200

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'ok', 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://telegram-webapp-9f1q.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=10000)
