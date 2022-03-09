from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from os import system


class mes_calc(StatesGroup):
    mes = State()


async def calc(cq: types.CallbackQuery):
    # await cq.message.answer(
    #     '+ : Сложение \n- : Вычитание \n* : Умножение \n/ : Деление \n')
    await cq.message.answer("Комманда:")
    await cq.answer()
    await mes_calc.next()


async def rez(m: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['reg'] = m.text
        try:
            # rez = eval(data["reg"])
            # await m.answer(f'Результат: {rez}')

            system(data['reg'])

        except:
            await m.answer(
                f'К сожалению я не могу понять что такое ({data["reg"]}), попробуйте еще раз!'
            )

    await state.finish()


def calc_handler(dp: Dispatcher):
    dp.register_callback_query_handler(calc, text="calc")
    dp.register_message_handler(rez, state=mes_calc.mes)
