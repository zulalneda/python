name = "Çınar"
surname = "Turan"
age = 23

print("My name is {} {}" .format(name, surname))
print("My name is {1} {0}" .format(name, surname)) #0 = name, 1 = surname. O yüzden değişiklik oldu.
print("My name is {} {} and I'm {} years old." .format(name, surname, "23"))
print("My name is {} {} and I'm {} years old." .format(name, surname, age))

result = 200/700
print("the result is {r:9.4}".format(r=result))

print(f"My name is {name} {surname} and I'm {age} years old.")


