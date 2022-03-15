from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from src.SQliter import SQlite_db

from emoji import emojize

from src.parsers import Animego_parser


class dialog (StatesGroup):
    url = State()


async def add(cq: types.CallbackQuery):
    await cq.message.answer("Дай мне ссылку на сайт:")
    await cq.answer()
    await dialog.next()


async def into_db(m: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['url'] = m.text
        user = m['from']
        db = SQlite_db(m['from']['id'], m['from']['first_name'])

        try:
            pars = Animego_parser(data['url'])
            anime_info = pars.get_all_info()

            db.new_record((data['url'], anime_info['title'],
                          anime_info['cur_episode'], anime_info['banner_url'], '0.0.0'))

        except:
            await m.answer("Эй! Это точно ссылка?")
    await state.finish()


def add_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(add, text='add')
    dp.register_message_handler(into_db, state=dialog.url)
