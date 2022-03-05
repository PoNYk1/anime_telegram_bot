from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from SQliter import SQlite_db


class dialog (StatesGroup):
    url = State()


async def add (cq: types.CallbackQuery):
    await cq.message.answer ("Дай мне ссылку на сайт:")
    await cq.answer()
    await dialog.next()

async def into_db (m : types.Message, state: FSMContext):
    db = SQlite_db ()

    async with state.proxy() as data:
        data['url'] = m.text
        user = m['from']

        try: 
            db.new_record((user['id'], user['first_name'], data['url'], "it's test", 'https//', '0.0.0'))
        except:
            await m.answer ("ВНИМАНИЕ! Ошибка записи!")

        # await m.answer (db.get_all_records())

    await state.finish()

def add_handlers (dp: Dispatcher):
    dp.register_callback_query_handler (add, text='add')
    dp.register_message_handler (into_db, state=dialog.url)
