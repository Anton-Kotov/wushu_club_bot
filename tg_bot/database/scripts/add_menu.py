import asyncio

from tg_bot.database.pg_commands import Database

db = Database()

async def add_menu_full():
    await db.create()
    await db.add_menu(
        "1_about", "О центре",
        "teacher", "Учителя",
        "ElFe", "Елена Федорова",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "1_about", "О центре",
        "teacher", "Учителя",
        "AnVk", "Антон Викторович",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "1_about", "О центре",
        "teacher", "Учителя",
        "GrFe", "Григорий Федоров",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "1_about", "О центре",
        "spholl", "Залы",
        "metro", "м. Автово",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "1_about", "О центре",
        "spholl", "Залы",
        "metro", "м. Выборгская",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "1_about", "О центре",
        "spholl", "Залы",
        "metro", "м. Девяткино",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "2_adult", "Взрослые группы",
        "styles", "Ланьшаньцюань",
        "metro", "м. Автово",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "3_child", "Детские группы",
        "spholl", "Залы",
        "metro", "м. Автово",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "4_articles", "Статьи",
        "spholl", "Залы",
        "metro", "м. Автово",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "5_photo", "Фотографии",
        "spholl", "Залы",
        "metro", "м. Автово",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "6_video", "Видео",
        "spholl", "Залы",
        "metro", "м. Автово",
        "Текст", "Ссылка на фото"
    )
    await db.close()

if __name__ == "__main__":
    try:
        asyncio.run(add_menu_full())
    except (KeyboardInterrupt, SystemExit):
        pass