import sqlite3


db = sqlite3.connect('users.db')
db_cursor = db.cursor()

db_cursor.execute("CREATE TABLE IF NOT EXISTS users (login TEXT, password TEXT)")
db.commit()

user_login = input('Login: ')
user_password = input('Pass: ')

db_cursor.execute("SELECT login FROM users")