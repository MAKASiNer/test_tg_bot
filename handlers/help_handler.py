from telebot.types import Message

from bot import bot
from filters import CommandHelp


@bot.message_handler(**CommandHelp)
def help_handler(msg: Message):
    bot.send_message(msg.chat.id, 'Сообщение со списком команд и их пояснением')


__all__ = [
    'help_handler'
]
