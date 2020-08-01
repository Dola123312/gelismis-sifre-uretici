import random
kucuk= "abcdefghijklmnopqrstuvwxyz"
buyuk= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayı= "0123456789"
sembol= "!@£$%^&*().,?"
try:
    uzunluk = input("şifre uzunluğu ? : ");uzunluk = int(uzunluk)
except(ValueError):
    uzunluk = input("lütfen yeniden giriniz : ");uzunluk = int(uzunluk)
a = input("abcdefghijklmnopqrstuvwxyz içersinmi(hayır/evet) : ")
if a != "evet" and a != "hayır":
    a = input(a+" yazdınız lütfen tekrar yazınız düzeltmezseniz program bunu hayır olarak algılayacaktır : ")
b = input("ABCDEFGHIJKLMNOPQRSTUVWXYZ içersinmi(hayır/evet) : ")
if b != "evet" and b != "hayır":
    b = input(b+" yazdınız lütfen tekrar yazınız düzeltmezseniz program bunu hayır olarak algılayacaktır : ")
c = input("0123456789 içersinmi(hayır/evet) : ")
if c != "evet" and c != "hayır":
    c = input(c+" yazdınız lütfen tekrar yazınız düzeltmezseniz program bunu hayır olarak algılayacaktır : ")
d = input("!@£$%^&*().,? içersinmi(hayır/evet) : ");password = "";e = ""
if d != "evet" and d != "hayır":
    d = input(d+" yazdınız lütfen tekrar yazınız düzeltmezseniz program bunu hayır olarak algılayacaktır : ")
if a=="evet":e += kucuk
if b=="evet":e += buyuk
if c=="evet":e += sayı
if d=="evet":e += sembol
for c in range(uzunluk):
    password += random.choice(e)
print(password)
