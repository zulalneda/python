sayilar = [1,3,5,7,9,12,19,21]

#1- Sayılar listesindeki hangi sayılar 3'ün katıdır?
for sayi in sayilar:
    if(sayi %3 == 0):
        print(sayi)


#2- Sayılar listesindeki tüm elemanların toplamı kaçtır?
toplam = 0
for sayi1 in sayilar:
    toplam += sayi1   # toplam = sayi1 + toplam
print("toplam: ", toplam)


#3- Sayılar listesindeki tek sayıların karesini alınz.
for sayi3 in sayilar:
    if (sayi3 % 2 == 1):
        print(sayi3 ** 2)

sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]
#4- Şehirlerden hangileri en fazla 5 karakterlidir?
for sehir in sehirler:
    if (len(sehir)<= 5):
        print(sehir)



