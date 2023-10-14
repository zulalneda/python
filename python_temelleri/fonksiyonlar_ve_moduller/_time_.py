import time

zaman = time.time() #programlama dillerinin başlangıç tarihi olarak kabul edilen 1 Ocak 1970'ten bu yana kaç saniye geçtiğini gösterir.
print(zaman)

baslangic = time.time()
liste = []
for i in range(10000000):
    liste.append(i)
bitis = time.time()
print(bitis - baslangic)

zaman = time.ctime() #güncel tarihi yazdırır.
print(zaman)

zaman = time.ctime(100000000) #içine yazılan değer saniyedir. 01.01.1970'ten bu yana geçen saniyeye bağlı tarihi yazdırır.
print(zaman) #type = string

zaman2 = time.localtime() #mevcut tarihi gösterir.
print(zaman2) #parantezin içine sayı alır.

zaman = time.asctime(zaman2) 
print(zaman) #localtime modülünü daha düzgün şekilde yazar.

zaman = time.strftime("%d.%m.%Y  %H.%M.%S")

print("program başlatıldı")
time.sleep(3) #3 saniye durakladı.
print("program sonlandı")

