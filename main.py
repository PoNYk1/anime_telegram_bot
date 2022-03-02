from aiogram.utils import executor
from aiogram import types, Dispatcher
from create_bot import bot, dp

from config import ADMINS

import logging


@dp.message_handler(commands=['start'])
async def start(m: types.Message):
    if str(m['from']['id']) in ADMINS:
        await m.answer("Вы админ!")

    await m.answer_photo(
        'https://avatarko.ru/img/kartinka/1/avatarko_anonim.jpg')
    await m.answer(
        "Приведствую! Напиши /menu что-бы узнать список доступных комманд.")


from handlers import client

client.register_client_handlers(dp)

print("Бот онлаин!")
executor.start_polling(dp, skip_updates=True)
