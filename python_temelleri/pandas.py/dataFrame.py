import pandas as pd
import numpy as np

data= np.random.randn(4,3)
# print(data)
dataFrame = pd.DataFrame(data)
# print(dataFrame)
# print(dataFrame[0][1])
yeniDataFrame = pd.DataFrame(data,index=["Atıl","Zeynep","Atlas","Mehmet"],columns=["Maaş","Yaş","Çalışma Saatleri"])
# print(yeniDataFrame)
# print(yeniDataFrame["Çalışma Saatleri"])
# print(yeniDataFrame[["Maaş","Çalışma Saatleri"]]) #kolonlar için geçerli

# print(yeniDataFrame.loc["Atıl"]) #indeksler için geçerli
# print(yeniDataFrame.iloc[0]) #indeksleri gösterir
# yeniDataFrame["Emeklilik Yaşı"] = yeniDataFrame["Yaş"] + yeniDataFrame["Yaş"] 
# print(yeniDataFrame)

# #print(yeniDataFrame.drop("Emeklilik Yaşı", axis = 1))

# print(yeniDataFrame.drop("Emeklilik Yaşı", axis = 1, inplace=True))

# print(yeniDataFrame.loc["Atıl","Yaş"])

#print(yeniDataFrame < 0)

booleanFrame = yeniDataFrame<0

#print(yeniDataFrame[booleanFrame])

#print("***")

#print(yeniDataFrame[yeniDataFrame["Çalışma Saatleri"]> 0])
# print(yeniDataFrame.reset_index()) #Başına 0-1-2-3 ekliyor

# yeniIndexListesi = ["Ati","Zey","Atl","Meh"]
# yeniDataFrame["Yeni Index"] = yeniIndexListesi

# print(yeniDataFrame.set_index("Yeni Index",inplace=True))


#Multi İndeksler

ilkIndeksler = ["Simpson","Simpson","Simpson","South Park","South Park","South Park"]

icIndeksler = ["Homer","Bart","Marge","Cartman","Kenny","Kyle"]

birlesmisIndeks = list(zip(ilkIndeksler,icIndeksler))
print(birlesmisIndeks)

birlesmisIndeks = pd.MultiIndex.from_tuples(birlesmisIndeks)
print(birlesmisIndeks)

benimCizgiFilmListem = [[40,"A"],[10,"B"],[30,"C"],[9,"D"],[10,"E"],[11,"F"]]
cizgiFilmNumpyDizisi = np.array(benimCizgiFilmListem)
cizgiFilmDataFrame = pd.DataFrame(cizgiFilmNumpyDizisi,index = birlesmisIndeks, columns=["Yas","Meslek"])
print(cizgiFilmDataFrame)
print(cizgiFilmDataFrame.loc["Simpson","Homer"])
# cizgiFilmDataFrame.index.names = ["Film Adi","Isim"]
# print(cizgiFilmDataFrame.index.names)

