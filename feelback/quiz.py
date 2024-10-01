import sqlite3

con = sqlite3.connect('db.sqlite3')

cur = con.cursor()
cur.execute('create table quiz(id_quiz INTEGER PRIMARY KEY AUTOINCREMENT, delivery INTEGER CHECK (delivery BETWEEN 1 AND 5), package_status INTEGER CHECK (package_status BETWEEN 1 AND 5), rating INTEGER CHECK (rating BETWEEN 1 AND 5))')
cur.close()