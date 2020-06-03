sure=int(input("Görüşme sürenizi dakika olarak giriniz: "))

sabitucret=0.5
dkucret=0.3

sayac=0
herbesdk=(sure//5)
faiz=0.20


while sayac<= herbesdk:
    sayac+=1
    dkucret=dkucret+(dkucret*faiz)

    break


ucret= sabitucret + sure*dkucret 

print(f"{sure} dakikalık görüşme ücretiniz: {ucret} TL")


