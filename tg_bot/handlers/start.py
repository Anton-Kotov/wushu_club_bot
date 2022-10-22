from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart

from tg_bot.keyboards.inline import register
from tg_bot.keyboards.reply import first_time


async def bot_start(message: types.Message):
    await message.answer_photo(photo="https://courses24.net/wp-content/uploads/2021/11/"
                                     "tajczzi-czigun-tri-stupeni-aleksandr-zhitomirskij_6196e682514cf.png",
                               caption="Добро пожаловать в центр традиционного ушу УЦЗИМЭНЬ")
    await message.answer(text="Вы уже учитесь у нас или еще нет?", reply_markup=first_time)

async def student(message: types.Message):
    await message.answer(text="Мы рады видеть вас в нашем боте")
    await message.answer(text="Вы пользуетесь ботом впервые.", reply_markup=register)  # здесь добавить проверку на наличие пользователя в бд


def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(student,text="Учусь")