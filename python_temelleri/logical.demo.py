#a = int(input("1. sayı: "))
#print((a>0) and (a<100))

#a = int(input("1. sayı: "))
#print((a>0) and (a %2 == 0))

#email = "email@gmail.com".strip()
#parola = "123123"

#userMail = input("email: ")
#userPassword = input("parola: ")

#print((email == userMail) and (parola == userPassword))


#a = int(input("1. sayı: "))
#b = int(input("2. sayı: "))
#c = int(input("3. sayı: "))

ad = str(input("Adınız: "))
soyad = str(input("Soyadınız: "))
kilo = float(input("Kilonuz: "))
boy = float(input("Boyunuz: "))

index = (kilo / (boy ** 2))
zayif = (index >= 0) and (index <= 18.5)
normal = (index >= 18.5) and (index <= 24.5)
kilolu = (index >= 24.5) and (index <= 30)
obez = (index > 30)

print(f"{ad} {soyad} kilo indeksiniz: {index} durumunuz zayıf: {zayif} ")
print(f"{ad} {soyad} kilo indeksiniz: {index} durumunuz normal: {normal} ")
print(f"{ad} {soyad} kilo indeksiniz: {index} durumunuz kilolu: {kilolu} ")
print(f"{ad} {soyad} kilo indeksiniz: {index} durumunuz obez: {obez} ")