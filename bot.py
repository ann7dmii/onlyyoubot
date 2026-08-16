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
    btn6 = types.KeyboardButton("💗 сколько я тебя люблю")
    btn3 = types.KeyboardButton("💌 сообщение от Ани")
    btn4 = types.KeyboardButton("🌙 если тебе грустно")
    btn5 = types.KeyboardButton("💌 открыть, когда...")
    btn7 = types.KeyboardButton("🔐 только для тебя")
    btn8 = types.KeyboardButton("🎲 случайное воспоминание")
    
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    keyboard.add(btn5)
    keyboard.add(btn6)
    keyboard.add(btn7, btn8)

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
            "❤️ почему я тебя люблю...\n\n"
            "я люблю тебя за то, какой ты есть.\n"
            "за то, как ты любишь меня, как относишься ко мне "
            "и как ведёшь себя рядом со мной.\n\n"
            "я люблю тебя не потому, что кто-то когда-то сказал мне, "
            "что именно так должна выглядеть любовь.\n"
            "я люблю тебя потому, что рядом с тобой я чувствую "
            "то, чего не чувствовала ни с кем другим 🥹\n\n"
            "мне нравится твой характер, твой голос, твои привычки, "
            "твои смешные моменты и даже те мелочи, которые иногда "
            "меня бесят 😭❤️\n\n"
            "я люблю наши разговоры, наши прогулки, наши объятия "
            "и даже самые обычные моменты, когда мы просто рядом "
            "и нам больше ничего не нужно 🫂\n\n"
            "спасибо тебе за то, что ты есть в моей жизни.\n"
            "за то, что любишь меня именно такой, какая я есть, "
            "со всеми моими загонами, переживаниями и странностями 🥹\n\n"
            "и самое главное — я люблю тебя просто потому, что это ты.\n\n"
            "и если бы мне снова пришлось выбирать, кого любить,\n"
            "я бы снова выбрала тебя.\n"
            "снова и снова. ❤️"
        )
    
    elif message.text == "📸 наши моменты":
        keyboard = types.InlineKeyboardMarkup()
        
        btn1 = types.InlineKeyboardButton(
        "🤍 первый момент",
        callback_data="first_moment"
        )
        
        btn2 = types.InlineKeyboardButton(
        "🥹 самые счастливые дни",
        callback_data="happy_days"
        )
        
        btn3 = types.InlineKeyboardButton(
        "🫂 наши обнимашки",
        callback_data="hugs"
        )
        
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        
        bot.send_message(
            message.chat.id,
            "📸 наш маленький альбом ❤️\n\n"
            "здесь будут храниться наши самые тёплые моменты 🥹\n\n"
            "каждая фотография — это маленькое воспоминание о нас 🤍\n\n"
            "выбери, что хочешь открыть 🫶",
            reply_markup=keyboard
        )
    
    elif message.text == "💗 сколько я тебя люблю":
        bot.send_message(
            message.chat.id,
            "💗 ты знаешь, сколько я тебя люблю?\n\n"
            "настолько, что никакого числа просто не существует 🥹\n\n"
            "я люблю тебя больше, чем могу объяснить словами.\n\n"
            "больше всех километров между нами,\n"
            "больше всех звёзд на небе,\n"
            "больше, чем ты даже можешь представить ❤️\n\n"
            "и если ты когда-нибудь спросишь меня:\n"
            "«насколько сильно?»\n\n"
            "я просто снова отвечу:\n"
            "«очень. безумно. бесконечно.» 🫂❤️"
        )
    
    elif message.text == "🔐 только для тебя":
        keyboard = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton(
            "❤️ открыть",
            callback_data="secret_open"
        )

        btn2 = types.InlineKeyboardButton(
            "🙈 передумал",
            callback_data="secret_no"
        )

        keyboard.add(btn1, btn2)

        bot.send_message(
            message.chat.id,
            "🔐 здесь спрятано кое-что только для тебя...\n\n"
            "ты точно хочешь открыть? 👀❤️",
            reply_markup=keyboard
        )
    
    elif message.text == "💌 сообщение от Ани":
        bot.send_message(
            message.chat.id,
            "💌 маленькое сообщение от Ани...\n\n"
            "тима, я хочу, чтобы ты всегда помнил одну вещь ❤️\n\n"
            "ты для меня очень особенный человек.\n\n"
            "спасибо тебе за все моменты, за смех, за объятия и за то, что ты рядом 🫂\n\n"
            "мне очень нравится просто быть с тобой, разговаривать с тобой и чувствовать, что у меня есть ты 🤍\n\n"
            "я надеюсь, что этот маленький бот иногда будет напоминать тебе о том, как сильно я тебя люблю 💘"
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
        
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "first_moment":
        bot.send_photo(
            call.message.chat.id,
            photo="AgACAgIAAxkBAAIBR2qBsrX-xMcXg_3DhjOu5phPSq8ZAAJSGmsbMREISOfeoP95QpZ9AQADAgADeQADPQQ",
            caption=
            "🤍 наш самый первый совместный момент...\n\n"
            "это наша первая фотография вместе 🥹\n\n"
            "тогда мы впервые пошли гулять вдвоём, "
            "а я ужасно стеснялась тебя 😭🤍\n\n"
            "сейчас даже немного смешно вспоминать, "
            "какая я была смущённая, но именно с этого маленького момента "
            "началось столько всего нашего 🫂❤️"
        )
    
    elif call.data == "happy_days":
        bot.send_photo(
            call.message.chat.id,
            photo="AgACAgIAAxkBAAIBWGqBttVKCdjLDsRnHByMK6A_lwqZAAJkGmsbMREISClb5qP3gUyAAQADAgADeQADPQQ",
            caption=
            "🥹 наши самые счастливые дни...\n\n"
            "иногда я пересматриваю наши фотографии "
            "и понимаю, как же много у нас уже всего было ❤️\n\n"
            "столько смеха, прогулок, объятий и маленьких моментов, "
            "которые хочется сохранить навсегда 🫂\n\n"
            "🤍 надеюсь, что впереди у нас будет ещё очень много "
            "таких счастливых дней."
        )
    
    elif call.data == "hugs":
        bot.send_photo(
            call.message.chat.id,
            photo="AgACAgIAAxkBAAIBXWqBt4nU1xldu10bCnB41BskIvT1AAJoGmsbMREISL94UBZwDRobAQADAgADeQADPQQ",
            caption=
            "🫂 наши обнимашки...\n\n"
            "есть моменты, которые даже не хочется описывать словами 🤍\n\n"
            "мне просто нравится обнимать тебя "
            "и чувствовать, что в этот момент ты рядом ❤️\n\n"
            "🥹 пусть таких обнимашек у нас будет ещё бесконечно много."
        )

    elif call.data == "miss":
        bot.send_photo(
            call.message.chat.id,
            photo="AgACAgIAAxkBAANham-xaGp3fBbmcP4nypd038wm4MIAArkhaxvHQIBLK0TLc4aDnQ4BAAMCAAN5AAM9BA",
            caption=
            "🥺 если ты сейчас скучаешь по мне...\n\n"
            "🤍 представь, что я рядом.\n\n"
            "🫂 я бы крепко тебя обняла и никуда не отпускала.\n\n"
            "💘 я тоже очень скучаю по тебе."
        )

    elif call.data == "sleep":
        bot.send_photo(
            call.message.chat.id,
            photo="AgACAgIAAxkBAANqam-0wU3sUmSkA2ItpViJ39V0ftUAArwhaxvHQIBLy8EAAfBMkZT5AQADAgADeQADPQQ",
            caption=
            "😴 если ты не можешь уснуть...\n\n"
            "🤍 закрой глаза и представь, что я рядом.\n\n"
            "🫂 желаю тебе самых спокойных снов."
        )

    elif call.data == "support":
        bot.send_photo(
            call.message.chat.id,
            photo="AgACAgIAAxkBAAO6am_H5R3s9SGbeDE8XAJpaW9cPtIAAi4Zaxtu_YBLU_NnL6Lbb2EBAAMCAAN5AAM9BA",
            caption=
            "💪 если тебе нужна поддержка...\n\n"
            "🤍 помни, что я верю в тебя.\n\n"
            "❤️ у тебя всё получится."
        )

    elif call.data == "sad2":
        bot.send_photo(
            call.message.chat.id,
            photo="AgACAgIAAxkBAAOzam_HeW-ErqDw_Dsrb9dFHS7Kiu8AAl4XaxsfF4FL7p8YaqKlHigBAAMCAAN5AAM9BA",
            caption=
            "🌧️ если тебе грустно...\n\n"
            "🤍 плохие моменты проходят.\n\n"
            "🫂 я рядом и всегда поддержу тебя."
        )
    
    elif call.data == "secret_open":
        bot.send_message(
            call.message.chat.id,
            "🔐 СЕКРЕТНЫЙ ДОКУМЕНТ\n\n"
            "после длительного и крайне серьёзного расследования было установлено:\n\n"
            "ты официально признан самым любимым человеком Ани. ❤️\n\n"
            "также установлено, что срок твоего наказания — пожизненный.\n\n"
            "в обязанности входит:\n"
            "— терпеть мои загоны 😭\n"
            "— выслушивать мои «ты точно меня любишь?»\n"
            "— переживать мои моменты ревности\n"
            "— обнимать меня, когда я грущу 🫂\n"
            "— и вообще никуда от меня не деваться 😈❤️\n\n"
            "обжалованию не подлежит.\n\n"
            "приговор окончательный: любить Аню.\n\n"
            "а теперь самое главное...\n\n"
            "я долго думала, что ещё написать сюда.\n\n"
            "очень долго.\n\n"
            "целых 3 минуты.\n\n"
            "и после тщательного анализа ситуации пришла "
            "к единственно правильному выводу:\n\n"
            "КУПИ МНЕ ЧТО-НИБУДЬ ВКУСНОЕ. 😭\n\n"
            "всё.\n"
            "секрет раскрыт.\n"
            "спасибо за внимание. 😂❤️"
        )
        
    elif call.data == "secret_no":
        bot.send_message(
            call.message.chat.id,
            "🙈 ну и ладно...\n\n"
            "но я всё равно знаю, что тебе интересно 👀😂❤️"
        )


@bot.message_handler(content_types=['photo'])
def get_photo_id(message):
    bot.send_message(
        message.chat.id,
        message.photo[-1].file_id
    )
        
    
    
    
        


bot.infinity_polling()
       
    
