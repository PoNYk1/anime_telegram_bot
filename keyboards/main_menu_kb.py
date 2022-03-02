from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

calc_btn = InlineKeyboardButton ('Канкулятор', callback_data="calc")

main_menu_kb = InlineKeyboardMarkup (resize_keyboard=True, one_time_keyboard=True)

main_menu_kb.add (calc_btn)