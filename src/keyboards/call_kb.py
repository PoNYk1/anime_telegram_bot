from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import ADMIN_MOD

call_kb = ReplyKeyboardMarkup(resize_keyboard=True)
menu_btn = KeyboardButton('/menu')
admin_btn = KeyboardButton('/admin')


print(ADMIN_MOD)
if ADMIN_MOD:
    call_kb.add(admin_btn)

call_kb.add(menu_btn)
