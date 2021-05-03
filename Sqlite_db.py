# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('Database1.db')
cur = conn.cursor()
#cur.execute("""CREATE TABLE FoodFat (
#                foodname text,
#                fat integer
#                )""")

cur.execute("INSERT INTO FoodFat VALUES ('³J»æ','261')")
conn.commit()
conn.close()