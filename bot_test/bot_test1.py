from random import choice
from telegram import ReplyKeyboardMarkup
import logging
import glob
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint
import settings
from emoji import emojize

logging.basicConfig(filename="bot.log", level=logging.INFO)


def greet_user(update, context):
    print('Вызван /start')
    context.user_data['emoji'] = get_smile(context.user_data)
    my_keyboard = ReplyKeyboardMarkup([['Прислать котика']])
    update.message.reply_text(
        f'Приветствую, пользователь {context.user_data["emoji"]}',
        reply_markup=my_keyboard
    )


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text} {context.user_data['emoji']}")


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile)
    return user_data['emoji']


def play_random(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число {user_number}, Мое число {bot_number}, Вы выиграли'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, Мое число {bot_number}, Ничья'
    else:
        message = f'Ваше число {user_number}, Мое число {bot_number} Я выиграл'
    return message


def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введите число'
    update.message.reply_text(message)


def send_cat_picture(update, context):
    cat_photo_list = glob.glob('images/cat*.jpeg')
    cat_pic_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'))


def planet_info(update, context):
    pass


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(CommandHandler('planet', planet_info))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать котика)$'), send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('bot start!')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
