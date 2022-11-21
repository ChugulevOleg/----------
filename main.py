from telebot import *
from config import token
import telebot
from keyboard import *

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])


def hello (massage):
    bot.send_message(massage.chat.id,"<i>Привет, красотка !</i>", parse_mode="html")
    bot.send_message(massage.chat.id,"<i>Я онлайн админ студии красоты  «EPIL BAR» :)</i>", parse_mode="html")
    bot.send_message(massage.chat.id,"<i>С радостью отвечу на все твои вопросы и помогу записаться на процедуры!</i>", parse_mode="html")
    bot.send_message(massage.chat.id,"<i>Кстати, для всех новых клиентов у нас действует скидочка 10% на первое посещение! Обязательно ею воспользуйся!</i>", parse_mode="html")
    next = bot.send_message(massage.chat.id,"Какую информацию прислать?", reply_markup = prise_list)
    bot.register_next_step_handler(next,zp)
    
def vpr (massage):
    if massage.text.lower() == "вернуться":
        next = bot.send_message(massage.chat.id,"one секонд)", reply_markup = prise_list)
        bot.register_next_step_handler(next,zp)
        
def vprG (massage):
    if massage.text.lower() == "вернуться":
        next = bot.send_message(massage.chat.id,"оки, Красотка", reply_markup = prise_list)
        bot.register_next_step_handler(next,zp)
    

def zp (massage):
    if massage.text.lower() == "прайс-лист":
        next = bot.send_message(massage.chat.id,"one секонд)", reply_markup = prise_list2)
        bot.register_next_step_handler(next,pr)
    elif massage.text.lower() == "услуги студии":
        next = bot.send_message(massage.chat.id,"one секонд)", reply_markup = ysl_p)
        bot.register_next_step_handler(next,yc)
    elif massage.text.lower() == "хочу записаться":
        bot.send_message(massage.chat.id,"<i>Отлично! Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время.</i> Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ :)", parse_mode = "html", reply_markup = prise_list)
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,zp)
        
        
def pr (massage):
    if massage.text.lower() == "депиляция":
        # bot.send_photo(massage.chat.id,"")
        bot.send_message(massage.chat.id,"<i>Записать тебя?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ :)")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193", reply_markup = prise_listD)
        bot.register_next_step_handler(next,pr)
    if massage.text.lower() == "реснички":
        # bot.send_photo(massage.chat.id,"")
        bot.send_message(massage.chat.id,"<i>Записать тебя?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ :)")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193", reply_markup = prise_listR)
        bot.register_next_step_handler(next,pr)
    if massage.text.lower() == "бровки":
        # bot.send_photo(massage.chat.id,"")
        bot.send_message(massage.chat.id,"<i>Записать тебя?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ :)")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193", reply_markup = prise_listB)
        bot.register_next_step_handler(next,pr)   
    if massage.text.lower() == "маникюр":
        # bot.send_photo(massage.chat.id,"")
        bot.send_message(massage.chat.id,"<i>Записать тебя?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ :)")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193", reply_markup = prise_listM)
        bot.register_next_step_handler(next,pr)
    if massage.text.lower() == "макияж":
        # bot.send_photo(massage.chat.id,"")
        bot.send_message(massage.chat.id,"<i>Записать тебя?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ :)")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193", reply_markup = prise_listMK)
        bot.register_next_step_handler(next,pr)
    if massage.text.lower() == "вернуться в главное меню":
        next = bot.send_message(massage.chat.id,"one секонд)", reply_markup = pl_gm)
        bot.register_next_step_handler(next,vpr)
        
def yc (massage):
    if massage.text.lower() == "депиляция":
        bot.send_message(massage.chat.id,"<i>Вижу, интересуешься процедурой депиляции?  Отлично! Сейчас все - все расскажу!</i>", parse_mode="html", reply_markup = teor_k)
        next = bot.send_message(massage.chat.id,"<i>Важно - процедура выполняется сертифицированным мастером с использованием профессиональных средств до/после депиляции. Способ депиляции выбирает клиент самостоятельно (шугаринг/ваксин) с учетом рекомендаций мастера!</i>", parse_mode="html")
        bot.register_next_step_handler(next,talk)
        
    if massage.text.lower() == "вернуться в главное меню":
        next = bot.send_message(massage.chat.id,"one секонд)", reply_markup = xyu_2)
        bot.register_next_step_handler(next, vprG)

    
def talk (massage):
    if massage.text.lower() == "вернуться в меню":
        next = bot.send_message(massage.chat.id,"Секундочку", reply_markup = teor_k)  
        bot.register_next_step_handler(next,talk)
    elif massage.text.lower() == "шугаринг":
        bot.send_message(massage.chat.id,"Шугаринг-это удаление волос сахарной пастой. Самый, между прочим, безопасный способ удаления волос.")
        bot.send_message(massage.chat.id,"Процедура шугаринга проводится по протоколу:", reply_markup = teor_m)
        bot.send_message(massage.chat.id,"1.Преддепиляционная обработка кожи;")
        bot.send_message(massage.chat.id,"2.Тальк;")
        bot.send_message(massage.chat.id,"3.Удаление волос;")
        bot.send_message(massage.chat.id,"4.Постдепиляционная обработка кожи.")
        next = bot.send_message(massage.chat.id,"<i>Какую зону будем депилировать?</i>", parse_mode="html")
        bot.register_next_step_handler(next,shuga)
    elif massage.text.lower() == "ваксинг":
        bot.send_message(massage.chat.id,"Ваксинг –удаление волос с помощью воска. ")
        bot.send_message(massage.chat.id,"Воски, их великое множество! Пленочки, теплые, синтетика, натуральные, гибридные, полимерные, с диоксидом титана и без, для больших и маленьких зон, для лица, для чувствительной кожи и т.д.")
        bot.send_message(massage.chat.id,"Воски гипоаллергенны и не адгезивны к коже. Температура плавления 37-39 градусов в профессиональных воскоплавах. Соответственно практически исключена возможность ожога. Воски наносятся мягко, не вызывая болевых ощущений, они пластичны, работать можно большими аппликациями.")
        bot.send_message(massage.chat.id,"Протокол ваксинга:", reply_markup = teor_m)
        bot.send_message(massage.chat.id,"1.Преддепиляционная обработка кожи;")
        bot.send_message(massage.chat.id,"2.Тальк;")
        bot.send_message(massage.chat.id,"3.Удаление волос;")
        bot.send_message(massage.chat.id,"4.Постдепиляционная обработка кожи.")
        next = bot.send_message(massage.chat.id,"<i>Какая зона интересует?</i>", parse_mode="html")
        bot.register_next_step_handler(next,vosk)
    elif massage.text.lower() == "тайминг":
        next = bot.send_message(massage.chat.id,"<i>Расскажу все коротко и по делу!</i>", parse_mode="html", reply_markup = time_w)
        bot.register_next_step_handler(next,clok)
    elif massage.text.lower() == "противопоказания к депиляции":    
        bot.send_message(massage.chat.id,"1. Открытые ранки, порезы, ожоги от солнца или плойки тоже считаются.")
        bot.send_message(massage.chat.id,"2. Приём оральных контрацептивов и некоторых антибиотиков — происходит изменение чувствительности и процедура может быть болезненной или может оставить раздражение на коже.")
        bot.send_message(massage.chat.id,"3. Аллергия на воск и другие составляющие депиляционной массы")
        bot.send_message(massage.chat.id,"4. Беременность — все индивидуально, чаще просто непереносимость любой боли. Первый и третий триместр — когда особенно не рекомендована депиляция.")
        bot.send_message(massage.chat.id,"5. Варикозное расширение вен")
        bot.send_message(massage.chat.id,"6. Заболевания сердца")
        bot.send_message(massage.chat.id,"7. Плохая свертываемость крови")
        bot.send_message(massage.chat.id,"8. Герпес на стадии обострения")
        bot.send_message(massage.chat.id,"<i>Если противопоказаний нет, записать тебя на депиляцию?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на он-лайн запись! Там все очень просто!</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ :)</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193", reply_markup = xyu_2)
        bot.register_next_step_handler(next, talk)
    if massage.text.lower() == "вернуться в главное меню":
        next = bot.send_message(massage.chat.id,"one секонд)", reply_markup = pl_gm)
        bot.register_next_step_handler(next, vprG)

def shuga (massage):        
    if massage.text.lower() == "глубокое бикини":
        bot.send_message(massage.chat.id,"Депиляция зоны глубокого бикини - удаление нежелательных волос по линии трусиков, с лобковой зоны, с зоны половых губ и межъягодичной складки.", reply_markup = teor_p)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию зоны глубокого бикини?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,shuga)
    elif massage.text.lower() == "мышки":
        bot.send_message(massage.chat.id,"Депиляция подмышечных впадин - удаление нежелательных волос в подмышечных впадинах.", reply_markup = teor_f)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию подмышечек?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,shuga)
    elif massage.text.lower() == "голени":
        bot.send_message(massage.chat.id,"Депиляция голеней - удаление нежелательных волос с зоны голени, включая коленочку и пальцы ног.", reply_markup = teor_a)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию голеней?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!,</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,shuga)
    elif massage.text.lower() == "ножки полностью":
        bot.send_message(massage.chat.id,"Депиляция зоны ног - удаление нежелательных волос с зоны голени, колена и бедра. ", reply_markup = teor_v)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию ног?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!,</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,shuga)
    elif massage.text.lower() == "ручки":
        bot.send_message(massage.chat.id,"Депиляция ручек до локтя - удаление нежелательных волос с рук до зоны локтя, включая тыльную сторону ладони и пальчики рук. ", reply_markup = teor_c)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию ручек?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!,</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,shuga)
    elif massage.text.lower() == "ручки полностью":
        bot.send_message(massage.chat.id,"Депиляция ручек полностью - удаление нежелательных волос с рук до зоны предплечья, включая тыльную сторону ладони и пальчики рук. ", reply_markup = teor_w)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию ручек?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!,</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,shuga)
    elif massage.text.lower() == "лицо":
        bot.send_message(massage.chat.id,"Депиляция лица - удаление нежелательных волос над верхней губой (усики).")
        bot.send_message(massage.chat.id,"Зона под нижней губой, зона подбородочка, зона щек, носик - являются отдельными зонами.", reply_markup = teor_z)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию лица?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!,</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,shuga)
    elif massage.text.lower() == "назад":
        next = bot.send_message(massage.chat.id,"Секундочку", reply_markup = teor_k)  
        bot.register_next_step_handler(next,talk)
        
def vosk(massage):
    if massage.text.lower() == "глубокое бикини":
        bot.send_message(massage.chat.id,"Депиляция зоны глубокого бикини - удаление нежелательных волос по линии трусиков, с лобковой зоны, с зоны половых губ и межъягодичной складки.", reply_markup = teor_p)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию зоны глубокого бикини?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,vosk)
    elif massage.text.lower() == "мышки":
        bot.send_message(massage.chat.id,"Депиляция подмышечных впадин - удаление нежелательных волос в подмышечных впадинах.", reply_markup = teor_f)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию подмышечек?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,vosk)
    elif massage.text.lower() == "голени":
        bot.send_message(massage.chat.id,"Депиляция голеней - удаление нежелательных волос с зоны голени, включая коленочку и пальцы ног.", reply_markup = teor_a)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию голеней?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!,</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,vosk)
    elif massage.text.lower() == "ножки полностью":
        bot.send_message(massage.chat.id,"Депиляция зоны ног - удаление нежелательных волос с зоны голени, колена и бедра. ", reply_markup = teor_v)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию ног?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!,</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,vosk)
    elif massage.text.lower() == "ручки":
        bot.send_message(massage.chat.id,"Депиляция ручек до локтя - удаление нежелательных волос с рук до зоны локтя, включая тыльную сторону ладони и пальчики рук. ", reply_markup = teor_c)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию ручек?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!,</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,vosk)
    elif massage.text.lower() == "ручки полностью":
        bot.send_message(massage.chat.id,"Депиляция ручек полностью - удаление нежелательных волос с рук до зоны предплечья, включая тыльную сторону ладони и пальчики рук. ", reply_markup = teor_w)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию ручек?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!,</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,vosk)
    elif massage.text.lower() == "лицо":
        bot.send_message(massage.chat.id,"Депиляция лица - удаление нежелательных волос над верхней губой (усики).")
        bot.send_message(massage.chat.id,"Зона под нижней губой, зона подбородочка, зона щек, носик - являются отдельными зонами.", reply_markup = teor_z)
        bot.send_message(massage.chat.id,"<i>Записать тебя на депиляцию лица?</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Сейчас пришлю ссылочку на онлайн запись! Там все очень просто!,</i>", parse_mode="html")
        bot.send_message(massage.chat.id,"<i>Выбираем либо по мастеру, либо по услуге. Далее смотрим удобный день и время. Вводим свои данные и нажимаем кнопочку ЗАПИСАТЬСЯ</i>", parse_mode="html")
        next = bot.send_message(massage.chat.id,"Записаться можно по ссылки: https://widget.sonline.su/ru/services/?placeid=999960193")
        bot.register_next_step_handler(next,vosk)
    elif massage.text.lower() == "назад":
        next = bot.send_message(massage.chat.id,"Секундочку", reply_markup = teor_k)  
        bot.register_next_step_handler(next,talk)
        
def clok (massage):
    if massage.text.lower() == "назад":
        next = bot.send_message(massage.chat.id,"one секонд)", reply_markup = time_w)
        bot.register_next_step_handler(next,clok)
    elif massage.text.lower() == "глубокое бикини":
        next = bot.send_message(massage.chat.id,"Процедура занимает от 15- 45 мин.", reply_markup = time_l)
        bot.register_next_step_handler(next,clok)
    elif massage.text.lower() == "мышки":
        next = bot.send_message(massage.chat.id,"Процедура занимает от 5 -15 мин.)", reply_markup = time_l)
        bot.register_next_step_handler(next,clok)
    elif massage.text.lower() == "голени":
        next = bot.send_message(massage.chat.id,"Процедура занимает от 15 - 45мин.", reply_markup = time_l)
        bot.register_next_step_handler(next,clok)
    elif massage.text.lower() == "ножки поностью":
        next = bot.send_message(massage.chat.id,"Процедура занимает от 30 - 60 мин.", reply_markup = time_l)
        bot.register_next_step_handler(next,clok)
    elif massage.text.lower() == "ручик":
        next = bot.send_message(massage.chat.id,"Процедура занимает от 15 - 30 мин.", reply_markup = time_l)
        bot.register_next_step_handler(next,clok)
    elif massage.text.lower() == "ручик полностью":
        next = bot.send_message(massage.chat.id,"Процедура занимает от 30 - 60 мин.", reply_markup = time_l)
        bot.register_next_step_handler(next,clok)
    elif massage.text.lower() == "лицо":
        next = bot.send_message(massage.chat.id,"Процедура занимает от 5 - 30 мин.", reply_markup = time_l)
        bot.register_next_step_handler(next,clok)
    elif massage.text.lower() == "вернуться назад":
        next = bot.send_message(massage.chat.id,"one секонд)", reply_markup = teor_k)
        bot.register_next_step_handler(next,talk)
    elif massage.text.lower() == "записаться":
        next = bot.send_message(massage.chat.id,"one секонд)", reply_markup = time_d)
        bot.register_next_step_handler(next,zp)
    elif massage.text.lower() == "вернуться в меню":
        next = bot.send_message(massage.chat.id,"one секонд)", reply_markup = teor_k)
        bot.register_next_step_handler(next,talk)
 
        
        
    

        



print("Бот запущен")

bot.infinity_polling()