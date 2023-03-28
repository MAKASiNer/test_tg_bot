from telebot.types import Message
from telebot.formatting import hcode

from bot import bot
from filters import CommandStart


@bot.message_handler(**CommandStart)
def start_handler(msg: Message):
    chat_id = str(msg.chat.id)
    user_id = str(msg.from_user.id)

    bot.send_message(
        chat_id=msg.chat.id,
        text=(
            'Привет!\n'
            f'char_id: {hcode(chat_id)}\n'
            f'user_id {hcode(user_id)}\n'
        )
    )


__all__ = [
    'start_handler'
]
