from aiogram import types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import config
from src.startup import startup
from create_bot import dp
from src.handlers import client

from emoji import emojize


@dp.message_handler(commands=['start', 'help'])
async def start(m: types.Message):
    menu_btn = KeyboardButton('/menu')
    admin_btn = KeyboardButton('/admin')
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(menu_btn)

    if str(m['from']['id']) in config.ADMINS:
        config.ADMIN_MOD = True

    if config.ADMIN_MOD:
        await m.answer("Вы админ!")
        kb.add(admin_btn)

    await m.answer_photo(
        'https://avatarko.ru/img/kartinka/1/avatarko_anonim.jpg')
    await m.answer(
        f"Приведствую! Напиши /menu что-бы узнать список доступных комманд.{emojize(':umbrella:')}",
        reply_markup=kb
    )


client.register_client_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=startup)
