#ekrandan alınan bir sayının faktöriyelini hesaplayan bir program yazınız.
#sayi = int(input("girilen sayı = "))


#faktoriyel = 1

#for i in range(1,sayi + 1):
 #   faktoriyel *= i
#print(f"{sayi}! = {faktoriyel}")

#i = 2
#while i <= sayi:
    #faktoriyel *= i
    #i += 1

#print(f"{sayi}! = {faktoriyel}")




#ekrandan alınan bir sayının asal olup olmadığını kontrol eden bir program yazınız.
#sayi = int(input("girilen sayı = "))

#prime = True #1) Değeri "True" olan bir ifade ata.

#for i in range(2, sayi): #2) 1'den başlamamamızın ve range'i "sayi" ile bitirmemizin nedeni her sayı 1e ve kendisine tam bölünür.
 #   if sayi %i == 0:
 #       prime = False
  #      break
#if prime == True:
 #   print(f"{sayi} sayısı asaldır.")
#else:
 #   print(f"{sayi} sayısı asal değildir.")



#ekrandan alınan bir sayının pozitif kaç tane böleni olduğunu bulan bir program yazınız.
#sayi = int(input("girilen sayı = "))

#bolen_sayisi = 0

#for i in range(1, sayi + 1):
 #   if sayi %i == 0:
  #      bolen_sayisi += 1
#print(f"{sayi} sayısının {bolen_sayisi} tane böleni vardır.")
# "i" ile "input sayısı" birbiriyle ilişkidedir.



#ekrandan okunan bir sayının rakamları toplamını hesaplayan bir program yazınız.

#sayi = int(input("girilen sayı = "))

#str_sayi = str(sayi)
#toplam = 0 
#for rakam in str_sayi:   #ifadenin üzerinde gezinebilmesi için int>str>int yaptık. 
 #   toplam += int(rakam)

#print(toplam)

#ya da sayıyı string'e çevirmeden yapmak istersek:
#sayi = int(input("girilen sayı = "))

#toplam = 0
#gecici_sayi = sayi

#while gecici_sayi != 0:
 #   basamak = gecici_sayi % 10
  #  toplam = toplam + basamak
   # gecici_sayi //= 10

#print(toplam)

#ekrandan peşpeşe okunan 5 sayının en küçüğünü ve en büyüğünü ekrana yazdıran bir program yazınız.

#liste = []
#for i in range(5):
 #   sayi = int(input("girilen sayı = "))
  #  liste.append(sayi)
#print(f"en büyük sayı : {max(liste)}")
#print(f"en küçük sayı : {min(liste)}")


#ekrandan okunan bir sayının herhangi bir sayının karesi olup olmadığını kontrol eden bir program yazınız.

#sayi = int(input("girilen sayı = "))

#karekok = sayi ** 0.5

#if karekok == int(karekok):
 #   print("Tamkare")
#else:
#    print("Tamkare değil")

#ekrandan okunan bir metinde hangi harfin kaç kere kullanıldığını gösteren bir program yazınız.

#metin = input("Bir metin giriniz: ")

#sozluk = dict()

#for harf in metin:
 #   if harf in sozluk:
  #      sozluk[harf] += 1
   # else:
    #    sozluk[harf] = 1
#for harf,adet in sozluk.items():
 #   print(harf,adet)

#ekrandan okunan bir metinde a harflerini büyük yapan bir program yapınız.
#metin = input("Bir metin giriniz: ")

#metin2 = ""

#for harf in metin:
 #   if harf == "a":
  #      metin2 += "A"
   # else:
    #    metin2 += harf
#print(metin2)




