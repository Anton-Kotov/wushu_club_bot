from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

register = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Регистрация",
                callback_data="register")
        ]
    ]
)
