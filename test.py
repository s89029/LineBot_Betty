
import Selffunction as SelF
import sqlite3

sl = input ('請輸入:')
dbfile = "FoodFat.db"
conn = sqlite3.connect(dbfile)
cursor = conn.execute("select * from FoodFat where foodname is '{}'".format(sl))
s=[]
for row in cursor:
    s.append(row)

print (s[0][2])
conn.close
