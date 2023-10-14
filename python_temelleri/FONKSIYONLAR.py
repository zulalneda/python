#sum() : bir dizi içerisindeki değerlerin toplamını alır.
#len() : listedeki elemanların sayısını döndürür.
#def : fonksiyonlarda kullanılır.

def ortalama_hesapla(liste):
    toplam = sum(liste)
    adet = len(liste)
    ortalama = toplam/adet
    print(f"Girilen sayıların ortalaması: {ortalama}")

ortalama_hesapla([1,2,3,4,5,6,7])


def buyuk_harfe_cevir(metin):
    metin = metin.upper()
    print(metin)

buyuk_harfe_cevir("öyle işte")


def selamla(mesaj, isim = "Anonim"):
    print(f"{mesaj} {isim}. ")

selamla("Merhaba","Elif")   #Merhaba Elif.


def selamla(mesaj, isim = "Anonim"):
    print(f"{mesaj} {isim}. ")

selamla("Merhaba")   #Merhaba Anonim.


def indirim_yap(fiyat,yuzde):
    indirim_miktarı = fiyat * (yuzde / 100)
    indirimli_fiyat = fiyat - indirim_miktarı
    print(f"İndirimli Tutar: {indirimli_fiyat}")

indirim_yap(50,10)


def indirim_yap(fiyat,yuzde = 20):
    indirim_miktarı = fiyat * (yuzde / 100)
    indirimli_fiyat = fiyat - indirim_miktarı
    print(f"İndirimli Tutar: {indirimli_fiyat}")

indirim_yap(50)


def topla(x,y):
    print(x + y)
    return x + y

topla(3,8)
sonuc = topla(3,8)
print(sonuc)

def ortalama_hesapla(x,y):
    return (x + y) / 2

a = ortalama_hesapla(2,6)
b = ortalama_hesapla(6,10)
print(a + b)


def buyuk_harfe_cevir(metin):
    return metin.upper()

c = buyuk_harfe_cevir("fghJkLmnBYtr")
print(c)

fonk = buyuk_harfe_cevir

sonuc = fonk("asdFGHjkLmnbTYu")
print(sonuc)
    


