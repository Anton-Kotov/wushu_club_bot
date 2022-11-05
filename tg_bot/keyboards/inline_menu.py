from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu_cd = CallbackData("sm", "level", "main", "category", "subcategory", "text", "photo")


def make_callback_data(level, main="0", category="0", subcategory="0",
                           text="0", photo="0"):

    return menu_cd.new(level=level, main=main, category=category, subcategory=subcategory,
                           text=text, photo=photo)

async def main_keyboard(db):
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup(row_width=2)

    maines = await db.get_main()

    for main in sorted(maines, key=lambda el: el[0]):

        button_text = f"{main[1]}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           main=main[0])
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    return markup


async def categories_keyboard(db, main):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardMarkup(row_width=2)
    categories = await db.get_categories(main)

    for category in sorted(categories, key=lambda el: el[0]):
        button_text = f"{category[1]}"
        callback_data = make_callback_data(level=CURRENT_LEVEL + 1,
                                           main=main,
                                           category=category[0])
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL - 1, main=main))
        )
    return markup
