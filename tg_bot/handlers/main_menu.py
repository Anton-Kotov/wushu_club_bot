from typing import Union

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import InputMedia

from tg_bot.keyboards.inline_menu import categories_keyboard, menu_cd, main_keyboard, subcategories_keyboard, \
    back_keyboard


async def list_main(message: Union[types.Message, types.CallbackQuery], *args, **kwargs):
    db = message.bot["db"]
    markup = await main_keyboard(db)
    if isinstance(message, types.Message):
        await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=06d9a7f70b4f1524d9051ec529ab8695-5876724-images-thumbs&n=13",
                                   caption="Добро пожаловать в центр традиционного ушу УЦЗИМЭНЬ",
                                   reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        callback = message
        photo = InputMedia(media="https://avatars.mds.yandex.net/i?id=06d9a7f70b4f1524d9051ec529ab8695-5876724-images-thumbs&n=13",
                           caption="Добро пожаловать в центр традиционного ушу УЦЗИМЭНЬ")
        await callback.message.edit_media(media=photo,
                                          reply_markup=markup)


async def list_categories(callback: types.CallbackQuery, main, state: FSMContext, *args, **kwargs):
    await callback.answer()
    db = callback.bot["db"]
    markup = await categories_keyboard(db, main)
    photo = InputMedia(
        media="https://avatars.mds.yandex.net/i?id=06d9a7f70b4f1524d9051ec529ab8695-5876724-images-thumbs&n=13",
        caption="Добро пожаловать в центр традиционного ушу УЦЗИМЭНЬ")
    await callback.message.edit_media(media=photo,
                                      reply_markup=markup)

async def list_subcategories(callback: types.CallbackQuery, main, category, state: FSMContext, *args, **kwargs):
    await callback.answer()
    db = callback.bot["db"]
    markup = await subcategories_keyboard(db, main, category)
    photo = InputMedia(
        media="https://avatars.mds.yandex.net/i?id=06d9a7f70b4f1524d9051ec529ab8695-5876724-images-thumbs&n=13",
        caption="Добро пожаловать в центр традиционного ушу УЦЗИМЭНЬ")
    await callback.message.edit_media(media=photo,
                                      reply_markup=markup)

async def show_informations(callback: types.CallbackQuery, main, category, subcategory, state: FSMContext, *args, **kwargs):
    await callback.answer()
    db = callback.bot["db"]
    informations = await db.get_informations(main, category, subcategory)

    photo = InputMedia(
        media=informations[0][1],
        caption=informations[0][0])
    markup = await back_keyboard(main, category, subcategory)
    await callback.message.edit_media(media=photo, reply_markup=markup)

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
                "1": list_categories,
                "2": list_subcategories,
                "3": show_informations
             }
    current_level_function = levels[current_level]

    await current_level_function(
        callback, main, category, subcategory, state)
    await callback.answer()



def register_main_menu(dp: Dispatcher):
    dp.register_message_handler(list_main, text="menu")
    dp.register_callback_query_handler(list_main, text="menu")
    dp.register_callback_query_handler(navigate, menu_cd.filter())
