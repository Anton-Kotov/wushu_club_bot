import asyncio

from tg_bot.database.pg_commands import Database

db = Database()

async def add_menu_full():
    await db.create()
    with open("C:\\Users\\root\\PycharmProjects\\wushu_club_bot\\tg_bot\\database\\texts\\master_elena.txt",
              "r", encoding="utf8") as file:
        text = file.read()
    await db.add_menu(
        "1_about", "О центре",
        "1_teacher", "Учителя",
        "1_ElFe", "Елена Федорова",
        text, "https://sun9-80.userapi.com/impf/c830208/v830208522/1adef9/rJCTBxQgfe4.jpg?size=916x642&quality=96&sign=5722b43dca277f843b4979b4f3dc0891&type=album"
    )
    await db.add_menu(
        "1_about", "О центре",
        "1_teacher", "Учителя",
        "2_AnVk", "Антон Викторович",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "1_about", "О центре",
        "1_teacher", "Учителя",
        "3_GrFe", "Григорий Федоров",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "1_about", "О центре",
        "2_spholl", "Залы",
        "metro", "м. Автово",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "1_about", "О центре",
        "2_spholl", "Залы",
        "metro", "м. Выборгская",
        "Текст", "Ссылка на фото"
    )
    await db.add_menu(
        "1_about", "О центре",
        "2_spholl", "Залы",
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