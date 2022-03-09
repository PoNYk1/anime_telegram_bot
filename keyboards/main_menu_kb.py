from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from emoji import emojize

from config import ADMIN_MOD

calc_btn = InlineKeyboardButton('Канкулятор', callback_data="calc")

add = InlineKeyboardButton(emojize(':white_small_square: Добавить.'),
                           callback_data="add")

rem = InlineKeyboardButton(emojize(':white_small_square: Удалить.'),
                           callback_data="del")

update = InlineKeyboardButton(emojize(':white_small_square: Обновить'),
                              callback_data="update")

list = InlineKeyboardButton(emojize(':white_small_square: Список подписок'),
                            callback_data="list")

info = InlineKeyboardButton(emojize(':white_small_square: Инструкция'),
                            callback_data="info")

root = InlineKeyboardButton('ROOT', callback_data="calc")

# main_menu_kb = InlineKeyboardMarkup (resize_keyboard=True, one_time_keyboard=True)
main_menu_kb = InlineKeyboardMarkup()

if ADMIN_MOD:
    main_menu_kb.add(root)

main_menu_kb.row(add, rem).add(update).add(list).add(info)
