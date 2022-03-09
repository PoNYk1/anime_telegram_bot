from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from src.SQliter import SQlite_db
from emoji import emojize


class dialog (StatesGroup):
    dell = State()


async def del_rec(qc: types.CallbackQuery):
    db = SQlite_db()

    user = qc['from']
    rec_list = db.get_user_records(user['id'])

    qc.answer()

    if len(rec_list) != 0:
        req = ''
        for rec in rec_list:
            req += emojize(f':small_blue_diamond: {rec[0]}. {rec[3]}  \n\n')

        await qc.message.answer("Напиши индекс подписки которую хотите удалить:")
        await qc.message.answer(req)
        await dialog.next()

    else:
        await qc.message.answer('У вас нет подписок.')


async def del_this(m: types.Message, state: FSMContext):
    db = SQlite_db()
    async with state.proxy() as data:
        data['dell'] = m.text
        db.del_by_id(data['dell'])
        await m.answer("Подписка удалена!")

    await state.finish()


def del_handler(dp):
    dp.register_callback_query_handler(del_rec, text='del')
    dp.register_message_handler(del_this, state=dialog.dell)
