import telebot
from config import keys, TOKEN
from utilits import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def instructions(message: telebot.types.Message):
    text = 'Для начала работы введите команду в следующем формате:  \
\n<имя валюты цену которой надо узнать> \ <имя валюты в которой считать цену> \ <количество первой валюты> \
\n Увидить список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)
    


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):

    values = message.text.lower()
    values = values.split(' ')
    try:
        if len(values) > 3:
            raise ConvertionException('Слишком много параметров.')
        elif len(values) < 3:
            raise ConvertionException('Недостаточно параметров')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()
