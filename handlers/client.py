from aiogram import types, Dispatcher
from keyboards import main_menu_kb

async def open_menu(m: types.Message):
    await m.answer("Список комманд:", reply_markup=main_menu_kb)


from .handlers_client import calc_handler


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(open_menu, commands=['menu'], )
    calc_handler(dp)
