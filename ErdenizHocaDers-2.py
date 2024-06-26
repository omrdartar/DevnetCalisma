#koşul, dongu, exeptions, fonksiyon, try-except, class
#Bunların hepsi 4 bosluk / 1 tab'dır.
# import time

# region Ornek-1


# sonuc = input("Sinav sonucunu gir:\t")
# if not sonuc.isdigit() or int(sonuc) > 100 or int(sonuc) < 0:
#     print("Yanlis Veri")
# else:
#     sonuc=int(sonuc)
#     if sonuc >= 85:
#         print("pek iyi")
#     elif sonuc >= 70:
#         print("İyi")
#     elif sonuc >= 55:
#         print("orta")
#     elif sonuc >= 45:
#         print("geçer")
#     else:
#         print("Kaldi")


# endregion


# Dongu içindeki try except else



# region Ornek-2

# sonuc = input("Sinav sonucunu gir:\t")
# while not sonuc.isdigit() or int(sonuc) > 100 or int(sonuc) < 0:
#     print("Yanlis Veri")
#     sonuc = input("Sinav sonucunu gir:\t")
#
# sonuc=int(sonuc)
# if sonuc >= 85:
#     print("pek iyi")
# elif sonuc >= 70:
#     print("İyi")
# elif sonuc >= 55:
#     print("orta")
# elif sonuc >= 45:
#     print("geçer")
# else:
#     print("Kaldi")

# endregion


# region Ornek-3

# sonuc = input("Sinav sonucunu gir:\t")
# while True:                 # Aşağıdakiler doğru olduğu sürece demek while True
#     if not sonuc.isdigit() or int(sonuc) > 100 or int(sonuc) < 0:
#         print("Yanlis Veri")
#         sonuc = input("Sinav sonucunu gir yada çıkış için C yaz:\t")
#         if sonuc.lower() == "c":
#             print("Çıkış")
#             break
#         else:
#             continue          #Burada continue dememizin sebebi yalnıs while seçeneğinde olduğumuz
#                               #için yalnış seçeneğinin içindeki döngünün başına atmak için yazdık
#     else:
#         sonuc=int(sonuc)
#         if sonuc >= 85:
#             print("pek iyi")
#         elif sonuc >= 70:
#             print("İyi")
#         elif sonuc >= 55:
#             print("orta")
#         elif sonuc >= 45:
#             print("geçer")
#         else:
#             print("Kaldi")
#             break

# endregion


# region Ornek-4


# sonuc = input("Sinav sonucunu gir:\t")
# while True:
#     try:
#         sonuc = int(sonuc)
#         if sonuc > 100 or sonuc < 0:
#             raise ValueError("sonuc 0 dan küçük 100 den büyük olamaz.")
#         else:
#             sonuc = int(sonuc)
#             if sonuc >= 85:
#                 print("pek iyi")
#             elif sonuc >= 70:
#                 print("İyi")
#             elif sonuc >= 55:
#                 print("orta")
#             elif sonuc >= 45:
#                 print("geçer")
#             else:
#                 print("Kaldi")
#             break
#     except Exception as e:
#         print("Yanlıs veri girdiniz.")
#         sonuc = input("Sinav sonucunu gir yada çıkış için C yaz:\t")
#         if sonuc.lower()=="c" :
#             print("Çıkış")
#             break
#         else:
#             continue

# endregion


# region Ornek-5

# while True:
#     try:
#         sonuc = int(input("Sinav sonucunu gir:\t"))
#         if sonuc > 100 or sonuc < 0:
#             raise ValueError("sonuc 0 dan küçük 100 den büyük olamaz.")
#         else:
#             sonuc = int(sonuc)
#             if sonuc >= 85:
#                 print("pek iyi")
#             elif sonuc >= 70:
#                 print("İyi")
#             elif sonuc >= 55:
#                 print("orta")
#             elif sonuc >= 45:
#                 print("geçer")
#             else:
#                 print("Kaldi")
#             break
#     except Exception as e:
#         print("Yanlıs veri girdiniz.")
#         while True:
#             devam = input("Devam etmek için E çıkış için C yaz:\t")
#             if devam.lower()=="c" :
#                 print("Çıkış")
#                 flag=True
#                 break
#             elif devam.lower()== "e":
#                 print("Devam")
#                 flag=False
#                 break
#             else:
#                 print("Yanlıs secim. E ya da C yaz.")
#         if  flag:
#             break
#         else:
#             continue

# endregion

"""

Keyboard

"""


# region Ornek-6


# import keyboard
#
# mesaj="Devnet"
# print("mesaj refansini print etmek için Space tuşuna bas. Cikis için ESC tuşuna bas")
# while True:
#     if keyboard.is_pressed("ESC"):
#         print("ESC Tusuna Basin")
#         print("Exit")
#         break
#     elif keyboard.is_pressed("SPACE"):
#         print("Space tuşuna bastın. Mesaj referansını print et")
#         print(f'mesaj:{mesaj}')
#         break

# endregion

"""

fOR

"""

# region Ornek-7


# import time
# isim = "DARTAR"
# for karekter in isim:
#     time.sleep(1)
#     print(karekter,end=',')


# kucuk=0
# isim = "DaRtAr"
# for karekter in isim:
#     if karekter.islower():
#         kucuk+=1
# print(kucuk)


# endregion


# region Ornek-8

"""

Emailimiz icin sifre kontrolu yapmaya
buyuk_harf min >= 2
bosluk >= min 2
digit >= min 2
not_alfa (#,$@><*()...) >= min 2
kucuk_harf_ascii >= min 2
kucuk_harf_Turkce >= min 2 (ığüöçş)
uzunluk >= min 13

"""

# sifre = input('Lutfen sifrenizi yaziniz: ')
#
# buyuk_harf = 0
# bosluk = 0
# digit = 0
# not_alfa = 0
# kucuk_harf_ascii = 0
# kucuk_harf_Turkce = 0
# uzunluk = len(sifre)
#
# for karakter in sifre:
#     if karakter.isupper():
#         buyuk_harf += 1
#     elif karakter.isspace():
#         bosluk += 1
#     elif karakter.isdigit():
#         digit += 1
#     elif not karakter.isalpha():
#         not_alfa += 1
#     elif karakter.islower() and karakter.isascii():
#         kucuk_harf_ascii += 1
#     elif karakter.islower() and not karakter.isascii():
#         kucuk_harf_Turkce += 1
#
# if uzunluk >= 13 and buyuk_harf >= 2 and bosluk >= 2 and digit >= 2 and not_alfa >= 2 and kucuk_harf_ascii >= 2 and kucuk_harf_Turkce >= 2:
#     print('Butun kosullar saglandi. Ailemize hosgeldiniz:)')
# else:
#     print('Sifre kabul edilmedi:(')


# endregion












