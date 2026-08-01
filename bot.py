import telebot
TOKEN = "8849172686:AAEMt0SoscNpCVNF4KkNvu90Q7OkdjFeWG8"
bot = telebot.Telebot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, "привет, я запущен!!❤️")
  bot.infinity_polling()
