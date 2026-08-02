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
    btn5 = types.InlineKeyboardButton("💌 открыть, когда...", callback_data="open_when")

    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    keyboard.add(btn4)
    keyboard.add(btn5)

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
    elif call.data == "sad":
        bot.send_message(
            call.message.chat.id,
            "🌙 если однажды тебе станет грустно...\n\n"
            "🤍 просто открой этого бота.\n\n"
            "💗 я надеюсь, что хотя бы одно сообщение отсюда сможет вызвать у тебя улыбку.\n\n"
            "🫂 даже если меня нет рядом, мысленно я всегда тебя обнимаю.\n\n"
            "😽 ты самый дорогой человек в моей жизни.\n\n"
            "💘 я очень сильно тебя люблю.\n\n"
            "✨ и никогда не забывай, какой ты замечательный."
        )

    elif call.data == "open_when":
        keyboard = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("🌧️ когда тебе грустно", callback_data="sad2")
        btn2 = types.InlineKeyboardButton("🥺 когда скучаешь по мне", callback_data="miss")
        btn3 = types.InlineKeyboardButton("😴 когда не можешь уснуть", callback_data="sleep")
        btn4 = types.InlineKeyboardButton("💪 когда нужна поддержка", callback_data="support")

        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)

        bot.send_message(
            call.message.chat.id,
            "💌 выбери момент, в который хочешь открыть письмо 🤍",
            reply_markup=keyboard
        ) 
        
    elif call.data == "miss":
        bot.send_photo(
            call.message.chat.id,
            photo= "AgACAgIAAxkBAANham-xaGp3fBbmcP4nypd038wm4MIAArkhaxvHQIBLK0TLc4aDnQ4BAAMCAAN5AAM9BA",
            caption=
            "🥺 если ты сейчас скучаешь по мне...\n\n"
            "🤍 представь, что я рядом.\n\n"
            "🫂 я бы крепко-крепко тебя обняла, уткнулась носиком в твоё плечо и никуда не отпускала.\n\n"
            "😽 совсем скоро мы снова увидимся.\n\n"
            "💘 а пока знай — я тоже очень скучаю по тебе."
        )


bot.infinity_polling()
       
    
