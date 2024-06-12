import sqlite3
import os

db_dir = os.path.join(os.path.dirname(__file__), '..', 'db')
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

db_path = os.path.join(db_dir, 'fitnesstracker.db')

CONN = sqlite3.connect(db_path)
