

def create_table(connection, cursor):

   with open("tg_bot/misc/db.sql", "r") as sql:

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


def get_student(cursor):
    cursor.execute("SELECT NAME "
                   "FROM common_info "
                   "INNER JOIN students_name ON common_info.student_id = students_name.student_id;")
    return cursor.fetchall()
