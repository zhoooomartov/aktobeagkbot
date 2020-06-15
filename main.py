import telebot
from telebot import types
token = "1125286137:AAFpfszaWPwoVQo0VbZ26tdgRqTCchcYWhU"
bot = telebot.TeleBot(token)

#Главный меню
@bot.message_handler(content_types=["text"])
def any_msg(message):
    send_mess = f"<b>Саламатсызба {message.from_user.first_name} {message.from_user.last_name}</b>!\n🇰🇿Тілді таңдаңыз/🇷🇺Выберите язык"
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    first_button = types.InlineKeyboardButton(text="🇰🇿Қазақ тілі", callback_data="first")
    second_button = types.InlineKeyboardButton(text="🇷🇺Руский язык", callback_data="second")
    kontakt_button = types.InlineKeyboardButton(text="📲Контакты", callback_data="kontakty")
    keyboardmain.add(first_button, second_button, kontakt_button)
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "mainmenu1":
        keyboardmain = types.InlineKeyboardMarkup(row_width=2)
        first_button = types.InlineKeyboardButton(text="🇰🇿Қазақ тілі", callback_data="first")
        second_button = types.InlineKeyboardButton(text="🇷🇺Руский язык", callback_data="second")
        kontakt_button = types.InlineKeyboardButton(text="📲Контакты", callback_data="kontakty")
        keyboardmain.add(first_button, second_button, kontakt_button )
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="🇰🇿Тілді таңдаңыз/🇷🇺Выберите язык",reply_markup=keyboardmain)

    #Контакты
    if call.data == "kontakty":
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        k1 = types.InlineKeyboardButton(text="📞Call Center", callback_data="nom1")
        k2 = types.InlineKeyboardButton(text="☎Қабылдау бөлімі", callback_data="nom2")
        k3 = types.InlineKeyboardButton(text="🔎WhatsApp", url="https://api.whatsapp.com/send?phone=77074560230")
        k4 = types.InlineKeyboardButton(text="🔎Сайт", url="http://aktobe-agk.kz")
        k5 = types.InlineKeyboardButton(text="🔎Instagram", url="https://www.instagram.com/aktobeagk/")
        k6 = types.InlineKeyboardButton(text="🔎Вконтакте", url="https://vk.com/aktobeagk")
        k7 = types.InlineKeyboardButton(text="🔎Facebook", url="https://Facebook.com/aktobeagk")
        k8 = types.InlineKeyboardButton(text="🔎YouTube", url="https://YouTube.com/aktobeagk")
        k9 = types.InlineKeyboardButton(text="🔎Telegram", url="https://t.me/aktobeagk")
        backbutton = types.InlineKeyboardButton(text="🔙Кері", callback_data="mainmenu1")
        keyboard.add(k1, k2, k3, k4, k5, k6, k7, k8, k9, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📍 Ақтөбе қаласы, Есет батыр көшесі 73",reply_markup=keyboard)

    elif call.data == "nom1":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="🔙Кері", callback_data="kontakty")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="📞Call Center 24/7         +77074560230", reply_markup=keyboard)

    elif call.data == "nom2":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        backbutton = types.InlineKeyboardButton(text="🔙Кері", callback_data="kontakty")
        keyboard.add(backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="☎Директордың қабылдау бөлімі +77132560230", reply_markup=keyboard)

    #Орысша жагы
    if call.data == "second":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="🏫О колледже", url="https://telegra.ph/okolledzheru-04-25")
        rele2 = types.InlineKeyboardButton(text="👨‍🎓Студент", callback_data="22")
        rele3 = types.InlineKeyboardButton(text="‼Абитуриент", callback_data="33")
        rele4 = types.InlineKeyboardButton(text="🕘Сроки приема документов", url="https://telegra.ph/kuzhatru-04-25")
        rele5 = types.InlineKeyboardButton(text="🏣Общежитие", url="https://telegra.ph/zhataqhanaru-04-25")
        rele6 = types.InlineKeyboardButton(text="⚡️Вступительная онлайн анкета", url="https://clck.ru/NAEHC")
        backbutton = types.InlineKeyboardButton(text="🔙Назад", callback_data="mainmenu1")
        keyboard.add(rele1, rele2, rele3, rele6, rele4, rele5, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="🔷Меню",reply_markup=keyboard)

    elif call.data == "22":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        stud1 = types.InlineKeyboardButton(text="⁉Задавать вопросы", callback_data="s1")
        stud2 = types.InlineKeyboardButton(text="ℹПолучить справку", callback_data="s2")
        backbutton = types.InlineKeyboardButton(text="🔙Назад", callback_data="second")
        keyboard3.add(stud1, stud2, backbutton, )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    elif call.data == "33":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        tal1 = types.InlineKeyboardButton(text="🔎Дневное отделение", callback_data="t11")
        tal2 = types.InlineKeyboardButton(text="🔎Дистанционное обучение", callback_data="t22")
        backbutton = types.InlineKeyboardButton(text="🔙Назад", callback_data="second")
        keyboard3.add(tal1, tal2, backbutton, )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    elif call.data == "t11":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        kl9 = types.InlineKeyboardButton(text="🔎После 9 класса", callback_data="k99")
        kl11 = types.InlineKeyboardButton(text="🔎После 11 класса", callback_data="k111")
        backbutton = types.InlineKeyboardButton(text="🔙Назад", callback_data="33")
        keyboard3.add(kl9, kl11, backbutton,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    elif call.data == "t22":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        dkl11 = types.InlineKeyboardButton(text="🔎После 11 класса или после колледжа", callback_data="dkl111")
        backbutton = types.InlineKeyboardButton(text="🔙Назад", callback_data="33")
        keyboard3.add(dkl11, backbutton,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    elif call.data == "k99":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        mam1 = types.InlineKeyboardButton(text="🔎0101013 «Воспитатель дошкольных организаций»", url="https://telegra.ph/0101013mdru-04-25")
        mam2 = types.InlineKeyboardButton(text="🔎0105013 «Учитель начального образования»", url="https://telegra.ph/0105013bkru-04-25")
        mam3 = types.InlineKeyboardButton(text="🔎0105033 «Учитель иностранного языка начального образования»", url="https://telegra.ph/0105033flru-04-25")
        mam4 = types.InlineKeyboardButton(text="🔎0111013 «Учитель казахского языка и литературы»", url="https://telegra.ph/0111013ktru-04-25")
        mam5 = types.InlineKeyboardButton(text="🔎0111063 «Учитель математики»", url="https://telegra.ph/0111063mkru-04-25")
        mam6 = types.InlineKeyboardButton(text="🔎0403013 «Педагог - организатор»", url="https://telegra.ph/0403013odru-04-25")
        backbutton = types.InlineKeyboardButton(text="🔙Назад", callback_data="t11")
        keyboard3.add(mam1, mam2, mam3, mam4, mam5, mam6, backbutton,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    elif call.data == "k111":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        mam1 = types.InlineKeyboardButton(text="🔎0101013 «Воспитатель дошкольных организаций»", url="https://telegra.ph/0101013mdru-04-25")
        mam2 = types.InlineKeyboardButton(text="🔎0105013 «Учитель начального образования»", url="https://telegra.ph/0105013bkru-04-25")
        mam4 = types.InlineKeyboardButton(text="🔎0111013 «Учитель казахского языка и литературы»", url="https://telegra.ph/0111013ktru-04-25")
        mam5 = types.InlineKeyboardButton(text="🔎0111063 «Учитель математики»", url="https://telegra.ph/0111063mkru-04-25")
        mam7 = types.InlineKeyboardButton(text="🔎0108000 «Музыкальное образование»", url="https://telegra.ph/0108000sbru-04-25")
        mam8 = types.InlineKeyboardButton(text="🔎0401013 «Библиотекарь»",url="https://telegra.ph/0401013kitru-04-25")
        backbutton = types.InlineKeyboardButton(text="🔙Назад", callback_data="t11")
        keyboard3.add(mam1, mam2, mam7, mam4, mam5, mam8, backbutton, )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    elif call.data == "dkl111":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        mam1 = types.InlineKeyboardButton(text="🔎0101013 «Воспитатель дошкольных организаций»", url="https://telegra.ph/0101013mdru-04-25")
        mam8 = types.InlineKeyboardButton(text="🔎0401013 «Библиотекарь»", url="https://telegra.ph/0401013kitru-04-25")
        backbutton = types.InlineKeyboardButton(text="🔙Назад", callback_data="t22")
        keyboard3.add(mam1, mam8, backbutton,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    #Казахша жагы
    if call.data == "first":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rele1 = types.InlineKeyboardButton(text="🏫Колледж туралы ақпарат", url="https://telegra.ph/okolledzhe-04-25")
        rele2 = types.InlineKeyboardButton(text="👨‍🎓Студент", callback_data="2")
        rele3 = types.InlineKeyboardButton(text="‼Талапкер", callback_data="3")
        rele4 = types.InlineKeyboardButton(text="🕘Құжаттарды қабылдау уақыты", url="https://telegra.ph/kuzhat-04-25")
        rele5 = types.InlineKeyboardButton(text="🏣Жатақхана", url="https://telegra.ph/zhataqhana-04-25")
        rele6 = types.InlineKeyboardButton(text="⚡Оқуға түсер алды сауалнама", url="https://clck.ru/NAEHC")
        backbutton = types.InlineKeyboardButton(text="🔙Кері", callback_data="mainmenu1")
        keyboard.add(rele1, rele2, rele3, rele6, rele4, rele5, backbutton)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="🔷Меню",reply_markup=keyboard)

    elif call.data == "2":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        stud1 = types.InlineKeyboardButton(text="⁉Cұрақтар қалдыру", callback_data="s1")
        stud2 = types.InlineKeyboardButton(text="ℹАнықтама алу", callback_data="s2")
        backbutton = types.InlineKeyboardButton(text="🔙Кері", callback_data="first")
        keyboard3.add(stud1, stud2, backbutton,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    elif call.data == "3":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        tal1 = types.InlineKeyboardButton(text="🔎Күндізгі оқу бөлімі", callback_data="t1")
        tal2 = types.InlineKeyboardButton(text="🔎Қашықтан оқу", callback_data="t2")
        backbutton = types.InlineKeyboardButton(text="🔙Кері", callback_data="first")
        keyboard3.add(tal1, tal2, backbutton, )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    elif call.data == "t1":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        kl9 = types.InlineKeyboardButton(text="🔎9 сыныптан кейін", callback_data="k9")
        kl11 = types.InlineKeyboardButton(text="🔎11 сыныптан кейін", callback_data="k11")
        backbutton = types.InlineKeyboardButton(text="🔙Кері", callback_data="3")
        keyboard3.add(kl9, kl11, backbutton,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    elif call.data == "t2":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        dkl11 = types.InlineKeyboardButton(text="🔎11 сыныптан немесе колледжден кейін", callback_data="dkl11")
        backbutton = types.InlineKeyboardButton(text="🔙Кері", callback_data="3")
        keyboard3.add(dkl11, backbutton,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    elif call.data == "k9":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        mam1 = types.InlineKeyboardButton(text="🔎0101013 «Мектепке дейінгі ұйымдардың тәрбиешісі", url="https://telegra.ph/0101013md-04-25")
        mam2 = types.InlineKeyboardButton(text="🔎0105013 «Бастауыш білім беру мұғалімі»", url="https://telegra.ph/0105013bk-04-25")
        mam3 = types.InlineKeyboardButton(text="🔎0105033 «Шетел тілінен бастауыш білім беру мұғалімі»", url="https://telegra.ph/0105033fl-04-25")
        mam4 = types.InlineKeyboardButton(text="🔎0111013 «Қазақ тілі мен әдебиеті мұғалімі»", url="https://telegra.ph/0111013kaz-04-25")
        mam5 = types.InlineKeyboardButton(text="🔎0111063 «Математика мұғалімі»", url="https://telegra.ph/011106mat-04-25")
        mam6 = types.InlineKeyboardButton(text="🔎0403013 «Ұйымдастырушы-педагог»", url="https://telegra.ph/040301od-04-25")
        backbutton = types.InlineKeyboardButton(text="🔙Кері", callback_data="t1")
        keyboard3.add(mam1, mam2, mam3, mam4, mam5, mam6, backbutton,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    elif call.data == "k11":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        mam1 = types.InlineKeyboardButton(text="🔎0101013 «Мектепке дейінгі ұйымдардың тәрбиешісі", url="https://telegra.ph/0101013md-04-25")
        mam2 = types.InlineKeyboardButton(text="🔎0105013 «Бастауыш білім беру мұғалімі»", url="https://telegra.ph/0105013bk-04-25")
        mam4 = types.InlineKeyboardButton(text="🔎0111013 «Қазақ тілі мен әдебиеті мұғалімі»", url="https://telegra.ph/0111013kaz-04-25")
        mam5 = types.InlineKeyboardButton(text="🔎0111063 «Математика мұғалімі»", url="https://telegra.ph/011106mat-04-25")
        mam7 = types.InlineKeyboardButton(text="🔎0108000 «Музыкалық білім беру»", url="https://telegra.ph/0108000muz-04-25")
        mam8 = types.InlineKeyboardButton(text="🔎0401013 «Кітапханашы»",url="https://telegra.ph/0401013kitap-04-25")
        backbutton = types.InlineKeyboardButton(text="🔙Кері", callback_data="t1")
        keyboard3.add(mam1, mam2, mam7, mam4, mam5, mam8, backbutton, )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

    elif call.data == "dkl11":
        keyboard3 = types.InlineKeyboardMarkup(row_width=1)
        mam1 = types.InlineKeyboardButton(text="🔎0101013 «Мектепке дейінгі ұйымдардың тәрбиешісі", url="https://telegra.ph/0101013md-04-25")
        mam8 = types.InlineKeyboardButton(text="🔎0401013 «Кітапханашы»", url="https://telegra.ph/0401013kitap-04-25")
        backbutton = types.InlineKeyboardButton(text="🔙Кері", callback_data="t2")
        keyboard3.add(mam1, mam8, backbutton,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔷Меню", reply_markup=keyboard3)

if __name__ == "__main__":
    bot.polling(none_stop=True)