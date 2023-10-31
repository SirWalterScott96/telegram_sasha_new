import telebot


token = '5888218155:AAGydUJBuI8I6dMl2FpFYPM8cOT9M4SY9fU'

bot = telebot.TeleBot(token)
slot_glob = ''
slot_info = {
    '1': 'ставка',
    '2': 'опис',
    '3': 'результати',
}

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, 'Привіт Сашко')

@bot.message_handler(commands=['reset'])
def reset_slot(message):
    bot.send_message(message.chat.id, 'Позиція на нулі')

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, '1 - ставка\n'
                                      '2 - опис\n'
                                      '3 - результати')

@bot.message_handler(content_types=['text'])
def reset_slot(message):
    global slot_glob
    slot_glob = message.text
    bot.send_message(message.chat.id, f'Можна закидати зображення з {slot_info[slot_glob]}')


@bot.message_handler(content_types=['photo'])
def hande_image(message):
    file_id = message.photo[-1].file_id

    file_info = bot.get_file(file_id)
    file_path = file_info.file_path

    download_file = bot.download_file(file_path)

    with open(f'imgs\{slot_glob}.jpg', 'wb') as file:
        file.write(download_file)

    bot.send_message(message.chat.id, f'Загрузив зображення для {slot_info[slot_glob]}')


bot.infinity_polling()
