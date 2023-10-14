# 1-100 e kadar
x = 1
while x <= 100:   #1'den başlayıp 100'e kadar yazdırır.
    print(x)
    x += 1
print("bitti.")


y = 1
while y <= 100:
    if (y % 2 == 1):
        print(f"sayı tek: {y}")
    else:
        print(f"sayı çift: {y}")
    y += 1
print("bitti.")


name = "" #False
while not name.strip():
    name = input("isminizi giriniz: ")
print(f"Merhaba. {name}")
#name bilgisini boşluk(yani hiçbir şey yazılmadan) girince sistem kabul etmeyip geçerli bir name bilgisi ister.

