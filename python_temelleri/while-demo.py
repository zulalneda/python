sayilar = [1,3,5,7,9,12,19,21]

#1- sayilar listesini while ile ekrana yazdırın.
i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1


#2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
baslangic = int(input("Başlangıç sayısı: "))
bitis = int(input("Bitiş sayısı: "))

while baslangic < bitis:
    baslangic += 1
    if (baslangic % 2 == 1):
        print(baslangic)


#3- 1-100 arasındaki sayıları azalan şekilde yazdırın.
x = 100
while x > 0:
    print(x)
    x -= 1


#4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
numbers = []

i=0

while i<5:
    sayi = int(input("sayı: "))
    numbers.append(sayi)
    i+=1

numbers.sort()
print(numbers)


#5- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#** ürün sayısını kullanıcıya sorun.
#** dictionary listesi (name,price) şeklinde olsun.
#** ürün ekleme işlemi bittiğinde ürünleri ekrana "while" ile listeleyin.





