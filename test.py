
import Selffunction as SelF
import sqlite3
import re

cost = 0
dbfile = "FoodFat.db"
conn = sqlite3.connect(dbfile)
cursorobj = conn.cursor()
total = "select * from Ordertemp" 
cursorobj.execute(total)
for row in cursorobj:
    cost = cost + int(row[3])
    conn.close
print (cost)
#cursor = conn.execute("select * from FoodFat where foodname is '{}'".format(sl))
#s=[]
#for row in cursor:
#    s.append(row)

#print (s[0][2])
conn.close
