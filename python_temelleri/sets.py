#value types
x = 10
y = 25

x = y
print(x, y)

y=5
print(x, y)


#List types
ListA = ["apple", "banana", "orange"]
ListB = ["apple", "banana", "orange"]

ListA = ListB

ListA.remove("apple")
print(ListA, ListB)

#value türlerinde üstte yapılan bir değişiklik altta yapılanı etkilemezken liste türlerinde yapılan bir değişiklik tüm kısmı etkiler.
