import numpy as np

Liste = [[10,20,30],[20,30,40],[30,40,50]]

benimMatrixDizim = np.array(Liste)
print(benimMatrixDizim)

print(benimMatrixDizim[2:,2:]) #ilk parametre sütun, ikinci parametre ilk sütundaki eleman.
#: koyunca tekrar köşeli paranteze (matrixe) alıyor.

print(benimMatrixDizim[[0,2]])


#operasyonlar

yeniBirDizi = np.random.randint(1,100,20)
print(yeniBirDizi)
print(yeniBirDizi > 24)
sonucDizisi = yeniBirDizi > 24
print(yeniBirDizi[sonucDizisi])
print(len(yeniBirDizi[sonucDizisi]))

sonDizi = np.array(0,24)
print(sonDizi)

