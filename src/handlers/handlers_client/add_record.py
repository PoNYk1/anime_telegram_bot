from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from src.SQliter import SQlite_db

import requests
from bs4 import BeautifulSoup as bs
from emoji import emojize


class dialog (StatesGroup):
    url = State()


async def add(cq: types.CallbackQuery):
    await cq.message.answer("Дай мне ссылку на сайт:")
    await cq.answer()
    await dialog.next()


async def into_db(m: types.Message, state: FSMContext):
    db = SQlite_db()

    async with state.proxy() as data:
        data['url'] = m.text
        user = m['from']

        try:
            req = requests.get(data['url'])
            if req.ok:

                db.new_record((user['id'], user['first_name'],
                               data['url'], "it's test", 0, 'https//', '0.0.0'))

            else:
                await m.answer("К сожалению не могу получить доступ к сайту по этой сылке.")
        except:
            await m.answer("Эй! Это точно ссылка?")
    await state.finish()


def add_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(add, text='add')
    dp.register_message_handler(into_db, state=dialog.url)
