from telebot.types import Message

from bot import bot
from filters import MyChatFilter


@bot.message_handler(**MyChatFilter)
def echo_handler(msg: Message):
    bot.send_message(msg.chat.id, msg.text)


__all__ = [
    'echo_handler'
]
