#1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
listAraba = ["Bmw","Mercedes","Opel","Mazda"]
#2- Liste kaç elemanlıdır?
print(len(listAraba))
#3- Listenin ilk elemanı nedir?
result = listAraba[0]
print(result)
#4- Mazda değerini Toyota ile değiştirin.
#listAraba[-1] = "Toyota"
#x = listAraba
#print(x)
#5- Mercedes listenin bir elemanı mıdır?
y = "Mercedes" in listAraba
print(y)
#6- Listenin -2 indeksindeki değer nedir?
z = listAraba[-2]
print(z)
#7- Listenin ilk 3 elemanını alın.
t = listAraba[-2:] #0:3  :3
print(t)
#8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
listAraba[2:] = ["Toyota", "Renault"] #-2: de olabilir.
c = listAraba
print(c)
#9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
z = listAraba + ["Audi", "Nissan"]
print(z)
#10- Listenin son elemanını silin.
#del listAraba[-1]
#m = listAraba
#print(m)
#11- Liste elemanlarını tersten yazdırınız.
n = listAraba[::-1]
print(n)



#12- Aşağıdaki verileri bir liste içinde saklayınız.
    #studentA = Yiğit, Bilgi, 2010, (70,60,70)
    #studentB = Sena, Turan, 1999, (80,80,70)
    #studentC = Ahmet, Turan, 1998, (80,70,90)

studentA = ["Yiğit" , "Bilgi" , 2010 , [70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan","1998",[80,70,90]]
Hepsi = [studentA + studentB + studentC]
print(Hepsi)

o = {studentA[3][0] + studentB[3][1] + studentC[3][2]}/3
print(o)

