from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime

from src.SQliter import SQLiter
from src.handlers._cancel_words import cancel_words
from emoji import emojize

from src.parsers import Animego_parser


class dialog (StatesGroup):
    url = State()


async def add(cq: types.CallbackQuery):
    site_list = InlineKeyboardMarkup()
    anigo = InlineKeyboardButton('AnimeGO', url='https://animego.org')
    site_list.add(anigo)

    await cq.message.answer("Дай мне ссылку на сайт:", reply_markup=site_list)
    await cq.answer()
    await dialog.next()


async def into_db(m: types.Message, state: FSMContext):
    if m.text in cancel_words:
        await m.answer('Хорошо')
    else:
        pars = Animego_parser()
        async with state.proxy() as data:
            data['url'] = m.text

            info = pars.get_all_info(data['url'])

            with SQLiter(m['from']['id']) as db:
                user_sub = db.get_user_sub()
                flag = True

                for anime in user_sub:
                    if info['title'] in anime:
                        flag = False

                if flag:
                    db.new_sub((data['url'], info['title'],
                                info['cur_episode'], info['banner_url']))

                    await m.answer_photo(info['banner_url'])
                    await m.answer(f"Аниме: <b>{info['title']}</b> \n\nТекущий эпизод: <b>{info['cur_episode']}</b>\n\nЗапись создана!",
                                   parse_mode='html')
                else:
                    await m.answer("Похоже вы уже подписаны на это аниме!")

    await state.finish()


def add_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(add, text='add')
    dp.register_message_handler(into_db, state=dialog.url)


# db = SQlite_db(m['from']['id'])

    # try:
    #     pars = Animego_parser()
    #     anime_info = pars.get_all_info(data['url'])

    #     ready_rec = (data['url'], anime_info['title'],
    #                  anime_info['cur_episode'], anime_info['banner_url'], datetime.now().date())

    #     if db.search_subscription_by_title(anime_info['title']) == True:

    #         db.new_record(ready_rec)

    #         await m.answer_photo(anime_info['banner_url'])
    #         await m.answer(f"Аниме: <b>{anime_info['title']}</b> \n\nТекущий эпизод: <b>{anime_info['cur_episode']}</b>\n\nЗапись создана!",
    #                        parse_mode='html')
    #     else:
    #         await m.answer("Похоже вы уже подписаны на это аниме!")
    # except:
    #     await m.answer("Эй! Это точно ссылка?")
