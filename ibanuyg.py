
ibanNo=input("İban numarasını giriniz: ")

krktruzun=26
ulkekodu="TR"

sayac=0

while sayac<1:
    sayac+=1

    if (len(ibanNo) != krktruzun) or (ulkekodu!=ibanNo[0:2]):
        print("HATA")
        break

    yenikod=ibanNo[4:] + ibanNo[0:4]
    yenikod=yenikod.replace("TR","2927")
    yenikod=int(yenikod)
    
    if (yenikod)%97==1:
        print("İban numarası geçerli.")
    else:
        print("İban numarası geçersiz.")


    

    


    




    
    








