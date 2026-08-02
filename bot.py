import telebot
from telebot import types

TOKEN = "8849172686:AAEMt0SoscNpCVNF4KkNvu90Q7OkdjFeWG8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("❤️ почему я тебя люблю", callback_data="love")
    btn2 = types.InlineKeyboardButton("📸 наши моменты", callback_data="moments")
    btn3 = types.InlineKeyboardButton("💌 сообщение от Ани", callback_data="message")
    btn4 = types.InlineKeyboardButton("🌙 если тебе грустно", callback_data="sad")

    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    keyboard.add(btn4)

    bot.send_message(
        message.chat.id,
        "привет, тима ❤️\n\nя сделала этот маленький бот специально для тебя 🥹\nздесь есть немного моей любви и мыслей о тебе 🫶",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "love":
        bot.send_message(call.message.chat.id, "я люблю тебя за то, какой ты есть ❤️")

    elif call.data == "moments":
        bot.send_message(call.message.chat.id, "тут скоро будут наши самые тёплые моменты 📸")

    elif call.data == "message":
        bot.send_message(call.message.chat.id, "ты очень важный человек для меня ❤️")

bot.infinity_polling()
