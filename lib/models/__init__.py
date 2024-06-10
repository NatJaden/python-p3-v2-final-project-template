import sqlite3

CONN = sqlite3.connect('db/library.db')
CURSOR = CONN.cursor()
