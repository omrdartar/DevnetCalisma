

# region Erdeniz Hoca Ders-1

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

"""

"""

mesaj='paramiko kutuphanesi netmiko kutuphanesi napalm kutuphanesi'
#mesaj= ana string
#kutuphanesi= substring
mesaj7=mesaj.split(' ')
mesaj9=' , '.join(mesaj)


print(mesaj7)
print(mesaj9)

"""

"""

sayi=int(input('sayi yaz: '))
if sayi >42:
    print('sayi 42"den buyuk')
elif sayi == 42:
    print('Sayi 42 ye eşittir.')
else:
    print('sayi 42"den kucuk')

"""

"""

sonuc = int(input('Sınav sonucunuzu giriniz: '))

if sonuc > 100 or sonuc < 0:
    print('Gecersiz veri girdiniz.')
else:
    if sonuc >= 85:
        print('Pekiyi aldınız')
    elif sonuc >= 70:
        print('iyi')
    elif sonuc >= 55:
        print('Orta')
    elif sonuc >= 45:
        print('Gecer')
    else:
        print('Kaldin')

"""

"""

sonuc = input('Sinav sonucunuzu giriniz: ')

if not sonuc.isdigit() or int(sonuc) > 100 or int(sonuc) < 0:
    print('Gecersiz veri')
else:
    sonuc=int(sonuc)
    if sonuc >= 85:
        print('Pek iyi')
    
    elif sonuc >= 70:
        print('Iyi')
    
    elif sonuc >= 55:
        print('Orta')
    
    elif sonuc >= 45:
        print('Gecer')
    
    else:
        print('Kaldin')

"""

"""

import time

gerisayim = int(input('geri sayim: '))
while gerisayim > 0:
    print(gerisayim)
    time.sleep(1)
    gerisayim-=1
print('Geri Sayim Bitti')

"""

"""

import time
gerisayim =int(input('gerisayim: '))
while gerisayim > 0:
    print(gerisayim,end=',')
    time.sleep(1)
    #gerisayim=gerisayim-1
    gerisayim-=1
print('gerisayim bitti')

"""

#sayi tahmin oyunu
#python 1-100 arasinda bir sayi secer
#ben de bunu tahmin edeyim
#tahminim sayidan buyuk ise: tahmin>sayi. Daha dusuk degerde tahmin yap
#tahminim sayidan kucuk ise: tahmin<sayi. Daha yuksek degerde tahmin yap
#tahmin==sayi: bingo

"""

import random as rd

sayi = rd.randint(1,100)
deneme = 0
while True:
    tahmin = int(input('Lütfen 1 ile 100 arasinda bir tahmin giriniz : '))
    deneme += 1
    if  tahmin < sayi:
        print('Daha yüksek bir değer giriniz: ')
    
    elif tahmin > sayi:
        print('Daha kücük bir değer giriniz: ')
    else:
        print(f'Bingo. {deneme} deneme yaparak buldunuz.')
        break
    
"""
"""
import random as rd

sayi = rd.randint(1,100)
deneme = 0

while True:
    tahmin = int(input('Lütfen 1 ile 100 arasında bir sayi giriniz: '))
    deneme+=1
    if tahmin < sayi:
        print('Lütfen daha büyük bir sayi giriniz')
    elif tahmin > sayi:
        print('Lütfen daha küçük bir sayi giriniz')         
    else:
        print(f'Bingo. {deneme} deneme yaparak buldunuz')
        break
"""


#sayi tahmin oyunu
#python 1-100 arasinda bir sayi secer
#ben de bunu tahmin edeyim
#tahminim sayidan buyuk ise: tahmin>sayi. Daha dusuk degerde tahmin yap
#tahminim sayidan kucuk ise: tahmin<sayi. Daha yuksek degerde tahmin yap
#tahmin==sayi: bingo
#tahmin hakki bastan belirlensin
#her tahmin hakkinda geriye kac hakkin kaldigi soylesin
#butun haklarini kullandin ve bilemedin: kaybettin. sayiyi acikla
#eger kazanirsa: su kadar hak kullanarak kazandin

"""

import random as rd
sayi = rd.randint(1,100)
tahmin = 0
tahmin_hakki=int(input('kac adet tahmin hakkin olsun: '))
hak = 0

while tahmin != sayi:
    
    tahmin = int(input('1-100 arasinda sayi yaz: '))
    hak += 1
    
    if tahmin_hakki == hak and tahmin != sayi:
        print(f'Bilemedin. Sayi da {sayi}')
        break
    
    elif tahmin > sayi:
        print(f'kalan hak:{tahmin_hakki-hak} Daha dusuk degerde tahmin yap')
    
    elif tahmin < sayi:
        print(f'kalan hak:{tahmin_hakki-hak} Daha yuksek degerde tahmin yap')
    
    else:
        print(f'Bingo. {hak} adet tahmin hakki kullanarak kazandin.')


"""


#if x is 15 python karşılıgı if x == 15
#if x is not 15 python karşılıgı if x != 15

# endregion


# region IF-THEN-ELSE-ELIF Aziz Hoca

# region if-giriş Örnek-1
# havaDurumu = input("Hava yağmurlu mu: ")
# if havaDurumu == "Yağmurlu":
#     print("Şemsiye al")
# else:
#     print("Peki o zaman")
# endregion

# region if-giriş Örnek-2
# a = int(input("Lütfen bir sayı giriniz: "))
# if a < 0:
#     print("{} sayısı negatiftir.".format(a))
# else:
#     print("{} Sayısı pozitiftir.".format(a))

# endregion

# region if-giriş Örnek-3
# kullaniciAdi = input("Lütfen kullanıcı adınızı giriniz: ")
# if kullaniciAdi == "admin":
#     print("Hoşegeldin Senior")
# elif kullaniciAdi == "user":
#     print("Hoşgeldin User")
# else:
#     print("Kullanıcı adınız bulunamadı.")

#endregion

# region if-giriş Örnek-4

# engeleDegdimi=input("Enegele Değdiniz mi : ")
# can, skor = 3, 0
# if engeleDegdimi == "Evet":
#     can -= 1
#     print("{} canınız kaldı".format(can))
# else:
#     skor += 1
#     print("{} puan aldınız".format(skor))

#endregion

# region if-giriş Örnek-5
# havaYagislimi = input("Hava Yagisli mi?: ")
# havaSogukmu = input("Hava Soguk mu?: ")
# kac_derece = int(input("Hava Kac Derece?: "))
# if havaYagislimi == "yagisli":
#     if havaSogukmu == "soguk":
#         print("Şemsiyeni al, mont giy")
#     else:
#         print("Mont Giy")
# elif havaSogukmu == "soguk":
#     if kac_derece >= int(20):
#         print("Hırka Al")
#     elif kac_derece == int(15):
#         print("Mont AL")
#     else:
#         print("Gocuk giy")
# else:
#     print("peki o zaman")
# endregion

# region if-giriş Örnek-6

# sayi1 = int(input("Lütfen 1.sayıyı giriniz: "))
# sayi2 = int(input("Lütfen 2.sayıyı giriniz: "))
# sayi3 = int(input("Lütfen 3.sayıyı giriniz: "))
#
#
# if sayi1 >= sayi2 and sayi1 >= sayi3:
#     if sayi2 >= sayi3:
#         print(sayi1, sayi2, sayi3)
#     else:
#         print(sayi1, sayi3, sayi2)
# elif sayi2 >= sayi1 and sayi2 >= sayi3:
#     if sayi1 >= sayi3:
#         print(sayi2,sayi1,sayi3)
#     else:
#         print(sayi2,sayi3,sayi1)
# else:
#     if sayi1 >= sayi2:
#         print(sayi3,sayi1,sayi2)
#     else:
#         print(sayi3,sayi2,sayi1)

#endregion

# region if-giriş örnek-7
# sayi1 = int(input("Lütfen 1.sayıyı giriniz: "))
# sayi2 = int(input("Lütfen 2.sayıyı giriniz: "))
# if sayi1 > 0 and sayi2 > 0:
#     print("Doğru")
# else:
#     print("Hatalı")
# endregion

""""
Yıllık Gelir Vergisi  (ygv) hesaplayan programı yazınız.

Not:

Vergi dilimi: 0 – 22.000 TL için %15.

Vergi dilimi: 22.000 TL – 49.000 TL için %20.

Vergi dilimi: 49.000 TL – 180.000 TL için %27.

Vergi dilimi: 180.000 TL – 600.000 TL için %35.

Vergi dilimi: 600.000 TL üzeri için %40 hesaplanacak.

"""

# region if-giriş örnek-8

# Yillik_Gelir = int(input("Lütfen yıllık kazancınızı giriniz: "))
#
# if 0 < Yillik_Gelir <= 22000:
#     print("Yıllık ödeyeceginiz vergi", Yillik_Gelir*15/100 )
# elif 22000 < Yillik_Gelir <= 49000:
#     print("Yıllık ödeyeceginiz vergi", Yillik_Gelir*20/100)
# elif 49000 < Yillik_Gelir <= 180000:
#     print("Yıllık ödeyeceginiz vergi", Yillik_Gelir*27/100)
# elif 180000 < Yillik_Gelir <= 600000:
#     print("Yıllık ödeyeceginiz vergi", Yillik_Gelir * 35 / 100)
# elif Yillik_Gelir > 600000:
#     print("Yıllık ödeyeceginiz vergi", Yillik_Gelir * 40 / 100)
# else:
#     print("Hatalı giriş.")



# endregion

""""

Girilen iki kenar uzunluğu için eşitlik durumuna göre ekrana alanı hesaplayıp çıktı veren programı yazalım



Örn;

Lütfen a kenarını giriniz:  4

Lütfen b kenarını giriniz:  6

Dikdörtgenin Alanı → 24 m2. dir



Lütfen a kenarını giriniz:  4

Lütfen b kenarını giriniz:  4

Karenin Alanı → 16 m2. dir

"""

# region if-giriş örnek-9

# kenarA = int(input("Lütfen a kenarını giriniz: "))
# kenarB = int(input("Lütfen b kenarını giriniz: "))
#
# if kenarA == kenarB :
#     print("Karenin alanı", kenarA * kenarB, "dir")
# else:
#     print("Dikdörgenin alanı", kenarA * kenarB, "dir")

#endregion









#endregion

# region DONGULER-LOOP-WHILE Aziz Hoca

"""
while True:
    print("burdayım")
    break

for i in "":
    print("burdayım")
"""

"""
Döngüler için kurallar : 
1-Başlangıç asla unutulmamalı.
2-Bitiş asla unutulmamalı.
3-Artış miktarı asla unutulmamalı.
"""

# region While Ornek-1

# i = 0                       #Başlangıç
# while i < 10:               #Bitiş
#     print("Süper Hızlı")    #Aksiyon
#     i += 1                  #Artış

# endregion

"""
        - Ekrana aşağıdaki çıktıyı verecegiz
            1.Öğrenci
            2.Öğrenci
            3.Öğrenci
            ...
"""

# region While Ornek-2
# ogrenciSayisi = 1
#
# while ogrenciSayisi < 4:
#     print("{}.Öğrenci".format(ogrenciSayisi))
#     ogrenciSayisi += 1
# endregion

"""

Başlangıç değerini kullanıcıdan istediğiniz bir geri sayım programı yazınız. 

"""

# region While Ornek-3

# i = int(input("Lütfen başlangıç değeri giriniz: "))

# while i > 0:
#     print(i, end=" ") # end=" " yan yana yazırmak için kullandık.
#     i -= 1
#
#
# i = int(input("Lütfen başlangıç değeri giriniz: "))
# while i > 0:
#     print(i) # Bu örnekte alt alta yazar.
#     i -= 1

#endregion

"""

Başlangıç değerini kullanıcıdan istediğiniz 2'şer 2'şer azalan bir program yaz. 

"""

# region While Ornek-4

# i = input("Lütfen başlangıç mikarı giriniz: ")
# if i.isdigit():
#     i = int(i)
#     while i > 0:
#         print(i, end= " ")
#         i -= 2
# else:
#     print("Hatalı giriş yaptınız.")

# endregion

"""

1 den 100 e kadar olan tek sayıları yazdıran bir program yaz. 

"""

# region While Ornek-5

# i = 1
# while i <= 99:
#     print(i, end=",")
#     i += 2


# i = 1
# while i <= 100:
#     if i % 2 == 1:
#         print(i, end=",")
#     i += 1

# endregion

"""

            - Döngü içinde kullanıcıdan 3 adet sayı girmesi istenir.
            - Ekrana Doğru formatta çıktı verilerek, sayıların toplamları yazılır.
                Çıktı
                Girilen ---- adet sayının toplamı ----- dır. 

"""

# region While Ornek-6

# i = 1
# toplam = 0
# while i <= 3:
#     s=int(input("Lütfen {}. sayıyı giriniz: ".format(i)))
#     toplam += s
#     i += 1
# print("Girilen {} adet sayısının toplamı {}".format(i, toplam))

# endregion

# region While Ornek-7

# i, toplam = 1, 0
#
# while i <= 3:
#     s = input("Lütfen {}. sayıyı giriniz.".format(i))
#     if s.isdigit():
#         s = int(s)
#         toplam += s
#     else:
#         print("Lütfen sayısal bir değer giriniz.")
#         continue
#     i += 1
# print("Girilen {} adet sayının ortalaması {} dır.".format(i - 1, round(toplam/(i-1),3)))


# endregion

"""

            - Döngü içinde kullanıcıdan x adet sayı girmesi istenir.
            -0 girene kadar sayı istemeye devam edecek.
            - Ekrana Doğru formatta çıktı verilerek, sayıların toplamları yazılır.
                Çıktı
                Girilen ---- adet sayının toplamı ----- dır. 

"""

# region While Ornek-8

# toplam, i = 0, 0
# while True:
#     s = int(input("Lütfen sayı giriniz:\t"))
#     if s == 0:
#         break
#     else:
#         toplam += s
#         i += 1
# print("Girilen {} adet sayısının toplamı {}".format(i, toplam))

# endregion

# region While Ornek-9

# deger = ""
# i, j = 0, 0
# while i < 5:
#     i += 1
#     while j < 5:
#         j += 1
#         deger += "* "
#     print(deger)
#     deger = ""
#     j = 0

# endregion

# region While Ornek-10


# deger = ""
# i, j = 0, 0
# while i < 10:
#     i += 1
#     while j < 15:
#         j += 1
#         deger += "* "
#     print(deger)
#     deger = ""
#     j = 0

# endregion

# region While Ornek-11


# deger = ""
# i, j = 0, 0
# while i < 10:
#     i += 1
#     while j < i:
#         j += 1
#         deger += "* "
#     print(deger)
#     deger = ""
#     j = 0

# endregion

# region While Ornek-12

# i = 1
# a, b = 0, 1
# while i < 30:
#     i += 1
#     c = a + b
#     print(c, end=" , ")
#     a = b
#     b = c

# endregion



# endregion

# region Fonksiyonlar Aziz Hoca


# region Fonksiyonlar Örnek-1 Parametre Almayan, Değer Döndürmeyen

# def Welcome():
#     ad = input("Adnız:\t")
#     print("Hoşgeldiniz", ad)
#
# Welcome()
# endregion

# region Fonksiyonlar Örnek-2 Parametre Almayan, Değer Döndüren

# def Topla():
#     s1 = int(input("S1:\t"))
#     s2 = int(input("S2:\t"))
#     sonuc = s1 + s2
#     return sonuc
#
# sonuc = Topla()
# print(sonuc)


# endregion

# region Fonksiyonlar Örnek-3 Parametre Alan, Değer Döndürmeyen-1

# import math
# def Alan(yaricap):
#     sonuc = math.pi * yaricap ** 2
#     print("Alan :", sonuc)
#
# s = int(input("Lütfen parametre giriniz: "))
# Alan(s)

# endregion-1-1

# region Fonksiyonlar Örnek-4 Parametre Alan, Değer Döndürmeyen-2

# def Karsilama(ad, soyad):
#     print("Merhaba", ad, soyad)
#
# ad = input("Lütfen Adınızı Giriniz.")
# soyad = input("Lütfen SoyAdınızı Giriniz.")
# Karsilama(ad, soyad)

# endregion

# region Fonksiyonlar Örnek-5 Parametre Alan, Değer Döndürmeyen-3

# def MutlakDeger(a):
#     if a < 0:
#         a *= -1
#     print("Mutlak Değer: {}".format(a))
#
# MutlakDeger(-10)

# endregion

# region Fonksiyonlar Örnek-6 Parametre Alan, Değer Döndüren

# def MutlakDeger(a):
#     if a < 0:
#         a *= -1
#     return "ABS: {}".format(a)
#
# print(MutlakDeger(-10))

# endregion

# region Fonksiyonlar Örnek-7

# def Hizlan():
#     global hiz
#     hiz += 5
#     print("Anlık Hızınız {} km/s".format(hiz))
#
# def Yavasla():
#     global hiz
#     hiz -= 5
#     print("Anlık Hızınız {} km/s".format(hiz))
#
# hiz = 80
#
# Hizlan()
# Hizlan()
# Hizlan()
# Hizlan()
# Yavasla()
# Hizlan()

# endregion

"""

    - Sonuc isimli fonsiyon olacak.
        Sonuc() içinde s1, s2 değişkenlerine kullanıcıdan değer alınacak.
    - Koşula göre değer dönecek
        Eğer s1 s2 den büyük ise çarpım değeri geriye dönecek
        Eğer s1 s2 den küçük ise bölme değeri geriye dönecek
        Eğer s1 s2 den eşit ise eşitlik değeri geriye dönecek

"""

# region Fonksiyonlar Örnek-8

# def Sonuc(s1, s2):
#     if s1 > s2 :
#         print(s1*s2)
#     elif s1 < s2:
#         print(s2/s1)
#     else:
#         print(s1,",", s2)
#
#
#
# a = int(input("Lütfen birinci sayıyı giriniz: "))
# b = int(input("Lütfen ikinci sayıyı giriniz: "))
#
# Sonuc(a,b)


# endregion

# region Fonksiyonlar Örnek-9

# def Sonuc():
#     s1 = int(input("S1: \t"))
#     s2 = int(input("S2: \t"))
#     if s1 > s2 :
#         return (s1*s2)
#     elif s1 < s2:
#         return (s2/s1)
#     else:
#         return (s1 , s2)
#
# x = Sonuc()
# print(x)
#

# endregion

# region Fonksiyonlar Örnek-10

# def Islem(operator, a, b):
#     if operator == "+":
#         return a + b
#     elif operator == "-":
#         return a -b
#     else:
#         return a * b
#
# sonuc = Islem(2, 10, "*")
# print(sonuc)


# endregion

# region Fonksiyonlar Örnek-11

# def Islem(operator, a, b):
#     if operator == "+":
#         return a + b
#     elif operator == "-":
#         return a -b
#     else:
#         return a * b
#
# sonuc = Islem(a=2, b= 10, operator="*")
# print(sonuc)


# endregion

# region Fonksiyonlar Örnek-12

"""
Bu Örnekte ortalama fonksiyon örnepği var fakat burada 4. değeri girersek fonsiyon bozuluyor.
Bir Sonraki örnekte bunu nasıl aşacagımıza bakacağız.
"""


# def Ortalama(a, b, c):
#     return (a + b +c) / 3
#
# print(Ortalama(3,6,9))

# endregion

# region Fonksiyonlar Örnek-12

# def Ortalama(*liste):
#     return sum(liste) / len(liste)
#
# print(Ortalama(10,20,30,40,50))

# endregion




# endregion

















