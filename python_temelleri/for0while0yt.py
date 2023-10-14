#Listeler ile for döngüsü
#range fonksiyonu ve for döngüsü
#iç içe for döngüleri
#break ve continue anahtar kelimeleri
#while döngüsü





Liste = [1,2,3,4,5,6]

for rakam in Liste:
    print(rakam)


isim = "Ahmet"

for harf in isim:
    print(harf)


demet = (1,2,3,4)

for i in demet:
    print(i)


for i in range(0,10):   #ilk sınırı dahil eder, son sınırı etmez! 
    print(i)     


for i in range(1,17,2):   #1'den 17'ye kadar ikişer aralıklarla yazdır.
    print(i)                 



#2^10'u hesaplamak için:
sonuc = 1
for i in range(3,13):   #ister (0,10), ister (1,11) olsun aralık 10 olunca işlem görür.
    sonuc *= 2
print(sonuc)


liste1 = ["a", "b", "c"]
liste2 = [1, 2, 3]

for harf in liste1:
    for rakam in liste2:
        print(harf,rakam)


#Çalışma mantığı: liste1den ilk harfi alır, rakam1den de ilk harfi alıp yazdırır. Sonra rakamdan 2. yi alır ve böyle gider.


liste3 = [1,2,3,4,5,6,7,8,9]

for i in liste3:
    if i == 3:
        print("3'ü atladık")
        continue
    print(i)

#"continue" döngüsü istenmeyen elemanı atıp döngüyü kaldığı yerden yazmaya yarar.

for i in liste3:
    if i == 3:
        print("3'te bitirdik")
        break
    print(i)

#"break" döngüsü istenilen elemanı da yazdırıp döngüyü sonlandırmaya yarar.

#3'e tam bölünen sayıları yazdıracağımız zaman:

liste4 = range(100)

for i in liste4:
    if i %3 != 0:
        continue
    print(i)



#3'e tam bölünen sayıları 78'e kadar (78 dahil) yazdıracağımız zaman:

liste4 = range(100)

for i in liste4:
    if i %3 != 0:
        continue
    if i == 81:
        break
    print(i)


x = 2

while x < 10:
    print("x = ", x)
    x += 1
print("x = ", x)


x = 2
y = 3

while x * y < 1000:
    print(x,y)
    x += 2
    y += 2


#while True ile sonsuz döngü oluşturulur.
i = 1
while True:
    print(i)
    i += 1
    if i == 10000:
        break



i = 1
while True:
    if (i %2 != 1):
        i +=1
        continue
    print(i)
    i += 1
    if i == 1000:
        break