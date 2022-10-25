

def create_table(connection, cursor):

   with open("tg_bot/misc/db.sql", "r") as sql:

    cursor.execute(sql.read())
    connection.commit()


def add_student_name(connection, cursor, name):
    cursor.execute("INSERT INTO students_name (NAME) VALUES (%s)", (f"{name}",))
    connection.commit()

def add_student_age(connection, cursor, birthdate):
    cursor.execute("INSERT INTO data (BIRTHDATE) VALUES (%s)", (f"{birthdate}",))
    connection.commit()
