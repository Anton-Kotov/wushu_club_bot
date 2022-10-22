from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

first_time = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Учусь"),
        ],
        [
            KeyboardButton(text="Еще нет")
        ]
    ],
    resize_keyboard=True
)