
"""

import requests

url = 'https://knowledgeclub.netdevopsakademi.net/tr'

response=requests.get(url)
print(response.text)

import this

"""

"""

import random as rd

if rd.randint(1,2) == 1:
    print('Yazi')
else:
    print('Tura')

"""

"""

import random as rd

sonuc = rd.randint(1,6)
print(sonuc)

"""

"""

import random as rd
import time as t
sayim = 1

while True:
    zar1 = rd.randint(1,6)
    zar2 = rd.randint(1,6)
    print(f'Zar Atişi {sayim}: Zar1: {zar1} Zar2: {zar2}')
    sayim+=1
    if zar1 == 6 and zar2 == 6:
        print('DÜŞEŞ')
        break
    else:
        continue
    t.sleep(0.2)

"""

"""

import math

a=int(input("kenar1: "))
b=int(input("kenar2: "))
h=math.sqrt(a**2+b**2)

print(f'a kenari: {a} b kenari: {b} ve Hypo: {int(h)}')

"""

from datetime import datetime
now=datetime.now()
day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.minute
second=now.second
print(f'Tarih: {day}.{month}.{year} Saat: {hour}:{minute}:{second}')




















































