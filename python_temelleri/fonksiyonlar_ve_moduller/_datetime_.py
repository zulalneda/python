# from datetime import date
# from datetime import datetime

# bugun = date.today()
# print(bugun)
# print(bugun.day) #ayın kaçı olduğunu gösterir.
# print(bugun.month) 
# print(bugun.year)
# print(bugun.weekday()) #liste mantığında 0'dan başlayıp haftanın kaçıncı günü olduğunu gösterir. 0 = pazartesi, 1 = salı, 2 = çarşamba vb.
# print(bugun.isoweekday()) #pazartesi = 1, salı = 2, çarşamba = 3 vb.

# gecmis_tarih = date(2015,8,13)
# print(gecmis_tarih.isoweekday())

# gecmis_tarih = date(1919,5,19)
# print(gecmis_tarih.isoweekday())

# gecen_zaman = bugun - gecmis_tarih
# print(gecen_zaman)
# print(type(gecen_zaman))











# suan = datetime.now()
# print(type(suan))
# print(suan)
# print(suan.year)
# print(suan.month)
# print(suan.day)
# print(suan.hour)
# print(suan.minute)
# print(suan.second)

# print(suan.ctime()) #print(datetime.ctime(suan))
# print(suan.date) 
# print(suan.time)
# print(suan.month) #print(suan.date().month)
# print(suan.date().month)




# bugun = date.today()
# suan = datetime.now()

# print(bugun.strftime("%d-%m-%Y %A"))

# print(datetime.strftime(bugun, "%d-%m-%Y"))
# print(suan.strftime("%d-%m-%Y"))



# from datetime import timedelta

# suan = datetime.now()
# tdelta = timedelta(days=7, hours=5,seconds=69)
# print(suan + tdelta)
# print(suan - tdelta)
