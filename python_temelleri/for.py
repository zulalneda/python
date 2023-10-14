numbers = [1, 2, 3, 4, 5]
for numbers in numbers:   #for num in numbers
    print(numbers)          #print(num)  print(x) dersek 5 defa x yazdırır.

names = ["Zülal","Neda","Sinem","Rumeysa","Şevval","Nisa"]
for name in names:
    print(f"seni seviyorum {name}")


name = "Neda Özmen"
for n in name:
    print(n)   #string ifade yazdırdığımızda ifadenin HER elemanı ekrana yazdırılır.

tuple = [(1,2),(1,3),(3,5),(5,7)]
for x in tuple:   #for (a,b) şeklinde tanımladığımızda elemanları parantezsiz şekilde verir.
    print(x)      # for (tek değişken) şeklinde tanımladığımızda () haliyle liste şeklinde verir.




d = {"k1":1, "k2":2, "k3":3}
for key in d.items(): #bu tipte d.items şeklinde yapmalıyız. eğer "key" gibi tek değişken atarsak ()li şekilde;
    print(key)        #"key,value" gibi çift değerler atarsak açık şekilde (üstteki liste mantığında) görürüz.

