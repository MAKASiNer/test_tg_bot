if __name__ == '__main__':
    from .bot import bot

    bot.infinity_polling(
        timeout=100,
        skip_pending=True
    )
