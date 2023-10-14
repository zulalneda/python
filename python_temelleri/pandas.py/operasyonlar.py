import numpy as np
import pandas as pd

sozlukVerisi = {"Istanbul": [30,29,np.nan], "Ankara" : [20, np.nan,25], "Izmir": [40,39,38]}
havaDurumuDataFrame = pd.DataFrame(sozlukVerisi)
print(havaDurumuDataFrame)
havaDurumuDataFrame.dropna() #satırda bir tane bile bilinmeyen olmasıyla tüm satırı siler. 
# == (axis = 0)
print(havaDurumuDataFrame.dropna(axis = 1)) #üsttekinin sütun hali

yeniFrame = {"Istanbul": [30,29,np.nan], "Ankara" : [20, np.nan,25], "Izmir": [40,39,38]}
yeniDataFrame = pd.DataFrame(yeniFrame)
print(yeniDataFrame.dropna(axis = 1, thresh = 2)) #sütunlardan 2 ve 2den fazla bilinmeyen değere sahip olanları at.

yeniDataFrame.fillna(20) #boş olanları "20" ile doldur.

#groupby

maasSozlugu = {"Departman": ["Yazılım","Yazılım","Pazarlama","Pazarlama","Hukuk","Hukuk"],
"Çalışan İsmi" : ["Ahmet", "Mehmet","Atıl","Burak","Zeynep","Fatma"],
"Maaş" : [100,150,200,300,400,500]
}

maasDataFrame = pd.DataFrame(maasSozlugu)
print(maasDataFrame)

grupObjesi = maasDataFrame.groupby("Departman")

print(grupObjesi.count()) #axis = 1 sütun kısımlarının aynı kısımlarını saydırır.

print(grupObjesi.mean()) #maaşlarının ortalaması

print(grupObjesi.max())
print(grupObjesi.min())

