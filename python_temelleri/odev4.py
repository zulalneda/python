ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

ogrenciler[number] = {
    "ad" : name,
    "soyad" : surname,
    "telefon" : phone
}

print(ogrenciler)

ogrenciler.update({
    number: {
        "ad": name,
        "soyad": surname,
        "telefon": phone
    }
})

print(ogrenciler)



ogrNo = input("öğrenci no: ")
ogrenci = ogrNo[number]

print(ogrenci)
