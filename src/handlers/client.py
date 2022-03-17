from .handlers_client import calc_handler, add_handlers, show_handler, \
    del_handler, update_handler
from aiogram import types, Dispatcher
from src.keyboards import main_menu_kb


async def open_menu(m: types.Message):
    await m.answer("Список комманд:", reply_markup=main_menu_kb)


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(open_menu, commands=['menu'])
    calc_handler(dp)
    add_handlers(dp)
    show_handler(dp)
    del_handler(dp)
    update_handler(dp)
