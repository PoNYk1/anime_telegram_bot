from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from src.SQliter import SQLiter
from src.handlers._cancel_words import cancel_words
from emoji import emojize


class dialog (StatesGroup):
    dell = State()


async def del_rec(qc: types.CallbackQuery):
    with SQLiter(qc['from']['id']) as db:
        user_subs = db.get_user_sub()
        anime_list = db.get_user_sub_anime()
        answer = ''

        if len(user_subs) != 0:
            for sub in user_subs:
                for anime in anime_list:
                    if sub[2] == anime[0]:
                        answer += emojize(
                            f':small_blue_diamond: {sub[0]}.    <b>{anime[2]}</b>  \n\n')

            await qc.message.answer("Напиши индекс подписки которую хотите удалить:")
            await qc.message.answer(answer, parse_mode='html')
            await dialog.next()
        else:
            await qc.message.answer('Пока что у вас нет подписок.')

    await qc.answer()


async def del_this(m: types.Message, state: FSMContext):
    if m.text in cancel_words:
        await m.answer('Хорошо')
    else:
        with SQLiter(m['from']['id']) as db:
            for sub in db.get_user_sub():
                if int(m.text) == sub[0]:
                    db.del_sub(m.text)
                    await m.answer('Подписка удаленна.')
                else:
                    await m.answer('В списке нет такого индекса!')
    await state.finish()


def del_handler(dp):
    dp.register_callback_query_handler(del_rec, text='del')
    dp.register_message_handler(del_this, state=dialog.dell)
