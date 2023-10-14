website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

#1-) "course" karakter dizisinde kaç karakter bulunmaktadır?
result = len(website)
print(result)

#2) "website" içinden www karakterlerini alın.
result = website[7:10]
print(result)

#3) "website" içinden com karakterlerini alın.
result = website[-3:]
print(result)

#4) "course" içinden ilk 15 ve son 15 karakterlerini alın.
result = course[:15]
print(result)

result = course[-15:]   #sondan başlayıp ilk 15 karaktere kadar yazdırmak isteseydik "-"yi silecektik.
print(result)

#5) "course" ifadesindeki karakterleri tersten yazdırın.
result = course[::-1]
print(result)



name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

#6) Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# "Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis."

x = str(32)
result = "Benim adım " + (name) + " " + (surname) + ", yaşım " + (x) + " "+ "ve mesleğim " + (job) + "."
print(result)
result = "Benim adım {0} {1}, yaşım {2} ve mesleğim {3}.".format(name, surname, age, job)
print(result)
result = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}."

#7) "Hello world" ifadesindeki w harfini "W" ile değiştirin.
s = "Hello world"
s = s[0:6] + "W" + s[-4:]
print(s)
s.replace("w","W")

#8) "abc" ifadesini yan yana 3 defa yazdırın.
result = "abc" * 3
print(result)

