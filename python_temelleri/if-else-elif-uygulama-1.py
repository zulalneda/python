#name = str(input("isim: ")).strip()
#age = int(input("yaş: "))
#education = str(input("eğitim düzeyi: ")).strip().lower()

#if (age >= 18) and (education in ["lise", "üniversite"]):
    #print("ehliyet alabilirsiniz")
#else:
    #print("ehliyet alamazsınız")





#yazili1 = float(input("1. yazılı: "))
#yazili2 = float(input("2. yazılı: "))
#sozlu = float(input("sözlü notu: "))

#ortalama = ((yazili1 + yazili2 + sozlu) / 3)

#if (ortalama >= 0) and (ortalama <= 24):
    #print(f"ortalamanız {ortalama} ve notunuz {0}")
#elif (ortalama > 24) and (ortalama <= 44):
 #   print(f"ortalamanız {ortalama} ve notunuz {1}")
#elif (ortalama > 44) and (ortalama <= 54):
  #  print(f"ortalamanız {ortalama} ve notunuz {2}")
#elif (ortalama > 54) and (ortalama <= 69):
 #   print(f"ortalamanız {ortalama} ve notunuz {3}")
#elif (ortalama > 69) and (ortalama <= 84):
 #   print(f"ortalamanız {ortalama} ve notunuz {4}")
#elif (ortalama > 84) and (ortalama <= 100):
 #   print(f"ortalamanız {ortalama} ve notunuz {5}")
#else:
  #  "Notunuz hesaplanamadı. Bilgilerinizi tekrar giriniz."




#sayi = float(input("sayı: "))
#if (sayi > 0) and (sayi < 100):
    #print(f"{sayi} sayısı 0 ile 100 arasındadır.")
#else:
    #print(f"{sayi} sayısı 0-100 arasında değildir.")


#sayi1 = int(input("sayı: "))
#if (sayi1 % 2 == 0):
#    if (sayi1 > 0):
 #       print(f"{sayi1} sayısı pozitif ve çift bir sayıdır.")
  #  else:
   #     print(f"{sayi1} sayısı pozitiftir fakat çift değildir.")
#else:
 #   print(f"{sayi1} sayısı ne pozitif ne de çift bir sayıdır.")




#email = "email@sadikturan.com".split()
#password = "abc123"

#logIn = input("email: ")
#sifre = input("sifre= ")

#if (logIn == "email@sadikturan.com"):
 #   if (sifre == "abc123"):
  #      print("Girilen bilgiler doğrudur.")
   # else:
    #    print("Şifrenizi yanlış girdiniz.")
#else:
 #   print("Kullanıcı adınızı yanlış girdiniz.")



ad = str(input("adınız: "))
kilo = float(input("kilonuz: "))
boy = float(input("boyunuz: "))

indeks = (kilo) / (boy) ** 2

