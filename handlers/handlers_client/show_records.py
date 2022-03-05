from aiogram import types, Dispatcher

from keyboards import main_menu_kb
from SQliter import SQlite_db
from emoji import emojize

async def show_records (cq : types.CallbackQuery):
    db = SQlite_db()
    rec_list = db.get_user_records(cq['from']['id'])

    await cq.message.answer ("Список ваших подписок:")
    for rec in rec_list:
        await cq.message.answer (emojize(f":small_orange_diamond: {rec[3]}"))

    await cq.answer ()
    await cq.message.answer ("Список комманд:",reply_markup=main_menu_kb)

def show_handler (dp: Dispatcher):
    dp.register_callback_query_handler (show_records, text="list")