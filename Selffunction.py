# -*- coding: utf-8 -*-
import random
import re
import codecs

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
