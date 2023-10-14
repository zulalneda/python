# sayi = int(input())
# faktoriyel = 1 
# gecici_sayi = sayi 

# while gecici_sayi > 1:
#     faktoriyel *= gecici_sayi
#     gecici_sayi -= 1

# print(f"{sayi} sayısının faktöriyeli: {faktoriyel}")

# sayi = int(input())
# faktoriyel = 1
# for i in range(2,sayi+1):
#     faktoriyel *= i

# print(f"{sayi} sayısının faktöriyeli: {faktoriyel}")

"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

"""

# liste=[]
# for sayi in range(10,1000):
    
#     toplam = 0
#     basamak = len(str(sayi))
#     for i in str(sayi):
#         toplam += int(i) ** basamak

#     if toplam == sayi:
#         liste.append(sayi)


# sayi = int(input("sayı gir. "))
# basamak = len(str(sayi))
# toplam = 0
# gecici_sayi = sayi

# while gecici_sayi !=0:
#     toplam += (gecici_sayi % 10) ** basamak
#     gecici_sayi //= 10

# if toplam == sayi:
#     print(f"{sayi} armstrong sayısıdır.")
# else:
#     print(f"{sayi} armstrong sayısı değildir.")


"""1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin."""


# for sayi1 in range(1,11):
#     print("-----------------")
#     for sayi2 in range(1,11):
#         print(f"{sayi1}x{sayi2}={sayi1*sayi2}")


"""
for (değişken) in (üstünde işlem yapılacak obje):

for demek içteki şeyler bitene kadar değişken değerinde işlem yapması ondan sonra da değişkenin
değerini değiştirip değişen değişkende işlem yapması demek.
"""

# 1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.
# sayi = 0
# while True:
#     if sayi == 100:
#         break
#     else:
#         sayi = sayi + 1
#         if sayi % 3 != 0:
#             continue
#         print(sayi)


































    



