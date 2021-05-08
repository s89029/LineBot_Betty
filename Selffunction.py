# -*- coding: utf-8 -*-
import random
import re
import codecs
import sqlite3

def checkevent(event):
    checkcontain = event.split('@')
    command = checkcontain
    return command
def PickDrink():
    f = open('DrinkShop.txt','r',encoding='utf-8')
    shoplist = []
    for shop in f.readlines():
        k=shop.strip('\n')
        shoplist.append(k)
    ran = random.randint(0,len(shoplist)-1)
    todaydrink = shoplist[ran]
    f.close()
    return todaydrink
def totalcost(event):
    dbfile = "FoodFat.db"
    conn = sqlite3.connect(dbfile)
    cursorobj = conn.cursor()
    total = "select * from Ordertemp" 
    cursorobj.execute(total)
    cost = 0
    for row in cursorobj:
        cost = cost + int(row[3])
    conn.close
    return cost

def foodfat(event):
    dbfile = "FoodFat.db"
    conn = sqlite3.connect(dbfile)
    cursor = conn.execute("select * from FoodFat where foodname is '{}'".format(event))
    s=[]
    for row in cursor:
        s.append(row)
    conn.close
    return s
def saveorder(event):
    command = checkevent(event)
    name = str(command[1])
    item = str(command[2])
    cost = int(command[3])
    dbfile = "FoodFat.db"
    conn = sqlite3.connect(dbfile)
    cursor = conn.execute("INSERT INTO Ordertemp (Morder, Item, cost) VALUES('{}','{}','{}')".format(name,item,cost))
    conn.commit()
    conn.close()
    return 0
def totalorder(event):
    dbfile = "FoodFat.db"
    conn = sqlite3.connect(dbfile)
    cursorobj = conn.cursor()
    total = "select * from Ordertemp" 
    cursorobj.execute(total)
    strtotal =''
    for row in cursorobj:
        s = "".join(str(row))
        s = re.sub(',','',s)
        s = re.sub("'",'',s)
        strtotal = strtotal + s + '\n'
    deleteall = "DELETE FROM Ordertemp;"
    cursorobj.execute(deleteall)
    conn.commit()
    conn.close()
    return strtotal