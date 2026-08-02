import telebot
from telebot import types

TOKEN = "8849172686:AAEMt0SoscNpCVNF4KkNvu90Q7OkdjFeWG8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    
    btn1 = types.KeyboardButton("❤️ почему я тебя люблю")
    btn2 = types.KeyboardButton("📸 наши моменты")
    btn3 = types.KeyboardButton("💌 сообщение от Ани")
    btn4 = types.KeyboardButton("🌙 если тебе грустно")
    btn5 = types.KeyboardButton("💌 открыть, когда...")
    
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    keyboard.add(btn5)

    bot.send_message(
        message.chat.id,
        "привет, тима ❤️\n\nя сделала этот маленький бот специально для тебя 🥹\nздесь есть немного моей любви и мыслей о тебе 🫶",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def menu(message):

    if message.text == "❤️ почему я тебя люблю":
        bot.send_message(
            message.chat.id,
            "я люблю тебя за то, какой ты есть ❤️"
        )

    elif message.text == "📸 наши моменты":
        bot.send_message(
            message.chat.id,
            "тут скоро будут наши самые тёплые моменты 📸"
        )

    elif message.text == "💌 сообщение от Ани":
        bot.send_message(
            message.chat.id,
            "ты очень важный человек для меня ❤️"
        )

    elif message.text == "🌙 если тебе грустно":
        bot.send_message(
            message.chat.id,
            "🌙 если тебе станет грустно...\n\n"
            "🤍 помни, что я рядом мыслями.\n\n"
            "🫂 я всегда верю в тебя ❤️"
        )

    elif message.text == "💌 открыть, когда...":
        keyboard = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("🌧️ когда тебе грустно", callback_data="sad2")
        btn2 = types.InlineKeyboardButton("🥺 когда скучаешь по мне", callback_data="miss")
        btn3 = types.InlineKeyboardButton("😴 когда не можешь уснуть", callback_data="sleep")
        btn4 = types.InlineKeyboardButton("💪 когда нужна поддержка", callback_data="support")

        keyboard.add(btn1, btn2)
        keyboard.add(btn3, btn4)

        bot.send_message(
            message.chat.id,
            "💌 выбери момент, в который хочешь открыть письмо 🤍",
            reply_markup=keyboard
        )
        
@bot.message_handler(content_types=['photo'])
def get_photo_id(message):
    bot.send_message(
        message.chat.id,
        message.photo[-1].file_id
    )
        
    
    
    
        


bot.infinity_polling()
       
    
