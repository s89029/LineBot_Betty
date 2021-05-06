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
    cost = int(event.split('/'))
    cost += cost
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