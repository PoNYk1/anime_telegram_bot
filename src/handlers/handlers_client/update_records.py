from cgitb import text
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from emoji import emojize

from src.parsers import Animego_parser
from src.SQliter import SQlite_db


async def update(qc: types.CallbackQuery):
    parser = Animego_parser()
    db = SQlite_db(qc['from']['id'], qc['from']['first_name'])
    records = db.get_user_records()

    if len(records) == 0:
        await qc.message.answer('Вы не подписаны не на одно аниме.')
        await qc.answer()
        return False

    await qc.message.answer("Обновляю список ваших подписок.")

    answer = ''
    anime_urls = InlineKeyboardMarkup()
    for rec in records:
        cur_epesode = int(parser.get_cur_epesode(rec[2]))

        if cur_epesode > rec[4]:
            answer += f'{emojize(":small_orange_diamond:")} <b>{rec[3]}</b>: Вышел новый эпизод!\n\n'
            anime_urls.add(InlineKeyboardButton(rec[3], url=rec[2]))
        else:
            answer += f'{emojize(":small_blue_diamond:")} <b>{rec[3]}</b>: Обновлений нет...\n\n'
    await qc.message.answer(answer, parse_mode='html', reply_markup=anime_urls)

    await qc.answer()


def update_handler(dp: Dispatcher):
    dp.register_callback_query_handler(update, text="update")
