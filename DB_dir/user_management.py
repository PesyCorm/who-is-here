import sqlite3


def test_db(db):
    try:
        db_cursor = db.cursor()
        db_cursor.execute("CREATE TABLE IF NOT EXISTS users (login TEXT, password TEXT)")
        db.commit()
        return True
    except:
        return False

def add_user_into_db(login, password):

	with sqlite3.connect('users_base.db') as db:

		if test_db(db):
			db_cursor = db.cursor()
			db_cursor.execute(f"SELECT login FROM users WHERE login = '{login}'")
			if db_cursor.fetchone() is None:
				db_cursor.execute(f"INSERT INTO users(login, password) VALUES ('{login}', '{password}')")
				db.commit()
				return("Все ОК!")
			else:
				return("Такая запись уже существует!")

def select_from_db():

	with sqlite3.connect('users_base.db') as db:

		if test_db(db):
			db_cursor = db.cursor()
			return db_cursor.execute("SELECT login FROM users")