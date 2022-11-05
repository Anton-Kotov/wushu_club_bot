from typing import Union

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from tg_bot.keyboards.inline_menu import categories_keyboard, menu_cd, main_keyboard



async def list_main(message: Union[types.Message, types.CallbackQuery], *args, **kwargs):
    db = message.bot["db"]
    markup = await main_keyboard(db)
    if isinstance(message, types.Message):
        await message.answer(text="Тестовое описание", reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        callback = message
        await callback.message.edit_text(text="Тестовое описание", reply_markup=markup)


async def list_categories(callback: types.CallbackQuery, main, state: FSMContext, **kwargs):
    await callback.answer()
    db = callback.bot["db"]
    markup = await categories_keyboard(db, main)
    await callback.message.edit_text(text="Тестовое описание", reply_markup=markup)



async def navigate(callback: types.CallbackQuery, callback_data: dict, state: FSMContext):
    current_level = callback_data.get('level')
    callback_data: dict
    main = callback_data.get('main')
    category = callback_data.get('category')
    subcategory = callback_data.get('subcategory')
    text = callback_data.get('text')
    photo = callback_data.get('photo')
    state: FSMContext

    levels = {
                "0": list_main,
                "1": list_categories
             }
    current_level_function = levels[current_level]

    await current_level_function(
        callback, main, state)
    await callback.answer()



def register_main_menu(dp: Dispatcher):
    dp.register_message_handler(list_main, text="menu")
    dp.register_callback_query_handler(list_main, text="menu")
    dp.register_callback_query_handler(navigate, menu_cd.filter())
