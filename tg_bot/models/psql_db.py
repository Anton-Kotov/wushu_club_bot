

def create_table(connection, cursor):

   with open("tg_bot/misc/db_register.sql", "r") as sql:

    cursor.execute(sql.read())
    connection.commit()


def create_table_info(connection, cursor):

   with open("tg_bot/misc/db_info.sql", "r") as sql:

    cursor.execute(sql.read())
    connection.commit()


def add_to_menu(connection, cursor):

   with open("tg_bot/misc/db_add_to_menu.sql", "r") as sql:

    cursor.execute(sql.read())
    connection.commit()


def add_student_name(connection, cursor, name):
    cursor.execute("INSERT INTO students_name (NAME) VALUES (%s)", (name,))
    connection.commit()


def add_data(connection, cursor, telegram_id, birthdate, start_date):
    cursor.execute("INSERT INTO data (TELEGRAM_ID, BIRTHDATE, START_DATE) VALUES (%s,%s,%s)",
                   (telegram_id, birthdate, start_date))
    connection.commit()


def add_student_style(connection, cursor, style):
    cursor.execute("INSERT INTO styles (STYLE) VALUES (%s)", (style,))
    connection.commit()


def add_student_level(connection, cursor, level):
    cursor.execute("INSERT INTO levels (LEVEL) VALUES (%s)", (level,))
    connection.commit()


def get_student(cursor, telegram_id):
    cursor.execute("SELECT NAME, TELEGRAM_ID, BIRTHDATE, START_DATE, STYLE, LEVEL "
                   "FROM  students_name "
                   "LEFT JOIN data ON students_name.data_id = data.data_id "
                   "LEFT JOIN styles ON data.style_id = styles.style_id "
                   "LEFT JOIN levels ON styles.level_id = levels.level_id "
                   f"WHERE TELEGRAM_ID = {telegram_id}")
    return cursor.fetchone()


def get_telegram_id(cursor):
    cursor.execute("SELECT TELEGRAM_ID FROM data;")
    return cursor.fetchall()
