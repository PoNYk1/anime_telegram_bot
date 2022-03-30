from aiogram import types, Dispatcher

from src.SQliter import SQLiter
from emoji import emojize


async def show_records(cq: types.CallbackQuery):
    with SQLiter(cq['from']['id']) as db:
        anime_list = db.get_user_sub_anime()
        answer = ''

        for anime in anime_list:
            answer += emojize(f":small_orange_diamond: {anime[2]} \n\n")

        await cq.message.answer('Вы подписанны на:')
        await cq.message.answer(answer)

    await cq.answer()


def show_handler(dp: Dispatcher):
    dp.register_callback_query_handler(show_records, text="list")


# db = SQlite_db(cq['from']['id'])
#     rec_list = db.get_user_subscriptions()

#     if len(rec_list) != 0:
#         req = ''
#         for rec in rec_list:
#             req += emojize(f":small_orange_diamond: {rec[2]} \n\n")
#         await cq.message.answer("Список ваших подписок:")
#         await cq.message.answer(req)

#     else:
#         await cq.message.answer('У вас нет подписок.')
