import numpy as np
benimListem = [20,30,40]
print(type(benimListem))
print(type(np.array(benimListem)))
print(np.array(benimListem))

matrixListesi = [[10,20,30],[20,30,40],[30,40,50]]
print(type(matrixListesi[1][2]))
print(np.array(matrixListesi))


#arange
print(list(range(0,10)))
print(np.arange(0,10,2))

#zeros
print(np.zeros(5))
print(np.zeros((2,2)))

#ones
print(np.ones(9))
print(np.ones((9,9)))

#linspace
print(np.linspace(0,10,100)) #1. başlangıç değeri(dahil), 2. bitiş değeri(dahil), 3. yazdırılmak istenen değer sayısı

#eye
print(np.eye(3,5)) #10 satırda 10 adet sol üstten başlayıp sağ aşağıya çapraz şekilde "1" yazdırıp kalanlara "0" yazdırır.

#random
print(np.random.randn(8)) #1 boyutlu
print(np.random.randn(4,4)) #2 boyutlu
print(np.random.randint(1,10)) #ikinci parametreyi (10) yazdırmaz.
print(np.random.randint(1,5,300)) #1. başlangıç değeri (dahil), 2. bitiş değeri (dahil değil), 3. yazdırılmak istenen değer sayısı

benimNumpyDizim = np.arange(30)
print(benimNumpyDizim)
print(np.arange(1,30,5))

#numpy dizi metodları
print(benimNumpyDizim.reshape(6,5)) #6 satır 5 sütun
print(benimNumpyDizim.max())
benimRandomDizim = np.random.randint(1,100,5)
print(benimRandomDizim.max())
print(benimRandomDizim.argmax()) #kaçıncı sırada olduğunu gösterir.


reshapeDizim = benimNumpyDizim.reshape(5,6)
print(reshapeDizim.shape) #mevcut dizimin hangi şekilde olduğunu söyler. (satır / sütun)
