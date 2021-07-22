
import telebot, config
import random

bot = telebot.TeleBot(config.key)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Добро пожаловать в игру 'Камень, ножницы, бумага'!\nНапиши свой вариант!")
    else:
        table = ['камень', 'ножницы', 'бумага']
        choise_user = message.text.lower()
        choise_pc = table[random.randint(0,2)]
        if choise_pc != choise_user:
            if choise_pc == "камень":
                if choise_user == "ножницы":
                    bot.send_message(message.chat.id, f"Мой выбор {choise_pc}, а ты выбрал {choise_user}, Я ВЫИГРАЛ!!!")
                elif choise_user == "бумага":
                    bot.send_message(message.chat.id, f"Мой выбор {choise_pc}, а ты выбрал {choise_user}, Ты победил...")
                elif choise_user != "камень" and choise_user != "ножницы" and choise_user != "бумага":
                    bot.send_message(message.chat.id, "Я же сказал писать либо ножницы, либо камень, либо бумага! давай заново.")
            elif choise_pc == "ножницы":
                if choise_user == "камень":
                    bot.send_message(message.chat.id, f"Мой выбор {choise_pc}, а ты выбрал {choise_user}, Ты победил...")
                elif choise_user == "бумага":
                    bot.send_message(message.chat.id, f"Мой выбор {choise_pc}, а ты выбрал {choise_user}, Я ВЫИГРАЛ!!!")
                elif choise_user != "камень" and choise_user != "ножницы" and choise_user != "бумага":
                    bot.send_message(message.chat.id, "Я же сказал писать либо ножницы, либо камень, либо бумага! давай заново.")
            elif choise_pc == "бумага":
                if choise_user == "камень":
                    bot.send_message(message.chat.id, f"Мой выбор {choise_pc}, а ты выбрал {choise_user}, Я ВЫИГРАЛ!!!")
                elif choise_user == "ножницы":
                    bot.send_message(message.chat.id, f"Мой выбор {choise_pc}, а ты выбрал {choise_user}, Ты победил...")
                elif choise_user != "камень" and choise_user != "ножницы" and choise_user != "бумага":
                    bot.send_message(message.chat.id, "Я же сказал писать либо ножницы, либо камень, либо бумага! давай заново.")
        else:
            bot.send_message(message.chat.id, 'Мы с тобой выбрали одно и тоже, продолжаем!')

bot.polling()