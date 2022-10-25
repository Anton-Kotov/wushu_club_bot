

def create_table(connection, cursor):

   with open("tg_bot/misc/db.sql", "r") as sql:

    cursor.execute(sql.read())
    connection.commit()

def add_telegram_id(connection, cursor, telegram_id):
    cursor.execute("INSERT INTO data (TELEGRAM_ID) VALUES (%s)", (f"{telegram_id}",))
    connection.commit()

def add_student_name(connection, cursor, name):
    cursor.execute("INSERT INTO students_name (NAME) VALUES (%s)", (f"{name}",))
    connection.commit()

def add_student_birthdate(connection, cursor, birthdate):
    cursor.execute("INSERT INTO data (BIRTHDATE) VALUES (%s)", (f"{birthdate}",))
    connection.commit()

def add_start_date(connection, cursor, start_date):
    cursor.execute("INSERT INTO data (START_DATE) VALUES (%s)", (f"{start_date}",))
    connection.commit()

def add_student_style(connection, cursor, style):
    cursor.execute("INSERT INTO styles (STYLE) VALUES (%s)", (f"{style}",))
    connection.commit()

def add_student_level(connection, cursor, level):
    cursor.execute("INSERT INTO levels (LEVEL) VALUES (%s)", (f"{level}",))
    connection.commit()