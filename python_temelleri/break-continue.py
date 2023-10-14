x = 0
while x < 5:
    x += 1
    if x == 2:
        continue
    print(x)
    


y = 0
toplam = 0
#while y <= 100:
#    toplam = toplam + y
#    y += 1
#print(toplam)


while y <= 100:
    y += 1
    if y % 2 == 0:
        continue
    toplam = toplam + y

print(toplam)



print(list(range(5,100,10)))


greeting = "Hello"

for item in enumerate(greeting):
    print(item)

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)

isimler = ["Oğuzhan", "Enes","Selim"]
for index,isim in enumerate(isimler, start = 1):
    print(index, isim)


print(" ")

counter = 0
for isim in isimler:
    counter += 1
    print(counter, isim)
