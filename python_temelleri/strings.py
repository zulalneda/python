name = "Neda"
surname = "Özmen"
age = 18

print("My name is "+ name + " " + surname + " and\nI am "+ str(age)+ " years old.")

greeting = "My name is "+ name + " " + surname + " and\nI am "+ str(age)+ " years old."
length = len(greeting) #greeting metninin uzunluğu

print(greeting[0]) #dizinin ilk elemanını ekrana yazdırır.
print(greeting[3]) #boşlukları da sayar.
print(greeting[length-1]) #dizinin son elemanını yazdırır.
#bunun sebebi sondan numaralandığında - ile başlanmasıdır.
print(greeting[-1])
print(greeting[-44])
print(length)

print(greeting[3:7]) #3'ten 7'ye kadar olan değerleri yazdırır.
print(greeting[3:]) #3'ten sonuna kadar yazdırır.
print(greeting[:15]) #baştan alıp 15'e kadar getir.
print(greeting[2:40:3]) #2'den 40'a kadar olan ifadeleri 3'er 3'er al.
