krktruzun=16

sayac=0

while sayac<1:
    sayac+=1

    krediNo= input("Kullanıcı kredi kartı numarasını giriniz: ")

    for i in krediNo:
        if i.isalpha():
            print("Harf girdiniz. Lütfen rakam giriniz.")
            break
            
    
    if (krktruzun != len(krediNo)):
        print("16 karakter giriniz")
        break
    
    yenikod=krediNo[0:15:2]
    hanetoplam=0
    ikitoplam=0
    sontoplam=0
    
    for i in yenikod:

        i=int(i)

        ikikati=i*2

        if len(str(ikikati))==2:
            for z in str(ikikati):
                hanetoplam += int(z)
        
        elif len(str(ikikati))==1:
            ikitoplam+=ikikati

    sonkod=krediNo[1:len(krediNo):2]

    for item in sonkod:
        item=int(item)
        sontoplam+=item
    
    toplam=hanetoplam + sontoplam +ikitoplam

    if toplam%10==0:
        print("Girilen kredi numarası geçerlidir.")
    else:    
        print("Girilen kredi numarası geçersizdir.")

            


        
            
            
        



   


            





    


    



    
    
    
        


