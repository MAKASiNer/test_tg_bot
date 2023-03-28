from telebot.types import Message

from bot import bot



@bot.message_handler(commands=['start'])
def start_handler(msg: Message):
    bot.send_message(msg.chat.id, 'Привет!')


__all__ = [
    'start_handler'
]