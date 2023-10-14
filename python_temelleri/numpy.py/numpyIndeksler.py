import numpy as np
benimDizim = np.arange(0,15)
print(benimDizim)
print(benimDizim[3:8]) 

diziIcindekiDegerleriIstenilenBirElemanlaDegistirme = benimDizim[3:8] = -5
print(benimDizim)

baskaDizi = np.arange(0,24)
print(baskaDizi)
slicingDizisi = baskaDizi[4:9]
slicingDizisi[:] = 700
print(slicingDizisi)
print(baskaDizi) 

ornekDizi = np.arange(0,30)
print(ornekDizi)
ornekDiziKopyasi = ornekDizi.copy()
print(ornekDiziKopyasi)
ornekDiziKopyasiSlicing = ornekDiziKopyasi[3:6]
print(ornekDiziKopyasiSlicing)
ornekDiziKopyasiSlicing[:] = 800
print(ornekDiziKopyasiSlicing)
print(ornekDiziKopyasi)
print(ornekDizi)