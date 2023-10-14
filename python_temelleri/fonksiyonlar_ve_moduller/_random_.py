import random

for i in range(10):
    print(random.random()) #random.random'ı 0-1 arasında rastgele sayı yazdırmak için kullanırız.

for i in range(10):
    print(random.uniform(10,30)) #istenen aralıkta rastgele ondalık sayı yazdırılmasını sağlar.

for i in range(10):
    print(random.randint(1,5)) #1 ve 5 de dahil bu aralıkta 10 tane rastgele tam sayı yazdırır.


print(" ")

for i in range(10):
    print(random.randrange(1,10,3)) #1 dahil olup 10 dahil olmayıp 3er 3er artan fonksiyonları göstermek amacıyla kullanılır.

print(" ")

liste = ["Siyah", "Beyaz", "Mavi", "Yeşil", "Gri", "Turuncu"]

print(random.choice(liste)) #liste, tuple ya da string bir ifadeden rastgele eleman seçip yazdırır.

random.shuffle(liste)
print(liste) #listedeki elemanları rastgele karıştırıp yeni liste yaratır.

print(random.sample(liste,3)) #listedeki elemanlardan 3 tanesini rastgele seçip liste şeklinde yazdırır.

zarlar = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(100000):
    zar = random.randint(1, 6)
    zarlar[zar] += 1

for zar in zarlar:
    print(f"{zar} gelme olasılığı: {zarlar[zar] / 100000}")


alti_alti = 0
deneme_sayisi = 0
while True:
    deneme_sayisi += 1
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)
    if  zar1 == 6 and zar2 == 6:
        alti_alti += 1
    if alti_alti == 10:
        print(f"10 kere 6-6 gelmesi için zarlar {deneme_sayisi} kadar atıldı.")
        break