#identites "is"
x = y = [1, 2, 3]
z = [1, 2, 3]

print(x==y)
print(x==z)   #değer olarak aynı old. için "true" yazdı.
print(x is y)
print(x is z)   #değerleri aynı olmasına rağmen adres bilgileri farklı old. için "false" yazdı.

#Membership Operator: in
x = ["apple", "banana"]
print("banana" in x)

#bir değerin istenilen listede olup olmama durumuna bakar.