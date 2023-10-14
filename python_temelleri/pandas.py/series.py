import numpy as np
import pandas as pd

benimSozlugum = {"Atıl" : 50, "Zeynep" : 40, "Mehmet" : 30}
print(pd.Series(benimSozlugum))

benimYaslarim = [50,40,30]
benimIsimlerim = ["Atıl", "Zeynep", "Mehmet"]

#print(pd.Series(benimYaslarim))
#print(pd.Series(benimIsimlerim))
#print(pd.Series(benimYaslarim, benimIsimlerim))
#print("***")
# print(pd.Series(benimIsimlerim, benimYaslarim)) #2. parametreyi önce yazdırıyor.
# print(pd.Series(data=benimYaslarim, index= benimIsimlerim))
# numpyDizisi = np.array([50,40,30])
# print(pd.Series(numpyDizisi, benimIsimlerim))

yarismaSonucu1 = pd.Series([10,5,1],["Atıl","Osman","Sinem"])
print(yarismaSonucu1)

yarismaSonucu2 = pd.Series([20,10,8],["Atıl","Osman","Sinem"])
print(yarismaSonucu2)
print(yarismaSonucu2["Atıl"])
print(yarismaSonucu1+yarismaSonucu2)

farkliSeries = pd.Series([20,30,40,50],["a","b","c","d"])
farkliSeries2 = pd.Series([10,5,3,1],["a","c","f","g"])

print(farkliSeries + farkliSeries2) #ortak değerleri float biçiminde toplar, diğerlerine NaN yazdırır.

