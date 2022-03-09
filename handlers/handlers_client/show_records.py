from aiogram import types, Dispatcher

from SQliter import SQlite_db
from emoji import emojize


async def show_records(cq: types.CallbackQuery):
    db = SQlite_db()
    rec_list = db.get_user_records(cq['from']['id'])

    if len(rec_list) != 0:
        req = ''
        for rec in rec_list:
            req += emojize(f":small_orange_diamond: {rec[3]} \n\n")
        await cq.message.answer("Список ваших подписок:")
        await cq.message.answer(req)

    else:
        await cq.message.answer('У вас нет подписок.')
    await cq.answer()


def show_handler(dp: Dispatcher):
    dp.register_callback_query_handler(show_records, text="list")
