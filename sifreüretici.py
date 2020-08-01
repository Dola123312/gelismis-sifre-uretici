import random
kucuk= "abcdefghijklmnopqrstuvwxyz"
buyuk= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayı= "0123456789"
sembol= "!@£$%^&*().,?"
uzunluk = input("şifre uzunluğu ? : ");uzunluk = int(uzunluk)
a = input("abcdefghijklmnopqrstuvwxyz içersinmi(hayır/evet) : ")
if a != "evet" and a != "hayır": z = input(a+" yazdınız program bunu hayır olarak algılayacaktır eğer devam etmek isterseniz entere basınız.")
b = input("ABCDEFGHIJKLMNOPQRSTUVWXYZ içersinmi(hayır/evet) : ")
if b != "evet" and a != "hayır": z = input(b+" yazdınız program bunu hayır olarak algılayacaktır eğer devam etmek isterseniz entere basınız.")
c = input("0123456789 içersinmi(hayır/evet) : ")
if c != "evet" and a != "hayır": z = input(c+" yazdınız program bunu hayır olarak algılayacaktır eğer devam etmek isterseniz entere basınız.")
d = input("!@£$%^&*().,? içersinmi(hayır/evet) : ");password = "";e = ""
if d != "evet" and a != "hayır": z = input(d+" yazdınız program bunu hayır olarak algılayacaktır eğer devam etmek isterseniz entere basınız.")
if a=="evet":e += kucuk
if b=="evet":e += buyuk
if c=="evet":e += sayı
if d=="evet":e += sembol
for c in range(uzunluk):
    password += random.choice(e)
print(password)
