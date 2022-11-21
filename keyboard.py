from telebot import types
import telebot

teor_k = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
teor_k.add(telebot.types.KeyboardButton("Шугаринг"),
telebot.types.KeyboardButton("Ваксинг"),telebot.types.KeyboardButton("Тайминг"),
telebot.types.KeyboardButton("Противопоказания к депиляции"),telebot.types.KeyboardButton("Вернуться в главное меню"))


teor_m = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
teor_m.add(telebot.types.KeyboardButton("Глубокое бикини"),
telebot.types.KeyboardButton("Мышки"),telebot.types.KeyboardButton("Голени"),
telebot.types.KeyboardButton("Ножки полностью"),telebot.types.KeyboardButton("Ручки"), 
telebot.types.KeyboardButton("Ручки полностью"),telebot.types.KeyboardButton("Лицо"))
           
teor_p = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
teor_p.add(telebot.types.KeyboardButton("Мышки"),
telebot.types.KeyboardButton("Голени"),telebot.types.KeyboardButton("Ножки полностью"),
telebot.types.KeyboardButton("Ручки"),telebot.types.KeyboardButton("Ручки полностью"),
telebot.types.KeyboardButton("Лицо"),telebot.types.KeyboardButton("Назад"))

teor_f = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
teor_f.add(telebot.types.KeyboardButton("Глубокое бикини"),
telebot.types.KeyboardButton("Голени"),telebot.types.KeyboardButton("Ножки полностью"),
telebot.types.KeyboardButton("Ручки"),telebot.types.KeyboardButton("Ручки полностью"),
telebot.types.KeyboardButton("Лицо"),telebot.types.KeyboardButton("Назад"))
  
teor_a = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
teor_a.add(telebot.types.KeyboardButton("Глубокое бикини"),
telebot.types.KeyboardButton("Мышки"),telebot.types.KeyboardButton("Ножки полностью"),
telebot.types.KeyboardButton("Ручки"),telebot.types.KeyboardButton("Ручки полностью"),
telebot.types.KeyboardButton("Лицо"),telebot.types.KeyboardButton("Назад"))   

teor_v = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
teor_v.add(telebot.types.KeyboardButton("Глубокое бикини"),
telebot.types.KeyboardButton("Мышки"),telebot.types.KeyboardButton("Голени"),
telebot.types.KeyboardButton("Ручки"),telebot.types.KeyboardButton("Ручки полностью"),
telebot.types.KeyboardButton("Лицо"),telebot.types.KeyboardButton("Назад"))   

teor_c = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
teor_c.add(telebot.types.KeyboardButton("Глубокое бикини"),
telebot.types.KeyboardButton("Мышки"),telebot.types.KeyboardButton("Голени"),
telebot.types.KeyboardButton("Ножки полностью"),telebot.types.KeyboardButton("Ручки полностью"),
telebot.types.KeyboardButton("Лицо"),telebot.types.KeyboardButton("Назад"))   

teor_w = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
teor_w.add(telebot.types.KeyboardButton("Глубокое бикини"),
telebot.types.KeyboardButton("Мышки"),telebot.types.KeyboardButton("Голени"),
telebot.types.KeyboardButton("Ножки полностью"),telebot.types.KeyboardButton("Ручки"),
telebot.types.KeyboardButton("Лицо"),telebot.types.KeyboardButton("Назад"))    

teor_z = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
teor_z.add(telebot.types.KeyboardButton("Глубокое бикини"),
telebot.types.KeyboardButton("Мышки"),telebot.types.KeyboardButton("Голени"),
telebot.types.KeyboardButton("Ножки полностью"),telebot.types.KeyboardButton("Ручки"),
telebot.types.KeyboardButton("Ручки полностью"),telebot.types.KeyboardButton("Назад"))   

xyu_2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
xyu_2.add(telebot.types.KeyboardButton("вернуться"))

prise_list = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
prise_list.add(telebot.types.KeyboardButton("прайс-лист"),telebot.types.KeyboardButton("услуги студии"),
telebot.types.KeyboardButton("хочу записаться"), telebot.types.KeyboardButton("акции"),
telebot.types.KeyboardButton("часто задаваемы вопросы"))

prise_list2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
prise_list2.add(telebot.types.KeyboardButton("депиляция"), telebot.types.KeyboardButton("реснички"),
telebot.types.KeyboardButton("бровки"),telebot.types.KeyboardButton("маникюр"),
telebot.types.KeyboardButton("макияж"),telebot.types.KeyboardButton("вернуться в главное меню"))

prise_listD = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
prise_listD.add(telebot.types.KeyboardButton("реснички"),
telebot.types.KeyboardButton("бровки"),telebot.types.KeyboardButton("маникюр"),
telebot.types.KeyboardButton("макияж"),telebot.types.KeyboardButton("вернуться в главное меню"))

prise_listR = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
prise_listR.add(telebot.types.KeyboardButton("депиляция"),
telebot.types.KeyboardButton("бровки"),telebot.types.KeyboardButton("маникюр"),
telebot.types.KeyboardButton("макияж"),telebot.types.KeyboardButton("вернуться в главное меню"))

prise_listB = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
prise_listB.add(telebot.types.KeyboardButton("депиляция"), telebot.types.KeyboardButton("реснички"),
telebot.types.KeyboardButton("маникюр"),telebot.types.KeyboardButton("макияж"),
telebot.types.KeyboardButton("вернуться в главное меню"))

prise_listM = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
prise_listM.add(telebot.types.KeyboardButton("депиляция"), telebot.types.KeyboardButton("реснички"),
telebot.types.KeyboardButton("бровки"),telebot.types.KeyboardButton("макияж"),
telebot.types.KeyboardButton("вернуться в главное меню"))

prise_listMK = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
prise_listMK.add(telebot.types.KeyboardButton("депиляция"), telebot.types.KeyboardButton("реснички"),
telebot.types.KeyboardButton("бровки"),telebot.types.KeyboardButton("маникюр"),
telebot.types.KeyboardButton("вернуться в главное меню"))

prise_list2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
prise_list2.add(telebot.types.KeyboardButton("депиляция"), telebot.types.KeyboardButton("реснички"),
telebot.types.KeyboardButton("бровки"),telebot.types.KeyboardButton("маникюр"),
telebot.types.KeyboardButton("макияж"),telebot.types.KeyboardButton("вернуться в главное меню"))

pl_gm = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
pl_gm.add(telebot.types.KeyboardButton("вернуться"))

ysl_p = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
ysl_p.add(telebot.types.KeyboardButton("депиляция"), telebot.types.KeyboardButton("наращивание ресничек"),
telebot.types.KeyboardButton("ламинирование ресничек"),telebot.types.KeyboardButton("оформление бровей"),
telebot.types.KeyboardButton("маникюр"),telebot.types.KeyboardButton("макияж"),
telebot.types.KeyboardButton("вернуться в главное меню"))

time_w = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
time_w.add(telebot.types.KeyboardButton("глубокое бикини"),telebot.types.KeyboardButton("мышки"),
telebot.types.KeyboardButton("голени"),telebot.types.KeyboardButton("ножки поностью"),
telebot.types.KeyboardButton("ручик"),telebot.types.KeyboardButton("ручик полностью"),
telebot.types.KeyboardButton("лицо"),telebot.types.KeyboardButton("вернуться назад"))

time_l = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
time_l.add(telebot.types.KeyboardButton("назад"), telebot.types.KeyboardButton("записаться"),
telebot.types.KeyboardButton("вернуться в меню"))

time_d = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
time_d.add(telebot.types.KeyboardButton("хочу записаться"))