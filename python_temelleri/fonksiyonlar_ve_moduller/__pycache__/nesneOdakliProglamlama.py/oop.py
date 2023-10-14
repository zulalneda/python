#insance & attribute
#sınıfların isimleri genellikle büyük harfle başlar "SuperKahraman"
class SuperKahraman():

    OzelGuc = "Uçabilmek"

    def __init__(self,isim,yas,meslek):
        self.isim = isim
        self.yas = yas
        self.meslek = meslek
        print("init çağrıldı")

    def OrnekMethod(self):
        print(f"ben süperkahramanım ve mesleğim {self.meslek}")

superman = SuperKahraman("Superman",30,"Gazeteci")

#batman = SuperKahraman()   #superman ve batman değişkenleri atadığımızda sınıfımızın içinde olduğu için print ifadesini yazdırır.

superman.isim = "Clark Kent"
superman.yas = 30
superman.meslek = "Gazeteci"

superman.OrnekMethod()
print(superman.isim)





class Kopek():
    insanCarpani = 7

    def __init__(self,yas):
        self.yas = yas
        
    def insanYasiniHesapla(self):
        return self.yas * self.insanCarpani #self yerine kopek de diyebiliriz.
    

benimKopek = Kopek(5)
print(benimKopek.yas)
print(benimKopek.insanYasiniHesapla())




class Hayvanlar():
    def __init__(self):
        print("hayvan sınıfı init çağrıldı.")
    def method1(self):
        return ("hayvan sınıfı method1 çağrıldı")
    def method2(self):
        return ("hayvan sınıfı method2 çağrıldı.")

benimHayvanim = Hayvanlar()

print(benimHayvanim.method1())
print(benimHayvanim.method2())

class Kedi():
    def __init__(self):
        Hayvanlar.__init__(self)
        print("kedi sınıfı init çağrıldı")

    def Miyavla(self):
        return ("miyav")

    def method1(self):
        Hayvanlar.method1(self)
        return ("kedi sınıfı method1 çağırıldı")   #override

benimKedi = Kedi()
print(benimKedi)
print(benimKedi.Miyavla())
print(benimKedi.method1())


class Elma():
    def __init__(self,isim):
        self.isim = isim
        
    def bilgiVer(self): 
        return (f"{self.isim} 100 kaloridir.")


class Muz():
    def __init__(self,isim):
        self.isim = isim
        
    def bilgiVer(self):
        return (f"{self.isim} 150 kaloridir.")

elma = Elma("elma")
muz = Muz("muz")

print(elma.bilgiVer())
print(muz.bilgiVer())

class Meyve():

    def __init__(self, isim, kalori):
        self.isim = isim
        self.kalori = kalori

    def __str__(self):
        return (f"{self.isim} şu kadar kaloridir : {self.kalori}")

    def __len__(self):
        return self.kalori

portakal = Meyve("Portakal", 30)
print(portakal.isim)
print(portakal.kalori)
print(portakal)
print(len(portakal))

kivi = Meyve("Kivi", 210)
print(kivi)
print(len(kivi))




        





