from config import ADMINS
from create_bot import bot


async def startup(_):
    print('Бот онлаин!')

    for user in ADMINS:
        await bot.send_message(user, 'Я тут!')
