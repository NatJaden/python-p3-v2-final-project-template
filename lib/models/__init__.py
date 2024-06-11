import sqlite3

CONN = sqlite3.connect('db/fitnesstracker.db')
CURSOR = CONN.cursor()
