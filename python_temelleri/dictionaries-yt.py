kisi = {"isim" : "ali", "yas" : 20, "cinsiyet" : "m", "hobiler": {"Sinema","Konser","Yazılım"}}

#print(kisi)
#print(kisi["isim"]) #ali
#print(kisi["hobiler"]) #{"Sinema", "Konser", "Yazılım"}

#kisi["isim"] = "Ahmet" #ali bilgisini ahmet ile değiştirdik.
#print(kisi)


#aynı anda birden fazla bilgiyi değiştirmek istersek: ".update" metodunu kullanırız.
#kisi.update({"isim" : "mehmet", "yas" : 30})
#print(kisi)

#kisi.update({"cinsiyet": "f"})
#print(kisi)

#olmayan bir alan eklemek istersek:
#kisi["id"] = 12345
#print(kisi) #en son olarak yazdırır.


#bir alanı silmek istersek: "del " metodunu kullanırız.

#del kisi ["id"]
#print(kisi)

#sözlüğümüzü "for" döngüsü ile yazdımak istersek:

for x in kisi:
    print(x) #"key" kısımlarını arka arkaya yazdırır. "isim yas cinsiyet hobiler"



for x in kisi:
    print(kisi[x]) #"value" kısımlarını arka arkaya yazdırır.
                   #ali 20 m {"Konser", "Sinema" , "Yazılım"}


#eğer sadece keys kısmını liste halinde almak istersek:
print(kisi.keys())


#eğer sadece values kısmını liste halinde almak istersek:
print(kisi.values())


#hem keys hem de values kısmını ekrana liste halinde yazdırmak istersek: ".items" kullanırız.
print(kisi.items())


#keys ve values kısımları aynı anda listesiz arka arkaya yazdırmak istersek:
for k in kisi.items():
    print(k)


#keys ve values kısımları aynı anda listesiz, virgülsüz ve parantezsiz şekilde arka arkaya yazdırmak istersek:
for k,v in kisi.items():
    print(k, ":" ,v)


print(kisi.get("id","Bulunamadı.")) #olmayan bir anahtar için "Bulunamadı." yazar, olan anahtarın değerini de virgülsüz parantezsiz şekilde gösterir.
