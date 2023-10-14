website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

#1) " Hello World " karakter dizisinin başındaki ve sonundaki boşlukları silin.
result = " Hello World "
#result = result.strip()
#print(result)
#result = result.lstrip() #left strip anlamına geliyor. yani sol taraftaki boşluğu sil.
#print(result)
result = result.rstrip() #right strip anlamına geliyor. yani sağ taraftaki boşluğu sil.
print(result)

#2) "www.sadikturan.com" içindeki sadikturan bilgisi haricindeki her karakteri silin.
result = "www.sadikturan.com".strip("w.com")
print(result)

#3) "course" karakter dizisinin tüm karakterlerini küçük yapın.
result = course.lower()
print(result)

#4) "website" içinde kaç tane a karakteri vardır?
a1 = website.count("a")
print(a1)

#5) "website" www ile başlayıp com ile bitiyor mu?
b1 = website.startswith("www")
print(b1)
c1 = website.endswith("com")
print(c1)

#6) "website" içinde ".com" ifadesi var mı?
d1 = website.find(".com")
print(d1)

#7) "course" içindeki karakterlerin hepsi alfabetik mi?
e1= course.isalpha()
print(e1)

#8) "Contents" ifadesini satırda 50 karakter içine yerleştirip sağına ve soluna * ekleyiniz.
f1= "Contents".center(50,"*")
print(f1)

#9)"course" dizisindeki tüm boşluk karakterlerini "-" ile değiştirin.
g1= course.replace(" ","-")
print(g1)

#10) "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştirin.
h1 = "Hello World".replace("World", "There")
print(h1)

#11)"course" karakter dizisini boşluk karakterlerinden ayırın.
i1 = course.split(" ")
print(i1)