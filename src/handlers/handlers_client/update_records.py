from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from emoji import emojize
from datetime import datetime

from src.SQliter import SQLiter
from src.parsers import Animego_parser


async def update(qc: types.CallbackQuery):
    pars = Animego_parser()
    with SQLiter(qc['from']['id']) as db:
        db.check_anime_list_status()
        user_subs = db.get_user_sub()

        if len(user_subs) != 0:
            await qc.message.answer("Обновляю список подписок.")

            for anime in db.get_anime_list():
                episode_count = pars.get_cur_epesode(anime[1])

                if episode_count > anime[3]:
                    db.update_episode(anime[0], episode_count)

            anime_urls = InlineKeyboardMarkup()
            answer = ''

            for anime in db.get_user_sub_anime():
                if anime[6] == 1:
                    answer += f'{emojize(":small_orange_diamond:")} <b>{anime[2]}</b>: Вышел новый эпизод!\n\n'
                    anime_urls.add(InlineKeyboardButton(
                        anime[2], url=anime[1]))

            if len(answer) == 0:
                await qc.message.answer('Пока-что обновлений нет.')
            else:
                await qc.message.answer(answer, parse_mode='html', reply_markup=anime_urls)
        else:
            await qc.message.answer('Пока что у вас нет подписок.')
    await qc.answer()


def update_handler(dp: Dispatcher):
    dp.register_callback_query_handler(update, text="update")


# f'{emojize(":small_orange_diamond:")} <b>{sub[3]}</b>: Вышел новый эпизод!\n\n'
# anime_urls.add(InlineKeyboardButton(sub[3], url=sub[2]))
