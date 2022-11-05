import asyncio

from tg_bot.database.pg_commands import Database

db = Database()

async def create_tables():
    await db.create()
    await db.create_table(
            """
            CREATE TABLE IF NOT EXISTS menu(
            MENU_ID SERIAL PRIMARY KEY NOT NULL,
            MAIN_CODE VARCHAR(20),
            MAIN_NAME VARCHAR(30),
    
            CATEGORY_CODE VARCHAR(20),
            CATEGORY_NAME VARCHAR(30),
    
            SUBCATEGORY_CODE VARCHAR(20),
            SUBCATEGORY_NAME VARCHAR(30),
    
            TEXT TEXT,
            PHOTO VARCHAR(250)
            );
            """
    )
    await db.close()

if __name__ == "__main__":
    try:
        asyncio.run(create_tables())
    except (KeyboardInterrupt, SystemExit):
        pass
