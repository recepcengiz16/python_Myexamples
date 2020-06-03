import random

sayi=random.randint(1,100)

can=int(input("Kaç can hakkı olduğunu giriniz: "))

hak=can
sayac=0

while hak>0:
    sayac+=1
    hak-=1
    tahmin=int(input("Tahmin ettiğiniz sayıyı giriniz: "))

    if sayi==tahmin:
        print(f"Tebrikler {sayac}. defada sayıyı bildiniz.Toplam puanınız: {100-(20*(sayac-1))}")
        break
    elif sayi>tahmin:
        print("Tahmin ettiğiniz değerden daha yüksek bir sayı giriniz.")
    else:
        print("Tahmin ettiğiniz değerden daha az bir değer giriniz.")

    if hak==0:
        print(f"Hakkınız sona ermiştir.Tutulan sayı: {sayi}. Toplam puanınız:0")
    
        
    



