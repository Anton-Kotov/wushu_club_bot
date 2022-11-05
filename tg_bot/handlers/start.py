from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from tg_bot.keyboards.inline import register
from tg_bot.keyboards.inline_menu import main_keyboard
from tg_bot.keyboards.reply import first_time
from tg_bot.models.psql_db import create_table, add_student_name, \
    add_student_style, add_student_level, add_data, get_student, get_telegram_id, create_table_info, add_to_menu


async def bot_start(message: types.Message, state: FSMContext):

    bot = message.bot
    db = bot["db"]

    markup = await main_keyboard(db)
    await message.answer(text=" Тесьт", reply_markup=markup)



    # connection = bot.get("connection")
    # cursor = bot.get("cursor")
    #
    # # create_table_info(connection, cursor)
    # add_to_menu(connection, cursor)
    # # create_table(connection, cursor)
    #
    # telegram_id_lst = [el[0] for el in get_telegram_id(cursor)]  # распаковываем кортежи
    #
    # if telegram_id_lst == [] or message.from_user.id not in telegram_id_lst:  # проверка на наличие пользователя в БД
    #
    #     await message.answer_photo(photo="https://courses24.net/wp-content/uploads/2021/11/"
    #                                      "tajczzi-czigun-tri-stupeni-aleksandr-zhitomirskij_6196e682514cf.png",
    #                                caption="Добро пожаловать в центр традиционного ушу УЦЗИМЭНЬ")
    #     await message.answer(text="Вы уже учитесь у нас или еще нет?", reply_markup=first_time)
    #     await state.set_state("учусь")
    # else:
    #     name = get_student(cursor, message.from_user.id)[0]
    #     await message.answer(text=f"Здравствуйте, {name}!", reply_markup=types.ReplyKeyboardRemove())
    #     await message.answer_photo(photo="https://courses24.net/wp-content/uploads/2021/11/"
    #                                      "tajczzi-czigun-tri-stupeni-aleksandr-zhitomirskij_6196e682514cf.png",
    #                                caption="Добро пожаловать в центр традиционного ушу УЦЗИМЭНЬ")


async def student(message: types.Message, state: FSMContext):

    await message.answer(text="Мы рады видеть вас в нашем боте.\n"
                              "Вы пользуетесь ботом впервые.", reply_markup=register)
    await state.finish()

async def register_name(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(text="Напишите: Фамилию Имя")
    await state.set_state("name")


async def register_birthdate(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data["name"] = message.text

    await message.answer(text="Дата рождения: дд.мм.гггг")
    await state.set_state("birthdate")


async def register_start_data(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data["birthdate"] = message.text
    await message.answer(text="Год, когда начали заниматься в центре УЦЗИМЭНЬ:")
    await state.set_state("start_data")


async def register_style(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data["start_date"] = message.text
    await message.answer(text="Какие стили ушу вы практикуете:")
    await state.set_state("style")

async def register_level(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data["style"] = message.text

    await message.answer(text="Какой у вас уровень?")
    await state.set_state("level")

async def register_final(message: types.Message, state: FSMContext):
    connection, cursor = message.bot["connection"], message.bot["cursor"]
    telegram_id = message.from_user.id
    level = message.text
    data = await state.get_data()

    telegram_id_lst = [el[0] for el in get_telegram_id(cursor)]  # распаковываем кортежи

    if telegram_id_lst == [] or message.from_user.id not in telegram_id_lst:

        add_data(connection, cursor, telegram_id, data["birthdate"], data["start_date"])
        add_student_name(connection, cursor, data["name"])
        add_student_style(connection, cursor, data["style"])
        add_student_level(connection, cursor, level)

        await message.answer(text="Благодарим за регистрацию")
    else:
        await message.answer(text="Вы уже зарегистрировались!")
    await state.reset_data()
    await state.finish()

    await message.answer_photo(photo="https://courses24.net/wp-content/uploads/2021/11/"
                                     "tajczzi-czigun-tri-stupeni-aleksandr-zhitomirskij_6196e682514cf.png",
                               caption="Добро пожаловать в центр традиционного ушу УЦЗИМЭНЬ")



def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    # dp.register_message_handler(student, text="Учусь", state="учусь")
    # dp.register_callback_query_handler(register_name, text="register")
    # dp.register_message_handler(register_birthdate, state="name")
    # dp.register_message_handler(register_start_data, state="birthdate")
    # dp.register_message_handler(register_style, state="start_data")
    # dp.register_message_handler(register_level, state="style")
    # dp.register_message_handler(register_final, state="level")


