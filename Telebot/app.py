bot = telebot.TeleBot(TOKEN)

# Функция обработки команды /start
@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Привет! \nЯ - волшебный конвертер валют и я вот какие чудеса я могу совершать. Вам нужно лишь ввести команду:  \n' \
           '- Показать список доступных для конвертации валют - /values \n' \
           '- Уточнить как здесь что работает - /help \n' \
           '(Но по секрету и только Вам скажу) Для конвертации валюты напишите заклинание: \n' \
           '<название валюты> <в какую валюту Вы желаете её перевести> <количество переводимой валюты>\n' \
    bot.reply_to(message, text)

# Функция обработки команды /help
@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = "Чтобы случилось чудо конвертации - введите команду в следующем формате:\n<имя валюты>,\
    <в какую валюту перевести>,\
     <количество валюты>\n Увидеть список всех доступных валют /values "
    bot.reply_to(message, text)

# Функция обработки команды /values
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Конвертация доступна для следующих валют:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

# Основная функция обработки команды на конвертацию с учетом возможных ошибок
@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Ай-яй-яй, Вы ввели слишком много или таки слишком мало параметров')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка ввода\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать комманду\n{e}')
    else:
        text = f'При конвертации {amount} единиц валюты {quote} - Вы получите {round(float(total_base) * float(amount), 2)} единиц валюты {base}'
        bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)